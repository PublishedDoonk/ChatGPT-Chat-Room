from files import *
from prompts import *
from chatbot import *

def main():
    load_openai_api_key()
    language = input('Type a language to practice: ')
    lb = LanguageBot(language)
    while True:
        msg = input('You: ')
        if msg in ['quit', 'exit', 'bye', 'goodbye', 'cya', 'q']:
            msg = 'Goodbye'
        response = lb.respond(msg)
        print('Chatbot:', response)
        if msg == 'Goodbye':
            break     
    
if __name__ == '__main__':
    main()