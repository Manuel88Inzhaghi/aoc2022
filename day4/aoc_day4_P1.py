file = open('day_4.txt').readlines()
overlaps = {'value': 0}

def compare(pair):
  elf1, elf2 = pair
  sect1 = elf1.split('-')
  sect2 = elf2.split('-')
  n1, n2 = sect1
  n3, n4 = sect2
  id1 = int(n1)
  id2 = int(n2)
  id3 = int(n3)
  id4 = int(n4)
  if id1 >= id3 and id2 <= id4:
    overlaps['value'] += 1
  elif id3 >= id1 and id4 <= id2:
    overlaps['value'] += 1
 
for item in file:
  pair = item.strip().split(',')
  compare(pair)

print(overlaps)
		