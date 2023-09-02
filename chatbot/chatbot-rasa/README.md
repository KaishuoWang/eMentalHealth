# Chatbot - Rasa

This is a simple demo of a Rasa chatbot illustrating how to use chatbot to collect user information.

## How to run this demo

### Run the chatbot with python and webhook
```bash
$ pip install -U rasa[spacy]
$ python -m spacy download en_core_web_lg
$ rasa train
$ rasa run
```

Then in another terminal, you need to run `chatbot-rasa.py` to chat with the bot. After chatting with the bot, the dialogue will be saved in the `dialogue.txt` file.

### Run the chatbot in terminal
```bash
$ pip install -U rasa[spacy]
$ python -m spacy download en_core_web_lg
$ rasa train
$ rasa shell
```
