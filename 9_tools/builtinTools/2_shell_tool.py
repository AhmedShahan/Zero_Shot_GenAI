from langchain_community.tools import ShellTool
Tool=ShellTool()

result=Tool("python --version")
print("Tools  Response:",result)