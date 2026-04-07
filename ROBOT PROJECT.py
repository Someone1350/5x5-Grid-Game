import random

layout = [["▌","┉","┉","▀","┉","┉","▀","┉","┉","▀","┉","┉","▀","┉","┉","▀","┉","┉","▐"],
          ["▌","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▐"],
          ["▌","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▐"], #GRID/LAYOUT
          ["▌","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▐"],
          ["▌","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▐"],
          ["▌","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▬","┉","┉","▐"],
          ["▌","┉","┉","▄","┉","┉","▄","┉","┉","▄","┉","┉","▄","┉","┉","▄","┉","┉","▐"]]

class variables:
    """Variable(layout): A list containing the grid layout which is a 5x5 grid
    Class(variables): A class system which acts as a store for variables that can be accessed by both classes give a cleaner look
    """
    def __init__(self):
        self.row = [3,6,9,12,15]
        self.col = [1,2,3,4,5]

        self.user = "☺"
        self.player_x= 0
        self.player_y = 0
        
        self.enemy = "☻"
        self.enemy_x = 0
        self.enemy_y = 0

        self.clicks = 0
        self.is_running = True
#--------------------------------------------------------------------------
class player():
    """Class(player): Class for player movements on the grid

    Methods:
    __init__(sharevar): Initialises shared variables and spawn_enemy
    spawn: Randomnly places the player during spawn into the grid
    bound(axis_player,move): Move player and updates the grid
    move: Asks the user for movement
    printer: Prints the grid"""

    def __init__(self,sharevar):
        """Initialises the player and spawn_enemy"""
        
        self.share = sharevar
        self.e = enemy(self.share)
        self.e.spawn_enemy() 

    def spawn(self):
        """Randomnly places the player on the grid and updates the grid"""

        self.share.player_x = random.choice(self.share.row)
        self.share.player_y = random.choice(self.share.col)
        layout[self.share.player_y][self.share.player_x] = self.share.user


    def bound(self,axis_player,move):
            """Decides the Direction using Parameter(axis_player_ and updates the grid"""

            if axis_player == "w" or axis_player == "s":
                if self.share.player_y + move in self.share.col:
                    layout[self.share.player_y][self.share.player_x] = "▬"
                    self.share.player_y += move
            else:
                if self.share.player_x + move in self.share.row:
                    layout[self.share.player_y][self.share.player_x] = "▬"
                    self.share.player_x += move

            layout[self.share.player_y][self.share.player_x] = self.share.user
            self.share.clicks+=1
            return True

    def move(self):
        """Controls the input of the user for movements"""
        combinations = {"w":-1,"s":1,"a":-3,"d":3}
        while True:
            if not self.share.is_running:
                print(f"\nYou Lost\nYour highscore is {self.share.clicks}")
                break
            else:
                movement = input("Make a move:   ")
                if movement in combinations.keys():
                    self.bound(movement,combinations.get(movement)) 
                    self.e.enemybound()
                    self.printer()    

    def printer(self):
        """Prints the layout after any new update"""
        for x in layout:
            print("")
            for y in x:
                print(y, end ="")
#--------------------------------------------------------------------------------
class enemy():
    """"Class(enemy): Handles the function for enemy movement and location
__init__(sharevar): Intialises self and shared class
spawn_enemy: Randomnly places the enemy onto the grid
enemybound: Decides the direction of the enemy after player movement
"""
    
    def __init__(self,sharevar):
        """Initialises the variables required
        Variable(self.share): Class(variables)
        Variable(axis): For the direction of motion of the enemy
        Variable(move_enemy): For the steps required to take in that direction"""

        self.share = sharevar
        self.axis = ""
        self.move_enemy = 0

    def spawn_enemy(self):
        """Sets the enemy x,y coordinate"""

        self.share.enemy_x = random.choice(self.share.row) #This one returns the spawn position of the player at the start
        self.share.enemy_y = random.choice(self.share.col)
        layout[self.share.enemy_y][self.share.enemy_x] = self.share.enemy
    
    def enemybound(self):
            """Decides the direction of motion of the enemy appropriately by comparing player x,y coordinates"""

            if self.share.enemy_y == self.share.player_y and self.share.enemy_x == self.share.player_x:
                    self.share.is_running = False
                    return True
            
            if self.axis == "":
                self.axis = random.choice(["x", "y"])

            if self.axis == "y":

                if self.share.enemy_y > self.share.player_y:
                    self.move_enemy = -1
                elif self.share.enemy_y < self.share.player_y:
                    self.move_enemy = 1

                    
                if self.share.enemy_y + self.move_enemy in self.share.col:
                    layout[self.share.enemy_y][self.share.enemy_x] = "▬"
                    self.share.enemy_y += (self.move_enemy)
                    layout[self.share.enemy_y][self.share.enemy_x] = self.share.enemy
            else:
                if self.share.enemy_x > self.share.player_x:
                    self.move_enemy = -3
                elif self.share.enemy_x < self.share.player_x:
                    self.move_enemy = 3

                if self.share.enemy_x + self.move_enemy in self.share.row:
                    layout[self.share.enemy_y][self.share.enemy_x] = "▬"
                    self.share.enemy_x += (self.move_enemy)
                    layout[self.share.enemy_y][self.share.enemy_x] = self.share.enemy 

            if self.share.enemy_y == self.share.player_y and self.share.enemy_x == self.share.player_x:
                    self.share.is_running = False
                    return True

            if self.axis == "y" and self.share.enemy_y == self.share.player_y:
                self.axis = ""
            if self.axis == "x" and self.share.enemy_x == self.share.player_x:
                self.axis = ""
            return True
#------------------------------------------------------------------------------------------------
shared = variables()
p = player(shared)

p.spawn()
for x in layout:
    print("")
    for y in x:
        print(y, end ="")
p.move()