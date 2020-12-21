from Users.BaseUser import BaseUser
from Users.GetUsersInfo import GetUsersInfo


class RegUser(BaseUser):

    def __init__(self):
        self.reg_user = GetUsersInfo()

    def command_manager(self, command, user_name):
        if command == '1':
            print(f"Balance's {user_name} is : {self.check_balance(user_name)}")
        elif command == '2':
            print(f"Take ur cash {self.withdrawn(user_name)} ")
        elif command == '3':
            self.top_up(user_name)
        else:
            print('ERROR IN command_manager')

    def choose_commander(self, name):
        while True:
            print('\n\n\n1 - check balance\n2 - withdrawn money\n3 - top up money\n4 - Exit')
            num_command = input('Ur operation is : ')
            if num_command not in ('1', '2', '3', '4'):
                print('Wrong command, try again')
            elif num_command == '4':
                break
            else:
                self.command_manager(num_command, name)

    def check_balance(self, user_name):
        return (self.reg_user.search_by_name(user_name)[1])

    def top_up(self, user_name):
        while True:
            try:
                count = int(input('How much do u wanna amount up:'))
            except:
                raise
            else:
                break
        self.reg_user.save_to_file(user_name, count)

    def withdrawn(self, user_name):
        while True:
            count = int(input('How much do u wanna withdrawn:'))
            user_info = self.reg_user.search_by_name(user_name)
            if int(user_info[1]) < count:
                print(f'U dont have enough money, but u can take credit : {int(user_info[1]) - count}')
                answer = input('Y for take credit, n = dont take credit')
                while True:
                    if answer == 'Y':
                        self.reg_user.save_to_file(user_name, -count)
                        break
                    elif answer == 'n':
                        continue
                    else:
                        print('WAT ???')
            else:
                self.reg_user.save_to_file(user_name, -count)
                break
            return count


