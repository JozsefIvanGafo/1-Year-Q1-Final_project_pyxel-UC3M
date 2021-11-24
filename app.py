import pyxel
from mario import Mario

class App:
    """This class contains all the information needed to execute the game
    """
    def __init__(self,width:int,height:int) :
        """This are the parameters to create the screen
        """
        self.width=width
        self.height=height
        #We spawn a Mario on the screen
        self.mario=Mario(100,200,True)
    #Update to create the controls of the program on pyxel
    def update(self):
        #Close the window
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    #We declare the function to draw the different elements on the code
    def draw(self):
        #We paint the background to black
        pyxel.cls(3)
        """We draw Mario taking the values from the mario object 
        invoked on the App __init__ class
        @param x
        @param y
        @image bank
        @start x
        @start y
        @size16x16
        @coolkey"""
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4])