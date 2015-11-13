from sklearn.naive_bayes import GaussianNB
from numpy import genfromtxt

train_data = genfromtxt("./data.csv", delimiter=',')

gnb = GaussianNB()
gnb.fit(train_data[0:10000], train_data[0:10000, 59])

output = gnb.predict(train_data)

i = 1
for x in output:
    print i ,":", x, "\n"
    i = i + 1
