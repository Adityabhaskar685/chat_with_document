from rag.client import RAGClient
c = RAGClient("/teamspace/studios/this_studio/data/2401.08406.pdf")
for r in c.stream('what is rag'):
    print(r , end = '')
print("-" * 10 , "END" , '-' * 10)