from pygame import *
font.init()
from random import randint
display.set_caption('Пинг-понг')
window = display.set_mode((700, 600))
background = transform.scale(image.load('green.jpg'), (700, 600))

sprites_ball = ['blueberry.png', 'toast.png', 'orange.png', 'apple.png']
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
      

class Player(GameSprite):
  def key_first_player(self):
    keys = key.get_pressed()
    if keys[K_DOWN] and self.rect.y < 500:
          self.rect.y += self.speed_y
    if keys[K_UP]and self.rect.y > 1:
          self.rect.y -= self.speed_y
  def key_second_player(self):
    keys = key.get_pressed()
    if keys[K_s] and self.rect.y < 500:
        self.rect.y += self.speed_y
    if keys[K_w] and self.rect.y > 2:
        self.rect.y -= self.speed_y
ball = GameSprite(sprites_ball[randint(0, 3)], 120, 300, 100, 100, 3, 3)
racket1 = Player('racket.png', 650, 300, 25, 100, 5, 5)
racket2 = Player('racket.png', 20, 300, 25, 100, 5, 5)

font = font.Font(None, 70)
lose1 = font.render('FIRST PLAYER LOSE!', True, (255, 215, 0))
lose2 = font.render('SECOND PLAYER LOSE!', True, (255, 215, 0))

FPS = 60
clock = time.Clock()
game = True
finish = False
ball.speed_x = 3
ball.speed_y = 3
while game:
    window.blit(background, (0, 0))
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
      ball.reset()
      racket1.reset()
      racket2.reset()
      racket1.key_first_player()
      racket2.key_second_player()

      ball.rect.x += ball.speed_x
      ball.rect.y += ball.speed_y

      if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
        ball.speed_x *= -1
        

      if ball.rect.y < 0 or ball.rect.y > 510:
          ball.speed_y *= -1 

      if ball.rect.x <= 0:
        window.blit(lose1, (60, 100))
      if ball.rect.x >= 690:
        window.blit(lose2, (60, 100))
        
        
    display.update()
    window.blit(background, (0, 0))
display.update()

