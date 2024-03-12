class Main:
    def f1(self, inputString):
        a = inputString.split(', ')
        for x in a:
            print(x)
    def f2(self, inputString):
        import math
        x = 0
        y = 0
        a = inputString.split(', ')
        for item in a:
            lst = item.split()
            direction, distance = lst
            if direction == "UP":
                x += int(distance)
            elif direction == "DOWN":
                x -= int(distance)
            elif direction == "LEFT":
                y -= int(distance)
            elif direction == "RIGHT":
                y += int(distance)
        res = math.sqrt(x**2 + y**2)
        print(round(res))
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        choice = int(input())
        inputString = input()
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
        