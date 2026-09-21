from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header('Greeting Tool')

model = ChatOpenAI()
# Loading dynamic prompt from a common location 
template = load_prompt('template.json')

user_input = st.text_input('Please enter your name')

language = st.number_input("Number of languages:", min_value=0, max_value=120, value=5, step=1)

if st.button('Greet'):
    if user_input and language:
        chain = template | model
        # chaining and binding the template parameter
        result = chain.invoke({'name':user_input,'languages':language})
        #prompt = template.invoke({'name':user_input,'languages':language})
        #result = model.invoke(prompt)
        st.write(result.content)

    else:
        st.info('Enter correct details')


