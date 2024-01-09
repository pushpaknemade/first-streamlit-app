from sentence_transformers import SentenceTransformer, util
 

def remove_duplicates_docs(docs):
    # Load a pre-trained BERT model for sentence embeddings
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
   
    # Extract document content and titles
    doc_contents = [doc.page_content for doc in docs]
    #doc_titles = [doc.metadata["title"] for doc in docs]
    
    # Compute embeddings for document content
    doc_embeddings = model.encode(doc_contents)
    # for i in range(len(docs)):
    #     print(doc_embeddings[i])
    
    # Calculate cosine similarity matrix
    similarity_matrix = util.pytorch_cos_sim(doc_embeddings, doc_embeddings)
    #print(len(similarity_matrix[0][1]))
    #print(similarity_matrix[0][1])
    
    # Set a threshold for similarity
    similarity_threshold = 1
    
    # Identify redundant documents
    redundant_indices = []
    for i in range(len(docs)):
        for j in range(i + 1, len(docs)):
            sim = similarity_matrix[i, j]
            if similarity_matrix[i, j] > similarity_threshold:
                redundant_indices.append(j)
    
    # Remove redundant documents
    filtered_docs = [doc for i, doc in enumerate(docs) if i not in redundant_indices]
    return filtered_docs