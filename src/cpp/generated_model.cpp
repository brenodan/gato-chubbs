#include <iostream>

// Model parameters (weights and bias)
float weight = 1.2424184083938599f;  // Example weight (to be replaced with actual value)
float bias = 1.0825127363204956f;    // Example bias (to be replaced with actual value)

// Function to make predictions
float predict(float x) {
    return weight * x + bias;
}

int main() {
    float input;
    std::cout << "Enter a value for x: ";
    std::cin >> input;

    float output = predict(input);
    std::cout << "The predicted value is: " << output << std::endl;

    return 0;
}
