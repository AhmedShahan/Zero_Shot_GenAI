from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


text='''
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



from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain.text_splitter import Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=400,
    chunk_overlap=0
)

chunk=splitter.split_text(text)
# print(chunk)

for i, docs in enumerate(chunk):
    print("Chunk ",i)
    print(docs)
    print("*"*50)