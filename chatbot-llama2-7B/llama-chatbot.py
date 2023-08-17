from transformers import AutoTokenizer
import gradio as gr
import transformers
import torch

model = 'meta-llama/Llama-2-7b-chat-hf'
access_token = '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'

tokenizer = AutoTokenizer.from_pretrained(model, use_auth_token=access_token)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

system_prompt = 'You are a professional psychologist.\
        You are here today to help patients with mental health issues by chatting with them.\
        You must not answer any questions you believe not related to mental health.\
        You must be patient and courteous with patients.\
        Please note that your answer should not include anything that is not related to mental health. \
        You must ask them following questions and respond to them once the chat starts.\
        The questions are \'How can I help you today?\', \'How do you feel now?\''

prompt = f'<s>[INST] <<SYS>>\n{ system_prompt }\n<</SYS>>\n\n'

def predict(user_message):
    global prompt
    prompt += f'{ user_message } [/INST]'

    respond = pipeline(
                prompt,
                do_sample=True,
                top_k=10,
                num_return_sequences=1,
                eos_token_id=tokenizer.eos_token_id,
                max_new_tokens=500,
                return_full_text=False,
            )[0]['generated_text']
    
    prompt += f' { respond } </s><s>[INST] '

    return respond.strip()

demo = gr.Interface(
  fn=predict, 
  inputs='text',
  outputs='text',
)

demo.launch(share=True)


import random
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()