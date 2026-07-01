// In C
#include <stdio.h>

int main()
{
    int x = 0;
    // Recurse to infinity
    x = main();
    printf("Infinite Recursion Complete");
    return 0;
}

// In Python
def recursive_call():
  recursive_call()

recursive_call()