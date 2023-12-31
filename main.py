import pgzrun
import json
from pgzero.actor import Actor 
from word_service import WordService
WIDTH=850
HEIGHT=800
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
hangman=Actor("hangman.png",(400,400))
stop = False
x = 50
y = 30
word_service_instance=WordService()
word_service_instance.loadDictonary()
overlap=""

def draw():
    global stop
    global overlap
    #screen.draw.text("A",(50,30),color="white")
    hangman.draw()
    if not stop:
        overlap = word_service_instance.getRandomWord()
        screen.draw.text(overlap[0],(435,700),color="red")
        screen.draw.text(overlap[1],(435,700),color="red")
        stop = True
    ### ? start -> letter, number, decimal?, stop, step
    rolling_position = 0
    for i in range(0,26):
        if i%10 == 0:
            rolling_position = 0

        screen.draw.text(str(letters[i]).upper(),( x + rolling_position * 40  ,y + int(i/10)* 40), color='white',fontsize=32,background="red")
        rolling_position +=1 
        
def on_mouse_up(pos):
    print("Mouse button clicked",pos)
    rolling_position =0
    for i in range(0,26):
        if i%10 == 0:
            rolling_position = 0
        if pos[0]>= (x+rolling_position*40-20)  and pos[0]<=(x+rolling_position*40+20) and pos[1]>=y + int(i/10)* 40 - 20 and pos[1]<=y + int(i/10)* 40 + 20: 
            print( f"{letters[i]} clicked ")
        rolling_position+=1
def update():
    pass
pgzrun.go()