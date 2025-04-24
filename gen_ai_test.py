import google.generativeai as genai
import os, json
from dotenv import load_dotenv


def bank_and_forth_chat(model):
    
    chat = model.start_chat()

    raw_response = chat.send_message("Start conversation")
    response_json_dict = json.loads(raw_response.text)
    response_text = response_json_dict["msg"]
    response_expression = response_json_dict["expression"]
    print("AI:", response_text)
    while True:
        user_input = input("You: ")        
        if user_input.lower() == "exit":
            print("Conversation ended.")
            break
        response = chat.send_message(user_input)
        print("AI:", response.text)

def main():
    load_dotenv()
    google_api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
    genai.configure(api_key=google_api_key)

    # get the system instruction from a text file
    with open(f'three_good_things_system_instruction.txt') as f:
        example_system_instruction = f.read()
    f.close()

    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro',
        system_instruction = example_system_instruction,
        generation_config={"temperature": 0, "response_mime_type": "application/json"} # text/plain is default 
    )

    bank_and_forth_chat(model)

if __name__ == "__main__":
    main()