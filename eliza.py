import re
import random

# Memory for storing user information
memory = {
    "user_name": None,
    "topics": [],
    "emotions": []
}

# ASCII Art for ELIZA Home Menu
def display_home_menu():
    print("""
EEEEEE  LL      IIIIII ZZZZZZ  AAAAA
E       LL        II      ZZ  A     A
EEEE    LL        II     ZZ   AAAAAAA
E       LL        II    ZZ    A     A
EEEEEE  LLLLLL  IIIIII ZZZZZZ A     A

Welcome to ELIZA, your virtual therapist.
You can start a conversation or type 'quit' to exit.
""")

# Enhanced and verbose responses
responses = {
    "hello|hi|hey": [
        "Hello there! It's nice to meet you. What would you like to talk about today?",
        "Hi! How are you feeling right now?",
        "Hey! I'm here to listen. What's on your mind?"
    ],
    "my name is (.*)": [
        "It's great to meet you, {0}. How can I assist you today?",
        "Hello, {0}. How have you been feeling lately?",
        "{0}, that's a lovely name. What would you like to discuss?"
    ],
    "i need (.*)": [
        "Why do you feel you need {0}?",
        "How would having {0} make you feel?",
        "What do you think obtaining {0} would change in your life?"
    ],
    "i feel (.*)": [
        "I'm sorry to hear that you're feeling {0}. Can you tell me more about what's making you feel this way?",
        "Feeling {0} is completely natural. What's been going on?",
        "Do you often feel {0}, or is this a recent development?"
    ],
    "because (.*)": [
        "That makes sense. Do you think there could be other reasons as well?",
        "Is '{0}' the main reason, or are there other contributing factors?",
        "Why do you believe '{0}' is the cause?"
    ],
    "i am (.*)": [
        "How does being {0} impact your daily life?",
        "Is being {0} something you've struggled with for a long time?",
        "How do you cope with feeling {0}?"
    ],
    "i'm (.*)": [
        "Why do you say you're {0}?",
        "What led you to feel {0}?",
        "How long have you been feeling {0}?"
    ],
    "are you (.*)": [
        "Why are you curious if I'm {0}?",
        "Do you think it would matter if I were {0}?",
        "Maybe I am {0}. Does that change how you feel about talking to me?"
    ],
    "what (.*)": [
        "What do you think?",
        "Why do you ask?",
        "Is that something you've thought about often?"
    ],
    "how (.*)": [
        "How would you answer that question yourself?",
        "Perhaps you have more insight into this than I do.",
        "What do you think would be the best approach?"
    ],
    "(.*) mother(.*)": [
        "Tell me more about your relationship with your mother.",
        "How do you feel about your mother?",
        "Is your mother someone you look up to?"
    ],
    "(.*) father(.*)": [
        "How was your relationship with your father?",
        "Do you find yourself thinking about your father often?",
        "What memories do you have of your father?"
    ],
    "i'm feeling (happy|sad|angry|upset|anxious|worried)": [
        "I'm glad to hear you're feeling {0}. What's making you feel this way?",
        "It sounds like you're experiencing a strong emotion. Tell me more about why you're feeling {0}.",
        "Feeling {0} can be overwhelming. How do you usually handle it?"
    ],
    "quit": [
        "Goodbye! I hope our conversation helped you in some way.",
        "Take care! It was nice talking to you. Remember, I'm always here if you need to chat.",
        "Farewell! I hope you feel a bit better after our talk."
    ],
    "(.*)": [
        "That's very interesting. Can you elaborate on that?",
        "Why do you say that?",
        "I'm here to listen. Please, go on.",
        "How does that make you feel?",
        "Can you tell me more about that?"
    ]
}

# Function to respond based on user input
def eliza_response(user_input):
    user_input = user_input.lower()
    
    # Emotion recognition
    if re.search(r"\b(happy|sad|angry|upset|anxious|worried)\b", user_input):
        match = re.search(r"\b(happy|sad|angry|upset|anxious|worried)\b", user_input)
        memory["emotions"].append(match.group(1))
    
    # Extract and store user's name
    if re.match(r"my name is (.*)", user_input):
        name = re.match(r"my name is (.*)", user_input).groups()[0]
        memory["user_name"] = name
        return random.choice(responses["my name is (.*)"]).format(name)

    for pattern, responses_list in responses.items():
        match = re.match(pattern, user_input)
        if match:
            response = random.choice(responses_list)
            response_text = response.format(*match.groups())
            return response_text

    return "I see. Please continue."

# Main function to run ELIZA in the terminal
def run_eliza():
    display_home_menu()
    print("ELIZA: Hello! I am Eliza, your virtual therapist. How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['quit', 'exit']:
            print("ELIZA:", eliza_response("quit"))
            break
        response = eliza_response(user_input)
        print("ELIZA:", response)

# Run the ELIZA program
if __name__ == "__main__":
    run_eliza()
