from Users.BaseUser import BaseUser
from Users.GetUsersInfo import GetUsersInfo


def start_window(base_user):
    return base_user.registration_window()


if __name__ == '__main__':
    get_user_info = GetUsersInfo()
    users_dict = get_user_info.read_info_from_file()
    base_user = BaseUser(users_dict)
    status = start_window(base_user)
    while True:
        if status == False:
            base_user.create_account(users_dict)
        base_user.login_user()
        while True:
            print('Check balance - 1\nRecharge - 2\nWithdrawn $ - 3\nExit - 4\n')
            command = input('Choose command:')
            # input correct num of command
            # choose rel-ve function untill 4

            break
        break
    print('SUCCESS')


