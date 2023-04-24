import config
import pickle
import json
import numpy as np
class LoanApprovalPrediction():
    def __init__(self,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        self.Gender = Gender
        self.Married = Married
        self.Dependents = Dependents
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area = 'Property_Area_'+Property_Area
        
    
    def load_model(self):
        with open(config.model_file_path,'rb') as f:
            self.model = pickle.load(f) # model file instance is created because we have to use it further

        with open(config.json_file_path,'r') as f:
            self.json_data = json.load(f)  # it contain label encoded data and columns names

    def get_loan_approval_prediction(self):
        self.load_model() # above function call here because we are going to use methods here
        Property_Area_index = self.json_data['columns'].index(self.Property_Area)
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.json_data['Gender'][self.Gender]
        test_array[1] = self.json_data['Married'][self.Married]
        test_array[2] = self.json_data['Education'][self.Education]
        test_array[3] = self.json_data['Self_Employed'][self.Self_Employed]
        test_array[4] = self.ApplicantIncome
        test_array[5] = self.CoapplicantIncome
        test_array[6] = self.LoanAmount
        test_array[7] = self.Loan_Amount_Term
        test_array[8] = self.Credit_History
        test_array[Property_Area_index] = 1
        
        predicted_charges = self.model.predict([test_array])
        return predicted_charges

