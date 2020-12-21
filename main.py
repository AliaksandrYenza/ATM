from Users.BaseUser import BaseUser
from Users.GetUsersInfo import GetUsersInfo
from Users.RegUser import RegUser


def start_window():
    base_user = BaseUser()
    while True:
        if base_user.registration_window():
            try:
                name = base_user.login_user()
                reg_user = RegUser()
                return name, reg_user
            except:
                print('Err : start_window : login_user')
                raise
        else:
            try:
                # it is not necessary, already in *create_account*
                # you can return the name and use it
                base_user.create_account()
                name = base_user.login_user()
                reg_user = RegUser()
                return name, reg_user
            except:
                print('Err : start_window : create_account')
                raise


if __name__ == '__main__':
    user_name, reg_user = start_window()
    print(f"user_name = {user_name}")
    print(f"reg_user = {reg_user}")
    if (reg_user) != None:
        reg_user.choose_commander(user_name)




