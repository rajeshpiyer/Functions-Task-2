original_list = ['Python', 3, 2, 4, 5, 'version']

max_value = max(filter(lambda x: isinstance(x, int), original_list))

print("Original list:", original_list)
print("Maximum value in the list using lambda:", max_value)