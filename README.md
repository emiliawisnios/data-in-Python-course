# data-in-Python-course
Homeworks from Data in Python course (University of Warsaw):

1. Translator between Morse code and polish/english (`morse_code.py`)
2. Write tests for functions from `homework.py` file. Test should cover checking if proper exceptions are raised on wrong argument type. Write test should be performed using temporary directory. Test suite should contain at least one test of `calculate` function witch mock of `take_from_list`. (`pytest-excercise`)
3. `python-directory-exercise`
  Part A:
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
4. Create project which will calculate base statistics of (mean, median and std) of every column except variety from `data/iris.csv file`.
   Project structure should be:
   <pre>
        ├── iris_analysis
    │   ├── __init__.py
    │   ├── io
    │   │   ├── __init__.py
    │   │   ├── load.py
    │   │   └── save.py
    │   └── calculate.py
    └── run_analysis.py
    </pre>
    File `iris_analysis/io/load.py` should contain functions needed to load and parse `data/iris.csv`.
    File `iris_analysis/io/save.py` should contain functions needed to save result to `.csv` file. 
    File `iris_analysis/calculate.py` should contain functions needed for statistic calculation. 
    File `run_analysis.py` should be script which import proper functions from `iris_analysis` package and call them to calculate statistics. 
    Each task should be performed using code from module with proper semantic name. Script should have two arguments: path to ada file and path to result file.
    
    Example run:

    `$ python run_analysis.py data/iris.csv result.csv`
   
