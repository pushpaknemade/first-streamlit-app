import streamlit as st
from remove_dup import remove_duplicates_docs
from langchain.docstore.document import Document

documents = [
    Document(page_content='content 1', metadata={'title': 'title 1', 'id': 1}),
    Document(page_content='content 2', metadata={'title': 'title 2', 'id': 2}),
    Document(page_content='content 3', metadata={'title': 'title 3', 'id': 3}),
    Document(page_content='content 4', metadata={'title': 'title 4', 'id': 4}),
    Document(page_content='content 5', metadata={'title': 'title 5', 'id': 5}),
    Document(page_content='content 6', metadata={'title': 'title 6', 'id': 6}),
    Document(page_content='content 7', metadata={'title': 'title 7', 'id': 7}),
    Document(page_content='content 8', metadata={'title': 'title 8', 'id': 8}),
    Document(page_content='content 9', metadata={'title': 'title 9', 'id': 9}),
    Document(page_content='content 10', metadata={'title': 'title 10', 'id': 10}),
    Document(page_content='content 11', metadata={'title': 'title 11', 'id': 11}),
    Document(page_content='content 12', metadata={'title': 'title 12', 'id': 12}),
    Document(page_content='content 13', metadata={'title': 'title 13', 'id': 13}),
    Document(page_content='content 14', metadata={'title': 'title 14', 'id': 14}),
    Document(page_content='content 15', metadata={'title': 'title 15', 'id': 15}),
    Document(page_content='content 16', metadata={'title': 'title 16', 'id': 16}),
    Document(page_content='content 17', metadata={'title': 'title 17', 'id': 17}),
    Document(page_content='content 18', metadata={'title': 'title 18', 'id': 18}),
    Document(page_content='content 19', metadata={'title': 'title 19', 'id': 19}),
    Document(page_content='content 20', metadata={'title': 'title 20', 'id': 20})
]

filtered_docs = remove_duplicates_docs(documents)

for i,doc in enumerate(filtered_docs):
    st.markdown(str(i)+") "+doc.page_content)
