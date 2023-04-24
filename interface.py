from flask  import Flask,jsonify,request,render_template
import config
app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('Welcome to flask')
    return 'Hello flask'


from project_app.utils import LoanApprovalPrediction
@app.route('/predicted_charges')
def get_loan_approval_prediction():
    data = request.form
    Gender = data['Gender']
    Married = data['Married']
    Dependents = data['Dependents']
    Education = data['Education']
    Self_Employed = data['Self_Employed']

    ApplicantIncome = eval(data['ApplicantIncome'])
    CoapplicantIncome = eval(data['CoapplicantIncome'])
    LoanAmount = eval(data['LoanAmount'])
    Loan_Amount_Term = eval(data['Loan_Amount_Term'])
    Credit_History = eval(data['Credit_History'])
    Property_Area = data['Property_Area']


    result_prediction = LoanApprovalPrediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
    loan = result_prediction.get_loan_approval_prediction()
    return jsonify ({'Result':f"Loan Approval prediction is : {loan}"})
app.run()
