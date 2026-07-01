data = [[18, 'Beginner'],
[32, 'Intermediate'],
[40, 'Advanced'],
[12, 'Beginner'],
[20, 'Intermediate']]

classifier = {
 'Low/Beginner': [],
 'Medium/Intermediate': [],
 'High/Advanced': []
}

def classify(data):
 for point in data:
  score = point[0]
  level = point[1]
  if score < 20 and level == 'Beginner':
   classifier['Low/Beginner'].append(point)
  elif score >= 20 and score < 40 and level == 'Intermediate':
   classifier['Medium/Intermediate'].append(point)
  elif score >= 40 and level == 'Advanced':
   classifier['High/Advanced'].append(point)

classify(data)
print(classifier)