import pygame
pygame.init()

#Ukuran layar game
win = pygame.display.set_mode((650, 600))

#judul game
pygame.display.set_caption("Si Maba")

#import sprite/gambar karakter dari folder ke pygame
walkRight = [pygame.image.load('./assets/sprite/maba/R1.png'), pygame.image.load('./assets/sprite/maba/R2.png'), pygame.image.load('./assets/sprite/maba/R3.png'), pygame.image.load('./assets/sprite/maba/R4.png'),
pygame.image.load('./assets/sprite/maba/R5.png'), pygame.image.load('./assets/sprite/maba/R6.png'), pygame.image.load('./assets/sprite/maba/R7.png'), pygame.image.load('./assets/sprite/maba/R8.png'), pygame.image.load('./assets/sprite/maba/R9.png')]
walkLeft = [pygame.image.load('./assets/sprite/maba/L1.png'), pygame.image.load('./assets/sprite/maba/L2.png'), pygame.image.load('./assets/sprite/maba/L3.png'), pygame.image.load('./assets/sprite/maba/L4.png'), 
pygame.image.load('./assets/sprite/maba/L5.png'), pygame.image.load('./assets/sprite/maba/L6.png'), pygame.image.load('./assets/sprite/maba/L7.png'), pygame.image.load('./assets/sprite/maba/L8.png'), pygame.image.load('./assets/sprite/maba/L9.png')]
bg = pygame.image.load('./assets/bg.jpg')
char = pygame.image.load('./assets/sprite/maba/standing.png')

#import sound effects dan music dari folder ke pygame
jumpSound = pygame.mixer.Sound("./assets/audio/jump.wav")
hitSound = pygame.mixer.Sound("./assets/audio/hit.wav")
music = pygame.mixer.music.load("./assets/audio/music.mp3")
pygame.mixer.music.play(-1)

#clock
clock = pygame.time.Clock()

semangat = 100
score = 0

#Atribut player (pemain)
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 8
        self.standing = True
        self.hitbox = (self.x,self.y,20,48)

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))
        self.hitbox = (self.x,self.y,20,48)

    def hit(self):
        hitSound.play()
        self.isJump = False
        self.jumpCount = 8
        self.x = 64
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans',100)
        text = font1.render('Terpajaki', 1, (225,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class enemy(object):
    walkRight = [pygame.image.load('./assets/sprite/senior_lvl1/R1E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R2E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R3E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R4E.png'),
    pygame.image.load('./assets/sprite/senior_lvl1/R5E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R6E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R7E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R8E.png'), pygame.image.load('./assets/sprite/senior_lvl1/R9E.png')]
    walkLeft = [pygame.image.load('./assets/sprite/senior_lvl1/L1E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L2E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L3E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L4E.png'), 
    pygame.image.load('./assets/sprite/senior_lvl1/L5E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L6E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L7E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L8E.png'), pygame.image.load('./assets/sprite/senior_lvl1/L9E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x,self.y,25,48)

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x,self.y,25,48)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        if score > 40:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 100:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 150:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 220:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 300:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 350:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 450:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 650:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 800:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 1000:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
        if score > 1500:
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel

def gameover():
    gameover = True
    win.blit(bg, (0,0))
    font2 = pygame.font.SysFont('comicsans',80)
    font3 = pygame.font.SysFont('comicsans',30)
    text = font2.render('GAME OVER', 1, (0,225,0))
    win.blit(text, (250 - (text.get_width()/2),130))
    text1 = font3.render('Tekan ESCAPE untuk keluar', 1, (225,0,0))
    win.blit(text1, (250 - (text.get_width()/2),250))
    pygame.display.update()
    while gameover:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameover = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def finish():
    win.blit(bg, (0,0))
    font2 = pygame.font.SysFont('comicsans',80)
    text = font2.render('LOLOS', 1, (0,225,0))
    win.blit(text, (250 - (text.get_width()/2),130))
    pygame.display.update()
    finish = True
    while finish:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    finish = False
                    run = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Semangat: ' + str(semangat),1,(225,0,0))
    win.blit(text, (540,10))
    text = font.render('Score: ' + str(score),1,(225,0,0))
    win.blit(text, (10,10))
    maba.draw(win)
    senior.draw(win)
    pygame.display.update()

#mainloop
font = pygame.font.SysFont('comicsans', 20, True)
maba = player(5, 550, 64, 64)
senior = enemy (100, 550, 64, 64, 450)
run = True
while run:
    clock.tick(27)

    if maba.hitbox[1] < senior.hitbox[1] + senior.hitbox[3] and maba.hitbox[1] + maba.hitbox[3] > senior.hitbox[1]:
        if maba.hitbox[0] + maba.hitbox[2] > senior.hitbox[0] and maba.hitbox[0] < senior.hitbox[0] + senior.hitbox[2]:
            maba.hit()
            semangat -= 20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and maba.x > maba.vel:
        maba.x -= maba.vel
        maba.left = True
        maba.right = False
    elif keys[pygame.K_RIGHT] and maba.x < 500 - maba.width - maba.vel:
        maba.x += maba.vel
        maba.right = True
        maba.left = False
    else:
        maba.right = False
        maba.left = False
        maba.walkCount = 0
    if not (maba.isJump):
        if keys[pygame.K_UP]:
            jumpSound.play()
            maba.isJump = True
            maba.right = False
            maba.left = False
            maba.walkCount = 0
    else:
        if maba.jumpCount >= -8:
            neg = 1
            if maba.jumpCount < 0:
                neg = -1
            maba.y -= (maba.jumpCount ** 2) * 0.5 * neg
            maba.jumpCount -= 1
        else:
            maba.isJump = False
            maba.jumpCount = 8
            score += 10
    if semangat < 1:
        gameover()
    if score > 2000:
        finish()

    redrawGameWindow()

pygame.quit()