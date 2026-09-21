from langchain_openai import ChatOpenAI;
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv;

load_dotenv()

model = ChatOpenAI();

chat_memory = [
    SystemMessage(content='You are a helpful bot')
];

while True:
    user_input = input('You : ')
    chat_memory.append(HumanMessage(content=user_input))
    if(user_input == 'exit'):
        break
    result = model.invoke(chat_memory)
    chat_memory.append(AIMessage(content=result.content))
    print('AI',result.content)

print(chat_memory)
