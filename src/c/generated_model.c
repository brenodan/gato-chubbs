#include <stdio.h>

// Model parameters (weights and bias)
float weight = 1.5631543397903442f;  // Example weight (to be replaced with actual value)
float bias = 0.3601642847061157f;    // Example bias (to be replaced with actual value)

// Function to make predictions
float predict(float x) {
    return weight * x + bias;
}

int main() {
    float input;
    printf("Enter a value for x: ");
    scanf("%f", &input);

    float output = predict(input);
    printf("The predicted value is: %f\n", output);

    return 0;
}
