from pyswip import Prolog
import os

# -----------------------------------------
# Function to create terminal progress bar
# -----------------------------------------
def progress_bar(score, max_blocks=10):
    num_blocks = int((score / 100) * max_blocks)
    return "█" * num_blocks + " " * (max_blocks - num_blocks)

# -------------------------
# Initialize Prolog
# -------------------------
prolog = Prolog()
prolog.retractall("prerequisite(_,_)")

# Load knowledge base
current_dir = os.path.dirname(os.path.abspath(__file__))
kb_path = os.path.join(current_dir, "..", "knowledge_base", "career_rules.pl")
prolog.consult(kb_path)

# -------------------------
# Questions for the user
# -------------------------
attributes = [
    {"name": "programming", "question": "Rate your programming skill (high/medium/low): "},
    {"name": "statistics", "question": "Rate your statistics skill (high/medium/low): "},
    {"name": "networking", "question": "Rate your networking skill (high/medium/low): "},
    {"name": "mathematics", "question": "Rate your mathematics skill (high/medium/low): "},
    {"name": "design", "question": "Rate your design skill (high/medium/low): "},
    {"name": "creativity", "question": "Rate your creativity (high/medium/low): "},
    {"name": "communication", "question": "Rate your communication skill (high/medium/low): "},
    {"name": "interest", "question": "What are you most interested in? (coding/data/design/marketing): "}
]

# -------------------------
# Collect user input
# -------------------------
user_inputs = {}

for attr in attributes:
    answer = input(attr["question"]).strip().lower()
    user_inputs[attr["name"]] = answer

# -------------------------
# Assert user facts into Prolog
# -------------------------
for name, value in user_inputs.items():
    prolog.assertz(f"prerequisite({name}, {value})")

# -------------------------
# Career display names
# -------------------------
display_names = {
    "software_engineer": "Software Engineer",
    "data_analyst": "Data Analyst",
    "ui_ux_designer": "UI/UX Designer",
    "digital_marketer": "Digital Marketer"
}

# -------------------------
# Careers to evaluate
# -------------------------
career_names = [
    "software_engineer",
    "data_analyst",
    "ui_ux_designer",
    "digital_marketer"
]

career_scores = []

# -------------------------
# Get scores from Prolog
# -------------------------
for career in career_names:

    score_result = list(prolog.query(f"career_score({career}, S)"))

    if score_result:
        score = score_result[0]["S"]
    else:
        score = 0

    career_scores.append({
        "career": career,
        "score": score
    })

# -------------------------
# Remove careers with 0 score
# -------------------------
career_scores = [c for c in career_scores if c["score"] > 0]

# -------------------------
# Sort careers by score
# -------------------------
career_scores.sort(key=lambda x: x["score"], reverse=True)

# -------------------------
# Display Results
# -------------------------
print("\nCareer Suitability Results")
print("-" * 50)

if career_scores:

    for item in career_scores:

        career = item["career"]
        score = item["score"]

        bar = progress_bar(score)

        # Get explanation
        reason_result = list(prolog.query(f"reason({career}, R)"))

        reason_text = ""

        if reason_result:
            reason_text = reason_result[0]["R"]

            if isinstance(reason_text, bytes):
                reason_text = reason_text.decode("utf-8")

        # Proper display name
        display_name = display_names.get(
            career,
            career.replace("_", " ").title()
        )

        print(f"{display_name:<25} {bar} {score}%")

        if reason_text:
            print(f"  Reason: {reason_text}")

        print()

    # -------------------------
    # Best Career Recommendation
    # -------------------------
    best_career = career_scores[0]

    best_name = display_names.get(
        best_career["career"],
        best_career["career"].replace("_", " ").title()
    )

    best_score = best_career["score"]

    print("-" * 50)
    print("Top Career Recommendation")
    print("-" * 50)

    print(f"{best_name} ({best_score}%) is your best career match based on your skills and interests.")

else:
    print("No matching careers found. Try adjusting your skills/interests.")

