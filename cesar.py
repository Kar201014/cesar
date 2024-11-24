# tarer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def cesar():
#     a = input("grir bar ")
#     shift = int(input("qani tarov bar"))
#     verdjnakn_text = ""
#     for i in a:
#                     y = tarer.index(i)
#                     y+=shift
#                     tar = tarer[y]
#                     verdjnakn_text += tar
#     print(verdjnakn_text)
# cesar()
# Mayraqaxaq = {
#     "Fransia": "Paris",
#     "Germania":"Berlin",
#     "Hayastan":"Erevan"
# }
# print(Mayraqaxaq)
# student = {
#     "name":"Aram",
#     "age":20,
#     "grade": 85
# }
    
# student["age"] = 98767
# print(student["age"])

# student["course"] = "Math"
# print(student) 


# for key in student.keys():
#     print(key)    
        
# for velue in student.values():
#     print(velue)
    
# for key, value in student.items():
#     print(key, ":", value) 
    
# if "grade" in student:
#     print("grade exists")
# else:
#     print("chka")
    
# print(len(student))
               
# student.pop("grade")
# print(student)                     
# student_scores = {
#     "Armen": 81,
#     "Sargis": 100,
#     "Ani": 99,
#     "Anna": 74,
#     "Sona":  62 ,
# }                        

# nor_bararan = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score >=90:
#         nor_bararan[student] = "shat lav"
#     elif score >=80:
#         nor_bararan[student] = "lav"
#     elif score >70:
#         nor_bararan[student] = "vat"
#     else:
#         nor_bararan[student] = " shat vat"
    
# print(nor_bararan)
        
# print("barev".upper())

# words_list = ["apple", "banana"]
# uppercase_words = [word.upper() for word in  words_list]
# print( uppercase_words)
# anun_list = ["Armen", "Ani", "Sona"]
# s_names = [i for i in anun_list if i.startswith('L')]
# print(s_names)

# shopping_cart = {
#     "apple":2.5,
#     "banana":1.2,
#     "orange":3.0,
#     "grapes":4.5,
# }

# discounted_prices = {}

# for item, price in shopping_cart.items():
#         if price >= 3.0:
#            discounted_prices[item] = price * 0.9
#         else:
#             discounted_prices[item] = price
            
# # print(discounted_prices)                   
# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#          return n * faktorial(n - 1)
# result = faktorial(5)
# print(f"The facyorial of 5 is: {result}")

# words_list = ["apple","banana","kiwi","orange"]
# filtered_words = []
# for i in words_list:
#      if len(i)>5:
#       filtered_words.append(i)
      
# print(filtered_words)

# words_list = ["apple","banana","kiwi","orange"]
# filtered_words = []
# for i in words_list:
#      if len(i)>4 and i.startswith("a"):
#       filtered_words.append(i)
      
      
# # print(filtered_words)
# import random

# def random_condition():
#     weather_conditions = ["andzrev", "dzyun"]                
#     random_condition = random.choice(weather_conditions)
#     return random_condition

# def format_masage(weather_condition):
#     format_masage = weather_condition.capitalize()
# #     if format_masage[0] in 'AEIOU':
# #         article = "an"                
# #     else:
# #         article = "a"
# #     masage = f"it s {article} {format_masage} dey"
# #     return masage

# # print(format_masage(random_condition()))

# temperatures_celsius = {
#     "Mondey":25,
#     "Tuesdey":30,
#     "Wednesdey":28,
# }
# temperatures_farenheit = {}

# for dey, celsius in temperatures_celsius.items():
#     farenheit = (celsius * 9/5) + 32
#     temperatures_farenheit[dey] = farenheit 
    
# print(temperatures_farenheit)
# students_scores = {
#     "Anna": 85,
#     "Karen": 70,
#     "Hakob": 658,
# }

# def calculate_average(scores):
#     total = sum(scores)
#     return total / len(scores)


# def print_bolow_average_students(students_scores):
#     average_score = calculate_average(students_scores.values())
#     print(f"dasarani mijin gnahatakany: {average_score}")
    
#     for student, score in students_scores.items():
#         if score < average_score:
#             print(f"{student}: {score}")
# print_bolow_average_students(students_scores)
# def zuyg_tver(a,b):
#     x = 0
#     y = 1
#     for i in range(a,b):
#         if i % 2 == 0:
#             x += i
#             y *= i
#     print(x,y)
# zuyg_tver(1,46)
# def x(n):
#     if n <= 1:
#         return n
#     else:
#         return x(n - 1) + x(n -2)
    
# print(x(7))

# def sum_list(numbers):
#     if not numbers:
#         return 0
#     else:
#         return numbers[0] + sum_list(numbers[1:])
# list = [1,2,3,4,5,6,7,8,9,10]
# print(sum_list(list))

# def power(x,n):
#     if n == 0:
#         return 1 
#     else:
#         return x * power(x, n - 1)
# print(power(8,57))
def revers_string(s):
    if len(s) == 0:
        return s 
    else:
        return s[-1] + revers_string(s[:-1])
print(revers_string("hakoby gnac tun "))