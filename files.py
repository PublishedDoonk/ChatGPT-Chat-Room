import os
from time import sleep
from IPython.display import clear_output

def read_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def write_to_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def append_to_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)
        
def ensure_folder_exists(folder: str) -> None:
    if not os.path.exists(folder):
        os.mkdir(folder)

def ensure_file_exists(folder: str, filename: str) -> None:
    ensure_folder_exists(folder)
    if not os.path.exists(folder + '/' + filename):
        write_to_file(folder + '/' + filename, '')

def get_all_text_files(folder):
    files = os.listdir(folder)
    files = [f for f in files if '.txt' in f]
    write_to_file('full draft/book.txt', '')
    for file in files:
        content = read_from_file('{0}/{1}'.format(folder, file))
        append_to_file('full draft/book.txt', content + '\n')
    print('done')
    
def get_filename(folder: str, msg: str) -> 'str':
    while True:
        sleep(.3)
        filename = input(msg)
        if os.path.isfile('{0}/{1}'.format(folder, filename)):
            print('File loaded successfully')
            return '{0}/{1}'.format(folder, filename)
        clear_output()
        print('Invalid filename. Try again.')