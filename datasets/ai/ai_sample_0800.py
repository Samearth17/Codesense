from collections import defaultdict

def calculate_relevance_score(query_terms):
    relevance_score = defaultdict(int)
    # Pre-process the query and extract each term
    terms = query_terms.split()
    # Calculate relevance scores for each term
    for term in terms:
        relevance_score[term] = len(term) # Simple example, can be replaced with a better relevance score
    return relevance_score

def search(query_terms):
    relevance_score = calculate_relevance_score(query_terms)
    # Perform the search and sort the results based on the relevance score
    search_results = sorted(search_results, key=lambda r: relevance_score[r], reverse=True)
    # Return the results
    return search_results