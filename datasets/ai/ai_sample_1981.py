import os 
from multiprocessing import Process
  
def print_pid(): 
 try: 
 # Prints process id 
 print("Process ID is : ", os.getpid()) 
 except: 
 print("Error occured") 
  
if __name__ == "__main__": 
 # Create process 
 p1 = Process(target=print_pid) 
 p2 = Process(target=print_pid) 
 p3 = Process(target=print_pid) 
  
 # Start process 
 p1.start() 
 p2.start() 
 p3.start() 
  
 # Wait till process finish execution 
 p1.join() 
 p2.join() 
 p3.join()