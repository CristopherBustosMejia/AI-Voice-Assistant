import pygame
import time

class AudioPlayer:
    def __init__(self):
        pygame.init()

    def playAudio(self, path: str):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                pygame.time.Clock().tick(10)
            pygame.mixer.music.unload()
            pygame.mixer.quit()
        except Exception as e:
            print(f"[Audio - Error] Error al reproducir el audio: {e}")
    
    def stayActive(self):
        pygame.event.pump()