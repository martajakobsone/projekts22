from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/test')
def test_page():
    return render_template ('test.html')




if __name__ == '__main__' :
    app.run(threaded= True, port= 5000) 
