from sys import exit
from time import sleep


# main func
def main():
    welcomer()
    calculator()

def welcomer():
    # Hailing user
    print('*'*27)
    print("""Welcome to Calculator 1.0.0
The one and only version
Please input op
Press 'q' to exit""")
    print('*'*27)

# callee func
def calculator():
    # operation times counter variable
    op_counter = 0

    # restricting user to prevent eval abuse
    allowed = ".0123456789+-*/ "

    # str to prompt user to input op just for once
    print("Op:")

    # checking if math op is valid
    while True: 
        op = input()

        # prompting user to input math op
        try:
            # if there is no op 
            if op == "":
                print("Please type op and try again!")
                continue

            # exit protocol
            if op == 'q':
                msg = "Exiting..."
                for i in range(len(msg)):
                    print(msg[i], end="", flush=True)
                    sleep(0.2)
        
                print("\n")
                exit(0)
        
            # restricting user input against eval func
            for i in range(len(op)):
                if op[i] not in allowed:
                    print("You used not calculation characters!")
                    exit(1)

            # updating op_counter
            op_counter+=1

            # for the 1st op
            if op_counter == 1:
                # calculation
                rslt = eval(op)
                print("%.2f" %rslt, end="")

            # for rest of it
            else:
                # calculation, making last rslt
                rslt = str(rslt) + op
                rslt = eval(rslt)
                print("%.2f" %rslt, end="")
        
        except ZeroDivisionError as zero:
            print("You can't divide a number to zero")
            print(zero)
            calculator()


# call main if not imported
if __name__ == "__main__":
    main()
