memory = []
for i in range(32768):
    memory.append(0)

ONLYvar = int()
globalinput = "Empty"
        
def interpret(code):
    global ONLYvar
    global globalinput
    
    if "i" in code:
        globalinput = 6969
        while globalinput > 255 or globalinput < 0:
            print("-------------------------------------------------")
            print("This programm requires user input.")
            print("Please enter an INTEGER from 0 to 255.")
            print("That integer will be used for the entire programm.")
            print("--------------------------------------------------")
            try:
                globalinput = int(input("Input: "))
            except:
                print()
                print('Invalid datatype. Input must be type "int"')


    else:
        globalinput = None
    
    global memory
    ptr = 0
    numOfIn = 0
    inp_lst = []
    memory = []
    for i in range(32768):
        memory.append(0)
        
    for cmd in code:      
        if cmd == "+":
            if memory[ptr] == 255:
                memory[ptr] = 0
            else:
                memory[ptr] += 1

        elif cmd == "-":
            if memory[ptr] == 0:
                memory[ptr] = 255
            else:
                memory[ptr] -= 1
        
        elif cmd == ">":
            ptr += 1
                
        elif cmd == "<":
            ptr -= 1

        elif cmd == "o": #output
            print(chr(memory[ptr]), end = "")

        elif cmd == "b": #back
            ptr = 0
            
        elif cmd == ":": #set pointer position to current memory
            ptr = memory[ptr]

        elif cmd == ";": #set current memory to pointer position
            memory[ptr] = ptr

        elif cmd == "z": #set current memory to 0
            memory[ptr] = 0

        elif cmd == "r": #reset memory to [0,0,0,0,0,0,...]
            memory = []
            for i in range(32768):
                memory.append(0)

        elif cmd == "i": #input
            memory[ptr] = globalinput

        elif cmd == "g": #get and write to only variable
            ONLYvar = memory[ptr]

        elif cmd == "w": #write variable to current memory
            memory[ptr] = ONLYvar

        


        
    print()



run = True
while run:
    command = input("<BrainFuck> ")
    command_lst = command.split(" ")
    command = command_lst[0]
    if command == "run":
        code = ""
        try:
            code_f = command_lst[1]
            with open(code_f) as f:
                code__ = f.readlines()
            for element in code__:
                code += element
                
            interpret(code) 

        except:
            print("Syntax Error. Expected valid filename.")
    
    elif command == "exit":
        run = False

    elif command == "getMemory":
        print(f"Memory: {memory}")
        print(f"Variable: {ONLYvar}")
        if globalinput == "Empty":
            print("Input: Null")
        else:
            print(f"Input: {globalinput}")

    elif command == "help":
        print("The commands are:")
        print('"run": used to run a programm.')
        print('"exit": exits the interpreter.')
        print('"getMemory": prints the memory.')
        print('"help": shows this')

    else:
        print('Unknown command. Please try again or type "help"!')

    print()
