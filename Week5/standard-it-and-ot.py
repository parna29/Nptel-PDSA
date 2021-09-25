#userdata = input()
#print(userdata)  #difficult to know if it's processing or waiting for input

#userdata = input('Type a number')
#print(userdata)  #better formatting possible

#userdata = input('Type a number: ')
#print(userdata)

#userdata = input('Type a number: \n')
#print(userdata)

#userdata = input('Enter a number')
#usernum = int(userdata) #type conversion

#try except block to deal with ValueError
while(True):
    try:
        userdata = input('Enter a number : ')
        usernum = int(userdata)

    except ValueError:
        print('Not a number. Try again')

    else:
        break  #helps in coming out of infinite loop
