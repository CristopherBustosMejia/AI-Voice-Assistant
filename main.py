import json
from tts.googletts import GoogleTTS
from tts.elevellabs import ElevenLabsTTS
from tts.coqui import CoquiTTS
from stt.stt_vosk import VoskSTT
from crud.crud_sakila import SakilaCrud
from llm.ollama_request import ollama_request

def main():
    print("Inicializando el asistente de voz...")
    tts = getTTS()
    stt = VoskSTT(model_path="E:\\VsCode\\Python\\AI-Voice-Assistant\\data\\models\\vosk-model-small-es-0.42")
    crud = SakilaCrud(host="localhost", user="root", password="0000", database="sakila", pool_size=10)
    
    FUNCTIONS_MAP ={
        "get_all_films": crud.get_all_films,
        "get_film_by_id": crud.get_film_by_id,
        "get_actors_by_film": crud.get_actors_by_film,
        "search_films_by_keyword": crud.search_films_by_keyword}
    
    question = stt.record()
    print(f"[TRANSCRIPCIÓN STT]: {question}")
    response = process_user_question(question, FUNCTIONS_MAP)
    print ("\n=== RESPONSE TO USER ===")
    aux = tts.speak(response)
    if aux == -1:
        print("[TTS] Cambiando a motor secundario (Google TTS).")
        tts = GoogleTTS()
        tts.speak(response)

def process_user_question(user_question, FUNCTIONS_MAP):
    print("=== STEP 1: Sending user question to Ollama Tool ===")
    response = ollama_request(user_question)
    print(f"[TOOL RESPONSE RAW]: {response}")
    try:
        parsed = json.loads(response)
        function_name = parsed.get("function_name")
        parameters = parsed.get("parameters", {})
    except (json.JSONDecodeError, TypeError, AttributeError):
        print("[INFO]: Ollama indicate no function available or invalid JSON.")
        function_name = None
        parameters = {}

    if function_name is None:
        print("[INFO]: No function to call, returning Ollama response.")
        return response
    
    db_result = None
    if function_name in FUNCTIONS_MAP:
        print(f"==== STEP 2: Executing function '{function_name}' with parameters {parameters} ====")
        try:
            db_result = FUNCTIONS_MAP[function_name](**parameters)
            print(f"[DB RESULT]: {db_result}")
        except Exception as e:
            print(f"[ERROR]: Exception calling function '{function_name}': {e}")
            db_result = None
    else:
        print(f"[WARNING]: Function '{function_name}' not found in FUNCTIONS_MAP.")
        db_result = None

    if db_result is None:
        return "No se encontraron resultados."

    print("==== STEP 3: Sending DB results back to Ollama for final response ====")
    final_query = json.dumps(db_result, default=str) if db_result else "[]"
    final_response = ollama_request(final_query, model="gpt-oss")
    print(f"[FINAL RESPONSE]: {final_response}")
    return final_response

def  getTTS():
    from config import TTS_ENGINE
    if TTS_ENGINE == "google":
        print("[TTS] Using Google TTS Engine.")
        return GoogleTTS()
    elif TTS_ENGINE == "elevenlabs":
        print("[TTS] Using ElevenLabs TTS Engine.")
        return ElevenLabsTTS()
    elif TTS_ENGINE == "coqui":
        print("[TTS] Using Coqui TTS Engine.")
        return CoquiTTS()
    else:
        print(f"[WARNING] Unknown TTS_ENGINE '{TTS_ENGINE}', defaulting to GoogleTTS.")
        return GoogleTTS()

if __name__ == "__main__":
    main()