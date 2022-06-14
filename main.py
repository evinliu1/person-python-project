class Person:  # class of people
    amount_of_people = 0
    people = []

    def __init__(self, name_, age_, sex_):  # constructor for a "Person class"
        self.name = name_
        self.age = age_
        self.sex = sex_
        Person.add_person()  # calling method for increasing "amount_of_people"

    @classmethod
    def number_of_people(cls):  # class method for returning the amount of people added to system
        return cls.amount_of_people

    @classmethod
    def add_person(cls):  # method for increasing the count of people by 1
        cls.amount_of_people += 1

    @classmethod
    def to_list(cls, person):  # adds each person to the list data structure
        cls.people.append(person)

    @classmethod
    def print_list(cls, people):  # prints the people in system in order (numbered chronologically)
        counter = 0  # counter for numbering the people printed off the list
        print("The people added to the system are :")
        for x in Person.people:  # for loop that goes through list of "Persons"
            counter += 1
            print(str(counter) + ". " + x.name + "\n")


def printlist(list_):
    counter = 0
    for x in list_:
        counter += 1
        print(str(counter) + ". " + x.name + "\n")


def s_name(name_, list_):
    key = list_.name_
    temp = []
    for x in list_:
        if list_.name == key:
            temp.append(x)
    printlist(list_)


def s_age(age_, list_):
    pass


def s_sex(sex, list_):
    pass


condition = True  # controls whether you go back to the nested while loop
condition2 = True  # controls whether you go back to the first while
while condition2:
    while condition:  # asks for input, if not recognizable try again
        name = input("Name: \n").upper()
        if isinstance(name, str):
            condition = False  # if "condition = false" that means "keep going"
        else:
            print("That doesn't seem right.. Try again\n")
    condition = True  # resets condition for re-use in the next while loop
    while condition:
        age = ""  # re-initializes "age" variable to a string in case of user input error after looping at least once
        age = input("Age: \n")
        if age.isnumeric():  # checks if user input only has numerical characters
            condition = False
            age = int(age)  # converts string value in "age" to an integer
        else:
            print("Hmm... I don't think I believe you.. Try again")
    condition = True
    while condition:
        sex = input("Sex (Male/Female): \n").upper()  # converts user input to uppercase for obvious reasons
        if isinstance(sex, str) and (sex == "MALE" or sex == "FEMALE"):  # checks for user input error
            condition = False
        else:
            print("Hmm.. I don't remember that being a sex.. Try again")
    condition = True
    while condition:  # gives user option to continue and add another "Person"
        cont = input("Would you like to enter the data for another person? (yes/no)\n").upper()
        if cont == "YES":
            break
        elif cont == "NO":
            condition2 = False  # condition2 = False means "no more people to add"
            break
        else:
            print("Um.. That doesn't seem right.. Try again")
            condition = False
    Person.to_list(Person(name, age, sex))  # this is within larger while loop (adds person to list data struct.)

print("\nTotal People : [" + str(Person.number_of_people()) + "]")  # prints the total amount of people
Person.print_list(Person.people)  # prints the list of people added to system
