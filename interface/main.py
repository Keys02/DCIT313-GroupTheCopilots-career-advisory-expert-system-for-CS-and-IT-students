from pyswip import Prolog
import os

prolog = Prolog()

# Load the knowledge base
current_dir = os.path.dirname(os.path.abspath(__file__))
kb_path = os.path.join(current_dir, "..", "knowledge_base", "career_rules.pl")
prolog.consult(kb_path)

# Assert facts
prolog.assertz("statistics(high)")
prolog.assertz("interest(data)")

# Query
results = list(prolog.query("career(X)"))

for r in results:
    print("Recommended career:", r["X"])

