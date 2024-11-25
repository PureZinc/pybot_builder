from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from pprint import pprint
import time


class Robot:
    def __init__(self, name: str, behavior: str, llm_api_key="", llm_temp=0.7, llm_model="gpt-3.5-turbo"):
        self.name = name
        self.behavior = behavior
        self.llm_model = ChatOpenAI(api_key=llm_api_key, temperature=llm_temp, model=llm_model)
        self.llm_workflow = StateGraph(state_schema=MessagesState)

    def generate_response(self, prompt) -> BaseMessage:
        try:
            response = self.llm_model.invoke([
                SystemMessage(self.behavior),
                HumanMessage(content=prompt)
            ])
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return BaseMessage(content="Sorry, I encountered an unexpected error.")
