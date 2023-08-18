n=int(input());
X=[];

for i in range(n):
  X.append([float(x) for x in input().split()]);
print(X);
y=[int(x) for x in input().split()];
print(y);
datapoint=[[float(x) for x in input().split()]];
from sklearn.linear_model import LogisticRegression;
model=LogisticRegression();
model.fit(X,y);
result=model.predict(datapoint);
for i in result:
    print(i);

