# src/python/code_generator.py

import os
import torch
import tensorflow as tf
from model import LinearRegressionModel  # Import the model class

def load_model(filepath, framework):
    """Load the trained model based on the framework."""
    if framework == 'tensorflow':
        return tf.keras.models.load_model(filepath)
    elif framework == 'pytorch':
        model = LinearRegressionModel()
        state_dict = torch.load(filepath)
        model.load_state_dict(state_dict)
        model.eval()  # Set the model to evaluation mode
        return model
    else:
        raise ValueError(f"Unsupported framework: {framework}")

def extract_weights_and_bias(model, framework):
    """Extract the weights and bias from the trained model."""
    if framework == 'tensorflow':
        weights, bias = model.layers[0].get_weights()
        weight = weights[0][0]  # Assuming single input feature
        bias = bias[0]
    elif framework == 'pytorch':
        # Assuming model is a simple nn.Linear model
        weight = model.fc.weight.data[0].item()  # Assuming single input feature
        bias = model.fc.bias.data[0].item()
    else:
        raise ValueError(f"Unsupported framework: {framework}")
    
    return weight, bias

def replace_placeholders(template_content, weight, bias):
    """Replace placeholders in the template with actual model parameters."""
    code = template_content.replace("float weight = 2.0f;", f"float weight = {weight}f;")
    code = code.replace("float bias = 1.0f;", f"float bias = {bias}f;")
    return code

def generate_code(model, target_language='c', framework='tensorflow'):
    """Generate C or C++ code based on the trained model."""
    # Load the appropriate template
    template_file = f"../../templates/model_template.{target_language}"
    
    with open(template_file, 'r') as file:
        template_content = file.read()

    # Extract weights and bias from the model
    weight, bias = extract_weights_and_bias(model, framework)

    # Replace placeholders in the template
    generated_code = replace_placeholders(template_content, weight, bias)

    # Save the generated code
    output_file = f"../../src/{target_language}/generated_model.{target_language}"
    with open(output_file, 'w') as file:
        file.write(generated_code)

    print(f"Code generated and saved to '{output_file}'")

if __name__ == "__main__":
    # Specify the training framework ('tensorflow' or 'pytorch')
    framework = input("Enter training framework ('tensorflow' or 'pytorch'): ").strip().lower()

    # Specify the model file path
    if framework == 'tensorflow':
        model_file = 'model.h5'
    elif framework == 'pytorch':
        model_file = 'model.pth'  # Common extension for PyTorch models
    else:
        raise ValueError("Unsupported framework. Please choose 'tensorflow' or 'pytorch'.")

    # Load the trained model
    model = load_model(model_file, framework)

    # Specify target language ('c' or 'cpp')
    target_language = input("Enter target language ('c' or 'cpp'): ").strip().lower()

    # Generate the code
    generate_code(model, target_language, framework)
