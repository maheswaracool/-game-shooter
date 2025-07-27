from pygame import *
from random import randint

init ()
win_height = 500
win_width = 700
window = display.set_mode((win_width,win_height))
display.set_caption("terserah kamu")

background = transform.scale(
        image.load('SpaceShooter/galaxy.jpg'),
        (700,500)
    )

mixer.init()
mixer.music.load('Spaceshooter/space.ogg')
mixer.music.play()
fire_sound  = mixer.Sound('SpaceShooter/fire.ogg')
lost   = 0
score = 0






class GameSprite(sprite.Sprite):
    def  __init__(self,imagefile,x,y,width,height,speed):
        super().__init__()
        self.image = transform.scale(image.load(imagefile),(width,height))

        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x        
        self.rect.y = y    

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y) )




class Player (GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        
        if keys_pressed[K_RIGHT] and self.rect.x < 700  -  50:
            self.rect.x += self.speed
        
    def fire(self):
        bullet = Bullet('Spaceshooter/bullet.png',self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)


#enemy clas
class Enemy(GameSprite):
    #enemy gerak
    def update(self):
        self.rect.y += self.speed
        global lost
        #menhilan kalau sampai inti bumi
        if self.rect.y > win_height:
            self.rect.x =  randint(80,win_width - 80)
            self.rect.y = 0
            lost = lost + 1




#tembakan classssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssSssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSsssssso
class Bullet(GameSprite):
    #tgerk tembakan ke  musuhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    def update(self):
        self.rect.y += self.speed
        #blablablablebleble
        if self.rect.y <0:
            self.kill()








bullets = sprite.Group()
enmy  =  sprite.Group()
for i in range(1,6):
    enm = Enemy('Spaceshooter/ufo.png',randint(80,win_width - 80),-40,80,50,randint(1,1)) 
    enmy.add(enm)
whosh = Player('SpaceShooter/rocket.png',200,400,80,100,10)
clock = time.Clock()
FPS = 60

is_game = True
is_finish = False
font.init()
fontStyle  = font.Font(None,36)
fontStyletwo = font.Font(None,100)
from time import time
start_tiime = 0
timer_start = False
brp_shot = 12
while is_game: 
    for e in event.get():
        if e.type == QUIT:
            is_game = False


        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if brp_shot >0:

                    fire_sound.play()
                    whosh.fire()
                    brp_shot-= 1
                elif timer_start== False:
                    timer_start  =  True
                    start_tiime = time()
                    
    if timer_start :
        new_time = time()
        if (new_time - start_tiime) >0.5 :
            timer_start = False
            brp_shot = 12   
        

    if not is_finish:
        window.blit(background,(0,0))
        whosh.update()
        whosh.reset()

        enmy.update()
        enmy.draw(window)
        bullets.update()
        bullets.draw(window)
        text_lose = fontStyle.render('lost: '+str(lost),1,(200,200,200))
        text_shott = fontStyle.render('shot: '+str(brp_shot),1,(200,200,200))
        text_score = fontStyle.render('score: '+str(score),1,(200,200,8))
        window.blit(text_score,(10,60))
        window.blit(text_shott,(win_width - 100,60))
        window.blit(text_lose,(10,20))
        collied = sprite.groupcollide(bullets,enmy,True,True)
        for z in collied:
            score += 1
            enm = Enemy('Spaceshooter/ufo.png',randint(80,win_width - 80),-40,80,50,randint(1,1)) 
            enmy.add(enm)
        if score >= 100:
            is_finish =  True
            text_win = fontStyletwo.render('win ',1,(200,200,200))
            window.blit(text_win,(300,300))
        if lost >= 3 or sprite.spritecollide(whosh,enmy,False):
            is_finish =  True
            text_lost = fontStyletwo.render('lost',1,(200,200,200))
            window.blit(text_lost,(300,300))


    display.update()


    clock.tick(FPS)
     
