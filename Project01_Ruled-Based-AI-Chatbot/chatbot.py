# # -------------------------------------------------
# # Rule-Based AI Chatbot
# # DecodeLabs - Project-1
# # -------------------------------------------------

# print("=" * 50)
# print("           Welcome to Rule-Based AI Chatbot")
# print("=" * 50)
# print("Bot: Hello! I am your AI Assistant.")
# print("Bot: Type 'exit' anytime to end the chat.\n")




# # creating dictionary 
# responses = {
#     "hello": "Hello! How can I help you today?",
#     "hi": "Hi! Nice to meet you.",
#     "how are you": "I'm doing great! Thanks for asking.",
#     "your name": "I'm a Rule-Based AI Chatbot.",
#     "python": "Python is a popular programming language used in AI and web development.",
#     "ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
#     "thank you": "You're welcome! Happy to help.",
#     "bye": "Goodbye! Have a great day!"
# }

#  #while loop repeats code.
# while True:
#     user_input = input("You: ").lower().strip()

#     # Exit
#     if user_input in ["exit", "quit"]:
#         print("Bot: Goodbye! Have a nice day.")
#         break

#     # Greetings
#     elif user_input in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]:
#         print("Bot: Hello! Nice to meet you. 😊")

#     # How are you
#     elif user_input == "how are you":
#         print("Bot: I'm doing great! Thanks for asking.")

#     # Name
#     elif user_input in ["your name", "who are you"]:
#         print("Bot: I'm a Rule-Based AI Chatbot created using Python.")

#     # Python
#     elif user_input == "python":
#         print("Bot: Python is a powerful programming language widely used in AI, Data Science, and Web Development.")

#     # AI
#     elif user_input in ["ai", "artificial intelligence"]:
#         print("Bot: Artificial Intelligence enables machines to simulate human intelligence.")

#     # Thank You
#     elif user_input in ["thanks", "thank you"]:
#         print("Bot: You're welcome! 😊")

#     # Help
#     elif user_input == "help":
#         print("Bot: You can ask me about Python, AI, my name, greetings, or type 'exit' to quit.")

#     # Default
#     else:
#         print("Bot: Sorry, I don't understand that.")







#     # print("Bot:", responses.get(user_input.lower().strip(), "Sorry, I don't understand that."))

# # .get(): If the key exists → return its value.
# # If the key does not exist → return the default message.


# ============================================================
# DecodeLabs Internship Project 1
# Rule-Based AI Chatbot
# Developed by: Your Name
# ============================================================

# -------------------------
# Welcome Message
# -------------------------

print("=" * 60)
print("          🤖 RULE-BASED AI CHATBOT")
print("=" * 60)
print("Bot : Hello! Welcome to the Rule-Based AI Chatbot.")
print("Bot : Type 'help' to see available commands.")
print("Bot : Type 'exit' anytime to end the conversation.")
print("=" * 60)

# -------------------------
# Knowledge Base
# -------------------------

responses = {
    "how are you": "I'm doing great! Thanks for asking.",
    "your name": "I'm a Rule-Based AI Chatbot developed using Python.",
    "who are you": "I'm a Rule-Based AI Chatbot developed using Python.",
    "python": "Python is a powerful programming language used in AI, Machine Learning, Data Science, and Web Development.",
    "ai": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",
    "artificial intelligence": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",
    "machine learning": "Machine Learning is a branch of AI that allows computers to learn from data.",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!",
    "creator": "I was created as part of DecodeLabs Internship Project 1.",
    "help": """
Available Commands:
• hello
• hi
• hey
• good morning
• good afternoon
• good evening
• how are you
• your name
• who are you
• python
• ai
• artificial intelligence
• machine learning
• thank you
• thanks
• creator
• help
• exit
"""
}

# -------------------------
# Greeting Keywords
# -------------------------

greetings = [
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"
]

# -------------------------
# Main Chat Loop
# -------------------------

while True:

    user_input = input("\nYou : ").lower().strip()

    # Exit Command
    if user_input in ["exit", "quit", "bye"]:
        print("\nBot : Thank you for chatting with me.")
        print("Bot : Have a wonderful day! 👋")
        break

    # Greeting
    elif user_input in greetings:
        print("\nBot : Hello! Nice to meet you. 😊")

    # Dictionary Responses
    elif user_input in responses:
        print("\nBot :", responses[user_input])

    # Unknown Question
    else:
        print("\nBot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see what you can ask.")