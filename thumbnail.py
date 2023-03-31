class Iyatomi():
    belonging = "null"
    tl = "Iyatomi"

    def __init__(self, grade):
        self.grade = grade

    def getTitle(self):
        return self.tl

class Plant(Iyatomi):
    def __init__(self, grade):
        self.belonging = "plant"
        self.tl = "radio"

class Medical(Iyatomi):
    def __init__(self, grade):
        self.belonging = "medical"
        self.tl = "Who is your favorite editor"

class nlp(Iyatomi):
    def __init__(self, grade):
        self.belonging = "nlp"
        self.tl = "?"

a = Iyatomi("B3")
b = Plant("M2")
c = Medical("B3")
d = nlp("D1")
pt = [a, b, c, d]
print("\n")

for e in pt:
    print(e.getTitle(), end=' ')

print("\n\n")

