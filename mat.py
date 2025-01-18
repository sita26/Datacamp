# import matplotlib.pyplot as plt
# year = [1950, 1980,2004,2006,2050]
# pop = [2.36,3.56,5.22,5.22,4.23]
# print(plt.plot(year, pop))
# print(plt.show())



#scatter plot

# import matplotlib.pyplot as plt
# year = [1950, 1980,2004,2006,2050]
# pop = [2.36,3.56,5.22,5.22,4.23]
# print(plt.scatter(year, pop))
# print(plt.show())



#Histogram

# import matplotlib.pyplot as plt
# values = [0,0.1,1.2,1.5,2.3,2.6,3.6,3.45,4.21,4.56,5.68,5.8]
# print(plt.hist(values, bins = 4))
# print(plt.show())



#Customization

import matplotlib.pyplot as plt

year = [2076,2077,2078,2079,2080,2081,2082]
bth = [15.56,16.255,17.459,18.156,19.215,20.852,21.326]
print(plt.plot(year,bth))
print(plt.xlabel('year'))
print(plt.ylabel('birthday'))
print(plt.title('Birthday Record'))
print(plt.yticks([15,20,25],['15B','20B','25B']))
print(plt.show())