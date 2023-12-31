import math
from random import choice
import numpy as np


import pygame


FPS = 30
k=0
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, CYAN]

WIDTH = 800
HEIGHT = 600
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Another_Ball:
    def __init__(self, screen: pygame.Surface,another_gun, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = another_gun.x
        self.y = another_gun.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 5

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x>=789 or self.x <= 10:
            self.vx = -(self.vx)*0.9
            if self.x>=789:
                self.x = self.x-5
            else:
                self.x = self.x +5
        if (self.y>=590) or self.y <=10:
            self.vy = -(self.vy)*0.9
            if (self.y >= 590):
                self.y = self.y - 5
            else:
                self.y = self.y + 5
        self.x += self.vx
        self.y += self.vy
        self.vy = self.vy + 1


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
        pygame.draw.circle(self.screen,BLACK,(self.x, self.y),self.r/2)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y-obj.y)**2)**0.5 <= (self.r + obj.r):
            return True
        return False
    def gunhittest(self,gun):
         if((self.x-(gun.x+20))**2 + (self.y-(gun.y-20))**2)**0.5 <= self.r+15:
             return True
         return False
class Ball:
    def __init__(self, screen: pygame.Surface,gun, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.x
        self.y = gun.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 5

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x>=789 or self.x <= 10:
            self.vx = -(self.vx)*0.9
            if self.x>=789:
                self.x = self.x-5
            else:
                self.x = self.x +5
        if (self.y>=590) or self.y <=10:
            self.vy = -(self.vy)*0.9
            if (self.y >= 590):
                self.y = self.y - 5
            else:
                self.y = self.y + 5
        self.x += self.vx
        self.y += self.vy
        self.vy = self.vy + 1


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            GREY,
            (self.x, self.y),
            self.r/2
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y-obj.y)**2)**0.5 <= (self.r + obj.r):
            return True
        return False
    def anothergunhittest(self,another_gun):
         if((self.x-(another_gun.x+20))**2 + (self.y-(another_gun.y-20))**2)**0.5<=self.r+15:
             return True
         return False
class FireBall:
    def __init__(self, screen: pygame.Surface ,gun , x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.x
        self.y = gun.y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = MAGENTA
        self.live = 5

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x>=789 or self.x <= 10:
            self.vx = -(self.vx)*0.9
            if self.x>=789:
                self.x = self.x-10
            else:
                self.x = self.x +10
        if (self.y>=590) or self.y <=10:
            self.vy = -(self.vy)*0.9
            if (self.y >= 590):
                self.y = self.y - 10
            else:
                self.y = self.y + 10
        self.x += self.vx
        self.y += self.vy
        self.vy = self.vy + 1


    def draw(self):
        pygame.draw.circle(
            self.screen,
            (250, 102, 0) ,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            GREY,
            (self.x, self.y),
            self.r/2
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y-obj.y)**2)**0.5 <= (self.r + obj.r):
            return True
        return False
    def anothergunhittest(self,another_gun):
         if((self.x-(another_gun.x+20))**2 + (self.y-(another_gun.y-20))**2)**0.5<=self.r+15:
             return True
         return False
class Another_FireBall:
    def __init__(self, screen: pygame.Surface ,another_gun ):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = another_gun.x
        self.y = another_gun.y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = MAGENTA
        self.live = 5

    def move(self):

        if self.x>=784 or self.x <= 15:
            self.vx = -(self.vx)*0.9
            if self.x>=789:
                self.x = 784 - abs(784 - self.x)
            else:
                self.x = 15 + abs(15 - self.x)
        if (self.y>=585) or self.y <=15:
            self.vy = -(self.vy)*0.9
            if (self.y >= 585):
                self.y = self.y - 10
            else:
                self.y = self.y + 10
        self.x += self.vx
        self.y += self.vy
        self.vy = self.vy + 1


    def draw(self):
        pygame.draw.circle(
            self.screen,
            (250, 102, 0) ,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r/2
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y-obj.y)**2)**0.5 <= (self.r + obj.r):
            return True
        return False
    def gunhittest(self,gun):
         if(((self.x-(gun.x+20))**2 + (self.y-(gun.y-20))**2)**0.5<=self.r+15):
             return True
         return False

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.vx = 1
        self.x = 20
        self.y = 150

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        k = choice([0,1])
        if k==0:
               new_ball = Ball(self.screen,gun)
        else:
            new_ball = FireBall(self.screen,gun)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        if k==0:
             balls.append(new_ball)
        else:
            fireballs.append(new_ball)
        self.f2_on = 0
        self.f2_power = 20

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((abs(event.pos[1]-450) + 1) /( abs(event.pos[0]-20) + 1))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        #FIXIT don't know how to do it
        pygame.draw.rect(self.screen,GREY,(self.x,self.y,40,40))


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x>=789 or self.x <= 10:
            self.vx = -(self.vx)
            if self.x>=789:
                self.x = self.x-5
            else:
                self.x = self.x +5
        self.x += self.vx



class Gun2:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.vy = 1
        self.x = 100
        self.y = 220

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global another_balls, another_fireballs,another_bullet
        another_bullet += 1
        k = choice([0,1])
        if k==0:
               new_ball = Another_Ball(self.screen, another_gun)
        else:
            new_ball = Another_FireBall(self.screen, another_gun)
        new_ball.r += 5
        self.an = math.atan2(abs((event.pos[1]-new_ball.y))+1, abs((event.pos[0]-new_ball.x))+1)
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        if k==0:
             another_balls.append(new_ball)
        else:
            another_fireballs.append(new_ball)
        self.f2_on = 0
        self.f2_power = 20

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((abs(event.pos[1]-450) +1 )/ (abs((event.pos[0]-20)) + 1))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        #FIXIT don't know how to do it
        pygame.draw.rect(self.screen,BLACK,(self.x,self.y,40,40))


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y>=590 or self.y <=100:
            self.vy = -(self.vy)
            if self.y>=590:
                self.y = self.y-5
            else:
                self.y = self.y +5
        self.y += self.vy





class Target:
    # self.points = 0
    # self.live = 1RED
    #         else:
    #             self.color = GREY
    #
    #     def move(self):
    #         """Движение пушки будет осуществляться с постоянной скоростью по оси х.
    #         """
    #         if self.x >= 800  or self.x <= 10:
    #             self.vx = -(self.vx)
    #             if
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self,screen,color,points = 0,live = 1):
        self.points = points
        self.live = live
        self.screen = screen
        self.color = color
        self.x = choice(list(range(600, 781)))
        self.y = choice(list(range(300, 550)))
        self.r = choice(list(range(15, 70)))
        self.vx = 2
        self.vy = 2

    def new_target(self,screen,color):
        """ Инициализация новой цели. """
        self.x = choice(list(range(600, 781)))
        self.y = choice(list(range(300, 400)))
        self.r = choice(list(range(10, 50)))
        self.vx = 1
        self.vy = 1
        self.screen = screen
        self.live = 1
        self.color = color

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x >= 800-self.r or self.x <= self.r:
            self.vx = -(self.vx)
            if self.x >= 800-self.r:
                self.x = self.x - 5

            else:
                self.x = self.x + 5
        if (self.y >= 600 - self.r) or self.y <= self.r:
            self.vy = -(self.vy)
            if (self.y >= 600 - self.r):
                self.y = self.y - 5
            else:
                self.y = self.y + 5
        self.x += self.vx
        self.y += self.vy


    def hit(self, pointss=1):
        """Попадание шарика в цель."""
        self.points += pointss  #добавила дополнительную s, чтобы отличать наши очки от той единицы, которая здесь добавояется про пропадании

    def draw(self):
        pygame.draw.circle(self.screen,self.color, (self.x, self.y), self.r)
class GravityTarget:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self,screen,color,points = 0,live = 1):
        self.points = points
        self.live = live
        self.screen = screen
        self.color = color
        self.x = choice(list(range(200, 400)))
        self.y = choice(list(range(400, 650)))
        self.r = choice(list(range(15, 60)))
        self.vx = 2
        self.vy = 0

    def new_target(self,screen,color):
        """ Инициализация новой цели. """
        self.x = choice(list(range(600, 781)))
        self.y = choice(list(range(300, 400)))
        self.r = choice(list(range(10, 50)))
        self.vx = 2
        self.vy = 1
        self.screen = screen
        self.live = 1
        self.color = color

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x >= 800-self.r or self.x <= self.r:
            self.vx = -(self.vx)
            if self.x >= 800-self.r:
                self.x = self.x - 8

            else:
                self.x = self.x + 8
        if (self.y >= 600 - self.r) or self.y <= self.r:
            self.vy = -(self.vy)*0.8
            if (self.y >= 600 - self.r):
                self.y = self.y - 8
            else:
                self.y = self.y + 8
        self.x += self.vx
        self.y += self.vy
        self.vx = self.vx + 1
        self.vy = self.vy + np.cos(self.vx)
    def hit(self, pointss=1):
        """Попадание шарика в цель."""
        self.points += pointss  #добавила дополнительную s, чтобы отличать наши очки от той единицы, которая здесь добавояется про пропадании

    def draw(self):
        pygame.draw.circle(self.screen,self.color, (self.x, self.y), self.r)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
another_bullet = 0
balls = []
fireballs = []
another_balls = []
another_fireballs = []
points = 0
another_points = 0
text = "blackpoints = 0, greypoints  = 0"

clock = pygame.time.Clock()
gun = Gun(screen)
another_gun = Gun2(screen)
target = Target(screen, RED)
another_target = GravityTarget(screen, CYAN)
finished = False

while not finished:
    screen.fill(WHITE)
    draw_text(screen, text, 18, WIDTH / 2, 10)
    gun.draw()
    another_gun.draw()
    target.draw()
    another_target.draw()
    target.move()
    another_target.move()
    gun.move()
    another_gun.move()
    text = "greypoints = "+str(points)+ "     blackpoints  = " + str(another_points)
    for b in balls:
        if b.live>0:
           b.draw()
    for f in fireballs:
        if f.live>0:
            f.draw()
    for ab in another_balls:
        if ab.live>0:
            ab.draw()
    for af in another_fireballs:
        if af.live > 0:
            af.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if k%2==0:
                gun.fire2_start(event)
            else:
                another_gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if k%2==0:
                gun.fire2_end(event)
            else:
                another_gun.fire2_end(event)
            k+=1
        elif event.type == pygame.MOUSEMOTION:
            if k%2==0:
                gun.targetting(event)
            else:
                another_gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live and b.live:
            target.live = 0
            target.hit()
            b.live-=1
            points+=1

            target.new_target(screen,RED)
        if b.hittest(another_target) and another_target.live and b.live:
            another_target.live = 0
            another_target.hit()
            b.live-=1
            another_target.new_target(screen,CYAN)
            points += 2
        if b.anothergunhittest(another_gun):
            b.vx = -b.vx
            b.vy = -b.vy
            if b.x<gun.x + 10:
                b.x -=5
            else:
                b.x +=5
            if b.y<gun.y - 10:
                b.y -=5
            else:
                b.y +=5
            points += 3
    for f in fireballs:
        f.move()
        if f.hittest(target) and target.live and f.live:
            target.live = 0
            target.hit()
            f.live -= 0.5
            target.new_target(screen,RED)
            points +=1
        if f.hittest(another_target) and another_target.live and f.live:
            another_target.live = 0
            another_target.hit()
            f.live-=0.5
            another_target.new_target(screen, CYAN)
            points +=2
        if f.anothergunhittest(another_gun):
            f.vx = -f.vx
            f.vy = -f.vy
            if f.x < gun.x + 10:
                f.x -= 5
            else:
                f.x += 5
            if f.y < gun.y - 10:
                f.y -= 5
            else:
                f.y += 5
            points += 3
    for ab in another_balls:
        ab.move()
        if ab.hittest(target) and target.live and ab.live:
            target.live = 0
            target.hit()
            ab.live -= 1
            target.new_target(screen, RED)
            another_points +=1
        if ab.hittest(another_target) and another_target.live and ab.live:
            another_target.live = 0
            another_target.hit()
            ab.live -= 1
            another_target.new_target(screen, CYAN)
            another_points +=2
        if ab.gunhittest(gun):
            ab.vx = -ab.vx
            ab.vy = -ab.vy
            if ab.x < another_gun.x + 10:
                ab.x -= 5
            else:
                ab.x += 5
            if ab.y < another_gun.y - 10:
                ab.y -= 5
            else:
                ab.y += 5
            another_points += 3
    for af in another_fireballs:
        af.move()
        if af.hittest(target) and target.live and af.live:
            target.live = 0
            target.hit()
            af.live -= 0.5
            target.new_target(screen, RED)
            another_points +=1
        if af.hittest(another_target) and another_target.live and af.live:
             another_target.live = 0
             another_target.hit()
             af.live -= 0.5
             another_target.new_target(screen,CYAN)
             another_points += 2
        if af.gunhittest(gun):
            af.vx = -af.vx
            af.vy = -af.vy
            if af.x < gun.x + 10:
                af.x -= 5
            else:
                af.x += 5
            if af.y < gun.y - 10:
                af.y -= 5
            else:
                af.y += 5
            another_points += 3
    gun.power_up()
    another_gun.power_up()

pygame.quit()
