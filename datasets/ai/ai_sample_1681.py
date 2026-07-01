import matplotlib.pyplot as plt 
  
# x axis values 
x = [1, 2, 3, 4, 5] 
# corresponding y axis values 
y = [20, 30, 35, 38, 45] 
  
# plotting the points  
plt.bar(x, y) 
  
# naming the x axis 
plt.xlabel('Months') 
# naming the y axis 
plt.ylabel('Amount') 
# giving a title to my graph 
plt.title('Company Sales Over Last 5 Months') 
  
# function to show the plot 
plt.show()