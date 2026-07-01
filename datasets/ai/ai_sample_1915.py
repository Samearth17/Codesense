import matplotlib.pyplot as plt 

# define data 
age = [15, 17, 20, 22, 25, 28, 33, 35, 37, 45, 50] 
sex = ["female","male","male","female","female","male","female","male","male","female","female"] 
income = [20000, 24000, 25000, 27000, 28000, 26000, 29000,
          33000, 31000, 50000, 52000] 

# create figure for plotting
fig = plt.figure()

# create 2D scatter graph of data
plt.scatter(age, income, c=sex, s=150) 

# add axis labels 
plt.xlabel('Age')
plt.ylabel('Income')

# add legend
plt.legend(["Female","Male"])

# show graph 
plt.show()