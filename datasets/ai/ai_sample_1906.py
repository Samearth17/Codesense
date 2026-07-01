from queue import PriorityQueue 

class Process: 
    def __init__(self, id, cpuburst, priority): 
        self.id = id 
        self.cpuburst = cpuburst 
        self.priority = priority 
        return
  
    def __lt__(self, other):
        return self.priority < other.priority

def Scheduler(processes): 
    
    ready_queue = PriorityQueue() 
    result = [] 
    
    for process in processes: 
        ready_queue.put(process) 
    
    while (not ready_queue.empty()): 
        process = ready_queue.get() 
        result.append([process.id, process.cpuburst]) 
    
    return result 
  
if __name__ =="__main__": 
    processes = [Process(1, 10, 1), Process(2, 6, 4), Process(3, 4, 5)] 
    print(Scheduler(processes)) 

Output:
[[1, 10],[2, 6],[3, 4]]