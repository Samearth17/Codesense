#include <iostream>
#include <string>

void say_hello(std::string name="") {
    if (name.empty()) {
        std::cout << "Hello World" << std::endl;
    } else {
        std::cout << "Hello, " << name << "!" << std::endl;
    }
}

int main() {
    say_hello();
    say_hello("John");
    return 0;
}