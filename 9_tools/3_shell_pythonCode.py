from langchain_community.tools import ShellTool

tool = ShellTool()

# Python code as a shell command
command = 'python3 -c "numbers = [5, 2, 9, 1, 7]; numbers.sort(); print(\'Sorted list:\', numbers)"'

# Run the command
result = tool.run(command)

# Print result
print("Shell Output:")
print(result)
