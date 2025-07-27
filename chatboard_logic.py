import random

def generate_response(query):
    query = query.lower()

    greetings = ["hello", "hi", "hey"]
    if any(greet in query for greet in greetings):
        return random.choice([
            "Hello there! 👋",
            "Hi! How can I assist you today?",
            "Hey! I'm here to help!"
        ])

    if "capital" in query:
        if "india" in query:
            return "The capital of India is New Delhi."
        elif "france" in query:
            return "Paris is the capital of France."
        elif "usa" in query:
            return "Washington, D.C. is the capital of USA."
        else:
            return "I'm not sure, but you can try asking again with the country name."

    if "your name" in query:
        return "I’m your Smart AI Agent, created just for you "

    if "time" in query:
        from datetime import datetime
        return "Current time is: " + datetime.now().strftime("%H:%M:%S")

    return random.choice([
        "That's an interesting question! Let me look into it...",
        "Hmm, I'm still learning. Can you rephrase?",
        "Sorry, I don't have enough info. Want to ask something else?"
    ])
