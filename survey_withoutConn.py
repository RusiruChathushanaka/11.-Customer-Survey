from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
import json
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'SeCrEt'

# Load Translations from JSON files for each language
def load_translations():
    json_path = os.path.join(os.path.dirname(__file__), 'translations.json')
    try:
        with open(json_path,'r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {json_path} does not exist.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {json_path} is not a valid JSON.")
        return {}
    
# Load the translations at startup
QUESTIONS = load_translations()

LANG_FULL_NAMES = {
    "english": "English",
    "hindi": "हिन्दी",
    "spanish": "Español",
    "malay": "Bahasa Melayu",
    "chinese": "中文",
    "indonesian": "Bahasa Indonesia",
    "vietnamese": "Tiếng Việt"
}

class Questionnaire(FlaskForm):
    # Labels will be set in the template. InputRequired messages could also be internationalized.
    q1 = RadioField('Q1', [InputRequired(message="Please select an option.")], choices=[(str(i), str(i)) for i in range(1, 11)])
    q2 = RadioField('Q2', [InputRequired(message="Please select an option.")], choices=[(str(i), str(i)) for i in range(1, 11)])
    q3 = RadioField('Q3', [InputRequired(message="Please select an option.")], choices=[(str(i), str(i)) for i in range(1, 11)])
    q4 = RadioField('Q4', [InputRequired(message="Please select an option.")], choices=[(str(i), str(i)) for i in range(1, 11)])
    q5 = RadioField('Q5', [InputRequired(message="Please select an option.")], choices=[(str(i), str(i)) for i in range(1, 11)])
    q6 = TextAreaField('Q6')



 
@app.route("/<tok>", methods=['GET', 'POST'])
def form_handling(tok):

    selected_lang = request.args.get('lang', 'english')
    if selected_lang not in QUESTIONS:
        selected_lang = 'english' # Fallback

    current_questions = QUESTIONS[selected_lang]
    form = Questionnaire(request.form) # Pass request.form for POST data

    if request.method == 'POST':
        if form.validate_on_submit(): # Validates and checks CSRF
            answer1 = form.q1.data
            answer2 = form.q2.data
            answer3 = form.q3.data
            answer4 = form.q4.data
            answer5 = form.q5.data
            answer6 = form.q6.data
            cus_id = tok
            # Here you would typically save the answers to a database or process them
            flash('Thank you for your submission!', 'success')
            print(f"Answers for {cus_id}:")
            print(f"Q1: {answer1}, Q2: {answer2}, Q3: {answer3}, Q4: {answer4}, Q5: {answer5}, Q6: {answer6}")
            # Redirect to a thank you page or another action

            return redirect(url_for('submit', id=cus_id, lang=selected_lang))
        else:
            pass


    return render_template('index.html',
                           form=form,
                           tok=tok,
                           questions=current_questions,
                           current_lang=selected_lang,
                           all_langs=LANG_FULL_NAMES)

@app.route("/<id>/submit1",methods=['GET','POST'])
def submit(id):
    selected_lang = request.args.get('lang', 'english')
    if selected_lang not in QUESTIONS:
        selected_lang = 'english'

    page_specific_questions = QUESTIONS[selected_lang]

    return render_template('submit.html',
                           customer_id=id,
                           questions=page_specific_questions, # Pass all questions for the selected language
                           current_lang=selected_lang,
                           all_langs=LANG_FULL_NAMES)

@app.route("/<id>/submit2",methods=['GET','POST'])
def alreadysubmit(id):
    selected_lang = request.args.get('lang', 'english')
    if selected_lang not in QUESTIONS:
        selected_lang = 'english'

    page_specific_questions = QUESTIONS[selected_lang]

    return render_template('alreadysubmit.html',
                           customer_id=id,
                           questions=page_specific_questions, # Pass all questions for the selected language
                           current_lang=selected_lang,
                           all_langs=LANG_FULL_NAMES)


if __name__ == "__main__":
    app.run(debug=True)
