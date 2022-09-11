# Dendrite.AI 


## Programming Language : Python
### Framework : Flask
### Database : Redis

## After Downloading Steps to Run
First step is important since windows does not support "fork" and AttributeError will arise.

`$ pip install git+https://github.com/michaelbrooks/rq-win.git#egg=rq-win`

#### Now Starting redis Server`
`$ redis-server --port 6380`

#### Now starting redis worker process
`$ rqworker -w rq_win.WindowsWorker`

#### Now running Flask server 
`$ flask run`

