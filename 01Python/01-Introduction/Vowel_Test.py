 #!/bin/python
#Python code to test whether the letter is vowel or not
#pip install readchar

from readchar import readkey
print("please enter your character: ") 
x=readkey()
print(x)
if x in 'aeiou' :
     print(f"the letter {x} is Vowel")
else:
     print(f"the letter {x} isnot Vowel")
