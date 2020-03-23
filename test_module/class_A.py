class A:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def __add__(self):
        return self.a + self.b
count= A('4',5)
print(count.add())