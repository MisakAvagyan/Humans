lst = []
rng = int(input("Write the number of people - "))
run = True


class Human:
    def __init__(self, n, s, a):
        self.Name = n
        self.Surname = s
        self.Age = a


for i in range(rng):
    name = input('Enter the name - ')
    surname = input('Enter the surname - ')
    age = int(input('Enter the age - '))
    print('\n')
    h = Human(name, surname, age)
    lst.append(h)

while run:
    sort = input('Enter the way of sorting - (Name, Surname or Age)\n')
    if sort == 'Name':
        run = False
    elif sort == 'Surname':
        run = False
    elif sort == 'Age':
        run = False
    else:
        print('No such option, please try again\n')
        run = True


if sort == 'Name':
    sorted_people = sorted(lst, key=lambda x: x.Name)
elif sort == 'Surname':
    sorted_people = sorted(lst, key=lambda x: x.Surname)
elif sort == 'Age':
    sorted_people = sorted(lst, key=lambda x: x.Age)

for person in sorted_people:
    print(f"{person.Name} {person.Surname}, {person.Age}")
