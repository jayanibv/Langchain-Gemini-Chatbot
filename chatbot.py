import os
import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Set your Gemini API Key
os.environ["GOOGLE_API_KEY"] = "your-API-key-here"

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# Conversation memory
memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Chatbot function
def chat_fn(history, message):
    # Ask LangChain
    response = conversation.predict(input=message)

    # Convert to Gradio 5 "messages" format
    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": response},
    ]
    return history, history

# Build Gradio UI
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(placeholder="Ask me something...")
    clear = gr.Button("Clear")

    state = gr.State([])

    msg.submit(chat_fn, [state, msg], [chatbot, state])
    clear.click(lambda: ([], []), None, [chatbot, state])

demo.launch()
