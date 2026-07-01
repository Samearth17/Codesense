#include <algorithm> 
#include <iostream> 
#include <string> 

int main() 
{ 
    // String array 
    std::string arr[] = { "Python", "Java", "C++" }; 
  
    int n = sizeof(arr) / sizeof(arr[0]); 
  
    // Sort the string array 
    std::sort(arr, arr + n); 
  
    // Print the sorted string array 
    for (int i = 0; i < n; i++) 
        std::cout << arr[i] << " "; 
    return 0; 
}