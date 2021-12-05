# Conflict-Serializability-Checker

This mini CLI tool serves to help students taking CS3223 Database Systems 
Implementation (NUS) to understand the idea of conflict serializability. 

## Prerequisites 

Ensure that you have at least Python 3.6 installed on your machine. 

## Input File Format 

Ensure that your input file contains only one line worth of database actions (read and write). 

An example input file looks like this: 

```
R1X, R2X, W2X, W1X, W2Y, W1Y
```

In this example, we can see that each action contains of the following: 

1. An action `R` (Read) or `W` (Write)
2. A transaction number (Can be `> 9`)
3. An object associated with the operation 

**NOTE**: Do note that if your objects are in different case, they **will be treated** as different objects by the evaluator. 

## Usage 

```
usage: main.py [-h] -i [INFILE]

Follow the following arguments to provide your sequence of transactions

optional arguments:
  -h, --help   show this help message and exit
  -i [INFILE]  file which contains transaction actions
```

## References 

1. [Ramakrishnan - Database Management Systems 3rd Edition](http://pages.cs.wisc.edu/~dbbook/openAccess/thirdEdition/supporting_material.htm)
