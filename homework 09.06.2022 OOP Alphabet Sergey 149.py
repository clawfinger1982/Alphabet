# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из
# входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
class Alphabet:
    def __init__(self, lang='Ru', letters='йцукенгшщзхъфывапролджэячсмитьбюё'):
        self.lang=lang
        self.letters=letters
    def prnt(self): # который выведет в консоль буквы алфавита
        print('Алфавит: ', self.letters)
    def letters_num(self): # который вернет количество букв в алфавите
        print('Кол-во букв в русском алфавите: ', len(self.letters))

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский
# метод __init__(). В качестве параметров ему будут передаваться обозначение языка
# (например, 'En') и строка, состоящая из всех букв алфавита(можно воспользоваться
# свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить
# количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра
# и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе он будет
# возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на
# английском языке.
import string
class EngAlphabet(Alphabet):
    def __init__(self, lang='En', letters_num='qwertyuiopasdfghjklzxcvbnm'):
        __letters_num=len(letters_num)
        self.lang=lang
    def is_en_letter(self, letter=input('input letter: ')):
        letters_num = 'qwertyuiopasdfghjklzxcvbnm'
        if letter in letters_num:
            print('Yes, this is English letter inputed')
        else:
            print('No, this is not English letter inputed')
    def letters_num(self, letters_num = 'qwertyuiopasdfghjklzxcvbnm'):
        self.__letters_num=letters_num
        print('English Alphabet: ',self.__letters_num)
    @staticmethod
    def example(): # возвращает пример текста на английском языке
        print("I'm learning Python")

alphabet=Alphabet()
engalphabet=EngAlphabet()
alphabet.prnt()
alphabet.letters_num()
engalphabet.is_en_letter()
engalphabet.letters_num()
engalphabet.example()
