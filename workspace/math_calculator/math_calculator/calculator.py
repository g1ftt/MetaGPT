## calculator.py

import math


class Calculator:
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The difference between the two numbers.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The quotient of the two numbers.
        """
        return a / b

    def square_root(self, a: float) -> float:
        """
        Calculate the square root of a number.

        Args:
            a (float): The number.

        Returns:
            float: The square root of the number.
        """
        return math.sqrt(a)

    def exponentiate(self, a: float, b: float) -> float:
        """
        Calculate the exponentiation of a number.

        Args:
            a (float): The base number.
            b (float): The exponent.

        Returns:
            float: The result of raising the base number to the exponent.
        """
        return a ** b

