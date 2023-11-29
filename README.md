# CSE573FinalProject

This project applied the Louvain Community Detection Algorithm to a dataset of twitter interactions.
These interactions consisted of users retweeting other user tweets about either Black Lives Matter or All Lives Matter topics.

Once the data was prepared and preprocessed, this project was broken down into two core steps.
The first step was to apply the Louvain Community Detection Algorithm to our full data-set. We would then filter out the weaker detected communities (communities of a size below a given threshold) until only relevant, strong communities were left.
The second step was to take these strong communities and merge them based on pairwise interactions between nodes in the communities until only two communities remained.

To run these files, you can simply run 
	\nsh ApplyCommunityDetection.sh\n
which will automatically read the data, run both files, and output a graph named "finalGraphOfNodes.gexf" which can be put into an application like Gephi for visualization

The results (visualization) of our runs are within the /Evaluations directory, along with our powerpoint describing our process and findings.

Our dataset can be found here: [INSERT LINK]
