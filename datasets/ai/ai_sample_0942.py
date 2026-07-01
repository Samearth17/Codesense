import numpy as np

class DecisionTree():
    def __init__(self):
        self.max_depth = 3
        self.tree = self._build_tree()

    def _build_tree(self):
        tree = {}
        tree['index'] = 0 # features index
        tree['thresh'] = 0. # threshold for feature
        tree['left'] = None # left subtree
        tree['right'] = None # right subtree
        return tree
    
    def fit(self, X, y):   
        self._build_tree(X, y, self.tree, 0, self.max_depth)
        return self.tree
    
    def _build_tree(self, X, y, node, depth, max_depth):
        # get index of all the samples
        samples_index = np.arange(X.shape[0]) 
        # node is pure or depth == max_depth
        if self._check_purity(y, samples_index) or depth == max_depth:
            self.__set_leaf_node(y, node)
            return
        
        # find best split 
        feature_index, threshold = self._get_best_split(X, y, samples_index)
        
        # create two subtrees 
        left_index, right_index = self._split(X, feature_index, threshold, samples_index)
        
        # add the returned feature index to the node
        node['index'] = feature_index
        # add the returned node threshold  to the node
        node['thresh'] = threshold 
        
        # define left and right children 
        node['left'] = self._build_tree(X, y, {}, depth+1, max_depth) 
        node['right'] = self._build_tree(X, y, {}, depth+1, max_depth)
        
        # build right and left subtrees
        self._build_tree(X, y, node['left'], depth+1, max_depth)
        self._build_tree(X, y, node['right'], depth+1, max_depth)
    
    def _check_purity(self, y, samples_index):
        # check for the purity of label
        unique_labels = np.unique(y[samples_index])

        if len(unique_labels) == 1:
            return True
        else:
            return False
        
    def _get_best_split(self, X, y, samples_index):
        best_index = 0
        best_threshold = 0
        max_ig = 0
        n_features = X.shape[1]
        
        # loop through all the feature and get the best split
        for col in range(n_features):
            ig, threshold = self._information_gain(X, y, col, samples_index)
            
            if ig > max_ig:
                max_ig = ig
                best_index = col 
                best_threshold = threshold
                
        return best_index, best_threshold
        
    def _information_gain(self, X, y, col, samples_index):
        # function to calculate information gain
        total_sets = len(samples_index)
        classes, counts = np.unique(y[samples_index], return_counts=True)
        entropies = self._entropy(counts, total_sets)
                
        #sort the X sample
        sorted_x = np.sort(X[samples_index, col])
        threshold_sets = [(sorted_x[i]+sorted_x[i+1])/2 for i in range(len(sorted_x)-1)] 
        
        max_ig = 0
        best_threshold = 0
        for thr in threshold_sets:
            l_set, r_set = self._split(X, col, thr, samples_index)
            l_classes, l_counts = np.unique(y[l_set], return_counts=True)
            r_classes, r_counts = np.unique(y[r_set], return_counts=True)
            l_entrp = self._entropy(l_counts, len(l_set))
            r_entrp = self._entropy(r_counts, len(r_set))
            entrp = (len(l_set)*l_entrp + len(r_set)*r_entrp) / total_sets
            ig = entropies - entrp
            
            if ig > max_ig:
                max_ig = ig
                best_threshold = thr
                
        return max_ig, best_threshold
        
    def _entropy(self, counts, total_samples):
        # calculate the entropy
        entropies = np.sum([(-count/total_samples)*np.log2(count/total_samples) for count in counts])
        return entropies    
    
    def _split(self, X, col, thresh, samples_index):
        # split data
        left_index = np.argwhere(X[samples_index, col] < thresh).flatten()
        right_index = np.argwhere(X[samples_index, col] >= thresh).flatten()
        return left_index, right_index
    
    def __set_leaf_node(self, y, node):
        # get predictions 
        node['predictions'] = np.bincount(y).argmax()