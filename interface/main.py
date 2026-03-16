from pyswip import Prolog
import os

def progress_bar(score, max_blocks=10):
    num_blocks = int((score / 100) * max_blocks)
    return "█" * num_blocks + " " * (max_blocks - num_blocks)

prolog = Prolog()

prolog.retractall("prerequisite(_,_)")

current_dir = os.path.dirname(os.path.abspath(__file__))
kb_path = os.path.join(current_dir, "..", "knowledge_base", "career_rules.pl")

prolog.consult(kb_path)

attributes = [
    {"name": "programming", "question": "Rate your programming skill (high/medium/low): "},
    {"name": "statistics", "question": "Rate your statistics skill (high/medium/low): "},
    {"name": "networking", "question": "Rate your networking skill (high/medium/low): "},
    {"name": "mathematics", "question": "Rate your mathematics skill (high/medium/low): "},
    {"name": "design", "question": "Rate your design skill (high/medium/low): "},
    {"name": "creativity", "question": "Rate your creativity (high/medium/low): "},
    {"name": "communication", "question": "Rate your communication skill (high/medium/low): "},
    {"name": "interest", "question": "What are you most interested in? (coding/data/design/marketing/security/networks): "}
]

user_inputs = {}

for attr in attributes:
    ans = input(attr["question"]).strip().lower()
    user_inputs[attr["name"]] = ans

for name, value in user_inputs.items():
    prolog.assertz(f"prerequisite({name}, {value})")

career_names = [
    "software_engineer",
    "data_analyst",
    "ui_ux_designer",
    "digital_marketer",
    "machine_learning_engineer",
    "cybersecurity_analyst",
    "network_engineer",
    "game_developer",
    "product_designer",
    "technical_writer"
]

display_names = {
    "software_engineer": "Software Engineer",
    "data_analyst": "Data Analyst",
    "ui_ux_designer": "UI/UX Designer",
    "digital_marketer": "Digital Marketer",
    "machine_learning_engineer": "Machine Learning Engineer",
    "cybersecurity_analyst": "Cybersecurity Analyst",
    "network_engineer": "Network Engineer",
    "game_developer": "Game Developer",
    "product_designer": "Product Designer",
    "technical_writer": "Technical Writer"
}

max_scores = {
    "software_engineer": 100,
    "data_analyst": 100,
    "ui_ux_designer": 90,
    "digital_marketer": 90,
    "machine_learning_engineer": 140,
    "cybersecurity_analyst": 110,
    "network_engineer": 100,
    "game_developer": 130,
    "product_designer": 110,
    "technical_writer": 60
}

career_scores = []

for career in career_names:

    result = list(prolog.query(f"career_score({career}, S)"))

    if result:
        raw_score = result[0]["S"]
        max_score = max_scores[career]
        score = int((raw_score / max_score) * 100)
    else:
        score = 0

    career_scores.append({
        "career": career,
        "score": score
    })

career_scores = [c for c in career_scores if c["score"] > 0]

career_scores.sort(key=lambda x: x["score"], reverse=True)

print("\nCareer Suitability Results")
print("-" * 50)

if career_scores:

    for item in career_scores:

        career = item["career"]
        score = item["score"]

        bar = progress_bar(score)

        reason_query = list(prolog.query(f"reason({career}, R)"))

        reason_text = ""

        if reason_query:
            reason_text = reason_query[0]["R"]

            if isinstance(reason_text, bytes):
                reason_text = reason_text.decode("utf-8")

        name = display_names.get(career)

        print(f"{name:<30} {bar} {score}%")

        if reason_text:
            print(f"  Reason: {reason_text}")

        print()

    best = career_scores[0]

    best_name = display_names.get(best["career"])
    best_score = best["score"]

    print("-" * 50)
    print("Top Career Recommendation")
    print("-" * 50)
    print(f"{best_name} ({best_score}%) is your best career match based on your skills and interests.")

else:
    print("No suitable careers found.")

