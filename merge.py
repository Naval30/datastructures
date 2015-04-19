def merge(items):
	if len(items) > 1:

		mid = len(items)/2
		left = items[:mid]
		right = items[mid:]
		merge(left)
		merge(right)

		l, r = 0, 0

		for i in range(len(items)):

			lval = left[l] if l < len(left) else None
			rval = right[r] if r < len(right) else None

			if (lval < rval and rval and lval) or rval is None:
				items[i] = lval
				l += 1

			elif (lval >= rval and rval and lval) or lval is None:
				items[i] = rval
				r += 1
			else:
				raise Exception("couldn't merge")

	return items			

	

items = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print merge(items)