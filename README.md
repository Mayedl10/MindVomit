# MindVomit
A minimalistic interpreted programming language, inspired by BrainFuck. It doesn't need fancy stuff like variables, functions or loops!

this language is based on an array with 32768 "slots". Each is "0" by default and can have a maximum value of "255". There is also a "pointer" that indicates your position in the array. By default it is at position "0".

Operators:
  - ">": Moves the pointer one slot to the right.
  - "<": Moves the pointer one slot to the left.
  - "+": Adds "1" to the value of the currently selected slot in memory.
  - "-": Subtracts "1" from the value of the currently selected slot in memory.
  - "o": Outputs the corresponding ASCII-character of the current slot to the console.
  - "b": Sets the pointers position to "0".
  - ":": Sets the pointers position to the value of the currently selected slot.
  - ";": Sets the currently selected slots value to its position.
  - "z": Sets the currently selected slots value to "0".
  - "r": Resets every slot in memory to "0".



Examples:
  - "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++o" outputs "H"
  - "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++o+o----------------------------------------o" outputs "HI!"
