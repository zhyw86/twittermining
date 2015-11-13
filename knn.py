from sklearn.neighbors import KNeighborsClassifier
from numpy import genfromtxt

train_data = genfromtxt("./data.csv", delimiter=',')

neigh = KNeighborsClassifier(n_neighbors=20)

neigh.fit(train_data[0:10000], train_data[0:10000, 59])

output = neigh.predict(train_data)

i = 1
for x in output:
    print i ,":", x, "\n"
    i = i + 1
