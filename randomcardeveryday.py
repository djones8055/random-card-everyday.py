import random

allcardslist = ['ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c',
	'jc', 'qc', 'kc', 'ad', '2d','3d', '4d', '5d', '6d', '7d', '8d', '9d',
	'10d', 'jd', 'qd', 'kd', 'ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h',
	'9h', '10h', 'jh', 'qh', 'kh', 'as', '2s', '3s', '4s', '5s', '6s', '7s',
	'8s', '9s', '10s', 'js', 'qs', 'ks' ]

foundcardslist = []
day = 0

while len(foundcardslist) < 52:
	day = day + 1
	todayscard = random.choice(allcardslist)
	
	print("Day: ", day)
	print("Todays card is: ", todayscard, '\n')
	
	if todayscard not in foundcardslist:
		foundcardslist.append(todayscard)
	
print("===========================================================")
print("Found all", len(foundcardslist), "cards in", day, "days.")
print("===========================================================")
