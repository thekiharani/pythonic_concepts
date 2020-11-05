import itertools

counter = itertools.count()
data = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
daily_data = list(zip(itertools.count(), data))

print(daily_data)