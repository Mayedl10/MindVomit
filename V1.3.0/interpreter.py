memory = [0]*32768 #thanks to u/F84-5

ONLYvar = 0
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
    global ptr
    
    global l1_ptr_begin
    global l2_ptr_begin
    global l3_ptr_begin

    l1_ptr_begin = 0
    l2_ptr_begin = 0
    l3_ptr_begin = 0

    execute_op = True
    
    global memory
    ptr = 0
    numOfIn = 0
    inp_lst = []
    memory = [0]*32768

    iterPos = 0
    itering = True
    while itering:

        #operators

        codeAtIterPos = code[iterPos]
        match codeAtIterPos:
        
            case "+":
                if execute_op:
                    if memory[ptr] == 255:
                        memory[ptr] = 0
                    else:
                        memory[ptr] += 1

            case "-":
                if execute_op:
                    if memory[ptr] == 0:
                        memory[ptr] = 255
                    else:
                        memory[ptr] -= 1
            
            case ">":
                if execute_op:
                    ptr += 1
                    
            case "<":
                if execute_op:
                    ptr -= 1

            case "o": #output
                if execute_op:
                    print(chr(memory[ptr]), end = "")

            case "n": #newline
                if execute_op:
                    print()
                    

            case "b": #back
                if execute_op:
                    ptr = 0
                
            case ":": #set pointer position to current memory
                if execute_op:
                    ptr = memory[ptr]

            case ";": #set current memory to pointer position
                if execute_op:
                    if 0 <= ptr <= 255:
                        memory[ptr] = ptr
                    else:
                        memory[ptr] = 255

            case "z": #set current memory to 0
                if execute_op:
                    memory[ptr] = 0

            case "r": #reset memory to [0,0,0,0,0,0,...]
                if execute_op:
                    memory = []
                    for i in range(32768):
                        memory.append(0)

            case "g": #get and write to only variable
                if execute_op:
                    ONLYvar = memory[ptr]

            case "w": #write variable to current memory
                if execute_op:
                    memory[ptr] = ONLYvar

            #loops
                    
            case "{":
                if execute_op:
                    l1_begin = iterPos
                    l1_ptr_begin = ptr

            case "}":
                if execute_op:
                    if memory[l1_ptr_begin] != 0:
                        iterPos = l1_begin

         

            case "[":
                if execute_op:
                    l2_begin = iterPos
                    l2_ptr_begin = ptr

            case "]":
                if execute_op:
                    if memory[l2_ptr_begin] != 0:
                        iterPos = l2_begin
            case "(":
                l3_begin = iterPos
                l3_ptr_begin = ptr

            case ")":
                if memory[l3_ptr_begin] != 0:
                    iterPos = l3_begin

            #if statements
            case "L":
                if memory[ptr] == 0:
                    execute_op = False
                else:
                    execute_op = True

            case "J":
                execute_op = True                    


            #enc chars

            case "?": #end char for endless running
                if execute_op:
                    iterPos = 0

            case "x": #end char for ending execution
                if execute_op:
                    itering = False

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

        case "iterMemory":
            iterMemoryCount = 0
            iterMemoryOutList = []
            for i in memory:
                if i != 0:
                    iterMemoryOutList.append(iterMemoryCount)
                iterMemoryCount += 1
            print(f"These parts of memory are not zero: {iterMemoryOutList}")

        case "help":
            print("The commands are:")
            print('"run": used to run a programm.')
            print('"exit": exits the interpreter.')
            print('"getMemory": prints the memory.')
            print('"help": shows this')
            print('"iterMemory": iters through the memory and returns the position of all non-zero values.')

        case other:
            print('Unknown command. Please try again or type "help"!')
    #thanks to u/F84-5

    print()
