import ollama

def ollama_request(user_query, model="llama3.2"):
    file_path = "data/prompts/prompt1.txt" if model == "llama3.2" else "data/prompts/prompt2.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        response = ollama.chat(
            model="gpt-oss",
            messages=[
                {
                    "role" : "system",
                    "content": content
                },
                {
                    "role" : "user",
                    "content": user_query
                }
            ]
        )
        raw_response = response["message"]["content"]
        return raw_response
    except Exception as e:
        print(f"Error during Ollama request: {e}")
        return None 