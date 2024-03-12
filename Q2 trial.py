class main:
    def GuessNumber(self, number):
        a = 0
        b = int(number)
        state = ''
        while state != 'c':
            comp = random.randint(a,b)
            if state == 'h':
                b = comp -1
            elif(state == '1'):
                a = comp + 1
        print('Well done! The computer guessed your number  ' + str(comp) + ' correctly')
        
    def main(self):
        number = input('Enter a range for guessed number: ')
        print('OUTPUT')
        self.GuessNumber(number)
    print("FINISH")
main = Main()
main.main()