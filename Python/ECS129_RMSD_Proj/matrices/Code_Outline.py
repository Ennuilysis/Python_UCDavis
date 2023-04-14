import sys
from typing import List,Union,Tuple,Dict

print("Welcome to RMSD")
#import core-wrapper library

#read file position inputs, argv(1) and argv(2)
model_file = sys.argv[1]
target_file = sys.argv[2]
#Read target_file as target
#Read model_file as model

#Search for CA atom in target file, save line position
#Search for CA atom in model file, save line position
#Looking for the annotation, "atom"
#print line target to be sure
#print line model to be sure

#while loop for each line in target file
#while loop for each line in model file

#use python bio library to find lambda max of target
#use python bio library to find lambda max of model

#use python bio to find barycenters of both

#run data through formula from paper. output should be a float type
#save output in array
#sum array to get total difference.