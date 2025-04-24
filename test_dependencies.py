from deepgram import *
import google.generativeai as genai
from openai import OpenAI
import ffmpeg, json, os, requests, socket, sys, time
from dotenv import load_dotenv
from mutagen.mp3 import MP3
from datetime import datetime
from time import sleep

sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), '..'), 'Python-SDK'))
from mistyPy.Robot import Robot
from mistyPy.Events import Events

if __name__ == "__main__":

    # load the environment variables from the .env file
    load_dotenv()

    # Load the Deepgram API key from the environment variable
    deepgram_api_key = os.getenv('DEEPGRAM_API_KEY')
    if not deepgram_api_key:
        raise ValueError("Please set the DEEPGRAM_API_KEY environment variable.")
    deepgram = DeepgramClient(deepgram_api_key)

    # initialize the OpenAI client for TTS with the OPEN_AI_API_KEY environment variable
    open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
    if not open_ai_api_key:
        raise ValueError("Please set the OPEN_AI_API_KEYY environment variable.")
    openai_client = OpenAI(api_key=open_ai_api_key)
    
    # Load the Google Gemini API key from the environment variable
    google_api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
    if not google_api_key:
        raise ValueError("Please set the GOOGLE_GEMINI_API_KEY environment variable.")
    genai.configure(api_key=google_api_key)