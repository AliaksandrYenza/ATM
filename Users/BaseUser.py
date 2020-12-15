from Users.GetUsersInfo import GetUsersInfo


class BaseUser:

    def __init__(self, users_dict):
        self.users_dict = users_dict

    def registration_window(self):
        print('Do u have account already?')
        have_account = input('Y/n:\n')
        while have_account not in ('Y', 'n'):
            have_account = input('Choose "Y" for yes, "n" for no:\n')
        print(f'have_acc = {have_account}')
        return True if have_account == 'Y' else False

    def login_user(self):
        user_info = GetUsersInfo()
        user_dict = user_info.read_info_from_file()
        print('Write account name, then password')
        name = input('Account name:')
        password = input(f"Password for {name}:")
        while True:
            while (name not in user_dict.keys()) or (password not in user_dict[name]):
                name = input('Name or/and password are incorrect, lets try again!\nAccount name:')
                password = input(f"Password for {name}:")
            break
        return name

    def create_account(self, user_dict):
        get_user = GetUsersInfo()
        print('Lets try to create new account')
        name1 = input('Write account name:\n')
        while name1 in user_dict.keys():
            name1 = input('This name already is.\nWrite new account name')
            name2 = input('Confirm name:\n')
            while (name1 != name2):
                print('Accounts name are not same\n')
                name1 = input('Write account name:\n')
                name2 = input('Confirm name:\n')
        password1 = input(f'Write {name1} password:\n')
        password2 = input('Confirm password:\n')
        while password1 != password2:
            print(f'Accounts password {name1} are not same\n')
            password1 = input(f'Write {name1} password:\n')
            password2 = input('Confirm password:\n')
        get_user.write_new_user_info(name1, password1)
        print(f' OK. User {name1} is created!')


