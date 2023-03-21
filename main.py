from files import *
from prompts import *
from persona import *

def main():
    load_openai_api_key()
    name_list = get_name_list('New York')
    print(name_list)
    name_list = name_list.split('\n')
    print(name_list)
    test_person = Persona('New York', name_list, 'English')
    print(get_persona_prompt(test_person, []))
    
if __name__ == '__main__':
    main()