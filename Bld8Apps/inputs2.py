def age_in_secs ():
    user_age = input('enter your age: ')
    age_seconds = int(user_age) * 365 * 24 * 60 * 60
    print('you have lived for {} seconds.'.format(age_seconds))
age_in_secs ()