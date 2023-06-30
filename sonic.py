from pygame import *
from random import *
font.init()
#pygame.init()
window=display.set_mode((320,620))
display.set_caption('sonc')
#background=transform.scale(image.load(''), (700,500))
window_width=700
color=(90,250,60)
width,height=200,100
rectx,recty=150,150
rectan=Rect(rectx,recty,width,height)
window.fill((0,0,0))
Font1=font.Font(None,30)
text=Font1.render('HP=9',True,(255,255,255))
game=True
pole=[[0,0,0],[0,0,0],[0,0,0]]
clock = time.Clock()
positions=[[(10,10),(110,10),(210,10)],[(10,210),(110,210),(210,210)],[(10,410),(110,410),(210,410)]]

def search(position):
    if position==1:
        i=0
        j=0
    if position==2:
        i=0
        j=1
    if position==3:
        i=0
        j=2
    if position==4:
        i=1
        j=0
    if position==5:
        i=1
        j=1
    if position==6:
        i=1
        j=2
    if position==7:
        i=2
        j=0
    if position==8:
        i=2
        j=1
    if position==9:
        i=2
        j=2
    return i,j

def interaction(player):
    i,j = search(player.position)
    player.atk+=pole[i][j].hp
    if pole[i][j].hp>player.atk:
        pole[i][j].hp+=player.atk
        if pole[i][j].hp>0:
            player.hp+=pole[i][j].hp
    else:
        player.atk+=pole[i][j].hp

    player.atk+=pole[i][j].atk  
    player.coins+=pole[i][j].coins  
    if player.hp<=0:
        game=False

class GameCard(sprite.Sprite):
    def __init__(self, card_image,card_x,card_y,card_hp,card_atk,card_coins,card_position):
        super().__init__()
        self.image=transform.scale(image.load(card_image),(65,65))
        self.rect=self.image.get_rect()
        self.rect.x=card_x
        self.rect.y=card_y
        self.hp=card_hp
        self.atk=card_atk
        self.coins=card_coins
        self.position=None


    def move(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and player.rect.y!=10:
            player.rect.y-=200
            player.reset()
            player.position-=3
            interaction(player)
        if keys_pressed[K_DOWN] and player.rect.y!=410:
            player.rect.y+=200
            player.reset()
            player.position+=3
            interaction(player)
        if keys_pressed[K_LEFT] and player.rect.x!=10:
            player.rect.x-=100
            player.reset()
            player.position-=1
            interaction(player)
        if keys_pressed[K_RIGHT] and player.rect.x!=210:
            player.rect.x-=100
            player.reset()
            player.position+=1
            interaction(player)

        
        window.blit(self.image,(self.rect.x,self.rect.y))
def create_hero():
    return GameCard('prot1.gif', 0, 0,15,5,1,None)
    
def create_monster():
    return GameCard('monst1.gif',0 , 0,-1*(randint(5,10)),0,randint(10,20),None)

def create_bonus_atk():
    return GameCard('palka.png',0 ,0,0,randint(5,10),0,None)

def create_bonus_hp():
    return GameCard('poison.png', 0, 0,randint(5,10),0,0,None)

def create_bonus_coins():
    return GameCard('coin.png', 0,0 ,0,0,randint(5,10),None)
def create_random(position):
    i,j =search(position)
    for i in range(3):
        x=randint(0,4)
        if x==1:
            pole[i][j] = create_monster()
        if x==2:
            pole[i][j] = create_bonus_atk()
        if x==3:
            pole[i][j] = create_bonus_coins()
        if x==4:
            pole[i][j] = create_bonus_hp()
            
            
            
player = create_hero()
pole=[[create_monster(),create_bonus_coins(),create_bonus_atk()],[create_monster(),create_monster(),create_bonus_coins()],[create_bonus_hp(),create_monster,create_bonus_hp()]]

v=0
def start_game():
    for i in range(3):
        for j in range(3):
            pole[i][j].rect.x , pole[i][j].rect.y = positions[i][j]
            pole[i][j].position = i*3 + j + 1
            create_random(v)
            v+=1
    k=randint(0,3)
    l=randint(0,3)
    pole[k][l] = player


        


while game:
    start_game()
    
    for e in event.get():
        if e.type == QUIT:
            game=False

    #window.exec()

    display.update()
    clock.tick(60)
