import tensorflow as tf
import os

def load_model(filepath='model.h5'):
    """Load the trained TensorFlow model."""
    return tf.keras.models.load_model(filepath)

def extract_weights_and_bias(model):
    """Extract the weights and bias from the trained model."""
    weights, bias = model.layers[0].get_weights()
    weight = weights[0][0]  # Assuming single input feature
    bias = bias[0]
    return weight, bias

def replace_placeholders(template_content, weight, bias):
    """Replace placeholders in the template with actual model parameters."""
    code = template_content.replace("float weight = 2.0f;", f"float weight = {weight}f;")
    code = code.replace("float bias = 1.0f;", f"float bias = {bias}f;")
    return code

def generate_code(model, target_language='c'):
    """Generate C or C++ code based on the trained model."""
    # Load the appropriate template
    template_file = f"../../templates/model_template.{target_language}"
    
    with open(template_file, 'r') as file:
        template_content = file.read()

    # Extract weights and bias from the model
    weight, bias = extract_weights_and_bias(model)

    # Replace placeholders in the template
    generated_code = replace_placeholders(template_content, weight, bias)

    # Save the generated code
    output_file = f"../../src/{target_language}/generated_model.{target_language}"
    with open(output_file, 'w') as file:
        file.write(generated_code)

    print(f"Code generated and saved to '{output_file}'")

if __name__ == "__main__":
    # Load the trained model
    model = load_model()

    # Specify target language ('c' or 'cpp')
    target_language = input("Enter target language ('c' or 'cpp'): ").strip().lower()

    # Generate the code
    generate_code(model, target_language)
