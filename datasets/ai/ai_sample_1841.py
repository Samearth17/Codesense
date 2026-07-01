import matplotlib.pyplot as plt

class_A = [85, 75, 95]
class_B = [89, 73, 72]
class_C = [82, 81, 89]

classes = ['Class A', 'Class B', 'Class C']

plt.bar(classes, [sum(class_A) / len(class_A), 
sum(class_B) / len(class_B), sum(class_C)/ len(class_C)])

plt.xlabel('Classes')
plt.ylabel('Average Score')
plt.title('Exam Scores')
plt.show()