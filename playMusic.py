import pygame                   # 导入pygame库
import time
file = r'./10261.mp3'


def goal_message():
    pygame.mixer.init()
    #print("播放音乐1")
    track = pygame.mixer.music.load(file)

    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()