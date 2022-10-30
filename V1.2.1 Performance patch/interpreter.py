memory = [0]*32768 #thanks to u/F84-5

ONLYvar = None
globalinput = None #thanks to u/F84-5
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
        while 0 <= globalinput <= 255: #thanks to u/F84-5
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
    memory = [0]*32768

    iterPos = 0
    itering = True
      while itering:

        #operators
        #thanks to u/F84-5 for suggesting match/case instead of if/elif/else

        codeAtIterPos = code[iterPos]
        match codeAtIterPos:
        
            case "+":
                if memory[ptr] == 255:
                    memory[ptr] = 0
                else:
                    memory[ptr] += 1

            case "-":
                if memory[ptr] == 0:
                    memory[ptr] = 255
                else:
                    memory[ptr] -= 1
            
            case ">":
                ptr += 1
                    
            case "<":
                ptr -= 1

            case "o": #output
                print(chr(memory[ptr]), end = "")

            case "b": #back
                ptr = 0
                
            case ":": #set pointer position to current memory
                ptr = memory[ptr]

            case ";": #set current memory to pointer position
                if 0 <= ptr <= 255:
                    memory[ptr] = ptr
                else:
                    memory[ptr] = 255

            case "z": #set current memory to 0
                memory[ptr] = 0

            case "r": #reset memory to [0,0,0,0,0,0,...]
                memory = [0]*32768

            case "i": #input
                memory[ptr] = globalinput

            case "g": #get and write to only variable
                ONLYvar = memory[ptr]

            case "w": #write variable to current memory
                memory[ptr] = ONLYvar

            #loops

            case "{":
                l1_begin = iterPos
                l1_ptr_begin = ptr

            case "}":
                if memory[l1_ptr_begin] != 0:
                    iterPos = l1_begin

                

            case "[":
                l2_begin = iterPos
                l2_ptr_begin = ptr

            case "]":
                if memory[l2_ptr_begin] != 0:
                    iterPos = l2_begin

                    

            case "(":
                l3_begin = iterPos
                l3_ptr_begin = ptr

            case ")":
                if memory[l3_ptr_begin] != 0:
                    iterPos = l3_begin

            #enc chars

            case "?": #end char for endless running
                iterPos = 0

            case "x": #end char for ending execution
                itering = False
                
            #thanks to u/F84-5 for suggesting match/case instead of if/elif/else
        iterPos += 1          


        
    print()



run = True
while run:
    command = input("<BrainFuck> ")
    command_lst = command.split(" ")
    command = command_lst[0]

    #thanks to u/F84-5 for suggesting match/case instead of if/elif/else
    match command:
        case "run":
            try:
                code_f = command_lst[1]
                with open(code_f) as f:
                    code = "".join(f.readlines()) #thanks to u/F84-5

                    
                if code[-1] in ["x","?"]:  
                    interpret(code)
                else:
                    print("Your code doesn't contain any closing-character")           

                
            except:
                print("Something went wrong...")

        case "exit":
            run = False

        case "getMemory":
            print(f"Memory: {memory}")
            print(f"Variable: {ONLYvar}")
            print(f"Input: {globalinput}") #thanks to u/F84-5

        case "help":
            print("The commands are:")
            print('"run": used to run a programm.')
            print('"exit": exits the interpreter.')
            print('"getMemory": prints the memory.')
            print('"help": shows this')

        case other:
            print('Unknown command. Please try again or type "help"!')
    #thanks to u/F84-5

    print()
