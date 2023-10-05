class MathProblemTrainer:
    task = 0
    def __init__(self, answer):
        MathProblemTrainer.task += 1
        self.answer = answer

    def Task_2a(self):
        print("Task:" +str(MathProblemTrainer.task))
        answerUser = float(input("Please input your answer :"))
        if answerUser == self.answer:
            self.status = True
        else:
            self.status = False
    def Task_2b(self):
        return self.status

class MultiplicationTrainer(MathProblemTrainer):

    def __init__(self, answer):
        super(answer)
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2
        self.answer = par1 * par2

    def StringMultiplication(self):
        return str(self.par1) + "*" + str(self.par2)


class AdditionTrainer(MathProblemTrainer):
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2
        self.answer = par1 + par2

    def StringAddition(self):
        return str(self.par1) + "+" + str(self.par2)

obj1 = MathProblemTrainer(7*5)
obj1.Task_2a()
print(obj1.Task_2b())
print()

obj2 = MathProblemTrainer(12+8)
obj2.Task_2a()
print(obj2.Task_2b())
print()

obj3 = AdditionTrainer(7, 8)
print(obj3.StringAddition())
obj3.Task_2a()
print(obj3.Task_2b())
print()

obj4 = MultiplicationTrainer(6,4)
print(obj4.StringMultiplication())
obj4.Task_2a()
print(obj4.Task_2b())
