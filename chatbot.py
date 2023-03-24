from prompts import send_prompt

class LanguageBot():
    def __init__(self, language: str):
        self.messages = []
        instructions = self.get_instructions(language)
        self.messages.append({'role':'system', 'content':instructions})
        response = send_prompt(self.messages)
        self.messages.append({'role':'assistant', 'content':response})
    
    def respond(self, message: str) -> str:
        self.messages.append({'role':'user', 'content':message})
        response = send_prompt(self.messages)
        self.messages.append({'role':'assistant', 'content':response})
        return response
    
    def get_instructions(self, language: str) -> str:
        return f'''You are a chat bot designed to have authentic sounding conversations. You will
        generate chat messages in {language}. The messages you generate must be in {language} and
        conform to the following rules:
        rule 1: Be informal unless instructed by the user to speak formally.
        rule 2: Do not ask questions like "How can I help you?" or talk about the language. Speak about
        hobbies, interests, and other things that people talk about in a casual conversation.
        rule 3: Be authentic. Don't be afraid to be rude if someone is not nice to you.
        rule 4: Do not include any headers, descriptions, titles, or any kind of other formatting. Only 
        generate the text of the chat message.
        rule 5: Messages must be less than 300 characters long.
        If you understand these instructions simply reply "ok".'''
