import pygame
import sys
from pygame.locals import *

# 初始化Pygame模块
pygame.init()
pygame.mixer.init()

# 创建窗口
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("日本阵亡模拟器")

# 加载图片
bg_image = pygame.image.load("JP.png")

# 设置字体
font = pygame.font.Font(None, 36)

# 设置点击计数
click_count = 0

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            click_count += 1

    # 绘制背景
    screen.blit(bg_image, (0, 0))

    # 绘制点击内容
    if click_count == 1:
        pygame.mixer.music.load('1.mp3')
        pygame.mixer.music.play()
        pygame.time.wait(2000)
        pygame.mixer.music.stop()
        
    elif click_count == 2:
        pygame.mixer.music.load('2.mp3')
        pygame.mixer.music.play()
        pygame.time.wait(2000)
        pygame.mixer.music.stop()
        
    elif click_count == 3:
        pygame.mixer.music.load('3.mp3')
        pygame.mixer.music.play()
        pygame.time.wait(2000)
        pygame.mixer.music.stop()
        
    elif click_count == 4:
        pygame.mixer.music.load('4.mp3')
        pygame.mixer.music.play()
        pygame.time.wait(2000)
        pygame.mixer.music.stop()
        
        
    elif click_count >= 5 and click_count<=58:
        pygame.mixer.music.load('5.mp3')
        pygame.mixer.music.play()
        pygame.time.wait(2000)
        pygame.mixer.music.stop()
        
    elif click_count >= 59:
        text = font.render("Japanese was Died", True, (0, 0, 0))
        screen.blit(text, (200, 200))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.update()
