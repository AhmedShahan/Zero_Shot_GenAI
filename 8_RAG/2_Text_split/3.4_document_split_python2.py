from langchain.text_splitter import PythonCodeTextSplitter

code = '''
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

# Example usage
calc = Calculator(10, 5)

print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
'''

splitter = PythonCodeTextSplitter(chunk_size=100, chunk_overlap=10)
chunks = splitter.split_text(code)

# Print split chunks
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---\n{chunk}")
