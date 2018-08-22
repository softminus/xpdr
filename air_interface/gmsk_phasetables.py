#!/usr/bin/env python3


from math import *

samples = 128
bitdepth = 8

beta = pi * 0.3 * sqrt(2 / log(2))

def erfint(normalised_time): # normalised time goes from 0 to 1 to represent 0 to T_b
    erfi = normalised_time * erf(beta * normalised_time) + (1 / ( beta *sqrt(pi))) * exp(-((beta*normalised_time)**2))
    return erfi


def traj_one(t):
    return 0.5 * pi * (erfint(t-1) -1)

def traj_two(t):
    return 0.5 * pi * (erfint(t) - erfint(0.0) - erfint(t-1) + 1 - t)

def traj_three(t):
    return 0.5 * pi * (erfint(t) - erfint(0.0))

def traj_seven(t):
    return 0.5 * pi * t


curve_table_1 = open("curve_1.txt",'w')
curve_table_2 = open("curve_2.txt",'w')
curve_table_3 = open("curve_3.txt",'w')
curve_table_7 = open("curve_7.txt",'w')




def fixup_phase_one(t):
    return (-traj_one(t))

def fixup_phase_two(t):
    return traj_two(t) + 2 * (sqrt(log(2)/(2*pi))/(4*0.3))

def fixup_phase_three(t):
    return traj_three(t) + 2 * (sqrt(log(2)/(2*pi))/(4*0.3))

def fixup_phase_seven(t):
    return traj_seven(t)


#### MASTER CURVES ####

def master_curve_one(t):
    return sin(fixup_phase_one(t))

def master_curve_two(t):
    return sin(fixup_phase_two(t))

def master_curve_three(t):
    return sin(fixup_phase_three(t))

def master_curve_seven(t):
    return sin(fixup_phase_seven(t))

#### float to binary ####

def scale(val, bits):
    norm = (2 ** (bits-1)-1)
    if (val < 0):
        val = 0
    return ceil(val * norm)

def conv(v):
    return scale(v, bitdepth)

for i in range(0,samples):  # from zero (inclusive) to 64 (EXCLUSIVE)
    time = i/samples        # time from 0 to 1 (to represent real time 0 to T_b)
    print (i, conv(master_curve_one(time))   , file=curve_table_1)
    print (i, conv(master_curve_two(time))   , file=curve_table_2)
    print (i, conv(master_curve_three(time)) , file=curve_table_3)
    print (i, conv(master_curve_seven(time)) , file=curve_table_7)

    

