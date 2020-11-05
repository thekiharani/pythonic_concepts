# Code like a Geek ~ Joe Gitonga Waire
class GeekyRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if(self.value >= self.end):
			raise StopIteration
		current = self.value
		self.value += 1
		return current

def geeky_range(start, end):
	current = start
	while current < end:
		yield current
		current += 1

nums = geeky_range(start=1, end=100000)

while True:
	try:
		print(next(nums))
	except StopIteration:
		print('End')
		break