# eMentalHealth
CSI 6900 project

## Conponents

Components we have built for the project

### [Semantic Search](https://github.com/KaishuoWang/eMentalHealth/tree/main/semantic%20search)

In this part, we utilized BERT, RoBERTa, XLNet, SGPT, and OpenAI embedding models to build a semantic search system.

### [Chatbot](https://github.com/KaishuoWang/eMentalHealth/tree/main/chatbot)

In this part, we utilized Rasa, and llama2 to build two chatbot demos.

* For the demonstration of the the Rasa chatbot, we wanted to show how a chatbot can be used to help psychiatrists gather information from patients. In this way, we can then use LLMs to summarize the dialogue between chatbot and user, and use the previously constructed search system to search the information required by the user from the database and make a preliminary diagnosis of the patient.
* For the demonstration of the Llama2 chatbot, we obtained the prompt that can guide users to complete the questionnaire and the appropriate temperature through multiple experiments. But this demo is not complete. For example: At present, all questions need to be manually entered in the prompt, and this demo cannot determine whether the user has completed the questionnaire and perform the next steps. These questions can be accomplished by implementing controlled text generation and adding steps for verification of user answers.
  
### [Translation](https://github.com/KaishuoWang/eMentalHealth/tree/main/translation-fr-en)

In this part, we fine-tuned a model using the dataset from [WMT2014 medical translation task](https://www.statmt.org/wmt14/medical-task/#download) to build a translation system. It can be used to translate from French to English. The reason we built this part is because not all the data in the dataset is available in French, so we wanted to take the next step by translating the dialogue between the users and the chatbot into English.

The fine-tuned model can be found [here](https://huggingface.co/kwang123/medical-mt-fr-en)
