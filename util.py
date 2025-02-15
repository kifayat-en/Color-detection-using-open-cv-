# import cv2 
# import numpy as np

# def get_limits(color):
#     c = np.uint([[color]])
#     hsvC =   cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
#     lower_limit = hsvC[0] [0] [0] - 10, 100, 100
#     upper_limit = hsvC[0] [0] [0] - 10, 255, 255
    
#     lower_l =  np.array(lower_limit, dtype=np.int8)
#     upper_l =  np.array(upper_limit, dtype=np.int8)
    
#     return lower_limit, upper_limit

import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]])  # Ensure color is in uint8 format
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # Convert BGR to HSV

    # Define the lower and upper HSV limits
    lower_limit = (hsvC[0][0][0] - 10, 100, 100)
    upper_limit = (hsvC[0][0][0] + 10, 255, 255)

    # Convert to numpy arrays with uint8 dtype
    lower_l = np.array(lower_limit, dtype=np.uint8)
    upper_l = np.array(upper_limit, dtype=np.uint8)

    return lower_l, upper_l

    
    
    
    