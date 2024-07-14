import re

class EnhancedRuleBasedChatbot:
    def __init__(self):
        self.responses = {
            'hello': 'Hi there! How can I help you today?',
            'how are you': 'I am just a bot, but I am functioning as expected. How about you?',
            'name': 'I am ChatBotX, your virtual assistant.',
            'bye': 'Goodbye! Have a great day!',
            'thanks': 'You are welcome!',
            'help': 'I am here to assist you. Please tell me how I can help you.',
            'weather': 'The weather is always perfect in the virtual world!',
            'who are you': 'I am ChatBotX, your friendly assistant.',
            'your creator': 'I was created by a team of talented developers.',
            'favorite color': 'As a bot, I don’t have preferences, but I think blue is quite nice!',
            'time': 'I am not equipped to tell time. Please check your device.',
            'day': 'Every day is a great day when I get to assist you!'
        }
        self.default_response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    def preprocess_input(self, user_input):
        user_input = user_input.lower().strip()
        user_input = re.sub(r'[^\w\s]', '', user_input)  # Remove punctuation
        user_input = re.sub(r'\b(ur|u)\b', 'you', user_input)  # Handle common typos and shortcuts
        return user_input

    def get_response(self, user_input):
        user_input = self.preprocess_input(user_input)
        
        # Check for exact matches first
        if user_input in self.responses:
            return self.responses[user_input]

        # Check for keywords using regex patterns
        patterns = {
            'hello': r'\b(hello|hi|hey|greetings)\b',
            'how are you': r'\b(how are you|how do you do|how is it going)\b',
            'name': r'\b(what is your name|who are you)\b',
            'bye': r'\b(bye|goodbye|see you)\b',
            'thanks': r'\b(thanks|thank you|thx)\b',
            'help': r'\b(help|assist|support)\b',
            'weather': r'\b(weather|forecast|temperature)\b',
            'who are you': r'\b(who are you|what are you)\b',
            'your creator': r'\b(your creator|who made you|your developer)\b',
            'favorite color': r'\b(favorite color|favourite colour|like best)\b',
            'time': r'\b(what time|current time|time now)\b',
            'day': r'\b(what day|current day|day today)\b'
        }

        for key, pattern in patterns.items():
            if re.search(pattern, user_input):
                return self.responses.get(key, self.default_response)
        
        return self.default_response

    def start_chat(self):
        print("ChatBotX: Hello! I am ChatBotX. Type 'bye' to exit the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower().strip() == 'bye':
                print("ChatBotX: " + self.responses['bye'])
                break
            response = self.get_response(user_input)
            print("ChatBotX: " + response)

if __name__ == "__main__":
    chatbot = EnhancedRuleBasedChatbot()
    chatbot.start_chat()
