import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def result_score():
    digits = load_digits()
    df = pd.DataFrame(digits.data,digits.target)
    df['target'] = digits.target

    X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis='columns'), df.target, test_size=0.3)
    rbf_model = SVC(kernel='rbf')
    rbf_model.fit(X_train, y_train)
    result_rbf = rbf_model.score(X_test,y_test)
    # print(result_rbf)

    linear_model = SVC(kernel='linear')
    linear_model.fit(X_train,y_train)
    result_linear = linear_model.score(X_test,y_test)

    # print(result_linear)

    return {"result_rdf": result_rbf , "result_linear":result_linear};





