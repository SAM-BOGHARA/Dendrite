from app import app 
from app.tasks import get_news_headlines
from flask import Flask,render_template,request
from app import r,q
from time import strftime


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get-news", methods=['GET', 'POST'])
def news():
    jobs = q.jobs
    message = None 

    if request.args:
        stock_input = request.args.get('stock_input')
        task = q.enqueue(get_news_headlines,stock_input)

        jobs = q.jobs

        length_queue = len(q)
        
        message = f"Task Queued at {task.enqueued_at.strftime('%a %d %b %Y %H:%M:%S')}. {length_queue} jobs queued"

        return render_template("index.html" ,message=message,jobs = jobs)

