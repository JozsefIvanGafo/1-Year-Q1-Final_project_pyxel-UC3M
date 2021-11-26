"""
Super mario bros game
description:
Here the program will create the class Mario that will be in charge of all the things related to mario
@Author: József Iván Gafo and Marcos González
@since 11/14/2021
@Version 0.0.1
"""
import pyxel
class Mario:
    """This class stores all the information about the entetie of Mario"""
    def __init__(self,x:int,y:int,looking_right:bool):
        """This method creates/spawns mario on such coordinates
        @param x the starting x pos of Mario
        @param y the starting y pos of Mario
        @param looking_right is a bool that indicates that mario 
        is looking right (True/False)
        """
        #We define the position of where to spwan Mario
        self.x=x
        self.y=y
        self.looking_right=looking_right
        #Here we define the sprite of Mario (bank,x pos on the bank, y pos on the bank, size height x base)
        self.sprite=(0,0,48,16,16)
    
    #We define the basic movement for mario(Do not forget to later put a parameter for the size of mushroom)
    def movement(self,direction:str):
        """
        This method defines the movment of mario
        @param direction is where mario will move next
        """
        #To check that the values are correct
        if direction.lower() in ("right","left","jump","down"):
            #Where the order is receive mario moves to the right (x+2)
            if direction.lower()=="right":
                self.x=self.x+1
            #Where mmario receives the order to move to the right (x-2)
            elif direction.lower()=="left":
                self.x=self.x-1
            #Where the order is receive mario moves to the right (y+1)
            if direction.lower()=="jump":
                self.y=self.y-1
            #Where mmario receives the order to move to the right (x-1)
            elif direction.lower()=="down":
                self.y=self.y+1

        #Else we raise an error and we close the program
        else:
            raise ValueError("To use the direction fun. of Mario the direction must be right or left or jump or down, check if you misspelled in your program using this function")
            raise pyxel.quit()
