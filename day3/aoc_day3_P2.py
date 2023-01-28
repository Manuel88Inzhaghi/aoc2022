p = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
tot_p = 0
rucksacks = []

# Divides data into groups of 3 rucksacks
data = open("day_3.txt").readlines()
x = 0
while x <= len(data)-3:
	group = [data[x].strip(), data[x + 1].strip(), data[x + 2].strip()]
	rucksacks.append(group)
	x += 3
	
# finds common item in all 3 rucksacks of group by looping 
# throuh the first line
for items in rucksacks:
    line1, line2, line3 = items
    x = 0
    while x < len(line1):
        if line1[x] in line2 and line1[x] in line3:
            tot_p += p.index(line1[x])
            break
        x += 1

print(tot_p)


		