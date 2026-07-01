import random

MAX_DISTANCE = 20

def race():
    print("Let's race!")
    car_a_distance = 0
    car_b_distance = 0

    while car_a_distance < MAX_DISTANCE and car_b_distance < MAX_DISTANCE:
        car_a_distance += random.randint(1, 5)
        car_b_distance += random.randint(1, 5)
        if car_a_distance == MAX_DISTANCE:
            print("Car A wins!")
        elif car_b_distance == MAX_DISTANCE:
            print("Car B wins!")
        else:
            print("Car A: " + str(car_a_distance) + " " + "Car B: " + str(car_b_distance))
    
race()