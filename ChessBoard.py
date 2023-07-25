from turtle import * 
import turtle
scr = turtle.Screen()
turtle.title("CHESS BOARD")
scr.bgcolor("blanchedalmond")   
tur = turtle.Turtle()
def draw():
  for i in range(4):
    tur.backward(35)
    tur.left(90)   
    tur.shape("square")
  tur.backward(35)
if __name__ == "__main__" :   
    scr.setup(700, 700) 
    tur.speed(110) 
    for i in range(8):
      tur.up()
      tur.setpos(100, 35 * i)
      tur.down()
      for j in range(8):
        if (i + j)% 2 == 0:
          col ='black'
        else:
          col ='white'
        tur.fillcolor(col)
        tur.begin_fill()
        draw()
        tur.end_fill()
    tur.hideturtle()
tur.clone()
         
