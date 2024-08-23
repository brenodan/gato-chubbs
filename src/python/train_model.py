import tensorflow as tf
import numpy as np

def generate_sample_data():
    # Generate some synthetic data: y = 2x + 1 + noise
    np.random.seed(0)
    X = np.random.rand(100, 1)  # 100 data points with a single feature
    y = 2 * X + 1 + np.random.normal(scale=0.1, size=(100, 1))
    return X, y

def build_regression_model():
    # Build a simple Sequential model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, input_shape=(1,))
    ])

    # Compile the model with mean squared error loss
    model.compile(optimizer='adam', loss='mse')
    return model

def train_regression_model(model, X, y, epochs=100):
    # Train the model
    history = model.fit(X, y, epochs=epochs, verbose=0)
    return model, history

def save_model(model, filepath='model.h5'):
    # Save the trained model to a file
    model.save(filepath)

if __name__ == "__main__":
    # Generate synthetic data
    X, y = generate_sample_data()

    # Build the regression model
    model = build_regression_model()

    # Train the model
    model, history = train_regression_model(model, X, y)

    # Save the model
    save_model(model)

    print("Model training complete and saved to 'model.h5'")