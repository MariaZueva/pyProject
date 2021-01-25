class NoNumb(Exception):
    def __init__(self, text):
        self.text = text


# определяет число или нет (ничего умнее не придумала)
def is_numb(nu):
    try:
        return float(nu)
    except ValueError:
        return False


num = ''
num_list = []
while True:
    num = input('Введите число, для выхода введите stop: ')
    try:
        if num == 'stop':
            break
        n = is_numb(num)
        if not n:
            raise NoNumb('No number!')
        num_list.append(n)
    except NoNumb as err:
        print(err)
print(num_list)
