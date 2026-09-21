from langchain_openai import ChatOpenAI;
from dotenv import load_dotenv;

load_dotenv()

model = ChatOpenAI();

chat_memory = [];

while True:
    user_input = input('You : ')
    chat_memory.append(user_input);
    if(user_input == 'exit'):
        break
    result = model.invoke(chat_memory)
    chat_memory.append(result.content)
    print('AI :',result.content)

print(chat_memory)

# DrawBack 

# Manually we are maintaing the role of the messages 
# even then also chat memory result not having the details of the owner of the messages
# in that case we need to create dic and maintain the dictory with proper user , AI and system messages
# But lang chain already provide us messages that we can use to solve our problem
# refere messsages directory for that