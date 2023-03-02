import sys 

if __name__ == "__main__":
    def print_arguments_and_their_name():
        """
            takes arguments, and lets you type the name into the input.
            example arguments: "1 2 3 'teste 2'"
            output example: "i received these arguments: dia02_entrada_e_saida.py
            i received these arguments: 1
            i received these arguments: 2
            i received these arguments: 3
            i received these arguments: test 2
            input example: "type your name here: caio"
            output example: "my name is caio
            c
            a
            i
            O
        """
        for argument in sys.argv:
            print("i received these arguments: ", argument)
        my_name = input("type your name here: ")
        print(f"my name is {my_name}")
        for letter in my_name:
            print(letter)

    def calculates_all_numbers():
        """
            takes numbers in the input separated by spaces and does the sum.
            input example: "1 2 3 4 5 6 7 8 9 10"
            output example: "the final sum is 55" 
        """
        nums = input("enter the numbers here separated by a space: ")
        numsArr = nums.split(" ")
        sum = 0
        for num in numsArr:
            if not num.isdigit():
                print(f"Erro ao somar valores, {num} não é um dígito.")
            else:
                sum += int(num)
        print(f"the final sum is {sum}")

    print_arguments_and_their_name()
    calculates_all_numbers()