def sequentialSearch(myList, item):
    pos = 0
    found = False

    while pos < len(myList) and not found:
        if myList[pos] == item:
            found = True
        else:
            pos += 1

    return found


def orderedSequentialSearch(myList, item):
	pos = 0
	found = False
	stop = False

	while pos < len(myList) and not found and not stop:
		if myList[pos] == item:
			found = True
		else:
			if myList[pos] > item:
				stop = True
			else:
				pos += 1

	return found


testlist = [1, 3, 325, 46, 34, 53, 23, 533, 64, 334]
testlist2 = [0, 2, 4, 5, 6, 9, 12, 15, 17, 20]

def main():
	print(sequentialSearch(testlist, 3))
	print(sequentialSearch(testlist, 79))
	print(orderedSequentialSearch(testlist2, 13))
	print(orderedSequentialSearch(testlist2, 15))


main()