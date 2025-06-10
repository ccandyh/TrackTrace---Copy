def log_run(name):
    if name:
        print(f"{name}'s run has been logged.")
        return f"Run logged for {name}"
    else:
        print("Name is empty. Please enter your name.")
        return "Please enter your name."

def calculate_calories(minutes, intensity="medium"):
    intensity_factors = {
        "low": 5,
        "medium": 10,
        "high": 15
    }
    return minutes * intensity_factors.get(intensity, 10)

def get_motivational_quote():
    import random
    quotes = [
        "Every step counts!",
        "You’re stronger than you think.",
        "Push yourself, because no one else will.",
        "One run at a time.",
        "Your only limit is you."
    ]
    return random.choice(quotes)
