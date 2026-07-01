#include <iostream>
#include <math.h>

int main() 
{ 
    int x1 = 3; 
    int y1 = 4; 

    int x2 = -9; 
    int y2 = -2;

    float distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)); 

    std::cout << "Distance between the two points is: " << distance << std::endl; 

    return 0; 
}