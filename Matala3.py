import datetime
import re
import json

def read_file(file):
    '''Reads Whatsapp text file into a list of strings'''
    x = open(file,'r', encoding = 'utf-8') #Opens the text file into variable x but the variable cannot be explored yet
    y = x.read() #By now it becomes a huge chunk of string that we need to separate line by line
    content = y.splitlines() #The splitline method converts the chunk of string into a list of strings
    return content

#Replace contact's number/name with unique id number
def anonymous_contact(chat:list):
    contact_id = 1
    result = []
    for line in chat:
        try:
            contact = re.findall('[0-9]+ - (.+): ', line)[0]
        except:
            continue
        if contact not in my_dict:
            my_dict[contact] = contact_id
            contact_id += 1
        line = line.replace(contact, str(my_dict[contact]) + " ")
        result.append(line)
    return result

#Create a list of dictionaries 
def createDict(chat):
    i=0   
    anonymous = anonymous_contact(chat)
    for line in anonymous:
        line = {}
        line['datetime'] = date[0+i]
        line['id'] = anonymous[0+i].split('-')[1]
        line['text'] = anonymous[0+i].split(':')[2]
        text_list.append(line)
        i=i+1
    return


# Create a dictionary of the chat's MetaData
def metadataDict(chat):
    i = 0
    metadata = {}
    metadata['chat_name'] = chat[1].split('"')[1]
    metadata['creation_date'] = chat[1].split(' -')[0]
    creator = chat[1].split(' - ')[1].split('ידי')[1]
    if not creator.isalnum():
        metadata['creator'] = chat[1].split(' - ')[1].split('ידי')[1].strip()[2:-2]
    else:
        creator = chat[1].split(' - ')[1].split('ידי')[1]
    createDict(chat)
    metadata['num_of_participants'] = len(my_dict)
    return metadata


chat = read_file('WhatsApp.txt')     
date = [chat[i].split('-')[0] for i in range(len(chat))]
my_dict = dict()
text_list = []
metadata = metadataDict(chat)
my_dict2 = {'metadata': metadata, 'messages': text_list}
path = "C:\\Users\\ograi\\Desktop\\Python\\"
# Convert to json
J_path = path + metadata['chat_name'] + '.json'
to_save = json.dumps(my_dict2, ensure_ascii=False)
with open(J_path, 'wb') as f:
    f.write(to_save.encode('utf-8'))