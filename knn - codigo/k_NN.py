import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class KNN():
    def __init__(self, X_train, y_train, n_neighbors, metric, weights='uniform'):

        self.X_train = X_train
        self.y_train = y_train

        self.n_neighbors = n_neighbors
        self.weights = weights

        self.n_classes = 10

    def euclidian_distance(self, a, b):
        return np.sqrt(np.sum((a - b)**2, axis=1))

    def manhattan_distance(self, a, b):
        return np.sum((a - b), axis=1)

    def kneighbors(self, X_test, metric, return_distance=False):

        dist = []
        neigh_ind = []

        if metric == 'euclidean':
          point_dist = [self.euclidian_distance(x_test, self.X_train) for x_test in X_test]
        elif metric == 'manhattan':
          point_dist = [self.manhattan_distance(x_test, self.X_train) for x_test in X_test]


        for row in point_dist:
            enum_neigh = enumerate(row)
            sorted_neigh = sorted(enum_neigh,
                                  key=lambda x: x[1])[:self.n_neighbors]

            ind_list = [tup[0] for tup in sorted_neigh]
            dist_list = [tup[1] for tup in sorted_neigh]

            dist.append(dist_list)
            neigh_ind.append(ind_list)

        if return_distance:
            return np.array(dist), np.array(neigh_ind)

        return np.array(neigh_ind)

    def predict(self, X_test, metric):

        if self.weights == 'uniform':
            neighbors = self.kneighbors(X_test, metric)
            y_pred = np.array([ np.argmax(np.bincount(self.y_train[neighbor]))
                for neighbor in neighbors
            ])

            return y_pred

        if self.weights == 'distance':

            dist, neigh_ind = self.kneighbors(X_test, return_distance=True)

            inv_dist = 1 / dist

            mean_inv_dist = inv_dist / np.sum(inv_dist, axis=1)[:, np.newaxis]

            cgt = []

            for i, row in enumerate(mean_inv_dist):

                row_pred = self.y_train[neigh_ind[i]]

                for k in range(self.n_classes):
                    indices = np.where(row_pred == k)
                    prob_ind = np.sum(row[indices])
                    cgt.append(np.array(prob_ind))

            pred = np.array(cgt).reshape(X_test.shape[0],
                                                    self.n_classes)

            y_pred = np.array([np.argmax(item) for item in pred])

            return y_pred

    def score(self, X_test, y_test):
        y_pred = self.predict(X_test)

        return float(sum(y_pred == y_test)) / float(len(y_test))


def generateResults(
  k, 
  metric, 
  file, 
  x_test, 
  y_test, 
  x_train, 
  y_train
):

  neighA = KNN(x_train, y_train, k)
  neighA.fit(x_train, y_train)
  neighA.predict(x_test, metric)

  textHeader = "{} - k: {}\n".format(metric, k)

  file.write(textHeader)
  file.write(classification_report(y_test, neighA.predict(x_test)));
  file.write(confusion_matrix(neighA, x_test));
  file.write('\n')

def loadData(preffixFileName, percentageToMantain):
  fileExtension = '.txt'

  testInputFileName = "{}Test{}".format(
    preffixFileName,
    fileExtension);

  trainingInputFileName = "{}Train__{}{}".format(preffixFileName, percentageToMantain, fileExtension)

  ts = np.loadtxt(testInputFileName, 'float', '#', ',');
  tr = np.loadtxt(trainingInputFileName, 'float', '#', ',');
  
  y_test = ts[:,-1]
  y_train = tr[:,-1]
  x_train = tr[:, 1 : -1]
  x_test = ts[:, 1 : -1]

  print(y_test, y_train, x_train, x_test)

  ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

  outputFileName = 'output__{}__{}{}'.format(
    preffixFileName, 
    percentageToMantain,
    fileExtension
  )

  file = open(outputFileName, 'w');

  for k in ks:
    generateResults(
      k, 
      'euclidean', 
      file, 
      x_test, 
      y_test, 
      x_train, 
      y_train)

  for k in ks:
    generateResults(
      k, 
      'manhattan', 
      file, 
      x_test, 
      y_test, 
      x_train, 
      y_train)

  file.close()

def main():
  percentages = [25, 50, 100]
  preffixesFileName = ['dig']

  for preffix in preffixesFileName:
    for percent in percentages:
      loadData(preffix, percent)
  
if __name__ == "__main__":
    main()