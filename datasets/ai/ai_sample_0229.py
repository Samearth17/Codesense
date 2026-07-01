import networkx as nx

def page_rank(G, alpha=0.85, personalization=None, 
 max_iter=100, tol=1.0e-6, nstart=None, weight='weight', 
 dangling=None):

"""
Return the PageRank of the nodes in the graph. 

G: graph
alpha: damping parameter for PageRank, default=0.85
personalization: 
    dict, optional 
    The "personalization vector" consists of a dictionary with a 
    key for every graph node and nonzero personalization value for each node. 
max_iter: 
    int, optional 
    Maximum number of iterations in power method eigensolve.
tol: float, optional
    Error tolerance used to check convergence in power method eigensolve.
nstart: 
    dict, optional 
    Starting value of PageRank iteration for each node.
weight: 
    key, optional 
    Edge data key to use as weight. 
dangling: 
    dict, optional 
    The outedges to be assigned to any "dangling" nodes, i.e., nodes without any outedges. 

Returns:
    Dictionary of nodes with PageRank as value.
"""

# Initialize results vector with (1-alpha)/N, 
# where N is the number of nodes in the graph.
N = G.number_of_nodes()
x = dict.fromkeys(G, (1 - alpha) / N)

# Check if personalization vector was passed in; if so, update results vector
if personalization is None:
    p = dict.fromkeys(G, 1 / N)
else:
    missing = set(G) - set(personalization)
    if missing:
        raise NetworkXError('Personalization dictionary '
                            'must have a value for every node. '
                            'Missing nodes %s' % missing)
    p = personalization
   p = p.copy()
    s = float(sum(p.values()))
    for k in p:
        x[k] = p[k] / s
        p[k] = p[k] / s

if dangling is None:
    # Use personalization vector if dangling vector not specified
    dangling_weights = p
else:
    # Dangling nodes are nodes with no outedges.
    # Use personalization vector if dangling vector is specified but
    # doesn't have an entry for every node
    missing = set(G) - set(dangling)
    if missing:
        raise NetworkXError('Dangling node dictionary '
                            'must have a value for every node. '
                            'Missing nodes %s' % missing)
    s = float(sum(dangling.values()))
    for k in dangling:
        dangling[k] /= s
    dangling_weights = dangling

# power iteration: make up to max_iter iterations
for _ in range(max_iter):
    xlast = x
    x = dict.fromkeys(xlast.keys(), 0)
    danglesum = alpha * sum(xlast[n] for n in dangling_weights)
    for n in x:

# this matrix multiply looks odd because it is
# doing a left multiply x^T=xlast^T*W
        for nbr in G[n]:
            x[nbr] += alpha * xlast[n] * G[n][nbr].get(weight, 1)
        x[n] += danglesum * dangling_weights.get(n, 0) + (1.0 - alpha) * p.get(n, 0)

# check convergence
err = sum([abs(x[n] - xlast[n]) for n in x])
if err < N*tol:
    return x
return x