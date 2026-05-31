
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

app = Flask(__name__)


def generate_local_report(data):
    """
    Local fallback AI-style analysis.
    This function does not require an external API.
    """

    team_a = data.get("team_a", "")
    team_b = data.get("team_b", "")
    score = data.get("score", "")
    shots = data.get("shots", "")
    possession = data.get("possession", "")
    events = data.get("events", "")

    return {
        "match_summary": f"{team_a} vs {team_b} - Score: {score}. {team_a} had {possession}% possession and the shot count was {shots}.",
        "attacking_performance": f"{team_a} showed attacking activity with {shots} shots. The scoreline suggests that key chances were converted effectively.",
        "defensive_risks": f"The event information suggests that defensive transitions, set pieces, and late-game concentration should be reviewed.",
        "tactical_observations": f"{team_a} should maintain attacking efficiency, while {team_b} may need to improve defensive recovery and chance creation.",
        "coaching_recommendations": "Review key match footage, focus on transition moments, improve set-piece defending, and use the event timeline to support tactical feedback.",
        "key_events_used": events,
        "human_review_note": "The generated report should be reviewed and edited by a human user before final decision-making.",
        "timestamp": datetime.now().isoformat()
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/sample-report")
def sample_report():
    return jsonify({
        "success": True,
        "data": {
            "match_summary": "Sample report generated successfully.",
            "strengths": "The system can receive data and return structured analysis.",
            "risks": "The output should be reviewed by a human user.",
            "recommendations": "Use this endpoint to test whether the API is working."
        },
        "human_review_required": True
    })


@app.route("/api/analyse", methods=["POST"])
def analyse():
    data = request.get_json() or {}

    required_fields = ["team_a", "team_b", "score", "shots", "possession", "events"]
    missing = [field for field in required_fields if not data.get(field)]

    if missing:
        return jsonify({
            "success": False,
            "error": "Missing required fields: " + ", ".join(missing)
        }), 400

    report_data = generate_local_report(data)

    return jsonify({
        "success": True,
        "data": report_data,
        "human_review_required": True,
        "human_review_note": "The generated report should be reviewed and edited by a human user before final decision-making."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
