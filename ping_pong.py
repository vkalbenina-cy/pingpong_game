from pygame import *

window = display.set_mode(800, 600)
display.set_caption('Пинг-понг')
back = ()
win_width = 700
win_height = 600
window = display.set_mode(win_width, win_height)
window.fill(back)

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

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
          self.rect.y += self.speed
    if keys[K_UP]and self.rect.y > 1:
          self.rect.y -= self.speed
  def key_second_player(self):
    keys = key.get_pressed()
    if keys[K_s] and self.rect.y < 500:
        self.rect.y += self.speed
    if keys[K_w] and self.rect.y > 2:
        self.rect.y -= self.speed
tenis_ball = GameSprite('blueberry.png', 100, 100, 100, 100, 5)
racket1 = Player('racket.png', 20, 20, 25, 100, 5)
racket2 = Player('racket.png', 650, 20, 25, 100, 5)

FPS = 60
clock = time.Clock()
game = True
finish = False
while game:
    window.blit(my_surface, (0, 0))
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

      ball.rect.x += ball.speed
      ball.rect.y += ball.speed

      if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
        ball.rect.x *= -1
        ball.rect.y *= -1
      if ball.rect.y == 100 or ball.rect.y == 500:
        ball.rect.x += ball.speed
        ball.rect.y += ball.speed

      # if ball.rect.x <= 100:
      #   window.blit(lose1, (60, 100))
      # elif ball.rect.x >= 600:
      #   window.blit(lose2, (60, 100))
        
    display.update()
    window.fill(back)
display.update()

