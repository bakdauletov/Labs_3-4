#1
#создал переменную с названием number
number = int(input("Enter your number: "))
number1 = 2
#Пока цифра 2 не дойдет до цифры которую ввел пользователь. 
while number1 <= number:
    #выводится number1 который равен 2 и number1 += 2 будет добавлять +2, пока не дойдет до ввода пользователя
    print(number1, end=' ')
    number1 += 2

#2
N = int(input("Enter your number: "))
factorial = 1
number = 1
#пока 1 не дойдет до ввода пользователя
while number <= N:
    #будет выполнятся умножения пока number <= N
    factorial *= number
    number += 1
print(factorial)

#3
while True:
    number = int(input("Enter your number: "))
    #если ввод будет равен к 42 то выполнится print и break, который останавливает ввод терминала
    if number == 42:
        print("Wrong number!")
        break

#4
word = input("Enter your string: ")
#здесь используется функция count, которая посчитает сколько букв внутри word. Букву которую нужно посчитать пишем внутри(). Приравниваем к a_word и пишем внутри print
a_word = word.count('a')
print(a_word) 

#5
number = (input("Enter your number: "))
sum = 0
# чтобы посмотреть каждый символ в number
for char in number:
    #если ввод является цифрой:
    if char.isdigit():
        #изменяет на целое цисло
        digit = int(char)
        #Затем значение добавляется к текущей сумме, то есть к sum.
        sum += digit
print(sum)

#6
N = int(input("Enter a positive integer (N): "))
# это подстраховка от ввода - чисел
if N <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    count = 0
    #создается цикл который будет продолжатся до тех пор пока count не дойдет до N
    while count < N:
        print(a, end=' ')
        #Значения переменных a и b обновляются, чтобы получить следующее число Фибоначчи. Теперь a = b, b= a + b. Это формула по которой можно определить следущее число Фибоначчи
        a, b = b, a + b
        count += 1
    print()

#7
word = input("Enter: ")
#создается переменная index которая равна длине word. Индексация символов в строке начинается с 0, поэтому мы вычитаем 1 чтобы начать с последнего символа.
index = len(word) - 1
for char in word:
    #сначала выводится последний символ ввода
    print(word[index], end='')
    #-1 чтобы перейти к следущему символу. (С правой стороны к левой)
    index -= 1

#8
sum = 0
while True:
    number = input("Enter a number: ")
    #если пишется q, терминал закроется
    if number == 'q':
        break  
    number = int(number)  
    #если число четное, то запускается continue. И цифра пропускается.  
    if number % 2 == 0:
        continue  
    sum += number  
print(sum)

#9
#импортирует модуль random, который позволяет генерировать случайные числа.
import random
number = random.randint(1, 100)
while True:
    quess = int(input("Take a guess: "))
    # если случайное число больше ввода, то пишется "Too small"
    if number > quess:
        print("Too small")
    # если случайное число меньше ввода, то пишется "Too high"
    elif quess > number:
        print("Too high")
    # если же случайное число равно вводу, то пишется "Correct number"
    else:
        print("Correct number!")
        break

#10
word = input("Enter: ")
left_side = 0
right_side = len(word) - 1
check = False
count = 0
for char in word:
    #Эти две переменные используются для отслеживания символов слева и справа в слове или фразе.
    if word[left_side] == word[right_side]:
        left_side += 1
        right_side -= 1
        #если они равны, будет True
        check = True
    else: 
        #если нет, то False
        check = False
        break
#если True выводится print("it is palindrom")
if check == True:
    print("it is palindrom")
#если нет выводится print("not a palindrom")
else:
    print("not a palindrom")


#11
x = int(input("Enter your X: "))
y = int(input("Enter your Y: "))
count = 1
# Эта переменная будет использоваться для хранения промежуточных результатов.
n = x
# Запускается цикл while, который будет выполняться, пока значение count меньше значения y
while count < y:
    # в каждом цикле текущее значение n умножается на x, и результат сохраняется обратно в n. После этого значение count увеличивается на 1
    n = x * n
    count += 1
print(n)

#12
N = int(input("Enter your number: "))
num = 2
#Запускается цикл while, который будет выполняться, пока значение num меньше или равно значения N.
while num <= N:
    is_prime = True
    #Этот цикл for перебирает числа от 2 до num 
    for divisor in range(2, num):
        #если делится без остатка, то значение is_prime будет False
        if num % divisor == 0:
            is_prime = False 
            break 
    #если же is_prime будет True
    if is_prime:
        print(num, end=' ')
    num += 1 

#13
number_str = input("Enter a number: ")
#создается временное хранилище
reversed_number_str = ""
for char in number_str:
    #каждый символ ввода идет в временное хранилище. Например ввод 45. Сначала идет 4 и после 5. То есть 4 пойдет в правую сторону и 5 пойдет после.(В левую) 
    reversed_number_str = char + reversed_number_str
print(reversed_number_str)

#14
def simple_number_check(n):
        for i in range(2, n + 1):
            if n == i:
                return True
            elif n % i == 0:
                return False
        return True

input = int(input("Number: "))
word = input

if not simple_number_check(input):
    if word % 2 == 0:
            word += 1
    else:
            word += 2

while True:
    if simple_number_check(word):
        print(word)
        break
word += 2

#15
word = str(input("String: ")).lower()
user_input = int(input("Number: "))

order = {}
one_piece = []

for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz', 1):
    order[letter] = i

while True:
    for j in word:
        index = 0
        index = order[j]
        index += user_input
        if index > 26:
            index -= 26
        for key, value in order.items():
            if index == value:
                one_piece += key
                break
        break
    for i in range(len(one_piece)):
        print(one_piece[i], end="")
