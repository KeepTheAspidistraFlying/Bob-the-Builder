# Bob-the-Builder
Using Machine Learning/ Logistic Regression

 Hey Guyz;
 
 so this is kinda easy but it can be a very good exercise if ure a beginner in ML.
 
Task:

ure given a feature matrix & a single datapoint to predict.(0 or 1)

build a Logistic Regression model with features & predict the datapoint.

the first few lines are:

n=int(input());

X=[];

for i in range(n):

   X.append([float(x) for x in input().split()]);
  
y=[int(x) for x in input().split()];

datapoint=[[float(x) for x in input().split()]];

************************************************************************

input:

6

1 3

3 5

5 7

3 1

5 3

7 5

1 1 1 0 0 0

2 4

************************************************************************

the output should be 1.


