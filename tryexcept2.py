print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats alot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')
