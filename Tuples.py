#tuples cannot be changed or modified
coordinates=(4,5)
coordinates = [(4,5), (8,22), (80,120)]# this is a tuple inside a list
coordinates[1]=10 #this would give an error sinsce tuples cannot be modified
print(coordinates[1])
print(coordinates)