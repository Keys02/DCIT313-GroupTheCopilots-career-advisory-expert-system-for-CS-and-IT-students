from pyswip import Prolog
import os

prolog = Prolog()
prolog.retractall("prerequisite(_,_)")  # Clear previous facts


# Load the knowledge base
current_dir = os.path.dirname(os.path.abspath(__file__))
kb_path = os.path.join(current_dir, "..", "knowledge_base", "career_rules.pl")
prolog.consult(kb_path)

attributes = [
    {"name": "programming", "type": "skill", "question": "Rate your programming skill (high/medium/low): "},
    {"name": "statistics", "type": "skill", "question": "Rate your statistics skill (high/medium/low): "},
    {"name": "networking", "type": "skill", "question": "Rate your networking skill (high/medium/low): "},
    {"name": "mathematics", "type": "skill", "question": "Rate your mathematics skill (high/medium/low): "},
    {"name": "interest", "type": "interest", "question": "What are you most interested in? (coding/data/networks/security/designing): "}
]

user_inputs = {}

for attr in attributes:
    answer = input(attr["question"]).strip().lower()
    user_inputs[attr["name"]] = answer

# Assert facts
for name, value in user_inputs.items():
    prolog.assertz(f"prerequisite({name}, {value})")

# Query
results = list(prolog.query("career(X)"))

print("\n") # Leave a space between question and career recommendations

if results:
    print("Recommended careers:")
    for r in results:
        print("-", r["X"])
else:
    print("No matching careers found. Try adjusting your skills/interests.")

