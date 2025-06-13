"""
    This lookup returns the result of two numbers based on the math operation.
"""

from ansible.plugins.lookup import LookupBase

def add(num1, num2):
    return num1 + num2
    
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

class LookupModule(LookupBase):
    def run(self, terms, **kwargs):
        num1 = float(terms[0])
        num2 = float(terms[1])
        operation = terms[2].lower()

        # Choose operation 

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            if num2 == 0:
                raise ValueError("Division by 0 is not allowed.")
            result = divide(num1, num2)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

        return [result]




    

