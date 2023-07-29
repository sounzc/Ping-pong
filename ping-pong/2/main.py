from pygame import *


class GameSprite(sprite.Sprite):
    def _init_(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super()._init_()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed
    def update_2(self):
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 490:
            self.rect.y += self.speed
        
win_width = 700
win_height = 500

display.set_caption('Пинг-понг')
window = display.set_mode((700, 500))
background = transform.scale(image.load('back.png'), (700, 500))
game = True

clock = time.Clock()
FPS = 60
#tenniss = GameSprite('tennis.png',20,20,50,50,5)
plat1 = Player('platform2.png', 250,30,20,100,5)
plat2 = Player('platform2.png', 250,600,20,100,5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0,0))
    #tenniss.reset()

    plat1.reset()
    plat2.reset()
    display.update()
    clock.tick(FPS)
