import streamlit as st
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

# Import the API key
import os
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAI model
llm = OpenAI(temperature=0.0)

# Load tools and initialize the agent
tools = load_tools(["wikipedia"], llm)
agent = initialize_agent(tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Create a Streamlit app
st.title('Wikipedia Bot App')

# Collect the question from the user
user_question = st.text_input('Ask a question about Wikipedia')

# Handle user input and provide answers
if user_question:
    # Run the agent to get an answer
    answer = agent.run(user_question)
    
    # Display the answer to the user
    st.write('Answer:', answer)
