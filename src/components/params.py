def params(for_model):

    parameters = {

        "SVR" : [
            {"kernel": ['linear', 'poly', 'rbf']},
            {"degree": list(range(0,5))},
            {'epsilon': [0.01, 0.1, 0.5, 1.0, 0.001]},
        ],

        "KNN": [
            {'n_neighbors': list(range(1,6))},
            {'weights': ['uniform', "distance"]},
            {"algorithm" : ['auto', 'ball_tree', 'kd_tree', 'brute']}
        ],

        "DT": [
            {'max_depth' : list(range(2, 15))},
            {'min_samples_split': list(range(2,10))},
            {'min_samples_leaf': list(range(1, 10))},
        ],

        "XGB": [
            {'n_estimators': list(range(2, 20))},
            {'max_depth': list(range(2, 15))},
            {'max_leaves': list(range(2, 20))},
            {'grow_policy':["lossguide"]},
            {'learning_rate': [0.001, 0.0001, 0.01, 0.1, 1]}
        ],

        "ADB":[
            {'n_estimators': list(range(2, 15))},
            {'learning_rate': [0.001, 0.0001, 0.01, 0.1, 1]},
        ],

        "GBR":[
            {'n_estimators': list(range(2, 20))},
            {'max_depth' : list(range(2, 15))},
            {'min_samples_split': list(range(2,10))},
            {'min_samples_leaf': list(range(1, 10))},
        ],

        "RF":[
            {'n_estimators': list(range(2, 20))},
            {'max_depth' : list(range(2, 15))},
            {'min_samples_split': list(range(2,10))},
            {'min_samples_leaf': list(range(1, 10))},
        ]

    }

    return parameters[for_model]