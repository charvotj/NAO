import re
import numpy as np

def substitute_numbers(latex_equation):
    # Regular expression to match numerical values in LaTeX format
    pattern = r'\\num{(.+?)}'

    # Find all numerical values in the LaTeX equation and convert them to floats
    numerical_values = [float(match.group(1)) for match in re.finditer(pattern, latex_equation)]

    # Replace numerical values with placeholders
    substituted_equation = re.sub(pattern, 'number', latex_equation)

    # Perform the substitution of numerical values
    for num in numerical_values:
        substituted_equation = substituted_equation.replace('number',f'{num}',1)

    return substituted_equation

def substitute_fractions(latex_equation):
    # Regular expression to match numerical values in LaTeX format
    pattern = r'\\frac{(.+?)}{(.+?)}'

    # Find all numerical values in the LaTeX equation and convert them to floats
    fraction_values = [(match.group(1),match.group(2)) for match in re.finditer(pattern, latex_equation)]

    # Replace numerical values with placeholders
    substituted_equation = re.sub(pattern, '((citatel)/(jmenovatel))', latex_equation)

    for frac in fraction_values:
        # Perform the substitution of numerical values
        substituted_equation = substituted_equation.replace('citatel',f'{frac[0]}',1)
        substituted_equation = substituted_equation.replace('jmenovatel',f'{frac[1]}',1)

    return substituted_equation

def substitute_symbols(latex_equation):
    sub_eq = latex_equation.replace('\\cdot','*')
    sub_eq = sub_eq.replace('^','**')
    sub_eq = sub_eq.replace('{','(')
    sub_eq = sub_eq.replace('}',')')
    # and other will follow
    return sub_eq

def parse_and_calc(eq):
    # Example usage
    eq = substitute_numbers(eq)
    eq = substitute_fractions(eq)
    eq = substitute_fractions(eq)
    eq = substitute_fractions(eq)
    eq = substitute_symbols(eq)


    # Evaluate the expression
    return eval(eq)



while True:
    # Get string input from the user
    user_input = input("Enter a latex equation (type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the loop...")
        break
    else:
        print(parse_and_calc(user_input))

