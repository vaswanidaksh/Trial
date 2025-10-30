class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks)
    def grade(self):
        if self.marks >=6:
            print("keep it up")
        elif self.marks<6 and self.marks>=0:
            print("hota h koi ni")
        else:
            print("tum rhene do")
s1 = student("Daksh",-1)
s2 = student("aryan",-99)
s1.display()
s1.grade()
s2.display()
s2.grade()



# class car:
#     tt=0
#     def __init__(self,model,avg):
#         self.model=model
#         self.avg=avg
#         car.tt+=1
#     def sd(self):
#         print(self.model,self.avg)
#     @classmethod
#     def st(cls):
#         print(cls.tt)
#     @staticmethod
#     def isgood(avg):
#         return avg > 15
# car1 = car("BMW",17)
# car2 = car("se",13)
# car1.sd()
# car2.sd()
# print(car.isgood(car1.avg))
# print(car.isgood(car2.avg))


# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self._author=author
#     def show_details(self):
#         print(self.title,self._author)
# h1=Book("fifty shades of grey","MR X")
# h2=Book("The summer i turned pritty","Some white woman")
# h1.show_details()
# h2.show_details()

# class car:
#     def __init__(self,speed):
#         self.__speed=0
#     def accelerate(self,amt):
#         if self.__speed+ amt<=200:
#             self.__speed+=amt
#         else:
#             self.__speed=200
#     def brake(self,amt):
#         if self.__speed-amt<=200:
#             self.__speed-=amt
#         else:
#             self.__speed=0
#     def get_speed(self):
#         print(self.__speed)
# Car=car(0)
# Car.accelerate(50)
# Car.get_speed()
# Car.brake(59)
        

# class shopping_cart:
#     def __init__(self):
#         self.__total_amt=0
#     def add_item(self,price):
#         if price >0:
#             self.__total_amt+=price
#             print(price,self.__total_amt)
#         else:
#             print("invalid")
#     def remove_item(self,price):
#         if 0<price<self.__total_amt:
#             self.__total_amt-=price
#         else:
#             print("Invalid")
#     def show_total(self):
#         print(self.__total_amt)
# cart=shopping_cart()
# cart.add_item(1000)
# cart.remove_item(400)
# cart.show_total()
        

        
