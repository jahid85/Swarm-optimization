# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:44:03 2022

@author: EON
"""

import numpy as np
import matplotlib.pyplot as plt 
import random

def objective_function(dims):
    y = sum([x**2 for x in dims])
    return y

range_ = (-8,8)


variables = 2
bounds = [range_ for _ in  range(variables)] 
swarms = []

particle_size = 5
iterations = 100 
w= 0.4 
c1 = 1 
c2 = 2 

init = float("inf")

class Particle:
    def __init__(self, bounds):
        self.particle_position = [] 
        self.particle_velocity = [] 
        self.local_best_position = [] 
        self.fit_local_best_position = init
        self.fit_position = init

        for i in range(variables):
            self.particle_position.append(random.uniform(bounds[i][0],bounds[i][1]) )
            self.particle_velocity.append(random.uniform(-1,1)) 
            
            
    def evaluation(self, objective_function):
        self.fit_position = objective_function(self.particle_position)
        
        if self.fit_position < self.fit_local_best_position:
            self.local_best_position = self.particle_position 
            self.fit_local_best_position = self.fit_position
        
            
    def update_velocity(self, global_best_position):
       for i in range(variables):
           r1 = random.random()
           r2 = random.random()

           cognitive_velocity = c1*r1 * (self.local_best_position[i]-self.particle_position[i])
           social_velocity = c2*r2 *(global_best_position[i]- self.particle_position[i])
           self.particle_velocity[i] = w * self.particle_velocity[i] + cognitive_velocity + social_velocity

   
    def update_pos(self, bounds):
       for i in range(variables):
           self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]

           if self.particle_position[i] > bounds[i][1]:
               self.particle_position[i] = bounds[i][1]
           if self.particle_position[i] <bounds[i][0]:
               self.particle_position[i] = bounds[i][0]
               
               
fit_global_best_position = init
global_best_position = []
best = []
for i in range(particle_size):
    swarms.append(Particle(bounds))

for i in range(iterations):
    for j in range(particle_size):
        swarms[j].evaluation(objective_function)
        if swarms[j].fit_position < fit_global_best_position:
            global_best_position = list(swarms[j].particle_position)
            fit_global_best_position = float(swarms[j].fit_position)
            
        if i==0:
            print(f"particle {j} particle postition {swarms[j].particle_position}")
        
    for j in range(particle_size):
        swarms[j].update_velocity(global_best_position)
        swarms[j].update_pos(bounds)
        
    if i==0:
        print(f"initial : {global_best_position}, score : {fit_global_best_position}")
    
    if i%10==0:
        print(f"iteration : {i} global best: {global_best_position},global best score : {fit_global_best_position}")
        
    best.append(fit_global_best_position)
    
    
#print(best)
            
plt.plot(range(len(best)),best,color="red")
plt.xlabel("iteration")
plt.ylabel("best")
plt.show()
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            