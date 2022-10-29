memory = []
for i in range(32768):
    memory.append(0)
        
def interpret(code):            
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
        print(memory)

    elif command == "help":
        print("The commands are:")
        print('"run": used to run a programm.')
        print('"exit": exits the interpreter.')
        print('"getMemory": prints the memory.')
        print('"help": shows this')

    else:
        print('Unknown command. Please try again or type "help"!')

    print()
