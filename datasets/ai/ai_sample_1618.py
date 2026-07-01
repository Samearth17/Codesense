import matplotlib.pyplot as plt

data = [
    ['Atlanta', 1500],
    ['Boston', 3000],
    ['Los Angeles', 2500],
    ['New York', 4000],
    ]

city = [x[0] for x in data]
cars = [x[1] for x in data]

plt.bar(city, cars)
plt.xlabel('City')
plt.ylabel('Number of cars')
plt.title('Number of cars in each city')
plt.show()