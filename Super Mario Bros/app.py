"""
Super mario bros game App class
description:
Here the program will create a class App that will execute the draw and update functions for the Main program
@Author: József Iván Gafo and Marcos González
@since 11/14/2021
@Version 0.0
"""
import pyxel
from mario import Mario

class App:
    """This class execute the draw and update functions"""
    def __init__(self,width:int,height:int) :
        """This are the parameters to create the screen
        """
        self.screen_width=width
        self.screen_height=height
        #We spawn a Mario on the screen (on the top down on the left)
        self.mario=Mario(0,self.screen_height-48,True)

    #Here we will put the diferent controls for mario and ennemies
    def update(self):
        #If we press the button escape the program will close
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        #If the user press the right key or D mario will move to the right (hold,period are paramaters so you can hold the key and mario will move)
        if (pyxel.btnp(pyxel.KEY_RIGHT,hold=1,period=1))  or (pyxel.btnp(pyxel.KEY_D,hold=1,period=1)):
            self.mario.movement("right")
        #If the user press the left key or A mario will move to the left (hold,period are paramaters so you can hold the key and mario will move)
        elif pyxel.btnp(pyxel.KEY_LEFT,hold=1,period=1)  or pyxel.btnp(pyxel.KEY_A,hold=1,period=1):
            self.mario.movement("left")
        #If the user press the up key or space or w mario will move to the right (hold,period are paramaters so you can hold the key and mario will move)    
        if (pyxel.btnp(pyxel.KEY_UP,hold=1,period=1))  or (pyxel.btnp(pyxel.KEY_SPACE,hold=1,period=1)) or (pyxel.btnp(pyxel.KEY_W,hold=1,period=1)):
            self.mario.movement("jump")
        #Temporary key until we add physics
        elif pyxel.btnp(pyxel.KEY_DOWN,hold=1,period=1)  or pyxel.btnp(pyxel.KEY_S,hold=1,period=1):
            self.mario.movement("down")
        

    #Here we declare the draw function, where it will do the graphics part
    def draw(self):
        #We project the tilemap on the screen (It needs to be first so it doesn't overwrite Mario)
        pyxel.bltm(0, 0, 0, 0, 0, 32, 32)
        """We draw Mario taking the values from the mario object 
        invoked on the App __init__ class
        @param x
        @param y
        @image bank
        @start x
        @start y
        @size16x16
        @colkey=0 is so that mario background on the sprite is transparent"""
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4],colkey=0)