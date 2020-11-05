nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i_nums = nums.__iter__()

while True:
	try:
		print(next(i_nums))
	except StopIteration:
		print('End')
		break