import unittest
import sys
import os
import tensorflow as tf
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/python')))
from src.python.code_generator import extract_weights_and_bias
from src.python.model import LinearRegressionModel  # Ensure this is the correct import for your setup

class TestWeightExtraction(unittest.TestCase):
    
    def test_extract_tensorflow_weights(self):
        # Given a TensorFlow model
        model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
        model.set_weights([tf.constant([[2.0]]), tf.constant([1.0])])
        weight, bias = extract_weights_and_bias(model, 'tensorflow')
        self.assertEqual(weight, 2.0)
        self.assertEqual(bias, 1.0)

    def test_extract_pytorch_weights(self):
        # Given a PyTorch model
        model = LinearRegressionModel()
        model.fc.weight.data.fill_(2.0)
        model.fc.bias.data.fill_(1.0)
        weight, bias = extract_weights_and_bias(model, 'pytorch')
        self.assertEqual(weight, 2.0)
        self.assertEqual(bias, 1.0)

    def test_extract_invalid_framework(self):
        # Given an invalid framework
        with self.assertRaises(ValueError):
            extract_weights_and_bias(None, 'invalid_framework')

if __name__ == '__main__':
    unittest.main()
