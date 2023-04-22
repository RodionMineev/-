import pygame as pg
import random

W, H, FPS = 800, 800, 120
SIZE = (W, H)
clock = pg.time.Clock()
'''
параметры экрана и фпс
'''

pg.init()
win = pg.display.set_mode(SIZE)
'''
создание экрана
'''


class Circle:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad
        self.dx = random.choice([-1, -0.5, -0.25, 0.25, 0.5, 1])
        self.dy = random.choice([-1, -0.5, -0.25, 0.25, 0.5, 1])
        self.color = random.choices(range(0, 256), k=3)
        '''
        выбирает рандомный элемент
        '''

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > H or self.x < 0:
            self.dx = -self.dx + random.randint(-1, 1)
        if self.y > H or self.y < 0:
            self.dy = -self.dy + random.randint(-1, 1)
        '''
        движение объекта
        '''

    def show(self):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)
        '''
        отображение объекта
        '''


circles = []
for i in range(100):
    circles.append(Circle(W // 2, H // 2, 50))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for circle in circles:
        circle.move()
    '''
    заствляет каждый круг двигатся
    '''

    win.fill((0, 0, 205))
    for circle in circles:
        circle.show()
    pg.display.flip()
    clock.tick(FPS)

'''
запуск игры
'''
