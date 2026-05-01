from classifier.classify import classify_text
from decision.rules import should_respond
from rag.retrieve import retrieve_context
from generator.generate import generate_response


def run_agent(text):
    classification = classify_text(text)

    if not should_respond(classification):
        return "No response"

    context = retrieve_context(text)
    response = generate_response(text, context)

    return response


if __name__ == "__main__":
    sample = "יש למישהי ניסיון עם תופעות לוואי של הקרנות?"
    print(run_agent(sample))