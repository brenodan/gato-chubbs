## Gato Chubbs

Simple repository for testing converting python to models.

## Files

*src/python/train_model.py* && train_model_torch.py

- Script for generating a simple model from synthetic data using a linear relationship (y = 2x + 1 + noise). 
This script also builds a simple neural network with one dense layer, which is appropriate for linear regression. Next, the script trains the model using the synthetic dat (if provided) for a specified number of epochs (default is 100). Lastly, it saves the trained model to a .h5 file (model.h5). The train_model.py uses TensorFlow, while train_model_torch uses PyTorch.

*src/python/code_generator.py*

- Script for loading a trained model and extracting the weights and biases. Then, it replaces placeholders in the C/C++ templates.
Lastly, it saves the generated code in the appropriate directory.

*template/model_template.c & template/model_template.cpp*

- The templates files include placeholders for the model parameters (i.e., weight and bias). These values will be replaced with the actual weights and bias obtained from the trained TensorFlow model on the target files. Each template has a simple function named predict is defined to perform the linear regression calculation. The main function in both templates asks the user to input a value for x, calls the predict function, and prints the predicted output.

## Usage

1. Generate the target model.h5:
    ```bash
    python src/python/train_model.py
    ```
2. Run the code generator:
    ```bash
    python src/python/code_generator.py
    ```
3. Compile and Test
    C targets:
    ```
    gcc generated_model.c -o generated_model 
    ./generated_model
    ```
    For C++ sources:
    ```
    g++ generated_model.cpp -o generated_model
    ./generated_model
    ```