with open("day_1.txt") as f:

  list_of_cals = []
  cals_per_elf = 0

  for cal in f:
    if len(cal) > 1:  
      food = int(cal)  
      cals_per_elf += food
    else:
      list_of_cals.append(cals_per_elf)  
      cals_per_elf = 0 

  sorted_cals = sorted(list_of_cals)  
  sorted_cals.reverse()

  # Part 1
  print(sorted_cals[0]) 

  # Part 2
  print(sum(sorted_cals[0:3]))

