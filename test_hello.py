import unittest
from hello import hello_world

class TestClass(unittest.TestCase):
    def test_01(self):
        output = hello_world()
        self.assertEqual(output, "Hello, World!")


if __name__ == "__main__":
    unittest.main()