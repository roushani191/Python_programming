#to find population at the end of each of the last 10 years
curr_pop = 10000

for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop = curr_pop/1.1 