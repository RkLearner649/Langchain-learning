from langchain_openai import ChatOpenAI;
from dotenv import load_dotenv;

load_dotenv()

model = ChatOpenAI();

chat_memory = [];

while True:
    user_input = input('You : ')
    chat_memory.append(user_input);
    if(user_input == 'exit'):
        break;
    result = model.invoke(chat_memory)
    chat_memory.append(result)
    print('AI :',result.content)