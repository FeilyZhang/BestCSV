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
{'A': 51, 'B': 27, 'E': 7, 'D': 3, 'C': 15}
```
