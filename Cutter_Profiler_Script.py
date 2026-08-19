# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:11:45 2026

@author: Jack
"""

import numpy as np

CUTTER_LIST = [0.005, 0.010, 0.015, 0.020, 0.030, 0.060, 0.090, 0.125] #List of available cutter sizes
CUTTER_ANGLE = np.radians(30) #The cutter angle of the cutters, usually 30 degrees for FLEX cutters
SHAFT_DIAMETER = 0.25 #The shaft diameter in inches, upper limit for single pass path width
MAX_CUT_DEPTH = 0.05 #The maximum allowable cut depth

#Input: font height in inches, output: closest cutter size and difference from optimal cutter size
def cutter_given_font_height (font_height): 
    height_percent_decimal = 0.12 #The percentage of the font height that makes the optimal cutter
    optimal_cutter = height_percent_decimal * font_height #Finds the optimal cutter, typically 12% of the font height though user discresion is advised
    
    cutter_array = np.array(CUTTER_LIST) #Form array from cutter list
    difference_array = np.abs(cutter_array-optimal_cutter) #Form array of absolute differences 
    minimum_index = np.argmin(difference_array) #Uses numpy's argmin function to return the index of the minimum value of the difference array
    
    #Print the aproptriate responce
    print(f"For a font height of {font_height} the best cutter available is a {cutter_array[minimum_index]:.3f} with a difference of {difference_array[minimum_index]:.3f}.\n")

#Input: path width in inches, output: cutters that could make that path width and the depth they should be set to to achive it
def depths_given_path_width (path_width):
    #Case handlers
    if path_width > SHAFT_DIAMETER:
        return print(f"The selected path width is greater than {SHAFT_DIAMETER} inches, meaning it will need multiple passes, please devide and try again.\n")
        
    if path_width < min(CUTTER_LIST):
        return print("The selected path width is impossible with the current cutter list, please update the list or increase path width.\n")
    
    
    virtual_depth = (path_width/2)/np.tan(CUTTER_ANGLE) #Depth needed for a 0.000 cutter
    actual_depths = virtual_depth - (np.array(CUTTER_LIST)/2)/np.tan(CUTTER_ANGLE) #Difference of the virtual depth and the diff of the cutter and a 0.000 cutter
    
    #Print the apropriate depth/cutter combos
    print(f"The apropriate cutter/depth combonation(s) for a {path_width}in. wide path: ", sep='', end='')
    valid_combinations = []
    for depth, cutter in zip(actual_depths, CUTTER_LIST): #Find valid combinations
        if depth > 0 and depth<=MAX_CUT_DEPTH:
            valid_combinations += [(cutter, depth),]
    
    for cutter, depth in valid_combinations[:-1]:
        print(f"{cutter:.3f} cutter with a depth of {depth:.3f}in. or a ", end='')
            
    print(f"{valid_combinations[-1][0]:.3f} cutter with a depth of {valid_combinations[-1][1]:.3f}in.")
        

    
    
    
done = False

while not done:
    #Get user option and do spacing
    print("Select operation:\n",
          "\t1. Find the best cutter for a given font height\n",
          "\t2. Find the depth of cut needed for each cutter for a given path width\n",
          "\t3. Quit",
          sep='')
    option_selected = int(input("\tSelection: "))
    print()
    
    #Implement selected option by calling relevent function or exiting
    if option_selected == 1:
        cutter_given_font_height(float(input("Enter font height in inches: ")))
        
    elif option_selected == 2:
        depths_given_path_width(float(input("Enter path width in inches: ")))
        
    else:
        done = True