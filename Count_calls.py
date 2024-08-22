calls = 0
list_to_search = []
import random
numbers = [1, 2, 3, 4, 5, 6]
c = random.choice(numbers)
print('Случайное число: ', c)
n = str('жы')
n = n.upper()
m = str('жи')
m = m.upper()
for i in range(0, c):
    def count_calls():
        global calls, list_to_search
        word = input('Введите слово, чтобы проверить его на "жы-жи": ')
        string_info = (len(word), word.upper(), word.lower())
        print(string_info)
        word = word.upper()
        list_to_search.append(word)
        calls += 1

    count_calls()

str(list_to_search).upper()
print(str(m),'есть в списке:',str(m) in str(list_to_search))
calls +=1
print(str(n), 'нет в списке:', str(n) not in str(list_to_search))
calls += 1
print('Вызовов:', calls)