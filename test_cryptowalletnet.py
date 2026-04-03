# test_cryptowalletnet.py
"""
Tests for CryptoWalletNet module.
"""

import unittest
from cryptowalletnet import CryptoWalletNet

class TestCryptoWalletNet(unittest.TestCase):
    """Test cases for CryptoWalletNet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoWalletNet()
        self.assertIsInstance(instance, CryptoWalletNet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoWalletNet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
