def minimum_subset(data):
 features = list(data[0].keys())[:-1] # get the feature names
 min_num_feature = float('inf')
 features_selected = []
 
 for i in range(1,len(features)+1):
 for combination in itertools.combinations(features,i):
 num_correct, num_total = 0, 0
 for datum in data:
 if all(datum[feat] > 0.5 for feat in combination):
 if datum['category'] == 1:
 num_correct += 1
 elif all(datum[feat] <= 0.5 for feat in combination):
 if datum['category'] == 0:
 num_correct += 1
 num_total += 1
 
 if num_total == 0:
 continue
 accuracy = num_correct / num_total
 
 if accuracy == 1 and min_num_feature > i:
 min_num_feature = i
 features_selected = combination
 
 return features_selected