# Multiple Inheritance

class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)


class Father:
    fathername = ""

    def father(self):
        print(self.fathername)


class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother name is :", self.mothername)


s1 = Son()
s1.fathername = "Daddy"
s1.mothername = "Mommy"
s1.parents()
