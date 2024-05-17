# Числовая угадайка
def is_valid(num):
    #if hi < int(num)  <  1:
    #if num.isdigit() == True and hi < int(num)  <  1:
     if num.isdigit() == True:   
          return True
     else:
          return False
print('Начинаем игру числовая угадайка')
print('По умолчанию угадываем число от 1 до 100')
count = 0
while True:
     print('Хотите изменить верхнюю границу? YES/NO')
     answer = input()
     #if answer == 'NO':
     if answer == 'YES':
          while True:
               print('Введите число верхней границы больше 1')
               hi = input()
               if  hi.isdigit() == False or int(hi) < 1:
                    print('А может всё таки введем целое число больше 1?')
                    continue
               if  int(hi) > 1 and hi.isdigit() == True:
                    print('Загадывается число от 1 до', hi)
                    hi = int(hi)
                    import random
                    num = random.randint(1, hi)
                    print('Напишите число от 1 до', hi)
                    while True:
                         xxx = input()
                         count += 1
                         if  is_valid(xxx) == True:
                              if int(xxx) > int(num):
                                   print('Ваше число больше загаданного, попробуйте ещё раз')
                                   continue
                              if int(xxx) < int(num):
                                   print('Ваше число меньше загаданного, попробуйте ещё раз')
                                   continue
                              if int(xxx) == int(num):
                                   print('Поздравляем вы угадали с ', count, 'раза') 
                                   count = 0
                                   print('Хотите сыграть ещё раз?')
                                   answer2 = input()
                                   if answer2 == 'YES':
                                        break
                                   else:
                                        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                                        break
                    else:
                         print('А может всё таки введем целое число от 1 до', hi, '?')
               break
     break