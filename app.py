from retriever import retrieve_chunks
from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def generate_answer(query):

    chunks = retrieve_chunks(query)

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the question ONLY using the context below.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    while True:

        query = input("\nAsk Question: ")

        if query.lower() == "exit":
            break

        answer = generate_answer(query)

        print("\nAnswer:\n")
        print(answer)
