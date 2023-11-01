# class Geeks:
#     name = "Geeks"
# geeks = Geeks()
# print(geeks.name)

# class User:
#     def hello_method(self):
        # print("Привет Наташа")
# user = User()
# user.hello_method()

# class User:
#     def hello_method(self):
#         return "Привет Наташа"
#         print("Привет Наташа")
# user = User()
# print(user.hello_method())

# class Students:
#     surname = "Beksultan"
#     def __init__(self,name,username,age):
#         self.name = name
#         self.username = username
#         self.age = age
#         print(f"Привет {self.name}")
#     def info(self):
#         print(f"Привет {self.name}, {self.username}, Вам {self.age}")
# students = Students("Geeks", "Osh", 18)
# students.info()

class Book:
    def __init__(self, title,autor):
        self.title = title
        self.autor = autor
    def info(self):
        print(f" Книга: {self.title}, Автор: {self.autor} ")
book = Book ("Гарри Поттер", "Джоан Роулинг")
book.info()

