import pyxel
from app import App
board=App(255,255)

#We create the pyxel window
pyxel.init(board.width,board.height,caption="Super Mario Bros (Final Project)")
#We load the entities pyxel editor where later we will store the different entities
pyxel.load("assets/entities.pyxres")
#We load Mario on the bank 1 on the position (0,0)
pyxel.image(1).load(0, 0, "assets/Mario.png")
pyxel.run(board.update,board.draw)
