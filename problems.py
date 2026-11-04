'''
This file will contain your the code for your problems. 
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

class Vehicle:
    #create a world for any kind of vehicle when an instance of the class is created so all the other functions can work and not crash if called without having to manually create the world first
    def __init__(self,rows=12, columns=15,seed=0, maxSteps=100):
        self.rows = rows
        self.columns = columns
        self.seed = seed
        self.maxSteps =maxSteps
        #create the hex grid calling the function
        self.centers = makeHexGrid(rows,columns)
        #random number generator is created once, and there is a seed to be able to create different maps later on when wanting to test
        self.randomNum = np.random.default_rng(seed)
        self.start,self.goal = pickStartAndGoal(self.centers,rows,columns,self.randomNum)
        self.reset()


    #take the vehicle back to the start
    def reset(self):
        #number of hex that the vehicle starts in
        self.currentIndex = self.start
        #position of the hex that the vehicle starts in 
        self.currentLocation = self.centers[self.start]
        #amount of moves yet
        self.steps = 0
        #which hexes have been visited 
        self.path = [self.start]


    #there are only 3 different speeds and 1 moves 1 unit per step and 2 moves 2 units per step and so on
    speed=[1,2,3]
    #angles work the same as in math; 0 points east and the direction goes counterclockwise
    angles=[0, 60, 120, 180, 240, 300] 
    directions=["E","NE","NW","W","SW","SE"]
    
    #calculates intended movement
    def move(self,speed, angle, currentLocation):
        #radians are needed for np to calculate x and y components with sin and cos functions
        radians = np.radians(angle)
        #change of location in x ( sqrt3 circumradii per step, that is 1 unit to INTEND TO move from one hex center to another)
        dx = np.sqrt(3) * speed * np.cos(radians)
        #change of location in y
        dy = np.sqrt(3) * speed * np.sin(radians)
        #returns how far the vehivle wants to move, but still no movement performed
        return np.array([dx,dy])
    
    #add disturbance (in the parent class there is no disturbance but each child will add their own type of distrubance to the terrain)
    def disturbance(self, intended):
        return np.array([0.0,0.0])

    #called by algorithms.py, will return all the possible movements 
    def getLegalMoves(self):
        moves =[]
        for s in self.speed:
            for a in self.angles:
                moves.append((s,a))
        return moves

        

#class Rover(Vehicle):
 #   def move():

#class Drone(Vehicle):
 #   def move():

#class Boat(Vehicle):
    
        
    #this creates a hex grid for the simulation and takes as input how many rows are needed and how many columns
def makeHexGrid(rows, cols):
    size = 1
    centers = []
    for row in range(rows):
        for col in range(cols):
            #the with of a hex is sqrt3 * size circumradius, then it gets shifted every other row by half
            x = np.sqrt(3) * (col + 0.5 *(row%2))
            #the distance between vertical hexs centers is 1.5 circumradi
            y=1.5*row
            centers.append([x,y])

    return np.array(centers)

#the movement will not be continous, it will be discrete so we need the vehicle to snap back to the closest center
def findClosestHexCenter(position, centers):
    distances = np.linalg.norm(centers - position, axis = 1)
    return np.argmin(distances)


#this function is for the rover, the scalar field determines the height of the terrain
#keeping the blur the same for all iterations but this can be changed later on BUT IT HAS TO BE AN ODD NUMBER BECAUSE THE BLUR NEEDS A CENTER
def makeScalarField(rows, cols, randomNum, blur=5):
    #creates a 2d array with cols as columns and rows as rows filled with random numbers from 0 to 1 
    noise = randomNum.random((rows,cols)).astype(np.float32)
    #the terrain gets smooth through a gaussian blur so that the terrain is more cohessive and actually is an average of the terrain around it
    smooth = cv2.GaussianBlur(noise,(blur,blur),0)
    #makes it so the highest point is 1 and the lowest is 0 so each grid has the same scale
    smooth = (smooth - smooth.min())/(smooth.max()-smooth.min())
    #turns the table into a list in the same order as makeHexGrid() function
    return smooth.flatten()

def makeVectorField(rows, cols, randomNum, blur=5):
    #strength field represents the force of a vector
    strength = makeScalarField(rows, cols, randomNum, blur)
    #angle field represents the direction of a vector
    angle = makeScalarField(rows, cols, randomNum, blur)
    #convert to angles 
    angle = angle * 360
    #convert degrees into radians
    angle = np.radians(angle)
    #x coordinate push
    x = np.cos(angle) * strength
    #y coordinate push
    y = np.sin(angle) * strength
    #return 2d stack with columns so 1st column is the xs and 2nd is the ys
    return np.stack([x,y], axis= 1)


#the boat faces both water and air conditions so both the fields get combined
def combineFields(fieldWater,fieldWind):
    #the wind has a weight of .5 because it moves the boat less than water does
    finalField = fieldWater + (fieldWind * 0.5)

    return finalField
    
#this function picks the end goal and the start point for all the vehicles
def pickStartAndGoal(centers,rows,cols, randomNum):
    #the distance has to be at least third of the length of the either the column or row depending on which is longer to keep the difficulty somewhat similar amongst simulations
    minDistance = max(rows,cols)/3
    #pick a random start 
    start = randomNum.choice(len(centers))
    #get the distance between the start all the other hexes
    distances = np.linalg.norm(centers- centers[start], axis =1)/np.sqrt(3)
    #get all the hexes that are far enough in a list 
    possibleGoals = np.where(distances >= minDistance)[0]
    #get the goal randomly
    goal = randomNum.choice(possibleGoals)
    return int(start), int(goal)

#def Simulation():

