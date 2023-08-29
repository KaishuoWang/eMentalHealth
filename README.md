# eMentalHealth
CSI 6900 project

## Conponents

Components we have built for the project

### [Semantic Search](https://github.com/KaishuoWang/eMentalHealth/tree/main/semantic%20search)

In this part, we utilized BERT, RoBERTa, XLNet, SGPT, and OpenAI embedding models to build a semantic search system.

### [Chatbot](https://github.com/KaishuoWang/eMentalHealth/tree/main/chatbot)

In this part, we utilized Rasa, and llama2 to build two chatbot demos to validate our assumptions regarding the utilization of chatbots to guide users through questionnaire completion.

* For the demonstration of the Rasa chatbot, it uses a predefined set of questions is used to guide users systematically through the questionnaire. However, we found that Rasa's reliance on predetermined question templates restricts its capacity to comprehend and adapt to diverse user responses. Instances may arise where users struggle to grasp the questions or require additional support, leading to potential disruptions in the information collection process. In such cases, Rasa tends to adhere to the scripted template without accommodating nuanced user inputs. Therefore, we think it's not a good option for this project.
* For the demonstration of the Llama2 chatbot, we obtained the prompt that can guide users to complete the questionnaire and the appropriate temperature through multiple experiments. But this demo is not complete. For example: At present, all questions need to be manually entered in the prompt, and this demo cannot determine whether the user has completed the questionnaire and performed the next steps. These questions can be accomplished by implementing controlled text generation and adding steps for the verification of user answers.
  
### [Translation](https://github.com/KaishuoWang/eMentalHealth/tree/main/translation-fr-en)

In this part, we fine-tuned a model using the dataset from [WMT2014 medical translation task](https://www.statmt.org/wmt14/medical-task/#download) to build a translation system. It can be used to translate from French to English. The reason we built this part is that not all the data in the dataset is available in French, so we wanted to take the next step by translating the dialogue between the users and the chatbot into English.

The fine-tuned translation model can be found [here](https://huggingface.co/kwang123/medical-mt-fr-en)
