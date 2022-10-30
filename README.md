# MindVomit
A minimalistic interpreted programming language, inspired by BrainFuck. It doesn't need fancy stuff like functions or loops!

this language is based on an array with 32768 "slots". Each is "0" by default and can have a maximum value of "255". There is also a "pointer" that indicates your position in the array. By default it is at position "0".

Operators:
  - ">" Moves the pointer one slot to the right.
  - "<" Moves the pointer one slot to the left.
  - "+" Adds "1" to the value of the currently selected slot in memory.
  - "-" Subtracts "1" from the value of the currently selected slot in memory.
  - "o" Outputs the corresponding ASCII-character of the current slot to the console.
  - "b" Sets the pointers position to "0".
  - ":" Sets the pointers position to the value of the currently selected slot.
  - ";" Sets the currently selected slots value to its position.
  - "z" Sets the currently selected slots value to "0".
  - "r" Resets every slot in memory to "0".
  - "g" Sets the only available variable to the value of the currently selected slot.
  - "w" Sets the value of the currently selected slot to the only variables value
  - "i" A constant which gets defined before running the code. "Input"
  
  The constant and the variable can only hold a value from "0" to "255"
  
 Loops:
  - "(" signals the opening of a loop. Corresponds to ")".
  - ")" signals the closing of a loop. Corresponds to "(".
  - "[" same as "(" but corresponds to "]"
  - "]" same as ")" but corresponds to "["
  - "{" same as "(" but corresponds to "}"
  - "}" same as "}" but corresponds to "}"
  
  -This means there can only be 3 layers of nested loops!
  
  How loops work:
  - memory = [0,0,0], ptr = 0
  - +++
  - memory = [3,0,0], ptr = 0
  - (>+++
  - memory = [3,3,0], ptr = 1
  - <-)
  - memory = [2,3,0], ptr = 0
  - ...
  
  The loop gets executed until the initial memory position = 0
  - +++(>+++<-)x would result in 
  - memory = [0,9,0] and ptr = 0
  - +++(>+++<-x) would result in an error
  - +++(>+++<-x)x would result in
  - memory = [2,3,0]
  
  
  
Closing-characters:
  - "x" a character that quits the execution of a programm.
  - "?" a character that converts the programm into an endless loop,
  - The last symbol in a script must always be one of these closing-characters.
  - They can be placed anywhere in the code but one of them must be the last character of any script. "x" can be useful when using loops as if-statements.



Examples:
  - "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ox" outputs "H"
  - "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++o+o----------------------------------------ox" outputs "HI!"
  - "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++go>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>
w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+ogx" outputs the alphabet in capital letters.
  - "igo>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+og>w+ogx" outputs the alphabet in capital letters if the constant is assigned as "65"
  - "+++++++(>++++++++++o<-)x" outputs "¶▲(2<F"


The Interpreter:
  - "run <filename>" executes the programm from a file (I like the .mvt file extension because of MindVomiT but this should work with .txt files as well)
  - "exit" exits the interpreter.
  - "getMemory" prints the entire memory to the console. only works after a programm is executed. "run" always resets memory.
  - "help" prints help for all commands
  
Versions:
  - Features [<>+-ob:;z] are available in all versions
  - Features [gwi] are only available in version 1.1.0 or higher
  - Features [x?] and loops are only available in versions 1.2.0 or higher
