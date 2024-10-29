#python
#creating a list
my_list = [1,2,3,4,5,6]
#append(): adds an element to the end of the list
my_list.append(7)
print("append:",my_list)

#remove(); removes the first occurence a specified value
my_list.remove(2)
print("remove:",my_list)

#pop(); removes and returns the last item on the list
popped_item = my_list.pop()
print("popped item",my_list.pop())
print("popped:",my_list)

#exdend(); extends a list with a given list
my_list.extend([2,8,9,10])
print("after extend:",my_list)

#sort(); sorts the in ascending order
my_list.sort()
print("after sort",my_list)


#reverse(); reverses the order of the list
my_list.reverse()
print("after reverse",my_list)




#creating a set

set_a = {1,2,3,4,5,6}
set_b = {6,1,12,13,14}
#add(); adds an element to the set
set_a.add(6)
print("after adding 6 to set_a",set_a)
#remove(); removes a specified element from the set
set_b.remove(14)
print("after removing 14 from set_b",set_b)

#union();returns a set that contains all elements from both sets
union_set = set_a.union(set_b)
print("union of set_a and set_b",union_set)

#intersection(); returns a set contains elements common to both sets
intersection_set = set_a.intersection(set_b)
print("intersection of set_a and set_b",intersection_set)


#difference(); returns a set that contains elementsin set_a but not in set_b
difference_set = set_a.difference(set_b)
print("difference of set_a and set_b:", difference_set)