#library for Generative Ai
import google.generativeai as genai

#Configuring Gemini API key

gemini_api_key = "AIzaSyDqrFFg7gddzqH-TlHyXCgjQq1It2cPacs"
genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash-001")

#create a function to define the prompt
def run_prompt(prompt_type, user_input):
    if prompt_type == "zero-Shot":
        prompt = f"{user_input}"
        
    elif prompt_type == "few-Shot":
        prompt = (
            "Q: Who is the President of India\n\n"
            "A: Ms. Draupadi Murmu"
            "Q: Who is the President of United States\n\n"
            "A: Mr. Donald Trump"
            f"Q:{user_input}\n"
            "A: "
        )    
        
    elif prompt_type == "Instruction-Based":
        prompt = (
            "Instruction: Summarize my article in 3 bullet points"
            f"Text: {user_input}"
        )
        
    elif prompt_type == "Chain-of-Thought":
        prompt = (
            "solve the Neural network backpropagation equation step by step"
            f"Text:{user_input}"
        )    
        
    elif prompt_type =="Role-based":
        prompt = (
            "you are a real estate consultant, pls tell me where and why should i purches"
            f"Text:{user_input}"
        )   
        
    else:
        prompt = user_input   
    
    response = model.generate_contant(prompt)
    return response.text.strip()    