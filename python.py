# a = int(input('print your number:'))
# print('таблиця множення на',a)
# for i in range(1,11):
#     print(f'{a}х{i}={i*a}')

# import random
# user_choice = ''
# while True:
#     user_choice = input("Виберіть камінь, ножиці або папір: ")
#     if user_choice == 'камiнь' or user_choice == 'ножиці' or user_choice == 'папір':
#         break
# options = ["камінь", "ножиці", "папір"]
# computer_choice = random.choice(options)

# if user_choice == computer_choice:
#     print("Нічия! Обидва вибрали", user_choice)
# elif (user_choice == "камінь" and computer_choice == "ножиці") or (user_choice == "ножиці" and computer_choice == "папір") or (user_choice == "папір" and computer_choice == "камінь"):
#     print("Ви перемогли! Користувач вибрав", user_choice, "і комп'ютер вибрав", computer_choice)
# else:
#     print("Ви програли! Користувач вибрав", user_choice, "і комп'ютер вибрав", computer_choice)
# import random

# a = random.randint(1,101)
# user_choice = None
# while user_choice != a:
#     user_choice = int(input('спробуй вгадати число вiд 1 до 100:'))
#     if user_choice < a:
#         print('загадане число бiльше')
#     elif user_choice > a:
#         print('загадане число менше')
# print('ви виграли')
# # list_games = ['rust','ark','dota2']
# # list_genre = ['survival','survival','moba']




# print(sorted(list_games))

# print(list(zip(list_games,list_genre)))

# print(list(enumerate(list_games)))

# list_star = int(input('напишiть скiльки у вас зiрок:'))

# list_money = int(input('напишiть скiльки коштує ваш номер:'))
# if list_star > 3:
#     if list_money > 300:
#         print('рейтинг високий вартiсть висока')
#     else:
#         print('рейтинг високий вартiсть низька')

# else:   
#     if list_money > 300:
#         print('рейтинг не високий, вартість висока')
#     else:
#         print('рейтинг не високий,вартість низька')


# matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# for row in matrix:
#     for element in row:
#         print(element,end = ' ')
#     print()


# num_subjects = int(input("Введіть кількість предметів: "))

# total_marks = 0
# for i in range(num_subjects):
#     mark = int(input(f"Введіть оцінку за предмет #{i+1}: "))
#     total_marks += mark

# average_mark = total_marks / num_subjects
# if average_mark >= 90:
#     print('ваш середній бал: A')
# elif average_mark >= 80:
#     print('ваш середній бал: B')
# elif average_mark >= 70:
#     print('ваш середній бал: C')
# elif average_mark >= 60:
#     print('ваш середній бал: D')
# else:
#     print('ваш середній бал: F')


# print(sorted(list_games))

# print(list(zip(list_games,list_genre)))

# print(list(enumerate(list_games)))


# a = []
# a.append('pc')
# a.append('pc')
# a.insert(0,'Xbox')
# a.remove('pc')
# a.pop(0)
# print(a.index('pc'))
# print(a.count('pc'))

# print(a)

# numbers = [1,2,3,4,5,6]
# num = [7,8]
# numbers += num
# print(numbers)

# list_ovochi = []

# list_sina = []

# list_kilkist = []


# while True:

    
#     a = input('напишіть бажаний овоч:')
#     list_ovochi.append(a)
#     b = input('напишіть бажану ціну овочів :')
#     list_sina.append(b)
#     c = input('напишіть бажану кількість овочів:')
#     list_kilkist.append(c)
#     print('овочі у кошику:',list_ovochi)
    
#     print('ціна одного овоча у кошику:',list_sina)
    
#     print('кількість овочів у кошику:',list_kilkist)

#     stop = input('хочете продовжити? так/ні')

#     if stop =='так':
#         continue
#     else:
#         break

# s = ('Вітя','Коля','Максим')
# print(s[0])
# for a in range(3):
#     print(s[a])
# for name in s:
#     print(name)

# list = [("Book", 10.99, 13), ()]
# k = (2.99,10,4,30)
# a, b, c, d= k



# print('назва:','книжкаж','ціна:',a,'кількість:',b)
# print('назва:','ліхтарик','ціна:',c,'кількість:',d)
# import Geometry.Triangle as tr
# import Geometry.Circle as circle
# import Geometry.Rectangle as rec

# from Geometry import Circle, Triangle, Rectangle
# # from Geometry import *
# print(Circle.lenght(3))

# print(Triangle.perimetr(3,8,4))

# print(Rectangle.perimeter
# class Car:
#     def __init__(self,mark,model):
#         self.mark = mark
#         self.model = model

#     def display_info(self):
#         print(f'mark: {self.mark}\nmodel: {self.model}')

# mark1 = Car('BMW','M5')

# mark1.display_info()









# class Student:
#     def __init__(self,name,last_name,course,grade):
#         self.name = name
#         self.last_name = last_name
#         self.course = course
#         self.grade = grade
#     def __str__(self):
#         return f'{self.name} {self.last_name} курc:{self.course} середній бал:{self.grade}'

# class Course:
#     def __init__(self,course_name):
#         self.course_name =course_name
#         self.student = []
#     def add_student(self,student):
#         self.student.append(student)
#     def get_student(self):
#         return self.student
#     def average_great(self):
#         if len(self.student) == 0:
#             return 0
#         else:
#             total_grade = sum(student.average_grade for student in self.student)
#             return total_grade / len(self.student)
# class University:
#     def __init__(self,name_universety):
#         self.name_universety = name_universety
#         self.courses = []
#     def add_course(self,course):
#         self.courses.append(course)
#     def get_course(self):
#         return self.courses
        
# university = University('Oxford')
# course1 = Course('math')
# course2 = Course('biology')
# course3 = Course('language')
# # print(university.get_course())
# university.add_course(course1)
# university.add_course(course2)
# university.add_course(course3)
# # print(university.get_course())      
# student1 = Student('Jayms','Vilkins',2,70)
# student2 = Student('Frank','Hosfild',4,77)
# student3 = Student('Tobi','Holand',1,80)

# course1.add_student(student1)
# course2.add_student(student2)
# course2.add_student(student3)
# course3.add_student(student3)

# for cur in university.get_course():
#     print(f'course:{cur.course_name}')
#     students = cur.get_student()
#     for stud in students:
#         print(f'student:{stud}')






# class Employee:
#     def __init__(self,name,position,salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#     def __str__(self):
#         return f"Ім'я: {self.name}, Посада: {self.position}, Зарплата:{self.salary}"

# employer1 = Employee('Andriy','Admin',300)


# print(employer1)



import math


class shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

class circle(shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius
    def area(self):
        return math.pi * self._radius ** 2
class rectangle(shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
circle1 = circle('circle',5)
circle1._radius = 10
print(circle1._radius)



# Додати до батьківського класу метод perimetr().
# Реалізувати метод в класі Rectangle.
# Додати дочірній клас Triangle реалізувати в ньому метод perimetr()
# За бажанням: в класі Triangle реалізувати метод area()

# class Rectangle:
#     def __init__(self, name,perimetr):
#         super().__init__(name)
#         self.perimetr = perimetr
#     def

        




