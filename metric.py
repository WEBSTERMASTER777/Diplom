

from sklearn.neighbors import KNeighborsClassifier

from sklearn import metrics



def knn_acc(test_em,test_labels,train_em,train_labels,n_neighbors,metric):
          knn=KNeighborsClassifier(n_neighbors,metric=metric)
          knn.fit(train_em,train_labels)
          y_pred=knn.predict(test_em)

          msg=f'Knn acc: {metrics.accuracy_score(test_labels,y_pred)} count neighbors: {n_neighbors}'
          print(msg)