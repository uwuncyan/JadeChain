# test_jadechain.py
"""
Tests for JadeChain module.
"""

import unittest
from jadechain import JadeChain

class TestJadeChain(unittest.TestCase):
    """Test cases for JadeChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JadeChain()
        self.assertIsInstance(instance, JadeChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JadeChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
