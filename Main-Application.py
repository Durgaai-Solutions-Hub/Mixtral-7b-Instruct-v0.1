# Importing Modules
import requests

# URL AND API
URL = 'https://durgaai-solutions-hub-server-mixtral7b-instruct-v0-1.hf.space/run-application'
API = 'Your Hugging Face Access Token'

# Custom Prompt
def Customize_Prompt(message, final_instructions=None):
    prompt = ""
    if final_instructions:
        prompt += f"[INST] {final_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Accessing Our Model
def Public_Model(prompt, instructions, temperature=0.1, max_new_token=2, top_p=0.95, repition_penalty=1.0):
    try:
        data = {'prompt': prompt, 'instructions': instructions, 'api_key': API}
        response = requests.post(URL, json=data)
        response_json = response.json()
        if 'Response' in response_json:
            return response_json['Response']
        else:
            return "Sorry, I'm Having Trouble Understanding Your Request. Please Try Again!"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Accessing The ChatBot
def Chatbot():
    print("Hello! I'm your chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        prompt = Customize_Prompt(user_input)
        response = Public_Model(prompt, "Answer The User's Question")
        print(f"Bot: {response}")

# Launching Application
if __name__ == "__main__":
    Chatbot()
