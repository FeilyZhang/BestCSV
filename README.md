# BestCSV
Parse csv format data files with Python's csv module and then count the results
# Way of using
### First import the module and specify an alias
`import bestCSV as bc`

### The parameters are as follows
fileName：The name of the file being parsed

indexList：Corresponding row index

*cleanFlag：Data flag to be cleaned up, variable length parameter

### one example
```
import bestCSV as bc

fileName = '/home/fei/python_work/2075089_seg_1.csv'
indexList = [5, 6]
cleanFlag1 = '2.你的学历'
print(bc.bestCSV(fileName, indexList, cleanFlag1))
```
The following is the result
```
[fei@localhost ~]$ python3.6 /home/fei/python_work/csvtest.py
{'A.大一': 51, 'B.大二': 27, 'E.其他': 7, 'D.大四': 3, 'C.大三': 15}
```
---
Note that subtracting 1 from the len() function is the actual length of the tuple, as shown in the 18th line of code.

Another point is that the module has no problem for multiple-choice questions (single), fill in the blanks to be updated.

### Updated August 17, 2018
Multiple choice data statistics support
