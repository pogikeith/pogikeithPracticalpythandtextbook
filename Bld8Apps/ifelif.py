price = 35
if price < 100:
    print('buy chair')
else: 
    print('dont buy')


price = 100
if price < 100:
    print('buy chair')
elif price == 100: 
    print('you can buy if you want to...')
else: print('dont buy')


def age_program():
    seconds_or_years = input('give me seconds (s) or years (y)?')
    if seconds_or_years == 's':
        #convert 
        user_value = input('enter the number of seconds you have lived for')
        print('you have lived for {} years'.format(int(user_value) / 60 / 60 /24 / 365))
    elif seconds_or_years == 'y': 
        user_value = input('enter the number of years you have lived for: ')
        print('you have lived for {} seconds'.format(int(user_value) * 365 * 24 * 60 * 60))

age_program() 