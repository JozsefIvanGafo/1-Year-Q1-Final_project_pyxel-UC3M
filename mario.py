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
        self.sprite=(1,0,0,16,16)
        