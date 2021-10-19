

#!/usr/bin/env python  

__author__ = 'Raphael Leber'

from math import cos, sin, tan, pi, sqrt, atan2, fmod, fabs
import turtle  
import time

BLUE    = (-80, 70)
GREEN   = (100, 140)
PURPLE  = (0, -150)

from vehicles.Bicycle import Bicycle
from vehicles.TurtleBot import TurtleBot


class VehicleSimlulator():
    def __init__(self):

        self.frame = turtle.Screen()
        self.frame.bgpic("img/turtle_pose.png")
        self.frame.setup(width=400,height=600)
        self.robot = turtle.Turtle()
        self.robot.shapesize(4, 1, 1)
        pass


    def updateVehiclePose(self, x, y, theta):
        self.robot.setx(x)
        self.robot.sety(y)
        self.robot.setheading(theta * 180 / pi )


    def selectVehicle(self, vehicle):
        self.vehicle = vehicle


    def toPoint(self, x, y, eps=1):

        for e in self.vehicle.toPoint(x, y, eps):

            self.updateVehiclePose( self.vehicle.x, self.vehicle.y, self.vehicle.theta )


    def turn(self, phi):

        for e in self.vehicle.turn(phi):

            self.updateVehiclePose( self.vehicle.x, self.vehicle.y, self.vehicle.theta )



if __name__ == '__main__':

    # create simulator instance
    vs = VehicleSimlulator()

    # create vehicle instance
    bicycle = Bicycle()
    turtlebot = TurtleBot()

    # Choose one particular vehicle
    vs.selectVehicle(bicycle)

    # --- SCENARIO ---
    vs.toPoint( *BLUE )
    vs.toPoint( *GREEN )
    vs.toPoint( *PURPLE )
    vs.turn( pi/4 )
   
    # End of Scenario
    vs.frame.mainloop()

