from langchain_core.runnables import RunnablePassthrough

x="What is Ai"
runnables=RunnablePassthrough()

y=runnables.invoke(x)
print(y)

'''
RunnablePassthrough is just passing the Result

'''