#openai requires pip install
from files import *
import openai
import threading

def load_openai_api_key() -> None:
    '''This loads the openai API key from openaiapikey.txt'''
    ensure_folder_exists('api_key')
    files = os.listdir('api_key')
    files = [f for f in files if '.txt' in f]
    if files == []:
        get_api_key()
        write_to_file('api_key/openai.txt', openai.api_key)
        return
    openai.api_key = read_from_file('api_key/' + files[0])
    return

def get_api_key() -> None:
    while True:
        print('You will need an openai api key. They can be found here:')
        print('https://platform.openai.com/account/api-keys')
        sleep(.3)
        openai.api_key = input('Enter your openai api key:')
        clear_output()
        if validate_api_key():
            return
        print('Invalid API key.\n')

def validate_api_key() -> bool:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{'role':'user', 'content':'Is this api key working?'}])
    except:
        return False
    return True

def send_prompt(messages: list) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
    except Exception as e:
        print(e)
        sleep(61)
        return send_prompt(messages)
    text = response['choices'][0]['message']['content'] # type: ignore
    return text.strip()

class Requester_Thread(threading.Thread):
    def __init__(self, messages: list):
        threading.Thread.__init__(self)
        self.messages = messages
        
    def run(self):
        self.value = send_prompt(self.messages)