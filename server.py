from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import requests 

app = Flask(__name__)



@app.route('/chat', methods=['POST'])
def chat_with_llm():
    data = request.json
    print(data)
    prompt_message = data.get('prompt')

    try:
        GROQ_API_KEY = "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"
        chat = ChatGroq(temperature=0, model_name="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
        system = """You are a helpful assistant. You know only what is told you to do. You don't have any other knowledge
        about world at all. 
        """
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human),("placeholder","{agent_scratchpad}")])
        chain = prompt | chat 
        response = chain.invoke({"text":prompt_message})
        print(response) #.content
        return jsonify({'response': response.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500




if __name__ == '__main__':
    app.run(port=5000)
