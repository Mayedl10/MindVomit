# MindVomit
A minimalistic interpreted programming language, inspired by BrainFuck. It doesn't need fancy stuff like functions or classes!

This language is based on an array with 32768 "slots". Each is "0" by default and can have a maximum value of "255". There is also a "pointer" that indicates your position in the array. By default it is at position "0".

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
  - "i" Works differently in different versions.
      - for versions 1.2.X and lower:
          - A constant which gets defined before running the code. Only available in versions lower than 1.3.0
      - for versions 1.4.X and higher:
          - Sets the currently selected slots value to an input-integer in range 0-255. The data gets input at the time the "i" in the code gets executed.
  - "n" Newline, enters a new line in output
  - "~" Sets the goto-entry-point at this position in code.
  - "#" Jumps to the last created goto-entry-point in code
  
  The input and the variable can only hold a value from "0" to "255"

 If-statements:
  - "L" opens an if-statement
  - "J" closes an if-statement
  - The code inside an if statement only runs if the currently selected slot at the "L" is not "0".

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
  - "L++++++++++++++++++++++++++++++++++oJx" wont output anything because the currently selected slot is "0" while the interpreter is looking at the "L"
  - "+L++++++++++++++++++++++++++++++++++oJx" will output "#" because the currently selected slot is not "0" while the interpreter is looking at the "L"


The Interpreter:
  - "run <filename>" executes the programm from a file (I like the .mvt file extension because of MindVomiT but this should work with .txt files as well)
  - "exit" exits the interpreter.
  - "getMemory" prints the entire memory to the console. only works after a programm is executed. "run" always resets memory.
  - "help" prints help for all commands
  - "iterMemory" iterates through the memory the last program left behind and outputs the position in memory of every non-zero value.
  
Versions:
  - Features [<>+-ob:;z] are available in all versions
  - Features [gwi] are only available in version 1.1.0 or higher
  - Features [x?] and loops are only available in versions 1.2.0 or higher
  - Features [nLJ] and the "iterMemory"-command are only available in versions 1.3.0 or higher
  - Features [i] are only available in versions lower than 1.3.0
