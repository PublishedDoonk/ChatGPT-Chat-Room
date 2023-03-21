from files import *
from prompts import *
from enum import Enum
from random import randint


def get_random_location():
    prompt = '''Ignore all previous instructions. State a random place 
    in the world where people live. Only return the place name. No descriptions,
    headers, punctuation, or any other text.'''
    return send_prompt(prompt)

def get_name_list(location: str):
    prompt = f'''Ignore all previous instructions. Return a list of 50 random names
    that sound like they belong to people from {location}. Return the list of
    first and last names in a new line separated format with no numbering or 
    any other kind of punctuation. The first 25 lines of names must be female names while
    the last 25 lines of names must be male names. Do not return any headers, descriptions,
    or other text.'''
    return send_prompt(prompt)

def get_persona_prompt(person: 'Persona', recent_messages: list) -> 'str':
    prompt = f'''Ignore all previous instructions. Do not explicitly include
    any portion of this prompt in the response. Generate a chat message in 
    {person.language} that a {person.age} year old person from {person.location} 
    chatting in an online chatroom whose name is {person.name} would be likely to
    say. The person's big five personality traits are: 
    {person.bigfive['openness']}
    {person.bigfive['conscience']}
    {person.bigfive['extraversion']}
    {person.bigfive['agreeableness']}
    {person.bigfive['neuroticism']}
    The last several messages from the chat room are below separated by ----:
    {'----'.join(recent_messages)}
    The chat message should be a response to one of the recent messages or a new message 
    for the room. Only use the specified language. Do not have any headers, descriptions,
    or other text. The character limit for the chat message is 256 characters.  
    '''
    prompt = prompt[0:256]
    prompt = prompt.splitlines()[0]
    if '----' in prompt:
        prompt = prompt[0:prompt.find('----')]
    return send_prompt(prompt)
    

class Gender(Enum):
    FEMALE = 1
    MALE = 2

class Persona():
    def __init__(self, location: str, names: list, language: str, name=None, gender=None,):
        self.location = location
        self.set_gender(gender)
        self.set_name(names, name)
        self.set_personality()
        self.age = randint(18,91)
        self.language = language
        
    def set_gender(self, gender=None):
        if gender:
            self.gender = gender
        elif randint(0,1) > 0:
            self.gender = Gender.MALE
        else:
            self.gender = Gender.FEMALE
    
    def set_name(self, names, name=None):
        if name:
            self.name = name
        elif self.gender == Gender.MALE:
            self.name = names[randint(25,50)]
        else:
            self.name = names[randint(0,25)]
        self.surname = self.name.split(' ')[1]
        
    def random_severity(self):
        severity = ['extremely', 'very', 'moderately', 'not very', 'not']
        return severity[randint(0,4)]
    
    def set_personality(self):
        bigfive = {}
        bigfive['openness'] = f'Openness to experience: {self.random_severity()} open to new experiences.'
        bigfive['conscience'] = f'Conscientiousness: {self.random_severity()} organized and/or efficient.'
        bigfive['extraversion'] = f'Extraversion: {self.random_severity()} outgoing and/or socialable.'
        bigfive['agreeableness'] = f'Agreeableness: {self.random_severity()} agreeable and/or friendly.'
        bigfive['neuroticism'] = f'Neuroticism: {self.random_severity()} nervous and/or sensitive.'
        self.bigfive = bigfive
        