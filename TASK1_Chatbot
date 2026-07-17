import re
import random
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self, name="CodBot"):
        self.name = name
        self.user_name = None

        self.rules = [
            (r"\b(hi|hello|hey|hola)\b",
             ["Hello there! How can I help you today?",
              "Hi! Nice to see you. What's up?",
              "Hey! How are you doing?"]),

            (r"how are you",
             ["I'm just a bunch of if-else statements, but I'm doing great! And you?",
              "Running smoothly! Thanks for asking. How about you?"]),

            (r"my name is (\w+)",
             ["_SET_NAME_"]),

            (r"what is your name|who are you",
             [f"I'm {name}, your friendly rule-based chatbot!"]),

            (r"\b(bye|goodbye|see you|exit|quit)\b",
             ["Goodbye! Have a great day!",
              "See you later!",
              "Bye! Come back anytime."]),

            (r"\b(thanks|thank you|thx)\b",
             ["You're welcome!", "No problem at all!", "Anytime!"]),

            (r"what (time|is the time)",
             ["_GET_TIME_"]),

            (r"what (day|date|is the date)",
             ["_GET_DATE_"]),

            (r"\bweather\b",
             ["I can't check live weather yet, but I hope it's sunny where you are!"]),

            (r"\bjoke\b",
             ["Why do programmers prefer dark mode? Because light attracts bugs!",
              "Why did the computer go to therapy? It had too many unresolved issues."]),

            (r"\b(help|what can you do)\b",
             ["I can chat about greetings, tell you the time/date, remember your name, "
              "and crack a joke or two. Try asking me something!"]),

            (r"codsoft",
             ["CodSoft runs this internship program — glad you're building a chatbot for it!"]),
        ]

        self.fallback_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Hmm, I don't have a rule for that yet. Try asking something else!",
            "Sorry, I didn't get that. Can you say it differently?",
        ]

    def get_response(self, user_input):
        text = user_input.lower().strip()

        for patterns, responses in self.rules:
            match = re.search(patterns, text)
            if match:
                response = random.choice(responses)

                if response == "_SET_NAME_":
                    self.user_name = match.group(1).capitalize()
                    return f"Nice to meet you, {self.user_name}!"
                if response == "_GET_TIME_":
                    return f"It's currently {datetime.now().strftime('%I:%M %p')}."
                if response == "_GET_DATE_":
                    return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."

                if self.user_name and random.random() < 0.3:
                    return f"{response} (by the way, good to chat with you, {self.user_name})"
                return response

        return random.choice(self.fallback_responses)

    def chat(self):
        print(f"{self.name}: Hi! I'm {self.name}. Type 'bye' anytime to exit.\n")
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

            if re.search(r"\b(bye|goodbye|see you|exit|quit)\b", user_input.lower()):
                break


if __name__ == "__main__":
    bot = RuleBasedChatbot(name="CodBot")
    bot.chat()