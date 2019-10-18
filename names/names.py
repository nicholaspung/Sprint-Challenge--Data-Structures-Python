import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Changing this
# Runtime: 5.519491910934448 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Answer for Sprint (Using BST)
# Runtime: 0.09100198745727539 seconds
# bst = BinarySearchTree(names_1[0])
# duplicates = []
# for name_1 in range(1, len(names_1)):
#     bst.insert(names_1[name_1])
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# Better answer for Spring
# Runtime: 0.0084228515625 seconds
duplicates = []
holder = {}
for name_1 in names_1:
    if name_1 in holder:
        holder[name_1] += 1
    else:
        holder[name_1] = 0

for name_2 in names_2:
    if name_2 in holder:
        holder[name_2] += 1
    else:
        holder[name_2] = 0

for key in holder:
    if holder[key] > 0:
        duplicates.append(key)

# Answer for Stretch
# Used python's built in verifier, runtime: 1.0983390808105469 seconds
# Worse than using BST, but better in terms of memory (doesn't use additional memory except to store results)
# duplicates = []
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Current runtime complexity: O(n^2)
