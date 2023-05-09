from django.test import TestCase

# Create your tests here.
import unittest
from .views import index

class TestJS2PYTranslator(unittest.TestCase):

# I need to mock the API request fully, including the POST method

    def test_empty_string(self):
        result = index("")
        self.assertEqual(result, "")

    def test_single_line_assignment(self):
        js_code = "var a = 5;"
        py_code = "a = 5"
        result = index(js_code)
        self.assertEqual(result, py_code)

    def test_single_line_function(self):
        js_code = "function add(a, b) { return a + b; }"
        py_code = "def add(a, b):\n    return a + b"
        result = index(js_code)
        self.assertEqual(result, py_code)

    def test_multi_line_function(self):
        js_code = """
        function factorial(n) {
            if (n <= 1) {
                return 1;
            } else {
                return n * factorial(n - 1);
            }
        }
        """
        py_code = """
        def factorial(n):
            if n <= 1:
            return 1
        else:
        return n * factorial(n - 1)
        """
        result = index(js_code)
        self.assertEqual(result, py_code)

    def test_conditional_statement(self):
        js_code = """
        var age = 18;
        if (age >= 18) {
            console.log("You are an adult.");
        } else {
            console.log("You are a minor.");
        }
        """
        py_code = """
        age = 18
            if age >= 18:
            print("You are an adult.")
        else:
            print("You are a minor.")
        """
        result = index(js_code)
        self.assertEqual(result, py_code)


if __name__ == '__main__':
    unittest.main()