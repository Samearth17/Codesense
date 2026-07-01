import networkx as nx 

def rank_influential_bloggers(data):
 G = nx.Graph()

 # Create a NetworkX graph based on the given dataset
 # ...

 # Calculate the influence of each node in the graph
 influencer_scores = nx.pagerank(G)

 # Sort the influencer scores in descending order
 sorted_influence_scores = sorted(influencer_scores.items(), key=lambda x: x[1], reverse=True)

 # Get the top 5 most influential bloggers
 top_influencers = [tuple[0] for tuple in sorted_influence_scores[:5]]

 return top_influencers