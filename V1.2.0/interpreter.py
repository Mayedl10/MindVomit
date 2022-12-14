memory = []
for i in range(32768):
    memory.append(0)

ONLYvar = "None"
globalinput = "Empty"
ptr = 0
iterPos = 0

l1_ptr_begin = 0
l2_ptr_begin = 0
l3_ptr_begin = 0

l1_exists = False
l2_exists = False
l3_exists = False

def interpret(code):
    global ONLYvar
    global globalinput
    global ptr
    
    global l1_ptr_begin
    global l2_ptr_begin
    global l3_ptr_begin
    
    l1_ptr_begin = 0
    l2_ptr_begin = 0
    l3_ptr_begin = 0
    
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

    iterPos = 0
    itering = True
    while itering:

        #operators
        
        if code[iterPos] == "+":
            if memory[ptr] == 255:
                memory[ptr] = 0
            else:
                memory[ptr] += 1

        elif code[iterPos] == "-":
            if memory[ptr] == 0:
                memory[ptr] = 255
            else:
                memory[ptr] -= 1
        
        elif code[iterPos] == ">":
            ptr += 1
                
        elif code[iterPos] == "<":
            ptr -= 1

        elif code[iterPos] == "o": #output
            print(chr(memory[ptr]), end = "")

        elif code[iterPos] == "b": #back
            ptr = 0
            
        elif code[iterPos] == ":": #set pointer position to current memory
            ptr = memory[ptr]

        elif code[iterPos] == ";": #set current memory to pointer position
            if 0 <= ptr <= 255:
                memory[ptr] = ptr
            else:
                memory[ptr] = 255

        elif code[iterPos] == "z": #set current memory to 0
            memory[ptr] = 0

        elif code[iterPos] == "r": #reset memory to [0,0,0,0,0,0,...]
            memory = []
            for i in range(32768):
                memory.append(0)

        elif code[iterPos] == "i": #input
            memory[ptr] = globalinput

        elif code[iterPos] == "g": #get and write to only variable
            ONLYvar = memory[ptr]

        elif code[iterPos] == "w": #write variable to current memory
            memory[ptr] = ONLYvar

        #loops

        elif code[iterPos] == "{":
            l1_begin = iterPos
            l1_ptr_begin = ptr

        elif code[iterPos] == "}":
            if memory[l1_ptr_begin] != 0:
                iterPos = l1_begin

            

        elif code[iterPos] == "[":
            l2_begin = iterPos
            l2_ptr_begin = ptr

        elif code[iterPos] == "]":
            if memory[l2_ptr_begin] != 0:
                iterPos = l2_begin

                

        elif code[iterPos] == "(":
            l3_begin = iterPos
            l3_ptr_begin = ptr

        elif code[iterPos] == ")":
            if memory[l3_ptr_begin] != 0:
                iterPos = l3_begin

        #enc chars

        elif code[iterPos] == "?": #end char for endless running
            iterPos = 0

        elif code[iterPos] == "x": #end char for ending execution
            itering = False

        iterPos += 1          


        
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

                
            if code[-1] in ["x","}"]:  
                interpret(code)
            else:
                print("Your code doesn't contain any closing-character")           

            
        except:
            print("Something went wrong...")

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
