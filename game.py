import numpy as np
np.random.seed(123)
coin = np.random.randint(0,3)    #randomly generate 1 or 2
print(coin)
if coin == 0 :
    print("Head")
else :
    print("Tail")