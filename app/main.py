from app.classifier.classify import classify_text
from app.decision.rules import should_respond
from app.rag.retrieve import retrieve_context
from app.generator.generate import generate_response


def run_agent(text):
    classification = classify_text(text)

    print("\n[CLASSIFIER]")
    print(classification)

    if not should_respond(classification):
        return "No response (filtered by decision layer)"

    context = retrieve_context(text)

    print("\n[CONTEXT]")
    print(context)

    response = generate_response(text, context, classification)

    return response


if __name__ == "__main__":
    test_input = "יש למישהי ניסיון עם תסמינים של גיל המעבר?"

    print("\n[USER INPUT]")
    print(test_input)

    result = run_agent(test_input)

    print("\n[FINAL RESPONSE]")
    print(result)