from flask import Flask, render_template, request, redirect, url_for
from forms import QuestionnaireForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        # 将数据写入文本文件
        with open('data/responses.txt', 'a') as f:
            f.write(f"Short-term goal: {form.short_term_goal.data}\n")
            f.write(f"Long-term goal: {form.long_term_goal.data}\n")
            f.write(f"Multiple choice: {form.multiple_choice.data}\n")
            f.write("\n")
        return redirect(url_for('thank_you'))
    return render_template('questionnaire.html', form=form)

@app.route('/thank_you')
def thank_you():
    return "Thank you for your response!"

if __name__ == '__main__':
    app.run(debug=True)
