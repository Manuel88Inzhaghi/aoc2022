tot_score = 0
with open("day_2.txt") as f:
	for a in f:

		if a[0] == 'A' and a[2] == 'X':
			score = 3
			tot_score += score

		elif a[0] == 'A' and a[2] == 'Y':
			 score = 4
			 tot_score += score

		elif a[0] == 'A' and a[2] == 'Z':
			 score = 8
			 tot_score += score

		elif a[0] == 'B' and a[2] == 'X':
			 score = 1
			 tot_score += score

		elif a[0] == 'B' and a[2] == 'Y':
			 score = 5
			 tot_score += score

		elif a[0] == 'B' and a[2] == 'Z':
			 score = 9
			 tot_score += score

		elif a[0] == 'C' and a[2] == 'X':
			 score = 2
			 tot_score += score
		elif a[0] == 'C' and a[2] == 'Y':
			 score = 6
			 tot_score += score

		elif a[0] == 'C' and a[2] == 'Z':
			 score = 7
			 tot_score += score

	print(tot_score)
		
		



