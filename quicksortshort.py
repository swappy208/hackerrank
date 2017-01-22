def quicksort(unsorted_list):
	if len(unsorted_list)<2:
		return unsorted_list
	else:
		pivot = unsorted_list.pop()
		l_list=[]
		r_list=[]
		for number in unsorted_list:
			if number>pivot:
				r_list.append(number)
			else:
				l_list.append(number)
		return quicksort(l_list)+[pivot]+quicksort(r_list)

list=[6,2,3,1,8,9,5,4,8]
print (quicksort(list).reverse())
