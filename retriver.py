from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect Qdrant
client = QdrantClient(":memory:")

collection_name = "gfg_python_tutorial"

def retrieve_chunks(query, top_k=5):

    query_embedding = embedding_model.encode(query)

    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_embedding.tolist(),
        limit=top_k
    )

    results = []

    for hit in search_result:
        results.append(hit.payload["text"])

    return results
