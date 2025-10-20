import unittest
from main import Greeter

class TestGreeter(unittest.TestCase):
    def setUp(self):
        # Create an instance before each test
        self.greeter = Greeter()

    def test_say_hello_returns_correct_string(self):
        self.assertEqual(self.greeter.say_hello(), "Hello, world!")

    def test_say_hello_returns_string_type(self):
        self.assertIsInstance(self.greeter.say_hello(), str)

    def test_say_hello_not_empty(self):
        self.assertTrue(len(self.greeter.say_hello()) > 0)

if __name__ == "__main__":
    unittest.main()
