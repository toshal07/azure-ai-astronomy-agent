import os
from dotenv import load_dotenv

print("Astronomy AI Agent Ready!")
print("Type quit to exit")

while True:
    user_input = input("USER: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    print("AGENT: You said ->", user_input)