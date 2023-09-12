"""
import click
from calculator import Calculator


@click.command()
def main():
    calculator = Calculator()

    click.echo("Welcome to the Math Operation Calculator!")
    click.echo("Please choose an operation:")
    click.echo("1. Add")
    click.echo("2. Subtract")
    click.echo("3. Multiply")
    click.echo("4. Divide")
    click.echo("5. Square Root")
    click.echo("6. Exponentiate")

    operation = click.prompt("Enter the operation number", type=int)

    if operation == 1:
        a = click.prompt("Enter the first number", type=float)
        b = click.prompt("Enter the second number", type=float)
        result = calculator.add(a, b)
        click.echo(f"The sum of {a} and {b} is {result}")
    elif operation == 2:
        a = click.prompt("Enter the first number", type=float)
        b = click.prompt("Enter the second number", type=float)
        result = calculator.subtract(a, b)
        click.echo(f"The difference between {a} and {b} is {result}")
    elif operation == 3:
        a = click.prompt("Enter the first number", type=float)
        b = click.prompt("Enter the second number", type=float)
        result = calculator.multiply(a, b)
        click.echo(f"The product of {a} and {b} is {result}")
    elif operation == 4:
        a = click.prompt("Enter the first number", type=float)
        b = click.prompt("Enter the second number", type=float)
        result = calculator.divide(a, b)
        click.echo(f"The quotient of {a} and {b} is {result}")
    elif operation == 5:
        a = click.prompt("Enter the number", type=float)
        result = calculator.square_root(a)
        click.echo(f"The square root of {a} is {result}")
    elif operation == 6:
        a = click.prompt("Enter the base number", type=float)
        b = click.prompt("Enter the exponent", type=float)
        result = calculator.exponentiate(a, b)
        click.echo(f"{a} raised to the power of {b} is {result}")
    else:
        click.echo("Invalid operation number. Please try again.")

    choice = click.prompt("Do you want to continue? (yes/no)", type=str)
    if choice.lower() == "yes":
        main()
    else:
        click.echo("Thank you for using the Math Operation Calculator!")


if __name__ == "__main__":
    main()
"""
