
def save_elements_r(n):

	res = []
	for i in range(n):
		res.append(i)
	return res


def save_elements_y(n):

	for i in range(n):
		yield i


if __name__ == '__main__':

	# makes a list in memory which is expensive
	res1 = save_elements_r(1000)
	print(res1)

	# returns a generator, which has a reference to the 
	# the first element, and then you can see all the elements 
	# one by one with loading them in memory.
	res2 = save_elements_y(1000)
	for elem in res2:
		print(elem)