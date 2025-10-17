import sys

def print_usage():    # prints usage information
    print("""
usage: calc.py <operation> <arg1> <arg2>
<operation> = add | sub | mul | div
arg1: any number
arg2: any number
          """)

def main(args: list[str]) -> None:  # main function to handle operations
    if args[0] == 'add':            # args[0] = [add, 1, 2](0,1,2)
        result = int(args[1]) + int(args[2])
        print(result)
    elif args[0] == 'sub':
        result = int(args[1]) - int(args[2])
        print(result)
    elif args[0] == 'mul':
        result = int(args[1]) * int(args[2])
        print(result)
    elif args[0] == 'div':
        if int(args[2]) == 0:
            print("Error: Division by zero")
            return
        result = int(args[1]) / int(args[2])
        print(result)

if __name__ == "__main__":
    #print(sys.argv)
    args = sys.argv[1::]            
    if len(args) != 3:     # check for correct number of arguments [operation, arg1, arg2]
        print("Invalid arguments passed")
        print_usage()
        exit(1)
        
    #print(args)
    main(args)          
    exit(0)