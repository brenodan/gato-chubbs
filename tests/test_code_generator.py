import unittest
import torch
import tensorflow as tf
import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/python')))

from src.python.model import LinearRegressionModel 
from src.python.code_generator import load_model

class TestCodeGenerator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.model_path_tensorflow = os.path.join(os.path.dirname(__file__), 'test_data', 'test_model.h5')
        cls.model_path_pytorch = os.path.join(os.path.dirname(__file__), 'test_data', 'test_model.pth')
    
    def test_load_tensorflow_model(self):
        model = load_model(self.model_path_tensorflow, 'tensorflow')
        self.assertIsInstance(model, tf.keras.Model)

    def test_load_pytorch_model(self):
        model = load_model(self.model_path_pytorch, 'pytorch')
        print(f"Loaded model type: {type(model)}")
        self.assertIsInstance(model, LinearRegressionModel)

    def test_load_invalid_framework(self):
        with self.assertRaises(ValueError):
            load_model(self.model_path_pytorch, 'invalid_framework')

if __name__ == '__main__':
    unittest.main()
