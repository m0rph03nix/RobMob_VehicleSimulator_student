#!/usr/bin/env python  

__author__ = 'Raphael Leber'

from math import cos, sin, tan, pi, sqrt, atan2, fmod, fabs, copysign
import turtle  
import time

from vehicles.Vehicle import Vehicle
from PathTools import PathTools



class Bicycle(Vehicle):

    def __init__(self, x=0, y=0, theta=0, Ks=0.1, Kv=2, L=1.8, steering_max_angle = pi/8, dt = 0.003):
        self.x = x
        self.y = y
        self.theta = theta
        self.Ks = Ks
        self.Kv = Kv         
        self.L = L
        self.steering_max_angle = steering_max_angle  
        self.dt = dt
        self.throttle_min = 400
        self.throttle_max = 1000        




    def model(self, throttle, guidon):
        """  Bicycle model
                           ___________________
                          |                   |
                          |                   |---> x           
            throttle  --->|                   |    
                          |      Bicycle      |
                          |                   |---> y
                          |       Model       |                        
            guidon    --->|                   |   
                          |                   |---> theta      
                          |___________________|          
        """        
        v = min(throttle, self.throttle_max)
        g = min(guidon, self.steering_max_angle) 
        dt = self.dt

        x_p = v * cos(self.theta)
        y_p = v * sin(self.theta)
        theta_p = (v / self.L) * tan( g )

        self.x = self.x + x_p*dt
        self.y = self.y + y_p*dt
        self.theta = self.theta + theta_p*dt

        return self.x, self.y, self.theta



    def toPoint(self, x, y, eps=0.5):
        """ Move to a point (x, y)

            Parameters:
            x (int): x coordinate to reach in the map
            y (int): y coordinate to reach in the map
            eps (float): epsilon below which we consider the goal is reached

            Returns:
            float: Returning throttle value (corresponding to euclidian distance vehicle-->goal) 

        """        
        Ks = self.Ks
        Kv = self.Kv          
        eucli_throttle = eps
        while eucli_throttle >= eps:

            eucli_throttle = sqrt( (x-self.x)**2 + (y-self.y)**2 )
            steering = atan2(  (y-self.y)  , (x-self.x) )

            v = max(min(eucli_throttle * Kv, self.throttle_max), self.throttle_min)
            s = PathTools().shortestAngleDiff(steering, self.theta) * Ks
        
            self.model(v, s)

            yield eucli_throttle



    def turn(self, phi, eps_angle=0.1):

        Ks = self.Ks
        Kv = self.Kv
        s = 1

        while fabs(s) > eps_angle:

            v = 10 # Because a bicyle/car CAN'T turn without linear velocity
            s = PathTools().shortestAngleDiff(phi, self.theta) 

            self.model(v, copysign(self.steering_max_angle, s))

            yield s            


    
    def toPose(self, x, y, theta):

        pass





    