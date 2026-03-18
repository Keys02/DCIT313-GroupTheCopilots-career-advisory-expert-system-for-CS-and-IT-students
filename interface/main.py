import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog
import os

# Initialize Prolog engine
prolog = Prolog()

# Get the current file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to the Prolog knowledge base file
kb_path = os.path.join(current_dir, "..", "knowledge_base", "career_rules.pl")

# Load the Prolog knowledge base
try:
    prolog.consult(kb_path)
except Exception as e:
    print(f"Failed to load knowledge base: {e}")

# List of questions to ask the user
attributes = [
    {"name": "programming", "label": "Rate your programming skill:", "options": ["high", "medium", "low"]},
    {"name": "statistics", "label": "Rate your statistics skill:", "options": ["high", "medium", "low"]},
    {"name": "networking", "label": "Rate your networking skill:", "options": ["high", "medium", "low"]},
    {"name": "mathematics", "label": "Rate your mathematics skill:", "options": ["high", "medium", "low"]},
    {"name": "design", "label": "Rate your design skill:", "options": ["high", "medium", "low"]},
    {"name": "creativity", "label": "Rate your creativity:", "options": ["high", "medium", "low"]},
    {"name": "communication", "label": "Rate your communication skill:", "options": ["high", "medium", "low"]},
    {"name": "interest", "label": "What are you most interested in?", "options": ["coding", "data", "design", "marketing", "security", "networks"]}
]

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

class CareerAdvisorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Career Advisory Expert System")
        self.geometry("600x600")
        self.configure(padx=20, pady=20)
        
        self.input_vars = {}
        
        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self, text="Career Advisory Expert System", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        input_frame = ttk.Frame(self)
        input_frame.pack(fill=tk.BOTH, expand=True)

        for i, attr in enumerate(attributes):
            lbl = ttk.Label(input_frame, text=attr["label"])
            lbl.grid(row=i, column=0, sticky=tk.W, pady=10, padx=5)

            var = tk.StringVar(self)
            var.set(attr["options"][0])  # Set default value
            self.input_vars[attr["name"]] = var

            cb = ttk.Combobox(input_frame, textvariable=var, values=attr["options"], state="readonly")
            cb.grid(row=i, column=1, sticky=tk.EW, pady=10, padx=5)

        input_frame.columnconfigure(1, weight=1)

        submit_btn = ttk.Button(self, text="Get Recommendations", command=self.evaluate_careers)
        submit_btn.pack(pady=20)

    def evaluate_careers(self):
        # Clear any previous user inputs stored in Prolog
        try:
            prolog.retractall("prerequisite(_,_)")
        except Exception as e:
            messagebox.showerror("Prolog Error", f"Error communicating with Prolog: {e}")
            return

        user_inputs = {name: var.get().lower() for name, var in self.input_vars.items()}

        for name, value in user_inputs.items():
            prolog.assertz(f"prerequisite({name}, {value})")

        career_scores = []
        for career in career_names:
            result = list(prolog.query(f"career_score({career}, S)"))
            
            if result:
                raw_score = result[0]["S"]
                max_score = max_scores.get(career, 100)
                score = int((raw_score / max_score) * 100)
                score = min(score, 100)
            else:
                score = 0
            
            career_scores.append({
                "career": career,
                "score": score
            })

        career_scores = [c for c in career_scores if c["score"] > 0]
        career_scores.sort(key=lambda x: x["score"], reverse=True)

        self.show_results(career_scores)

    def show_results(self, career_scores):
        results_window = tk.Toplevel(self)
        results_window.title("Career Suitability Results")
        results_window.geometry("700x600")
        results_window.configure(padx=20, pady=20)
        
        # Scrollable area
        canvas = tk.Canvas(results_window)
        scrollbar = ttk.Scrollbar(results_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        if not career_scores:
            ttk.Label(scrollable_frame, text="No suitable careers found.", font=("Helvetica", 14)).pack(pady=20)
            return

        ttk.Label(scrollable_frame, text="Career Suitability Results", font=("Helvetica", 16, "bold")).pack(pady=(0, 20))

        # Show best recommendation at the top
        best = career_scores[0]
        best_name = display_names.get(best["career"], best["career"].replace("_", " ").title())
        best_score = best["score"]

        summary_frame = ttk.Frame(scrollable_frame, padding=15)
        summary_frame.pack(fill=tk.X, expand=True, pady=(0, 20))
        
        ttk.Label(summary_frame, text="Top Career Recommendation", font=("Helvetica", 14, "bold")).pack()
        ttk.Label(summary_frame, text=f"{best_name} ({best_score}%) is your best career match based on your skills and interests.", wraplength=550, justify=tk.CENTER).pack(pady=10)

        for item in career_scores:
            career = item["career"]
            score = item["score"]
            name = display_names.get(career, career.replace("_", " ").title())
            
            reason_query = list(prolog.query(f"reason({career}, R)"))
            reason_text = ""
            if reason_query:
                reason_text = reason_query[0]["R"]
                if isinstance(reason_text, bytes):
                    reason_text = reason_text.decode("utf-8")

            frame = ttk.Frame(scrollable_frame, borderwidth=1, relief="solid", padding=10)
            frame.pack(fill=tk.X, expand=True, pady=5)

            header_frame = ttk.Frame(frame)
            header_frame.pack(fill=tk.X)
            
            ttk.Label(header_frame, text=name, font=("Helvetica", 12, "bold")).pack(side=tk.LEFT)
            ttk.Label(header_frame, text=f"{score}%", font=("Helvetica", 12, "bold")).pack(side=tk.RIGHT)
            
            progress = ttk.Progressbar(frame, orient="horizontal", mode="determinate", length=400)
            progress["value"] = score
            progress.pack(fill=tk.X, pady=5)

            if reason_text:
                ttk.Label(frame, text=f"Reason: {reason_text}", wraplength=550).pack(fill=tk.X, pady=(5,0))

if __name__ == "__main__":
    app = CareerAdvisorApp()
    app.mainloop()

