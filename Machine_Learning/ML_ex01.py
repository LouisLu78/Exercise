'''
The codes underneath are all copied form textbook.

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()

features = data['data']
print(features.shape)
print(features)


feature_names = data['feature_names']
print(feature_names)

target = data['target']
print(target)
print(target.shape)

for t,marker,c in zip(range(3),">ox","rgb"):
# We plot each class on its own to get different colored markers
    plt.scatter(x=features[target == t,0], y=features[target == t,1], marker=marker, c=c)
plt.show()
'''
# This program is mostly written by myself.
from matplotlib import pyplot as plt
import numpy as np
import requests

res=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt')
res.raise_for_status()
with open('seeds_dataset.txt', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)

data = np.loadtxt('seeds_dataset.txt',usecols=(0,2,7))
area, compactness, target = data[:,0], data[:,1], data[:,2]

def plot(x, y):
    plt.xlabel('area')
    plt.ylabel('compactness')
    for t,marker,c in zip(range(1,4),">ox","rgb"):
        plt.scatter(x[target == t], y[target == t], marker=marker, c=c)

plot(area, compactness)
plt.show()

def z_score(feature):
    feature-=np.mean(feature)
    feature /= np.std(feature)
    return feature

area, compactness = z_score(area), z_score(compactness)
plot(area, compactness)
plt.show()

