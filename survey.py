
from email.policy import default

from flask import Flask, render_template, flash, request,redirect, url_for,jsonify
from flask_wtf import FlaskForm
from flask_wtf import Form

from wtforms import StringField, BooleanField, TextAreaField
from wtforms import Form, validators, SubmitField, SelectField 
from wtforms import EmailField,RadioField
# import email_validator

import pyodbc
import pandas as pd
import sqlalchemy as sa
from sqlalchemy.sql import exists   

from flask_cors import CORS
from flask import send_from_directory  



app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SeCrEt'

class Questionnaire(Form):

    ##name = StringField('Name:',[validators.InputRequired()])
    ##email = StringField('Email:',[validators.InputRequired(),validators.Email()])
    q1 = RadioField('How likely are you to recommend the dart global logistics',[validators.InputRequired()],choices=[('1', '1'),('2', '2'), ('3', '3'),('4', '4'), ('5', '5'),('6', '6'), ('7', '7'),('8', '8'), ('9', '9'),('10','10')])
    q2 = RadioField('Service delivery to your expectation',[validators.InputRequired()],choices=[ ('1', '1'),('2', '2'), ('3', '3'),('4', '4'), ('5', '5'),('6', '6'), ('7', '7'),('8', '8'), ('9', '9'),('10','10')])
    q3 = RadioField('Our account manager takes the ownership of your task',[validators.InputRequired()],choices=[ ('1', '1'),('2', '2'), ('3', '3'),('4', '4'), ('5', '5'),('6', '6'), ('7', '7'),('8', '8'), ('9', '9'),('10','10')])
    q4 = RadioField('Our understanding of your service standards',[validators.InputRequired()],choices=[ ('1', '1'),('2', '2'), ('3', '3'),('4', '4'), ('5', '5'),('6', '6'), ('7', '7'),('8', '8'), ('9', '9'),('10','10')])
    q5 = RadioField('Our comprehensive and timely response to your queries',[validators.InputRequired()],choices=[ ('1', '1'),('2', '2'), ('3', '3'),('4', '4'), ('5', '5'),('6', '6'), ('7', '7'),('8', '8'), ('9', '9'),('10','10')])
    q6 = TextAreaField('Please share any additional feedback about your experience')



 
@app.route("/<tok>", methods=['GET', 'POST'])
def form_handling(tok):
    server = 'sqlsrv-01\dglbi,4083' # to specify an alternate port
    database = 'DartCusSurvey' 
    username = 'iislogin' 
    password = 'ASDqwe123##'

    engine = sa.create_engine('mssql+pyodbc://iislogin:ASDqwe123##@sqlsrv-01\dglbi/DartCusSurvey?driver=SQL+Server+Native+Client+11.0')

    user_table = pd.read_sql_table(table_name="CustomerValid_New", con=engine)
    id =user_table['Token'].values 

    
    

    form = Questionnaire(request.form)

   
    answer1= form.q1.data
    answer2= form.q2.data
    answer3 =form.q3.data
    answer4 = form.q4.data
    answer5 = form.q5.data
    answer6 = form.q6.data
    cus_id = tok

    
    respo = pd.read_sql_table(table_name="test_responses_withText", con=engine)
    exist_id =respo['id'].values 
    chck =cus_id in exist_id

    
    
    for id in id:
       
        if id == cus_id:
            if request.method == 'POST':
                if form.validate():

                    if chck ==False: 

                        sql_insert = '''INSERT INTO test_responses_withText(Question1,Question2,Question3,Question4,Question5,Question6,id,SubmitTime) VALUES (?,?,?,?,?,?,?,(convert(datetime,SYSDATETIME(),121)))'''
                        engine.execute(sql_insert,answer1,answer2,answer3,answer4,answer5,answer6,cus_id)
                        return redirect(url_for('submit',id=id))
  

                    else:
                        
                        return redirect(url_for('alreadysubmit',id=id))


  

    return render_template('index.html', form=form,tok=tok)

@app.route("/<id>/submit1",methods=['GET','POST'])
def submit(id):
    id=request.args.get('id')
    return render_template('submit.html')

@app.route("/<id>/submit2",methods=['GET','POST'])
def alreadysubmit(id):
    id=request.args.get('id')
    return render_template('alreadysubmit.html')


if __name__ == "__main__":
    app.run()
