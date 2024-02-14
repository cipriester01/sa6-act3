list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
intersect = list(filter(lambda x: x in list1, list2))
print(f"Intersection of lists: {intersect}")
