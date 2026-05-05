from flask import Blueprint, request, render_template
from app.classifier.classify import classify_text
from app.decision.rules import should_respond
from app.rag.retrieve import retrieve_context
from app.generator.generate import generate_response

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    age = data.get("age")
    cancer_type = data.get("cancer_type")
    brca = data.get("brca")
    stage = data.get("stage")
    text = data.get("text")

    classification = classify_text(text)

    if not should_respond(classification):
        return {"response": "No response"}

    context = retrieve_context(text + " " + str(cancer_type))

    enriched_input = f"""
Age: {age}
Cancer type: {cancer_type}
BRCA status: {brca}
Stage: {stage}

User text:
{text}
"""

    response = generate_response(enriched_input, context, classification)

    return {"response": response}