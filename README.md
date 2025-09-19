# Asistente de Voz Inteligente para Base de Datos de Películas 🎬🗣️

Este proyecto es un asistente de voz tipo Alexa desarrollado en Python. Permite al usuario interactuar mediante comandos de voz para consultar información sobre películas almacenadas en una base de datos MySQL (Sakila). El sistema reconoce la voz, interpreta la pregunta usando IA y responde en voz alta.

---

## Características

- **Reconocimiento de voz (STT):** Utiliza Vosk para convertir audio en texto.
- **Procesamiento de lenguaje natural:** Usa modelos LLM (Ollama) para interpretar las preguntas y decidir qué consulta ejecutar.
- **Consultas a base de datos:** Acceso seguro a la base de datos Sakila para obtener información de películas y actores.
- **Síntesis de voz (TTS):** Responde al usuario usando GoogleTTS, CoquiTTS o ElevenLabs.
- **Reproducción de audio:** Utiliza Pygame para reproducir las respuestas generadas.
- **Modularidad:** Fácil de extender con nuevos modelos o funciones.

---

## Requisitos

### Hardware

- PC con Windows, Linux o Raspberry Pi 4 (recomendado para proyecto tipo Alexa)
- Micrófono USB
- Altavoz o salida de audio

### Software

- Python 3.8 o superior
- MySQL Server con base de datos Sakila instalada

### Dependencias Python

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt
```

Principales dependencias:
- vosk
- sounddevice
- gtts
- pygame
- coqui-tts
- mysql-connector-python
- ollama (cliente Python)
- elevenlabs (opcional)

---

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/CristopherBustosMejia/AI-Voice-Assistant.git
   cd AI-Voice-Assistant
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura la base de datos:**
   - Instala MySQL y la base de datos Sakila.
   - Actualiza las credenciales en `main.py` y/o archivos de configuración.

4. **Descarga el modelo Vosk para español:**
   - [Vosk Models](https://alphacephei.com/vosk/models)
   - Coloca el modelo en `data/models/`.

---

## Uso

Ejecuta el asistente desde la terminal:

```bash
python main.py
```

Sigue las instrucciones en pantalla, habla tu consulta y espera la respuesta por voz.

---

## Ejemplo de interacción

- Usuario: "¿Cuáles son las películas más recientes?"
- Asistente: "Las películas más recientes son: ..."

---

## Propuesta de Hardware tipo Alexa

- Raspberry Pi 4
- Micrófono USB
- Altavoz USB o Bluetooth
- Carcasa personalizada
- Conexión WiFi

---

## Créditos

- Vosk Speech Recognition
- Coqui TTS
- Google TTS
- ElevenLabs
- Sakila Database

---

## Licencia

MIT

---

¿Tienes dudas o sugerencias? ¡Abre un issue!