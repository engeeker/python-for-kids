import pygame
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()

# 游戏初始化
pygame.init()
screen = pygame.display.set_mode([800, 600])

# 设置背景颜色和白板颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
keep_going = True

#加载图片和设置图片初识位置
pic = pygame.image.load("smile.png")
picx = 0
picy = 0
pich = pic.get_height()   # 图片的高度
picw = pic.get_width()    # 图片的宽度

# 设置白板的初始位置坐标
paddlex = 300
paddley = 550

# 白板的宽度和高度
paddlew = 200
paddleh = 50

# 笑脸的运动速度
speedx = 18
speedy = 18

# 标题
point = 0
lives = 5

# 标题字体
font = pygame.font.SysFont("Times", 24)

while keep_going:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    if lives == 0:
        keep_going = False
        messagebox.showinfo('Game Over','Game Over')
    # 设置背景和显示笑脸图片
    screen.fill(BLACK)
    picx = picx + speedx
    picy = picy + speedy
    screen.blit(pic, (picx, picy))

    if picy > 500 or picy < 0:
        speedy = -speedy
        if picy > 500:
            lives = lives - 1
    if picx + picw > 800 or picx < 0:
        speedx = -speedx


    # 显示白板以及跟随鼠标移动
    paddlex = pygame.mouse.get_pos()[0] - paddlew/2
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))

    #判断是否进入白板范围
    if picy + pich >= paddley and picy + pich <=paddley + paddleh and speedy >0:
        if picx + picw/2 >= paddlex and picx + picw/2 <= paddlex + paddlew:
            speedy = -speedy
            point = point + 1

    # 设置一个标题
    title = "Lives: " + str(lives) +  "Points: " + str(point)
    text = font.render(title, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()