import pickle
import numpy as np
import config
import json



def obesity_prediction(Age, Gender, Height, Weight, BMI,
       PhysicalActivityLevel):

    with open(config.model_file_path, 'rb') as f:
        model = pickle.load(f)

    with open(config.col_data_json, 'r') as f:
        col_data = json.load(f)

    Gender = col_data['Gender'][Gender]

    test_array = np.zeros((1,model.n_features_in_))
    test_array[0,0] = Age
    test_array[0,1] = Gender
    test_array[0,2] = Height
    test_array[0,3] = Weight
    test_array[0,4] = BMI
    test_array[0,5] = PhysicalActivityLevel

    pred_obes_cate = model.predict(test_array)
    print("predicted obesity category :",pred_obes_cate)

    return pred_obes_cate
