from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt

train_data = genfromtxt("./data.csv", delimiter=',')

print train_data

forest = RandomForestClassifier(n_estimators=400)

forest = forest.fit(train_data[0:10000], train_data[0:10000, 59])

output = forest.predict(train_data)

i = 1
for x in output:
    print i ,":", x, "\n"
    i = i + 1


