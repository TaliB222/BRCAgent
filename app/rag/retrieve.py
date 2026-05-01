knowledge_base = [
    "Radiation therapy can cause fatigue and skin irritation.",
    "Tamoxifen side effects may last several months.",
    "Support groups can help patients cope emotionally."
]

def retrieve_context(query):
    # MVP: מחזיר הכל (בהמשך נחליף ל-embeddings)
    return "\n".join(knowledge_base)