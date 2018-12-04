""" þessi kóði á að virka til að hreinsa skjáinn á bæði mac/win. hægt að setja hann sem aðferð í UI fall og kalla svo alltaf í áður en eitthvað er prentað """

# import only system from os 
from os import system, name 
  
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
 
clear() 
