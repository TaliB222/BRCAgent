# knowledge_base = [
#     "Radiation therapy can cause fatigue and skin irritation.",
#     "Tamoxifen side effects may last several months.",
#     "Support groups can help patients cope emotionally."
# ]

# def retrieve_context(query):
#     # MVP: מחזיר הכל (בהמשך נחליף ל-embeddings)
#     return "\n".join(knowledge_base)

from pathlib import Path


def load_documents(folder_path="data/websites"):
    docs = []

    for file in Path(folder_path).glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            docs.append(f.read())

    return docs


def split_into_chunks(text, chunk_size=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# נטען מסמכים
documents = load_documents()

# נהפוך ל-chunks
chunks = []
for doc in documents:
    chunks.extend(split_into_chunks(doc))


def retrieve_context(query):
    query = query.lower()
    query_words = [w for w in query.split() if len(w) > 2]

    scored_chunks = []

    for chunk in chunks:
        chunk_lower = chunk.lower()

        # ניקוד לפי כמה מילים תואמות
        score = sum(1 for word in query_words if word in chunk_lower)

        if score > 0:
            scored_chunks.append((score, chunk))

    # מיון לפי ציון
    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    # אם אין התאמות
    if not scored_chunks:
        return ""

    # מחזירים top 3 chunks
    top_chunks = [chunk for _, chunk in scored_chunks[:3]]

    return "\n\n".join(top_chunks)