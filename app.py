from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(255),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task {}>'.format(self.id)



@app.route('/', methods=['GET', 'POST'])
def  index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
        except:
            return 'Issue in Post CodeBlock'
    else:
        pass

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)