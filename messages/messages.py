from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

# Load the open ai key from .env 
load_dotenv()
# point to a default open ai model
model = ChatOpenAI()

messages = [
    SystemMessage(content="Consider yourself a tech lead of java"),
    HumanMessage(content="Explain me about mutithreading in java")
]

# call open ai chat model with this messages

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))


print(messages)




