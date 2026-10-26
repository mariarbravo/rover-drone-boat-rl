'''
This file will contain your the code for your problems. 
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

class Vehicle:
    def __init__(self,currentLocation):
        self.currentLocation = currentLocation
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

#def makeVectorField():

#def makeScalarField():

#def combineFields():


def Simulation():

