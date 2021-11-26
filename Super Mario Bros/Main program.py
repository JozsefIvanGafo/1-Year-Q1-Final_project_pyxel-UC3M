"""
Super mario bros game
description:
Here the program will exectu the code
@Author: József Iván Gafo and Marcos González
@since 11/14/2021
@Version 0.0
"""
#We import the libraries and classes needed for the program
import pyxel
from app import App

#We eecute the class app so the program can run
app=App(256,256)          

#We create the pyxel window
pyxel.init(app.screen_width,app.screen_height,caption="Super Mario Bros (Final Project)")

#We load the marioassets.pyxres file where we store the bank of images,music
pyxel.load("assets/marioassets.pyxres")


#Here it executes the program
pyxel.run(app.update,app.draw)
