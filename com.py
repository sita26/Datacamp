#code from Intro to Python Data Science

import numpy as np 
np_roll = np.array([8,6,9,8,4,7,3,5])
np_seat = np.array([88,56,22,53,47,45,33,48])
bmi = np_seat/np_roll ** 2
print(bmi)
print(bmi > 40)
print(bmi[bmi>2])