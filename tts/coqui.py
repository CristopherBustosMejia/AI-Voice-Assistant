import os
import tempfile
from TTS.api import TTS
from tts.base import TTSBase
from utils.audio import AudioPlayer

class CoquiTTS(TTSBase):
    def __init__(self, model_name="tts_models/es/css10/vits"):
        self.tts = TTS(model_name)
        self.mediaPlayer = AudioPlayer()

    def speak(self, text: str):
        if not text.strip():
            print("[TTS - Coqui] Texto vacío. No se generará audio.")
            return
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tempAudio:
                tempAudioPath = tempAudio.name
                self.tts.tts_to_file(text=text, file_path=tempAudioPath)
            if os.path.getsize(tempAudioPath) == 0:
                print("[TTS - ElevenLabs] El archivo de audio generado está vacío.")
                return
            self.mediaPlayer.playAudio(tempAudioPath)
        except Exception as e:
            print(f"[TTS - ElevenLabs - Error] Error playing audio: {e}")
        finally:
            try:
                os.unlink(tempAudioPath)
            except OSError as e:
                print(f"[ERROR] Error deleting temporary audio file: {e}")