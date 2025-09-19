import sounddevice as sd
import queue
import sys
import json
import threading
from pathlib import Path
from vosk import Model, KaldiRecognizer

class VoskSTT:
    def __init__(self, model_path: str, sample_rate: int = 16000):
        self.model_path = model_path
        self.sample_rate = sample_rate
        self.q = queue.Queue()
        self.stop_recording = threading.Event()
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, self.sample_rate)
        self.transcription = ""
        print(f"[STT - Vosk] Modelo cargado desde: {model_path}")

    def _audio_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def _recording_loop(self):
        with sd.RawInputStream(samplerate=self.sample_rate, blocksize=8000,
                               dtype='int16', channels=1, callback=self._audio_callback):
            print("Grabando... presiona ENTER para detener")
            while not self.stop_recording.is_set():
                try:
                    data = self.q.get(timeout=0.1)
                    if self.recognizer.AcceptWaveform(data):
                        res = json.loads(self.recognizer.Result())
                        self.transcription += res.get("text", "") + " "
                except queue.Empty:
                    continue
            # Procesar audio final
            final_res = json.loads(self.recognizer.FinalResult())
            self.transcription += final_res.get("text", "")

    def record(self):
        self.transcription = ""
        self.stop_recording.clear()
        thread = threading.Thread(target=self._recording_loop)
        thread.start()
        input()  # Espera Enter para detener
        self.stop_recording.set()
        thread.join()
        return self.transcription.strip()
