"""
A python program to track friends birthdays
This program teaches what a python dictionary is
"""
#here we define a dictionary called birthDays
"""
but what is a dictionary?
In python a dictionary is a data structure that uses
key-value pairs to store data
a dictionary is declared like this
 myDictionary ={}
here we create an empty dictionary that can store data
"""
# in this dictionary the key is 'ousmane'
# the value is '1995'
birthDays = {
    'ousmane': '1995'
}

# here we simulate an infinite loop
while True:
    #all this code will keep running until we break out of the loop

    print('Find your friend: ')
    # here we define a variable name and store whatever the user enters
    name = input()

    """
    python dictionaries allow us to check if a certain key exists
    we do this using 'for key in dictionary'
    """
    #here we check if the name the user entered is there in
    # the birthDays dictionary
    if name in birthDays:
        #if the name is there
        #we grab the value corresponding to that name
        #we use dictionary[key] to do that
        print(birthDays[name])
    else:
        #this code will only execute if the name is not there
        print('not fund please add')

        #because the name is not there so we dont have the birthday
        # for that name
        # so we allow the user to enter the birthday for that name
        # then we map the name to the birthday like this
        # birthDays[name]=newBirthDay
        print('Enter your birthday:')
        birthday = input()
        birthDays[name] = birthday
        print('We have aded you to database')

