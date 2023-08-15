# run `rasa run` in command line first to start the server
import requests

url = 'http://0.0.0.0:5005/webhooks/rest/webhook'

# user_input = ''

# while user_input != 'exit':
#     user_input = input("Enter your message: ")
#     myobj = {'sender': 'test', 'message': user_input}
#     bot_message = requests.post(url, json = myobj).json()
#     print(bot_message)
#     for each in bot_message:
#         print(each['text'])
user_input = ''
dialogue = ''

print('This is a demo for chatbot-rasa. You can type \'exit\' to exit at anytime.')

while user_input != 'exit':
    user_input = input("Enter your message: ")
    if user_input == 'exit':
        break
    dialogue += 'User: ' + user_input + '\n'
    myobj = {'sender': 'test', 'message': user_input}
    bot_message = requests.post(url, json = myobj).json()
    for each in bot_message:
        print(each['text'])
        dialogue += 'Bot: ' + each['text'] + '\n'

# Save dialogues
import os

# Check if the file exists
file_path = "dialogue.txt"
if os.path.exists(file_path):
    os.remove(file_path)  # Delete the old file

# Create and write content to the new file
with open(file_path, "w") as file:
    file.write(dialogue)

print(f"Dialogue saved in '{file_path}'.")