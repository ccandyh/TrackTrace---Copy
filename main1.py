def log_run(name, date, distance, time, goal, goal_met, mood):
    if not name:
        return "Please enter your name."

    run_data = (
        f"Name: {name}\n"
        f"Date: {date}\n"
        f"Distance: {distance} km\n"
        f"Time: {time} minutes\n"
        f"Goal: {goal} km\n"
        f"Goal Met: {goal_met}\n"
        f"Mood: {mood}\n"
        "--------------------------\n"
    )

    try:
        with open("Run_logs.txt", "a") as file:
            file.write(run_data)
        return "Run saved successfully!"
    except:
        return "Could not save the run."

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

