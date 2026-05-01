def should_respond(classification):
    if not classification["relevant"]:
        return False

    if classification["sensitivity_level"] == "high" and classification["intent"] != "question":
        return False

    return classification["should_respond"]