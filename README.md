# CSE573FinalProject
Community Detection Algorithm applied to BLM/ALM Twitter data set

1. Abstract
In this project, we propose to survey and develop community detection techniques and 2D/3D visualizations for analyzing US Race Relations data. We will employ advanced algorithms and methods to detect meaningful communities within the US Race Relations category and visualize them in a way that provides insights and facilitates comprehension. The techniques developed in this study will not only be applicable to the US Race Relations domain but can also be extended to other categories for community detection and visualization.
2. Problem Definition
	This project aims to address the following key problems:
Identify and define communities within the US Race Relations category.
Apply filtering techniques to clarify data results and improve coherence of visualizations.
Develop effective visualization methods to represent the identified communities in an intuitive and informative manner.
3. Data Sets
We will be using a dataset of twitter interactions occurring during the month of May of 2023. The interactions consist of users retweeting other users’ tweets about topics relating to the Black Lives Matter vs. All Lives Matter movements. These retweets will be used to determine which users are interacting with one another and thus comprise different communities. This dataset was collected before the start of the project and provided to us by Professor Davalcu’s lab.
4. State-of-Art Methods & Algorithms
The paper, Detecting Cohesive and 2-mode Communities in Directed and Undirected Networks [1] provides a detailed and comprehensive analysis of networks and visualizing their communities. It defines a cohesive method of taking an unlabeled, directed network and finding 2-mode communities.

Then the scientific report, “From Louvain to Leiden: guaranteeing well-connected communities” [2], discusses the Louvain Community Detection Algorithm and the purpose that it serves. The Louvain algorithm is a highly effective and widely adopted technique for identifying communities in complex networks. It operates by aiming to maximize the density of connections within communities while minimizing connections between them using a metric known as Modularity. 

Modularity is further elaborated on in “Fast unfolding of communities in large networks” [3] and it measures the strength of division of a network into communities compared to a random graph. It is a scalar that is between the values 1 and -1. By maximizing modularity, the Louvain algorithm seeks to unveil the most cohesive and well-defined communities present within the network, allowing for a comprehensive understanding of the underlying relationships and interactions in the dataset.

Additionally, while the Louvain algorithm provides a foundational understanding of the communities, we will employ the network analysis and visualization capabilities of Gephi, a powerful tool designed for visualizing and exploring networks. Martin Grandjean [4] assists in breaking down Gephi’s features. This tool allows for an in-depth visualization of the graph produced by the Louvain algorithm, enhancing our ability to interpret and comprehend the community structure within the dataset. By utilizing Gephi's features, we can customize the visualization, apply various layouts, highlight important nodes and edges, and gain insights into the intricate relationships and patterns present within the communities identified by the Louvain algorithm. The integration of Louvain's community detection and Gephi's advanced visualization capabilities forms a comprehensive approach to uncovering and presenting meaningful insights from the US Race Relations dataset.
5. Research Plan
	In order to complete this project, there are many steps which will need to be completed. First, we will conduct an extensive literature review to understand existing approaches to community detection and visualization. This step will provide us an important foundation not only in the nomenclature of the field but also provide us with background on why and how these approaches have been developed.
	Next, the selected US Race Relations datasets will be analyzed to identify relevant features. This data will then be preprocessed and prepared. Once the data is processed, the Louvain community detection algorithm can be applied to the resulting graph and will identify communities within the dataset. 
From here, we will utilize visualization tools like Gephi to represent the detected communities in a way that is easy to understand. Once the data is visualized, our approach will be evaluated in its effectiveness in conveying meaningful information to users. 
6. Evaluation Plan
It is important not only to create this visualization of communities within the database, but also to measure our efficacy in producing meaningful results. Thus, we must also create metrics for evaluating the performance of our approach. Various methods to evaluate network analysis are described in “Generalized measures for the evaluation of community detection methods” [5]. Such methods include: Purity, Adjusted Rand Index (ARI) , and Normalized Mutual Information (NMI). Purity describes the extent to which items in a single cluster are related to each other; ARI describes how similar separate clusters are to one another using pairs; and NMI is a measure of the mutual information shared between two different clusters of data.

In addition to the quantitative metrics proposed above, we will also evaluate the success of our project by:
Qualitatively assessing the visualizations by soliciting feedback from domain experts and potential end-users.
Comparing our results with existing methodologies and benchmarks for community detection and visualization.
Adjusting the minimum thresholds set for edge weight to produce communities of marginally varying size to determine which is best.
Evaluate the efficacy of the algorithm based on modularity produced for different thresholds.
