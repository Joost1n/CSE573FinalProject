import networkx as nx
import community as community_louvain
from collections import defaultdict
import pickle

# Load the three cleaned datasets
fileName1 = "clean_race_tw_01.txt"
fileName2 = "clean_race_tw_15.txt"
fileName3 = "clean_race_tw_24.txt"
fileToRead1 = open(fileName1)
fileToRead2 = open(fileName2)
fileToRead3 = open(fileName3)

# Initialize edges array
edges = []

# Read the nodes from the dataset and append their edges to the edges array
for line in fileToRead1:
    u,p = [int(x) for x in line.rstrip("\n").split(",")]
    edges.append((u,p))
for line in fileToRead2:
    u,p = [int(x) for x in line.rstrip("\n").split(",")]
    edges.append((u,p))
for line in fileToRead3:
    u,p = [int(x) for x in line.rstrip("\n").split(",")]
    edges.append((u,p))

# Initialize the NetworkX graph
G = nx.Graph()

# Add the edges to the graph
G.add_edges_from(edges)

# Perform Louvain in order to identify communities within a graph and then set those identified communities as an attribute for each node
partition = community_louvain.best_partition(G)
nx.set_node_attributes(G, partition, 'community')

# Calculates the total size of each community and removes the small communities if they are below a specific threshold 
#   in order to only see strong communities
community_sizes = {}
for node, comm_id in partition.items():
    community_sizes[comm_id] = community_sizes.get(comm_id, 0) + 1
    
threshold = 10000 

strong_communities = [comm_id for comm_id, size in community_sizes.items() if size >= threshold]

# Create a new graph with only the strong communities
strong_community_graph = nx.Graph()
for node, comm_id in partition.items():
    if comm_id in strong_communities:
        strong_community_graph.add_node(node)
for edge in G.edges():
    u, v = edge
    if partition[u] in strong_communities and partition[v] in strong_communities:
        strong_community_graph.add_edge(u, v)

# Partitioning was the most computationally expensive operation so we only perform it once and
# store the Graph, partition, and strong communities for it to be used in the second part
pickle.dump(strong_community_graph, open('final_strong_community_graph.pickle', 'wb'))
pickle.dump(partition, open('final_strong_community_partition.pickle', 'wb'))
pickle.dump(strong_communities, open('final_strong_community_comms.pickle', 'wb'))
