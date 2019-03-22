# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository. 
#
#Delete these comments before commit!
#Good luck.
    
from __future__ import division
import random as ran

class Car:
	def __init__(self, v_0, ang):
		self.speed = v_0
		self.angle = ang
	def print_parameters(self):
		print "Current angle is", self.angle
		print "Current speed is", self.speed
	def change_speed(self, dv):
		self.speed = self.speed + dv
	def change_angle(self, da):
		if ran.random >= 0.5:
			self.angle = self.angle + da
		else:
			self.angle = self.angle + da
	def obstacle(self, time):
		print "You will crash into obstacle in ", time, " seconds"
	def set_new_param(self, new_speed, new_angle):
		self.speed = new_speed
		self.angle = new_angle


start_velocity = float(raw_input("Type velocity: "))
start_angle = float(raw_input("Type wheel angle: "))

car = Car(start_velocity, start_angle)
car.print_parameters()
t = 10

while 1:
	while t>0:
		car.obstacle(t)
		car.change_speed(-2)
		car.change_angle(5)
		car.print_parameters()
		t = t-1
		if car.speed <0:
			car.speed = 0
			break
	if car.speed <= 0:
		print "You successfully stopped before crashing into obstacle"
	else:
		print "CRASH"

	end = int(raw_input("Would you like to stop the program? (1 - yes), anything else - no : "))	
	if end == 1:
		break
	else:
		new_velocity = float(raw_input("Type new velocity: "))
		new_ang = float(raw_input("Type new wheel angle: "))
		car = Car(new_velocity,new_ang)
	
