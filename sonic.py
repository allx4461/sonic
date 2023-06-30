from pygame import *
import random
window=display.set_mode((700,500))
display.set_caption('sonc')
#background=transform.scale(image.load(''), (700,500))
window_width=700

game=True

clock = time.Clock()


class GameCard(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed_x=player_speed
        self.speed_y=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    #def create(self):

'''короче чтобы не забыть
дефчик креэйт дает по шаблону разные экземляры опр типа через рандом
непонятно, как реализовать наложение картинки на карту
со списками сложно непонятно'''



def choosesprite(card):
    num=randint(0,2) 
    if num==1:
        monster.create()

    if num==2:
        bonus.create()

str1=[card1,card2,card3]
str2=[card1,card2,card3]
str3=[card1,card2,card3]
