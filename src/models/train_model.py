import sklearn as sk

def cv_5(model, features, target):
    # 5-fold cross validation
    Rcross = sk.model_selection.cross_val_score(model,features,target, cv=5, scoring='neg_mean_squared_error')
    print(model)
    print('Mean: '+str(- Rcross.mean())+', Std: '+str(Rcross.std()))