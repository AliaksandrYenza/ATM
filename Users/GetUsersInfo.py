class GetUsersInfo():

    def __init__(self):
        self.FILE_NAME = "D:/alex/projects/ATM/Users/user_dates.txt"

    def read_info_from_file(self):
        with open(self.FILE_NAME, 'r', encoding="utf8") as file:
            text = file.readlines()
        return self.dict_from_list(text)

    def dict_from_list(self, list):
        user_dict = dict()
        for i in range(len(list)):
            list[i] = list[i].lstrip()
            list[i] = list[i].replace('\n', '')
            list[i] = list[i].split(':')
            user_dict[list[i][0]] = list[i][1:3]
        return user_dict

    def write_new_user_info(self, name, password, amount=1000):
        with open(self.FILE_NAME, 'a', encoding="utf8") as file:
            file.write('\n')
            file.write(name + ":" + password + ":" + str(amount))

    def update_user_info(self):
        pass
