# data-in-Python-course
Homeworks from Data in Python course (University of Warsaw):

1. Translator between Morse code and polish/english (`morse_code.py`)
2. Write tests for functions from `homework.py` file. Test should cover checking if proper exceptions are raised on wrong argument type. Write test should be performed using temporary directory. Test suite should contain at least one test of `calculate` function witch mock of `take_from_list`. (`pytest-excercise`)
3. Part A:
  <pre>
  Create 7 folders named: Monday, ... , Sunday
  In every folder create 2 subfolders: morning, evening
  In every subfolder create 'Solutions.csv' file.
  The 'Solutions.csv' should consist of two lines:
  " Model; Output value; Time of computation; "
  " A ; 17 ; 465s; "
  The first line is always the same.
  The second one should be generated randomly (x in {A,B,C}, 0-1000, 0-1000s)
  </pre>
  
  Part B: 
  <pre>
  Output sum of "Time of computation" for the model A.
  Assume that you do not know how many folders and subfolders there are.
  </pre>
