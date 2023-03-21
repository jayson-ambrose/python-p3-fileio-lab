import ipdb

def write_file(file_name, file_content):

    file_thing = (file_name + ".txt")
    with open(file_thing, mode='w', encoding='utf-8') as text_file:
        text_file.write(file_content)
    pass

def append_file(file_name, append_content):
    file_thing = (file_name + ".txt")
    with open(file_thing, mode='a', encoding='utf-8') as text_file:
        text_file.write(append_content)
    pass

def read_file(file_name):

    with open(file_name + ".txt", encoding='utf-8') as text_file:
        return(text_file.read())
    pass

