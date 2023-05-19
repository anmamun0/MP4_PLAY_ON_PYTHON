# You need to install this module 
# pip install pygame
# pip install moviepy

import pygame
from moviepy.editor import *

clip = VideoFileClip('video_file.mp4')
clip.preview()
 
pygame.quit()
