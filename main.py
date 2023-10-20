########################################################_Task_#########################################################
# Variant_1
# Завдання_1. Створити 'class User' з властивостями:
# - id
# - name
# - user_name
# - password
# Завдання_2. Створити метод для зміни паролю

#####################################################_Variant_1_#######################################################

#Вирішення завдання

class User():
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password
    def change_pass(self, new_pass):
        if self.password == old_pass:
            self.password = new_pass
            return True
        else:
            return False

user = User(1, 'Denys', 'denisko010011001110', '111222')

old_pass = input('Щоб змінити пароль, введіть свій теперіщній пароль: ')
if user.change_pass(old_pass):
    print('Поточний пароль:', user.password)

# Змінюю пароль
    new_pass = input('Придумайте новий пароль: ')
    user.change_pass(new_pass)
    print('Вітаємо, ваш пароль успішно оновлено!')

# Виводжу оновлений пароль
    print('Оновлений пароль:', user.password)
else:
    print('Введений вами пароль неправильний!')
