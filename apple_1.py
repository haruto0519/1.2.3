#   a123_apple_1.py
import turtle as trtl
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()



#-----function calls-----
draw_apple(apple)

xcor = 0
ycor = -150

def drop_apple():
  apple.goto(xcor,ycor)
  apple.clear()

drawer = trtl.Turtle()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.
wn.onkeypress(drop_apple,"a")

draw_an_A()


wn.listen()



wn.mainloop()