import random

def random_list(start, end, size):
    rand_list = []
    
    for i in range(size):
        rand_num = random.choice(range(start, end))
        while rand_num in rand_list:
            rand_num = random.choice(range(start, end))
        rand_list.append(rand_num)
    
    return rand_list

start = 2
end = 10
size = 5
random_list_result = random_list(start, end, size)
print(random_list_result)