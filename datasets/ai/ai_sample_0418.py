list=[2,4,5,7,1,3]

even_sum= 6
odd_sum= 15

def sum_even_odd(list):
    even_sum=0
    odd_sum=0
    
    for num in list:
        if num % 2 == 0:
            even_sum+=num
        else:
            odd_sum+=num 
    
    print("even_sum=",even_sum)
    print("odd_sum=",odd_sum)
    
sum_even_odd(list)