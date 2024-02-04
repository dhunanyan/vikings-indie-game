import os
import pygame 
# import imageio

sprites = {}
audios = {}

# THIS IS FOR GIF
#
# def load_sprites():
#   path = os.path.join('assets', 'sprites')
#   for file in os.listdir(path):
#       name, extension = os.path.splitext(file)
#       if extension.lower() == '.gif':
#         gif_path = os.path.join(path, file)
#         gif_images = imageio.mimread(gif_path)
#         rotated_frames = [pygame.transform.rotate(pygame.surfarray.make_surface(img), -90) for img in gif_images]
#         sprites[name] = rotated_frames
#       else:
#         sprites[name] = pygame.image.load(os.path.join(path, file))

def load_sprites():
  path = os.path.join('assets', 'sprites')
  for file in os.listdir(path):
    sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
  return sprites[name]

def load_audios():
  path = os.path.join('assets', 'audios')
  for file in os.listdir(path):
    audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))
    
def play_audio(name):
  audios[name].play()