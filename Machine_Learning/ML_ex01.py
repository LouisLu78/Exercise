'''
The codes underneath are all copied form textbook.
'''
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

# plength = features[:, 2]
# # use numpy operations to get setosa features
# is_setosa = (labels == 'setosa')
# # This is the important step:
# max_setosa =plength[is_setosa].max()
# min_non_setosa = plength[~is_setosa].min()
# print('Maximum of setosa: {0}.'.format(max_setosa))
# print('Minimum of others: {0}.'.format(min_non_setosa))
#
# if features[:,2] < 2:
#     print('Iris Setosa')
# else:
#     print('Iris Virginica or Iris Versicolour')