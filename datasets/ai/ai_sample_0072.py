import time
import heuristics_algorithm1
import heuristics_algorithm2

#input data for algorithms
data1 = ...
data2 = ...

#Evaluate and compare the performance of two different heuristics algorithms
start = time.time()
result1 = heuristics_algorithm1.run(data1)
end = time.time()
time1 = end - start

start = time.time()
result2 = heuristics_algorithm2.run(data2)
end = time.time()
time2 = end - start

if time1 < time2:
    print("Algorithm 1 is faster than algorithm 2")
elif time2 < time1:
    print("Algorithm 2 is faster than algorithm 1")
else:
    print("Both algorithms have the same performance time")