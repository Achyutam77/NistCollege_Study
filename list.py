#list
fruits=["banana", "apple", "orange"]
print(fruits[0])  # banana
print(fruits[1])  # apple    
print(fruits[2])  # orange
print(fruits[-1])  # orange
print(fruits[-2])  # apple
#from negative value comes from last element

#slicing
print(fruits[0:2])  # ['banana', 'apple']

#to print reverse order
print(fruits[::-1])  # ['orange', 'apple', 'banana']

#loop in list
for fruit in fruits:
    print(fruit)

#add an item to the list
fruits.append("grape")
print(fruits)  # ['banana', 'apple', 'orange', 'grape']

#remove an item from the list
fruits.remove("banana")

#change an item in the list
fruits[0] = "kiwi"  
print(fruits)  # ['kiwi', 'apple', 'orange', 'grape']

#tuples
#tuples can not change elements after defining it once
colors = ("red", "green", "blue")
print(colors[0])  # red

#set
#in set we con't have duplicate values
#there is no order in set so we can not access elements by index i.e set[0]
my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)  # {1, 2, 3, 4, 5}

#union of two sets
set1 = {1, 2, 3}    
set2 = {3, 4, 5}
set_union = set1.union(set2)
print(set_union)  # {1, 2, 3, 4, 5}
#intersection of two sets
set_intersection = set1.intersection(set2)  
print(set_intersection)  # {3}
print(set1 & set2)  # {3}

#dictionary
my_dict = {
    "name": "Alice",
    "age": 22,
    "city": "New York",
    "subjects": ["Math", "Science", "English"]
}

print(my_dict["name"])  # Alice
print(my_dict["age"])  # 22 
print(my_dict["city"])  # New York
print(my_dict["subjects"])  # ['Math', 'Science', 'English']

#changing a value in dictionary
my_dict["name"] = "Achyutam"
print(my_dict["name"])  # Achyutam

#to make string capital and lower case
print(my_dict["name"].upper())  # ACHYUTAM 
print(my_dict["name"].lower())  # achyutam

#including all
student1 = {
    "name": "Alice",
    "marks": [75, 85, 90],
    "hobbies": ("reading", "swimming", "coding"),
    "skills": {"Python": "Advanced", "Java": "Intermediate"},
}
student2 = {
    "name": "Bob",
    "marks": [80, 70, 95],
    "hobbies": ("gaming", "painting"),
    "skills": {"Python": "Intermediate", "Java": "Advanced"},
}
my_list= [student1,student2]
print(my_list) 