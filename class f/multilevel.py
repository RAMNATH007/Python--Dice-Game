# class fruit():
#     def apple(self):
#         print("good")
# class sweet(fruit):
#     def mango(self):
#         print("The sweetest")
# class soar(sweet):
#     def lemon(self):
#         print("The soar")
# t=soar()
# t.lemon()
# t.mango()
# class fruit():
#     def apple(self):
#         print("good")
# class sweet(fruit):
#     def mango(self):
#         print("The sweetest")
# class soar(fruit):
#     def lemon(self):
#         print("The soar")
# t=soar()
# t.lemon()
class fruit():
    def apple(self):
        print("good")
    def sweet(self,a):
        a="Fruits are good to health"
class soar(fruit):
    def lemon(self):
        super().sweet(self,)
        print("The soar")
t=soar()
t.lemon()

