# Problem Statement:
#You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

#Task 1: Given the two lists:

#submitted = ["Alice", "Bob", "Charlie", "David"]
#attended = ["Charlie", "Eve", "Alice", "Frank"]
#Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
attended = set(attended)
submitted = set(submitted)
common = attended.intersection(submitted)
print(common)

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted = set(submitted)
attended = set(attended)
if submitted == attended:
    print("The two lists are identical.")
else:
    print("The two lists are not identical.")

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted = set(submitted)
attended = set(attended)
attended = attended.intersection(submitted)
print(attended)

