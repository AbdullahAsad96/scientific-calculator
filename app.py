
import streamlit as st
import math
import re

# Title for the Streamlit app
st.title("🔢 Scientific Calculator with Base Conversion and Advanced Operations")

# Dropdown to choose the input type (Decimal, Binary, Octal, Hexadecimal)
input_type = st.selectbox("Select Input Type", ["Decimal", "Binary", "Octal", "Hexadecimal"])

# Input box for user expression
expression = st.text_input(f"Enter your {input_type} expression:", "")

# Helper function to convert individual parts to decimal
def to_decimal(part, input_type):
    try:
        if input_type == "Binary":
            return int(part, 2)
        elif input_type == "Octal":
            return int(part, 8)
        elif input_type == "Hexadecimal":
            return int(part, 16)
        return float(part)  # Decimal supports floating-point values
    except ValueError:
        raise ValueError(f"Invalid input '{part}' for {input_type} format.")

# Helper functions for new operations
def factorial(n):
    return math.factorial(n)

def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Secure evaluation function with custom operations
def evaluate_expression(expr, input_type):
    try:
        # Split expression into numbers and operators
        parts = re.split(r'(\D)', expr)

        # Convert numeric parts to decimal if necessary
        decimal_expr = ''.join(
            str(to_decimal(part, input_type)) if part.strip().isdigit() else part
            for part in parts
        )

        # Secure evaluation with built-in functions + new operations
        result = eval(
            decimal_expr,
            {"__builtins__": None},  # Restrict access to built-in functions
            {
                "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "log": math.log, "pi": math.pi, "e": math.e, "pow": math.pow, "abs": abs,
                "P": permutation, "C": combination, "factorial": factorial
            }
        )

        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Button to evaluate expression
if st.button("Calculate"):
    result = evaluate_expression(expression, input_type)

    # Display results in multiple formats
    st.write(f"**Result in Decimal:** {result}")
    if isinstance(result, int):
        st.write(f"**Binary:** {bin(result)}")
        st.write(f"**Octal:** {oct(result)}")
        st.write(f"**Hexadecimal:** {hex(result)}")
    else:
        st.write("Conversions are only shown for integer results.")

# Sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
This calculator supports:
- **Base conversions:** Binary, Octal, Hexadecimal, Decimal
- **Arithmetic operations:** `+`, `-`, `*`, `/`
- **Trigonometry:** `sin(x)`, `cos(x)`, `tan(x)`
- **Logarithms:** `log(x)` (natural log)
- **Exponentials:** `pow(x, y)`, `e`, `pi`
- **Square root:** `sqrt(x)`
- **Absolute value:** `abs(x)`
- **Factorial:** `factorial(n)` or `n!`
- **Permutation:** `P(n, r)` or `nPr`
- **Combination:** `C(n, r)` or `nCr`
- **Percentage:** Use `%` directly in expressions
""")
