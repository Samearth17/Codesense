#include <iostream> 
#include <string> 

std::string s = "AABCDBAGRQPY";
  
int commonChar(std::string str)  
{  
    int l = str.length();  
    int count[length] = { 0 };  
    int index;  
    int res = INT_MAX;  
  
    for (int i = 0; i < l; i++) {  
        index = str[i] - 'a';  
        count[index]++;  
  
        if (count[index] == 1)  
            res = i;  
    }  
  
    return res;  
}  

int main() 
{ 
    int index = commonChar(s); 
    if (index == INT_MAX) 
        std::cout << "Either all characters are repeating or string "
                        "is empty"; 
    else
        std::cout << "First non-repeating character is "
                  << s[index]; 
    return 0; 
}