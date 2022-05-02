import requests

try:
     list_of_numbers=list(map(int, input('Введите последовательность чисел через пробел: ').split()))
     any_number=int(input(('Введите любое число: ')))
     import random
     def sort(array,left,right):
         p = random.choice(array[left:right+1])
         i, j = left, right
         while i <= j:
             while array[i] < p:
                 i += 1
             while array[j] > p:
                 j -= 1
             if i <= j:
                 array[i], array[j] = array[j], array[i]
                 i += 1
                 j -= 1
         if j > left:
             sort(array, left, j)
         if right > i:
             sort(array, i, right)
         return array
     def binary_search_position(array,element,left,right):
         global any_number
         if left>right:
             return False
         middle = (right + left) // 2
         if array[middle - 1] < element <= array[middle]:
             return (middle-1)
         elif element<=array[middle-1]:
             return (binary_search_position(array, element,left,middle-1))
         elif element>array[middle]:
             return (binary_search_position(array,element,middle+1,right))
     ind=binary_search_position(list_of_numbers,any_number,0,len(list_of_numbers)-1)
     if ind:
         print('Номер позиции элемента, удовлетворяющего условиям - ',ind)
     else:
         print('Элемент, удовлетворяющий требованиям, отсутствует')
 except ValueError:
     print ('Введите, пожалуйста, числовые данные')
