 #understanding dictionaries
students = {}
while True:
    print("------Student Score Manager----------")
    print('1. Add/update student')
    print('2. View all students')
    print('3. Delete a student')
    print('4. Search for a student')
    print('5. exit')
    choice= input('Enter your choice: ')
    if choice == "1":
        name= input('ENter the student name: ')
        score= int(input(f'enter {name} score: '))
        students[name]= score
        print(f'{name} added successfully.')
    elif choice == "2":
        if not students:
            print('no students has been added into the list')
        else:
            print('LIST OF STUDENTS')
            for name, score in students.items():
                print(f'{name}:{score}')
    elif choice =="3":
        name= input('ENter the student name to delete:')
        if name in students:
            del students[name]
            print(f'{name} deleted suscessfully!')
        else:
            print('invalid name!')
    elif choice == "4":
        name=input('enter the student name to be searched: ')
        print(f'{name} score: {students.get(name,'not found')}')
    elif choice == "5":
        print('goodbye'.upper())
        break
    else:
        print('invalid choice!')
        
                