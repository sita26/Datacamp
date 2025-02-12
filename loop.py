#while loop

# error = 40.0
# while error > 6:
#     error = error/4
#     print(error)


#for loop

fam = [23.4, 43.23, 12.32, 75.32, 22.43, 24.32]
# for height in fam :
#     print(height)
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))