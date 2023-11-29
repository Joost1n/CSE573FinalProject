# CSE573FinalProject

This project applied the Louvain Community Detection Algorithm to a dataset of twitter interactions.
These interactions consisted of users retweeting other user tweets about either Black Lives Matter or All Lives Matter topics.

Once the data was prepared and preprocessed (using DataCleaner.py), this project was broken down into two core steps.
The first step was to apply the Louvain Community Detection Algorithm to our full data-set. We would then filter out the weaker detected communities (communities of a size below a given threshold) until only relevant, strong communities were left.
The second step was to take these strong communities and merge them based on pairwise interactions between nodes in the communities until only two communities remained.

<p align="center">
  <img src="https://github.com/Joost1n/CSE573FinalProject/blob/main/Evaluations/GraphCommunitiesIdentified.png" />
</p>

To run these files, you can simply run 

	sh ApplyCommunityDetection.sh

which will automatically read the data, run both files, and output a graph named "finalGraphOfNodes.gexf" which can be put into an application like Gephi for visualization. NOTE: You will need to make sure you install the relevant dependencies.

The results (visualization) of our runs are within the /Evaluations directory, along with our powerpoint describing our process and findings.

Our dataset can be found here: https://drive.google.com/drive/folders/1rjP8vIOcwWX10Imu8kxV7RVoUKoGmO0M
