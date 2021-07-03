# to activate the virtual environment
exec(open("venv/bin/activate_this.py").read(), {'__file__': "venv/bin/activate_this.py"})

from src.findByPin import findByPin
from src.findByName import findByName
from src.getDistricts import getDist
from src.getStates import getStates
from time import sleep
from datetime import datetime

if __name__ == '__main__':
    print('\n\nCoWin_Terminal')
    print('------------------------\n\n')

    stateORpin = int(input('Find slots by:\n1. Pincode\n2. State\n(enter 1 or 2)\n'))
    if stateORpin == 1:
        # ask pincode
        pincode = int(input('Enter your pincode: '))

        # age filter menu
        age = int(input('Search for which ages ?\n1. under 18 (12 - 18)\n2. 18 - 45\n3. no age filter\n'))
        min_age = -1
        max_age = 114

        if (age == 1):
            min_age = 12
            max_age = 18
        elif (age == 2):
            min_age = 18
            max_age = 45
        elif (age == 3):
            min_age = -1
            max_age = 114
        else:
            print('           Invalid !') 
            print('*** Default options selected ***')

        # vaccine filter
        vaccine = int(input('Which vaccine to search ?\n1. Covishield\n2. Covaxin\n3. Both\n'))
        url_params = ''

        if (vaccine == 1):
            url_params = 'COVISHIELD'
        elif (vaccine == 2):
            url_params = 'COVAXIN'
        elif (vaccine == 3):
            url_params = ''

        # finding slots by pin
        print('Checking...')
        while (True):
            print("\033c") # clears the entire screen so that we can rewrite on the terminal without having to scroll too much
            print("Date: ", datetime.today().strftime("%d / %m / %Y"), "\n") # print an extra blank line for formatting
            while(findByPin(pincode, min_age, max_age, url_params) != True):
                sleep(5)
                findByPin(pincode, min_age, max_age, url_params)

            # refresh the data ?
            choice = str(input('Press Y to refresh and n to stop: '))
            if (choice == 'n' or choice == 'N'):
                break

    elif stateORpin == 2:
        # location menu
        print('Select State:')
        getStates()
        stateID = int(input('Enter the state ID from the above list: '))

        print("\033c") # clears the entire screen so that we can rewrite on the terminal without user having to scroll too much        
        
        print('Select district:')
        getDist(stateID)
        distID = int(input('Enter the district ID from the above list: '))

        # age filter menu
        print("\033c") # clears the entire screen so that we can rewrite on the terminal without user having to scroll too much
        age = int(input('Search for which ages ?\n1. under 18 (12 - 18)\n2. 18 - 45\n3. no age filter\n'))
        min_age = -1
        max_age = 114

        if (age == 1):
            min_age = 12
            max_age = 18
        elif (age == 2):
            min_age = 18
            max_age = 45
        elif (age == 3):
            min_age = -1
            max_age = 114
        else:
            print('           Invalid !') 
            print('*** Default options selected ***')

        # vaccine filter
        vaccine = int(input('Which vaccine to search ?\n1. Covishield\n2. Covaxin\n3. Both\n'))
        url_params = ''

        if (vaccine == 1):
            url_params = 'COVISHIELD'
        elif (vaccine == 2):
            url_params = 'COVAXIN'
        elif (vaccine == 3):
            url_params = ''

        # finding...
        print('Checking...')
        while (True):
            print("\033c") # clears the entire screen so that we can rewrite on the terminal without having to scroll too much
            print("Date: ", datetime.today().strftime("%d / %m / %Y"), "\n") # print an extra blank line for formatting
            while(findByName(distID, min_age, max_age, url_params) != True):
                sleep(5)
                findByName(distID, min_age, max_age, url_params)

            # refresh the data ?
            choice = str(input('Press Y to refresh and n to stop: '))
            if (choice == 'n' or choice == 'N'):
                break
    else:
        print('           Invalid !')
