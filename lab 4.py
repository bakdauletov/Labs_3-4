# 1.1
# создал переменную с названием "word"
word = input("Enter your input: ")                    
# если переменная "word" не содержит в себе пустые поля или же просто пустой ввод будет выполнятся print(char_tuple).
char_tuple = tuple(word)                          
# Команда and проверяет ввод, не пусто ли там. any(char.isspace() for char in word) проверяет пустые поля для каждой буквы в переменной "word"
if word and not any(char.isspace() for char in word): 
    char_tuple = tuple(word)                           
    print(char_tuple)                                 
# если ввод содержит пустые поля или же пустой ввод будет выполнятся else.
else:                                                 
    print("The input contain errors. Try again")  

#1.2
my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
# В этой строке используется "" чтобы между буквами не было пробелов, и если например написать " " вот так, то между буквами будет пробел.
# join работает вместе с "". Если говорить просто, то join объединяет элементы друг с другом. 
print("".join(my_tuple))  

#1.3
tuple_a = (1,2,3,4,5,6,7)
tuple_b = (5,6,7,9,7,1,10,10)
# С помощью команды len вычисляем длину и делим ее на половину, чтобы вычислить первую половину tuple_a и вторую половину tuple_b.
First_a = len(tuple_a) // 2
Last_b = len(tuple_b) // 2
# После вычисление половины объединяем их с помощью +, и используем : для выбора половины tuple_b или a. То есть, в первом случае считается с начала First_a, а во втором идет от середины до конца.   
Point = tuple_a[:First_a + 1] + tuple_b[Last_b:] # добавляем +1 если нечетное количесто чисел и нужно приравнять к Last_b.
print("The output is:", Point)

#1.4
#cоздаем массив
elements = [] 
# пока это команда выполняется:
while True:
    word = input("Enter an element : ")
        # если пишется done, терминал остановится
    if word.lower() == 'done':
        break
    elements.append(word)
tuple = tuple(elements)
element_counts = {}
for element in tuple:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
result_tuple = tuple((element, count) for element, count in element_counts.items())

print(result_tuple)

#1.5
#создал три переменных, которых оставил пустыми пока, чтобы вызывать в будущем.
int_tuple = ()  
float_tuple = ()
str_tuple = ()
while True:
    user_input = input("Enter a data object: ")
    # импут будет продолжаться пока не напишется команда done. После этого сработает break.
    if user_input.lower() == 'done':  
        break
    # если импут содержит цифру, то будет выполнятся isdigit и все это закидывается в int_tuple.
    elif user_input.isdigit():
        int_tuple += (int(user_input),)
    # если цифра содержит точку, то есть, если пишется как 5.0 (нецелое число) то replace заменяет точку на пустое поле и потом закидывается в float_tuple
    elif user_input.replace('.', '', 1).isdigit():
        float_tuple += (float(user_input),)
    #если же не выполняется предыдущие if, elif, то выполняется это команда. Не нужно писать код так как это последний вариант из трех форматов. 
    else:
        str_tuple += (user_input,)
print(int_tuple)
print(float_tuple)
print(str_tuple)

#2.1
while True:
    try:
        user_input = input("Enter a string without whitespaces: ")
        # если ввод содержит пробел то будет выполнятся ValueError.
        if any(char.isspace() for char in user_input):
            raise ValueError("Input contains whitespaces. Please enter a string without whitespaces.")
        # x здесь будет считатся как временное хранилище. Ввод который пользователь внес будет хранится в x и потом через str(x) превращается в "tuple" 
        char_set = {str(x) for x in user_input}

        print(f"Created set is: {char_set}")
        break

    except ValueError as e:
        print(e)

#2.2
while True:
    try:
        input_A = input("Enter elements for set A: ")
        # input_A.split(',') вот это команда пишет ввод внутри [] и с ''. После этого map(int) меняет ввод на целое число. Например [1,2,3]. 
        # А команда set удаляет дубликаты и можно сказать что оставляет только уникальные числа.
        set_A = set(map(int, input_A.split(',')))

        input_B = input("Enter elements for set B: ")
        #тоже самое как на set_A
        set_B = set(map(int, input_B.split(',')))

        #удаляет числа которые встречаются друг у друга. Для этого и пишется две команды.
        difference_A_B = set_A - set_B
        difference_B_A = set_B - set_A

        #union объединяет два сета и создает новый сет. Но смысл писать предыдущие команды если union делает то что надо? 
        #union не удаляет числа которые встречаются у обоих сетов, он просто удалает дуликаты. А для задачи нужно удалить числа которые встречаются у обоих. 
        result_set = difference_A_B.union(difference_B_A)
        print(result_set)
        break

    except ValueError:
        print("Invalid input. Please enter comma-separated integers for both sets.")

#2.3
try:
    input_A = input("Enter elements for A: ")
    set_A = set(map(int, input_A.split(',')))
    input_B = input("Enter elements for B: ")
    set_B = set(map(int, input_B.split(',')))
    # удаляет одинаковые значения в set_B и set_A. Теперь, set_B хранит в себе только значения которые есть в Set_B(удалил значения которые есть в Set_A) 
    set_B.difference_update(set_A)
    print(set_B)
except ValueError as e:
    print("Error:", e)

#2.4
try:
    input_A = input("Enter elements for A : ")
    set_A = set(map(int, input_A.split(',')))

    input_B = input("Enter elements for B : ")
    set_B = set(map(int, input_B.split(',')))

    input_C = input("Enter elements for C : ")
    set_C = set(map(int, input_C.split(',')))
    #команда intersection находит одинаковые значения у двух сетов и создает новый сет с этим списком. Суть задачи найти одинаковые значения
    #в A и B. И потом сравнить совпадает ли с эти числа с числами внутри C 
    common_elements = set_A.intersection(set_B)

    #update сравнивает два сета и если первый сет имеет значения которые существует внутри С то удаляет эти значения. Можно сказать, что 
    #это команда обновляет сеты с уникальными значениями. Например, первый сет(1, 2, 3) и второй сет(3,4,5). То получится(1, 2, 3, 4, 5)
    set_C.update(common_elements)

    print(f"New C: {set_C}")

except ValueError as e:
    print("Error:", e)

#3.1
try:
    cars_list = {}
    while True:
        input_data = input("Enter manufacturer and model and when you done with this input 'done': ")
        # импут будет продолжаться пока не напишется команда done. После этого сработает break.
        if input_data.lower() == 'done':
            break
        #разделяет инпут в две части, manufacturer и model
        manufacturer, model = map(str.strip, input_data.split(','))
        
        #Затем код проверяет, находится ли manufacturer внутри cars_list.
        if manufacturer in cars_list:
            # Если это так, то он добавляет model к существующему manufacturer
            cars_list[manufacturer].append(model)
        else:
            cars_list[manufacturer] = [model]

    #то есть это команда выводит все значения внутри manufacturers. (удаляя дубликаты)
    manufacturers = list(cars_list.keys())
    manufacturers.sort() #сортирует в алфавитном порядке

    for manufacturer in manufacturers:
        models = cars_list[manufacturer]
        count = len(models)
        #название и количество
        print(manufacturer, count)
        #выводит каждую модель с начальным дефисом
        for model in models:
            print(f"- {model}")
#try и except используется для того чтобы предотвращать разные исключения которые могут возникнуть. Неравильный string и т.д
except Exception as e:
    print("Error:", e)
