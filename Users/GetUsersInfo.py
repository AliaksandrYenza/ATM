import re


class GetUsersInfo():

    def __init__(self):
        self.FILE_NAME = "D:/alex/projects/ATM/Users/user_dates.txt"
        self.text = self.get_text_from_file()

    def get_text_from_file(self):
        with open(self.FILE_NAME, 'r', encoding="utf8") as file:
            text = file.readlines()
        for i in range(len(text)):
            text[i] = text[i].lstrip()
            text[i] = text[i].replace('\n', '')
            text[i] = text[i].split(':')
        return text

    def do_dict_from_list(self):
        user_dict = dict()
        for i in range(len(self.text)):
            user_dict[self.text[i][0]] = self.text[i][1:3]
        return user_dict

    def search_by_name(self, name):
        self.text = self.get_text_from_file()
        dict_names = self.do_dict_from_list()
        return dict_names[name]

    def add_to_file_new_user(self, name, password, amount=0):
        with open(self.FILE_NAME, 'a', encoding="utf8") as file:
            file.write('\n')
            file.write(name + ":" + password + ":" + str(amount))

    def save_to_file(self, name, new_amount):
        dict_users = self.do_dict_from_list()
        with open(self.FILE_NAME, 'w', encoding="utf8") as file:
            for k in dict_users.keys():
                if name == k:
                    amount = int(dict_users[name][1])
                    amount += int(new_amount)
                    dict_users[name][1] = str(amount)
                file.write(str(k) + ":" + str(dict_users[k][0]) + ":" + str(dict_users[k][1]) + '\n')
        print(name + ":" + dict_users[name][1])


# gg:ggg:10000
# alex:ale:20000
# admin:1111:9999999