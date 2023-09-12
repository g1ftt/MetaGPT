## Original Requirements:
The boss wants you to create a sample math operation calculator in Python.

## Product Goals:
- Create a simple and user-friendly math operation calculator.
- Provide accurate and efficient calculations.
- Support a variety of math operations.

## User Stories:
- As a user, I want to be able to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
- As a user, I want to be able to input multiple numbers and perform calculations on them.
- As a user, I want to be able to see the result of my calculations displayed clearly on the calculator.
- As a user, I want to be able to easily clear the calculator and start a new calculation.
- As a user, I want to be able to perform more advanced operations such as square root and exponentiation.

## Competitive Analysis:
- Python Snake Game: A popular Python game that allows users to control a snake and eat food to grow longer.
- Python Calculator: A simple Python calculator that allows users to perform basic arithmetic operations.
- Python Math Library: A comprehensive library in Python that provides various mathematical functions and constants.
- Python Graphing Calculator: A Python calculator that not only performs calculations but also allows users to graph functions.
- Python Scientific Calculator: A Python calculator that includes advanced scientific functions such as trigonometry and logarithms.
- Python Matrix Calculator: A Python calculator that specializes in matrix operations and calculations.
- Python Financial Calculator: A Python calculator that helps users with financial calculations such as loan payments and interest rates.

## Competitive Quadrant Chart:
```mermaid
quadrantChart
    title Reach and engagement of calculators
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 Python Snake Game: [0.3, 0.6]
    quadrant-2 Python Calculator: [0.45, 0.23]
    quadrant-3 Python Math Library: [0.57, 0.69]
    quadrant-4 Python Graphing Calculator: [0.78, 0.34]
    quadrant-1 Python Scientific Calculator: [0.4, 0.34]
    quadrant-2 Python Matrix Calculator: [0.35, 0.78]
    quadrant-3 Python Financial Calculator: [0.5, 0.6]
    "Our Target Product": [0.6, 0.7]
```

## Requirement Analysis:
The product should be a simple and efficient math operation calculator that supports basic arithmetic operations, as well as more advanced operations such as square root and exponentiation. It should provide accurate calculations and have a clear and user-friendly interface. The calculator should allow users to input multiple numbers and perform calculations on them. It should also have a clear display of the calculation results and provide an option to clear the calculator and start a new calculation.

## Requirement Pool:
```python
[
    ("Support addition operation", "P0"),
    ("Support subtraction operation", "P0"),
    ("Support multiplication operation", "P0"),
    ("Support division operation", "P0"),
    ("Support square root operation", "P1")
]
```

## UI Design draft:
The calculator will have a simple and clean design. It will include a number pad for inputting numbers and buttons for performing various operations such as addition, subtraction, multiplication, division, square root, and exponentiation. The display area will show the input numbers and the result of the calculation. There will also be a clear button to reset the calculator and start a new calculation. The layout will be intuitive and easy to use, with clear labels and buttons arranged in a logical manner.

## Anything UNCLEAR:
There are no unclear points.