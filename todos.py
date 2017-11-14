
"""
A python program that tracks your todos
This program teaches lists in python
List as a data structure is a value that is used to store sequence of
data
a list is declrared like this []
we can assign it to a variable too like this
myList = []
What is special about a list is that it stores items at indexes
so for example if we have a list
myNames = ['cool','kull']
here if we do print(myNames[0]) --> cool
this tells us the list starts at 0 and ends at length of list minus 1
Hope we remember how to find the length of the list in python?
len(myNames) --> returns the number of items in the list
List also has methods that we can use to add ,remove and sort the items
The one used in our program is append which adds an item to the end
of the list
"""

#here we create an empty todos list
#remember this is a global variable
#it can be accessed anywhere in our code
todos = []
print("Am your todos manager")

#here we simulate an infinite loop
while True:
    print("Enter what you plan to do:")

    #we get whatever the user types
    todo = input()

    #we add whatever the user types to our list
    todos.append(todo)

    #we check if the user used the ENTER key
    #the value of the enter key is ''
    if todo == '':
        #because they didnt enter anything we break
        #break from what?
        #we break from the infinite loop we just made using while True
        #note that this doesnt mean we break out of the whole program
        break
    print("Todo added: Please do it")

#after the 'break' our program contiues here
print("Good: Here are your todos")

# here we use the old good for i in range
# except this time we are walking through each item in our list
for todo in todos:
    #we check if the current item is 'code'
    #we dont like to code so we skip it :)
    if todo =='code':
        continue
    else:
        print(' '+todo)
