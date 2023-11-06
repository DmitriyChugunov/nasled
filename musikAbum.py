# import random
#
#
# class MusicAlbum:
#
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
# Название: {self.title}
# Исполнитель: {self.artist}
# Год выпуска: {self.release_year}
# Жанр: {self.genre}
# Список трэков: {self.tracklist}
#             ''')
#
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
#
# album4 = MusicAlbum('Алабуга', 'Дмитрий', '1900', 'Драма',["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# album4.get_info()
# print(album4.play_random_track())

################# 2 #############
#
# class Stusent:
#
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def info(self):
#         print(f'Имя: {self.name}')
#         print(f'Возраст: {self.age}')
#         print(f'Класс: {self.grade}')
#         print(f'Оценки: {self.scores}')
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# student2 = Stusent('Дмитрий Чугунов', '15', '1 курс', [2, 3, 2, 3, 5, 5, 5])
# student2.info()
# print('Средний балл: ', student2.average_score())
#

################### 3 #################

# class Recipe:
#
#     def __init__(self, ing, dish):
#         self.ing = ing
#         self.dish = dish
#
#     def print_ingredients(self):
#         print(f'Ингредиенты для {self.dish}:')
#         for item in self.ing:
#             print(f'- {item}')
#
#     def cook(self):
#         print(f'''
# Сегодня мы готовим {self.dish}
# Выполняем инструкцию по приготовлению блюда {self.dish}
# Блюдо {self.dish} готово!
# ''')
#
# spaggeti = Recipe(['Спагетти', 'Фарш', 'Томатный соус', 'Лук', 'Чеснок', 'Соль'], 'Спагетти болоньезе')
# spaggeti.print_ingredients()
# spaggeti.cook()
# keks = Recipe(['Мука', 'Яйца', 'Молоко', 'Сахар', 'Сливочное масло', 'Соль'], 'Кекс')
# keks.print_ingredients()
# keks.cook()

################ 4 ################

# class Publisher:
#
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         print(f'Готовим {self.name} к публикации в {self.location}')
#
# class BookPublisher(Publisher):
#
#     def __init__(self, name, location, message, author, publishing, straniz, stats):
#         super().__init__(name,location)
#         self.message = message
#         self.author = author
#         self.publishing = publishing
#         self.stats = stats
#         self.straniz = straniz
#     def publish(self):
#         print(f'Готовим {self.name} к публикации в {self.location}')
#         print(f'Передаем рукопись {self.message}, написанную автором {self.author} в издательство {self.publishing}')
#         print(f'Печатаем свежий номер со статьей {self.stats} на главной странице в издательстве {self.straniz}')
#
# class NewspaperPublisher(Publisher):
#
#     def __init__(self, name, location, stats, message, author, publishing,  straniz):
#         super().__init__(name,location)
#         self.stats = stats
#         self.message = message
#         self.author = author
#         self.publishing = publishing
#         self.straniz = straniz
#
#     def publications(self):
#         print(f'Готовим {self.name} к публикации в {self.location}')
#         print(f'Передаем рукопись {self.message}, написанную автором {self.author} в издательство {self.publishing}')
#         print(f'Печатаем свежий номер со статьей {self.stats} на главной странице в издательстве {self.straniz}')
#
# a = Publisher('Справочник писателя', 'АБВГД Пресс(Москва)')
# a.get_info()
# print()
# b = BookPublisher('Справочник писателя', 'АБВГД Пресс(Москва)','Приключения Чебурашки', 'В.И. Пупкин', 'Важные Книги (Самара)', 'Московские вести (Москва)', 'Новая версия Midjourney будет платной')
# b.publish()

############### 5 ##################

# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []
#
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append("Внесение наличных на счет: " + str(amount))
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append("Снятие наличных: " + str(amount))
#         else:
#             print("Недостаточно средств на счете.")
#
#     def add_interest(self):
#         interest = self.__balance * self.__interest_rate
#         self.__balance += interest
#         self.__transactions.append("Начислены проценты по вкладу: " + str(interest))
#
#     def history(self):
#         for transaction in self.__transactions:
#             print(transaction)
#
# account = BankAccount(100000, 0.05)
# account.deposit(15000)
# account.withdraw(7500)
# account.add_interest()
# account.history()


################### 6 ###############

# class Employee:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#         self.__bonus = 0
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return self.__salary + self.__bonus
#
# employee = Employee("Марина Арефьева", 30, 90000)
# employee.set_bonus(15000)
#
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())


############# 7 ###############


# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(self.name, "подает голос")
#
#     def move(self):
#         print(self.name, "дергает хвостом")
#
#
# class Dog(Animal):
#     def __init__(self, name, species, legs, breed):
#         super().__init__(name, species, legs)
#         self.breed = breed
#
#     def bark(self):
#         print(self.breed, self.name, "лает")
#
#
# class Bird(Animal):
#     def __init__(self, name, species, legs, wingspan):
#         super().__init__(name, species, legs)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(self.species, self.name, "летит")
#
#
# dog = Dog("Геральт", "доберман", 4, "доберман")
# bird = Bird("Вася", "попугай", 2, "средний")
#
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()


############### 8 ################

# class Shape:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def describe(self):
#         print(f"Это геометрическая фигура, цвет - {self.color}.")
#
#
# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__("окружность", color)
#         self.radius = radius
#
#     def area(self):
#         return round(3.14 * self.radius ** 2, 1)
#
#     def describe(self):
#         print(f"Это {self.color} {self.name}. Радиус - {self.radius} см, цвет - {self.color}.")
#
#
# class Rectangle(Shape):
#     def __init__(self, color, length, width):
#         super().__init__("прямоугольник", color)
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def describe(self):
#         print(f"Это {self.color} {self.name}. Длина - {self.length} см, ширина - {self.width} см, цвет - {self.color}.")
#
#
# class Triangle(Shape):
#     def __init__(self, color, base, height):
#         super().__init__("треугольник", color)
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#     def describe(self):
#         print(
#             f"Это {self.color} {self.name} с основанием {self.base} см и высотой {self.height} см, цвет - {self.color}.")
#
#
# circle = Circle("красный", 5)
# rectangle = Rectangle("синий", 3, 4)
# triangle = Triangle("фиолетовый", 6, 8)
#
# circle.describe()
# rectangle.describe()
# triangle.describe()
#
# print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")
#

######################## 9 ########################


# class Candy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
# class Chocolate(Candy):
#     def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
#         super().__init__(name, price, weight)
#         self.cocoa_percentage = cocoa_percentage
#         self.chocolate_type = chocolate_type
#
# class Gummy(Candy):
#     def __init__(self, name, price, weight, flavor, shape):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.shape = shape
#
# class HardCandy(Candy):
#     def __init__(self, name, price, weight, flavor, filled):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.filled = filled
#
# chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
# gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
# hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)
#
# print("Шоколадные конфеты:")
# print(f"Название конфет: {chocolate.name}")
# print(f"Стоимость: {chocolate.price} руб")
# print(f"Вес брутто: {chocolate.weight} г")
# print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
# print(f"Тип шоколада: {chocolate.chocolate_type}")
# print("\nМармелад жевательный:")
# print(f"Название конфет: {gummy.name}")
# print(f"Стоимость: {gummy.price} руб")
# print(f"Вес брутто: {gummy.weight} г")
# print(f"Вкус: {gummy.flavor}")
# print(f"Форма: {gummy.shape}")
# print("\nФруктовые леденцы:")
# print(f"Название конфет: {hard_candy.name}")
# print(f"Стоимость: {hard_candy.price} руб")
# print(f"Вес брутто: {hard_candy.weight} г")
# print(f"Вкус: {hard_candy.flavor}")
# print(f"Начинка: {hard_candy.filled}")



####################### 10 ########################

# class Soldier:
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self.__rank = rank
#         self.__service_number = service_number
#
#     def get_rank(self):
#         return self.__rank
#
#     def confirm_service_number(self):
#         return self.__service_number
#
#     def promote(self):
#         if self.__rank == "рядовой":
#             self.__rank = "ефрейтор"
#             print(f"{self.name} повышен в звании, он теперь {self.__rank}")
#         else:
#             print(f"{self.name} уже имеет более высокое звание")
#
#     def demote(self):
#         if self.__rank == "ефрейтор":
#             self.__rank = "рядовой"
#             print(f"{self.name} понижен в звании, он теперь {self.__rank}")
#         else:
#             print(f"{self.name} уже имеет более низкое звание")
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
# print("Создан новый игровой персонаж типа Soldier с атрибутами:", vars(soldier1))
# print("Персонаж", soldier1.name, "имеет звание", soldier1.get_rank())
# soldier1.promote()
# soldier1.demote()

####################################################################################