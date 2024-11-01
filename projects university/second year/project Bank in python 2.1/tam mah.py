# class test:
#     def __init__(self):
#         self.variable = ['Old',5]
#         self.Change(self.variable)
#     def Change(self, var):
#         var += ['New',10]
# obj=test()
#
# print(obj.variable)


class t:
    def __init__(self):
        self.x=5
        print('super')
    def ta(self):
        print('Ta')
class m(t):
    def __init__(self):
        super().__init__()
        print('M')
    def tb(self):
        print('Tb')
u=m()
u.tb()
u.ta()
print(u.x)
# #
# #
# #
# #
# #
#
#
