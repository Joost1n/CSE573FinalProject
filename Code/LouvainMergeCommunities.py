import networkx as nx
import community as community_louvain
from collections import defaultdict
import pickle

# Read inputs from first process
# Splitting the process into two steps reduced the total run-time required to test specific portions of the code
strong_community_graph = pickle.load(open('final_strong_community_graph.pickle', 'rb'))
partition = pickle.load(open('final_strong_community_partition.pickle', 'rb'))
strong_communities = pickle.load(open('final_strong_community_comms.pickle', 'rb'))

print("number of communities: " + str(len(strong_communities)))
communityMapping = {}

# Create a map data structure which will measure the pairwise interactions between communities
print("initializing mapping")
for from_comm_id in strong_communities:
    for to_comm_id in strong_communities:
        stringID = str(from_comm_id) + "-" + str(to_comm_id)
        communityMapping[stringID] = 0
print("map initialized")

# Every time there is a connection between two nodes, increment the counter in the map
print("adding data to mapping")
nodes = strong_community_graph.nodes()
for edge in strong_community_graph.edges():
    u, v = edge
    comm1 = list(nodes[u].values())[0]
    comm2 = list(nodes[v].values())[0]
    if(comm1 != comm2):
        communityMapping[str(comm1) + "-" + str(comm2)] += 1
print("map structure complete")

# Delete any combinations in the map that are zero (no interactions between those communities)
communityMapping = {x:y for x,y in communityMapping.items() if y!=0}

# Create a new graph of the commnunities so to better track the interactions and
# in the future, the merging of said communities
print('making community graph')
communityGraph = nx.Graph()
for item in communityMapping.items():

    #Retrieve interaction from graph 
    node1, node2 = item[0].split("-")
    node1 = node1.rstrip()
    node2 = node2.rstrip()

    # add nodes to graph
    communityGraph.add_node(node1)
    communityGraph.add_node(node2)

    totalWeightToBeAdded = item[1]

    # add edge from node1 to node2
    if not communityGraph.has_edge(node1, node2):
        communityGraph.add_edge(node1, node2, weight=totalWeightToBeAdded)
    # since interactions can go node1 -> node2 or node2 -> node1, we must add to the existing weights so that
    # we do not accidentally overwrite previous graph weights
    else:
        totalWeightToBeAdded = totalWeightToBeAdded + communityGraph[node1][node2]['weight']
        communityGraph[node1][node2]['weight'] = totalWeightToBeAdded
print('made community graph')

# sort the edge weights from biggest to smallest for merging
edges = sorted(communityGraph.edges(data=True), key=lambda edge: edge[2].get('weight'), reverse=True)
counter = 0

# It was determined that we should only do this once based on the graph specific to this dataset
# merge two biggest communities
while counter < 1:
    counter += 1

    edge = edges.pop(0)
    u = list(edge)[0]
    v = list(edge)[1]

    communityGraph.remove_edge(u,v)
    print("merging communities: " + str(u) + " , " + str(v))

    #rewrite the community assignment in the original graph as we merge
    for node in strong_community_graph.nodes(): 
        # if its in comm2, change it to comm1 so that we merge them
        if str(partition[node]) == str(v): 
            partition[node] = u


    # Fix datastructure to add edge weights from old comms to new comm
    # (i.e. if merging comm1 and comm2, merge edge weight comm1->comm3 and comm2->comm3)
    for edge in communityGraph.edges():
        a = list(edge)[0]
        b = list(edge)[1]
        #if statement in case v is first or second edge, could be either bc they are returned in numerical order
        if a == v and u != b:
            if communityGraph.has_edge(u, b) and communityGraph.has_edge(v, b):
                edgeWeightToAdd1 = communityGraph[v][b]['weight']
                edgeWeightToAdd2 = communityGraph[u][b]['weight']
                totalEdgeWeightToAdd = edgeWeightToAdd2 + edgeWeightToAdd1

                communityGraph.remove_edge(v,b)
                communityGraph.remove_edge(u,b)

                communityGraph.add_edge(u, b, weight=totalEdgeWeightToAdd)
        elif b == v and u != a:
            if communityGraph.has_edge(u, a) and communityGraph.has_edge(v, a):
                edgeWeightToAdd1 = communityGraph[v][a]['weight']
                edgeWeightToAdd2 = communityGraph[u][a]['weight']
                totalEdgeWeightToAdd = edgeWeightToAdd2 + edgeWeightToAdd1

                communityGraph.remove_edge(v,a)
                communityGraph.remove_edge(u,a)

                communityGraph.add_edge(u, a, weight=totalEdgeWeightToAdd)

    # Remove the node from the graph so the community is no longer represented
    communityGraph.remove_node(v)

    # list must be resorted after edges are merged - important in the case that this process is performed multiple times
    edges = sorted(communityGraph.edges(data=True), key=lambda edge: edge[2].get('weight'), reverse=True)
    
# Create a new partition where the merged nodes are in one community, and all others are in a second community
new_partition = {node: 1 if str(partition[node]) == '1' else 2 for node in strong_community_graph.nodes()}

# Save new partition
print("applying new partition")
nx.set_node_attributes(strong_community_graph, new_partition, "best_community")

# Calculate Modularity
new_modularity = community_louvain.modularity(new_partition, strong_community_graph)
print(f"Modularity: {new_modularity}")

print("outputting file")
# Save outputs to be used in Gephi 
# Note: we are not sure why this happens, but only the first output file listed will actually be returned
#       If you want the community graph instead of the node graph, swap the order of these two lines
nx.write_gexf(strong_community_graph, "finalGraphOfNodes.gexf")
nx.write_gexf(communityGraph, "finalGraphOfCommunities.gexf")
