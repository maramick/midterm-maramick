class AIChatBot:
    def __init__(self, name, age):
        self.name = name
        self.age = str(age)

    def showSubjectName(self):
        print("AI for robot system")
        return

    def showStudentYear(self):
        y = str(input(""))
        y = int(y[0]+y[1])
        print(66-y)
        return

    def calculator(self):
        y = str(input(""))
        x1 = int(input(""))
        x2 = int(input(""))

        if y == '+':
            print(x1+x2)
            return

        if y == '-':
            print(x1-x2)
            return

    def main(self):
        while True:
            x = str(input(""))
            
            if x == 'subject':
                p1.showSubjectName()

            if x == 'year':
                p1.showStudentYear()

            if x == 'calc':
                p1.calculator()


p1 = AIChatBot("init", 0)
p1.main()
        
