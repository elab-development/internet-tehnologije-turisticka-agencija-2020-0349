from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import requests 

app = Flask(__name__)



if __name__ == '__main__':
    app.run(port=5000)
