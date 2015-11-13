from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt

train_data = genfromtxt("./data.csv", delimiter=',')

print train_data

<<<<<<< HEAD
forest = RandomForestClassifier(n_estimators=50)
=======
forest = RandomForestClassifier(n_estimators=10)
>>>>>>> c5135128258352e00364dc850e464f0c5e6723bd

forest = forest.fit(train_data[0:10000], train_data[0:10000, 59])

output = forest.predict(train_data)


for x in output:
    status = 'unpopular'
    if x > 1400:
        status = 'popular'

    print "%lf,%s" % (x, status)
