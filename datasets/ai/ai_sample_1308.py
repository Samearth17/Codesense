"""
Create a Python program to classify an animal into one of four classes

"""
# define the characteristics
is_cold_blooded = True
lays_eggs = True
has_scales = True

# determine the animal class
if is_cold_blooded and lays_eggs and has_scales:
    animal_class = 'Reptile'
elif is_cold_blooded and lays_eggs and not has_scales:
    animal_class = 'Bird'
elif is_cold_blooded and not lays_eggs and has_scales:
    animal_class = 'Fish'
elif not is_cold_blooded and not lays_eggs and not has_scales:
    animal_class = 'Mammal'

# print the result
print('The animal belongs to class:', animal_class)