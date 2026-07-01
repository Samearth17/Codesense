def find_important_features(X, y):
    """Finds the most important features for a given dataset.

    Args:
        X(ndarray): The independent variables.
        y(ndarray): The dependent variable.

    Returns:
        important_features(list): The list of most important features.
    """

    # Initializing list with default values
    important_features = []

    # Initializing feature importance score
    feature_importance_scores = [0] * X.shape[1]

    # Iterating over all the features
    for i in range(X.shape[1]):
        # Calculating the mutual information score
        score = mutual_info_score(X[:, i], y)

        # Updating feature importance scores
        feature_importance_scores[i] += score

    # Sorting the feature importance scores
    sorted_scores_idx = list(reversed(np.argsort(feature_importance_scores)))

    # Retrieving top-k features
    for idx in sorted_scores_idx:
        important_features.append(idx)

    return important_features