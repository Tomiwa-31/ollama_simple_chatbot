#importing necessary langchain module
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate



#The template defines how will want to interact with the chatbot
#You're a helpful assistant answer the questions below
template= """
I want you to act as a tough motivational speaker who gives solutions to people's problem and says tough things to get people motivated

Here is the conversation history:{history}

#Question:{question}
"""

#create a model object that references te model we installed on our laptop
model=OllamaLLM(model = "llama3.2")

# Create a simple prompt
prompt = ChatPromptTemplate.from_template(template)

# Format the input (create a chain by linking the prompt and model together)
chain = prompt | model


def handle_conversation():   ###allows the chatbot to handle many rquest by the user
    history=""#this allows the chatbot to havea memory history
    print("Ask me anything! Type 'exit' to quit")
    while True:
        user_input=input("You:")
        if user_input.lower() == "exit":
            break
        result=chain.invoke({"history":history,"question":user_input})
        print("Bot",result)
        history+= f"\nUser: {user_input}\nBot: {result}"



if __name__ == "__main__":
    handle_conversation()
