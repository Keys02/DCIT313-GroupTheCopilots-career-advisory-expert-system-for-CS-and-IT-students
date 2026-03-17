from pyswip import Prolog
import os

# Function to create a visual progress bar based on percentage score
def progress_bar(score, max_blocks=10):
    # Convert percentage score into number of filled blocks
    num_blocks = int((score / 100) * max_blocks)
    return "█" * num_blocks + " " * (max_blocks - num_blocks)

# Initialize Prolog engine
prolog = Prolog()

# Clear any previous user inputs stored in Prolog
prolog.retractall("prerequisite(_,_)")

# Get the current file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to the Prolog knowledge base file
kb_path = os.path.join(current_dir, "..", "knowledge_base", "career_rules.pl")

# Load the Prolog knowledge base
prolog.consult(kb_path)

# List of questions to ask the user
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

# Dictionary to store user responses
user_inputs = {}

# Ask user all questions and store responses
for attr in attributes:
    ans = input(attr["question"]).strip().lower()
    user_inputs[attr["name"]] = ans

# Send user inputs to Prolog as facts
for name, value in user_inputs.items():
    prolog.assertz(f"prerequisite({name}, {value})")

# List of careers to evaluate
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

# Friendly display names for output
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

# Maximum possible score for each career (used for normalization)
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

# List to store computed career scores
career_scores = []

# Loop through each career and calculate its score
for career in career_names:

    # Query Prolog to compute score for this career
    result = list(prolog.query(f"career_score({career}, S)"))

    if result:
        # Get raw score from Prolog
        raw_score = result[0]["S"]

        # Get maximum possible score for this career
        max_score = max_scores[career]

        # Convert raw score into percentage
        score = int((raw_score / max_score) * 100)
    else:
        # If no result, assign 0
        score = 0

    # Store the result
    career_scores.append({
        "career": career,
        "score": score
    })

# Remove careers with 0% score (not suitable)
career_scores = [c for c in career_scores if c["score"] > 0]

# Sort careers from highest score to lowest
career_scores.sort(key=lambda x: x["score"], reverse=True)

# Print header
print("\nCareer Suitability Results")
print("-" * 50)

# If there are suitable careers
if career_scores:

    # Loop through each career and display results
    for item in career_scores:

        career = item["career"]
        score = item["score"]

        # Generate progress bar
        bar = progress_bar(score)

        # Get explanation (reason) from Prolog
        reason_query = list(prolog.query(f"reason({career}, R)"))

        reason_text = ""

        if reason_query:
            reason_text = reason_query[0]["R"]

            # Decode if returned as bytes
            if isinstance(reason_text, bytes):
                reason_text = reason_text.decode("utf-8")

        # Get display-friendly name
        name = display_names.get(career)

        # Print career name, progress bar and score
        print(f"{name:<30} {bar} {score}%")

        # Print explanation if available
        if reason_text:
            print(f"  Reason: {reason_text}")

        print()

    # Get the best career (highest score)
    best = career_scores[0]

    best_name = display_names.get(best["career"])
    best_score = best["score"]

    # Print top recommendation
    print("-" * 50)
    print("Top Career Recommendation")
    print("-" * 50)
    print(f"{best_name} ({best_score}%) is your best career match based on your skills and interests.")

else:
    # If no suitable careers found
    print("No suitable careers found.")

