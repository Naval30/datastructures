def binary(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		mid = (first + last)/2
		if alist[mid] == item:
			found = True
		else:
			if alist[mid] > item:
				last = mid - 1
			else:
				first = mid + 1	
			
	return found









list = [0,1,4,7,9,10,12,14,16];
print(binary(list, 13));
print(binary(list, 12));