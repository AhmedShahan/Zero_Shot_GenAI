from langchain_community.document_loaders import CSVLoader

loader=CSVLoader('/home/shahanahmed/Zero_Shot_GenAI/RAG/Document_loader/documents/bdeconomy.csv')
docs=loader.load()

'''
এখানে প্রতিটা column একেকটা document হিসেবে আসে। 

'''

print(docs[0].page_content)
'''
Indicator: GDP
Value: 460
Unit: Billion USD
Year: 2025
Remarks: Estimated nominal GDP
'''

## Print All the contents

for i in range (len(docs)):
    print(docs[i].page_content)
    print("*************")

