import os
import pygame

sprites = {}
audios = {}


def load_sprites():
    path = os.path.join(r'c:\Users\trong\Desktop\flappy-bird\flappy-bird\assets\sprites')
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    print(f"Found directory: {path}")
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        print(f"Found file: {full_path}")
        sprites[file.split('.')[0]] = pygame.image.load(full_path)


def get_sprite(name):
    return sprites[name]


def load_audios():
    path = os.path.join(r'c:\Users\trong\Desktop\flappy-bird\flappy-bird\assets\audios')
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    for file in os.listdir(path):
        if file.endswith(('.wav', '.mp3')):  
            print(f"Loading audio: {file}")
            audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))
        else:
            print(f"Skipping non-audio file: {file}")


def play_audio(name):
    audios[name].play()
