import pgzrun
WIDTH=800
HEIGHT=800
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def draw():
    screen.draw.text("A",(50,30),color="white")
def on_mouse_up(pos):
    print("Mouse button clicked",pos)
    if pos[0]>=30 and pos[0]<=70 and pos[1]>=10 and pos[1]<=50: 
        print("a was clicked")
def update():
    pass
pgzrun.go()