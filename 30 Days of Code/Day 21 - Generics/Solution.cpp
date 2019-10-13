/*
@author: zepman85
*/

#include <iostream>
#include <vector>
#include <string>

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

template <typename T>
void printArray(std::vector<T>& genericVec)
{
    for (auto &val : genericVec)
    {
        std::cout << val << '\n';        
    }
}

// Write your code here

int main() {
	int n = 0;
	
	std::cin >> n;
	std::vector<int> int_vector(n);
	for (int i = 0; i < n; ++i) {
		int value;
		std::cin >> value;
		int_vector[i] = value;
	}
	
	std::cin >> n;
	std::vector<std::string> string_vector(n);
	for (int i = 0; i < n; ++i) {
		std::string value;
		std::cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<std::string>(string_vector);

	return 0;
}