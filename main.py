from flask import Flask, jsonify, render_template, json
from flask import request

app = Flask('app')

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/test')
def test_page():
    return render_template ('test.html')


@app.route('/chats/suti', methods = ["POST"])
def suti_zinu():
    dati = request.json 
    with open("chats.txt", "a", newline="") as f :
        f.write(dati["chats"]+"\n") 
    return ielasit_chatu() 

@app.route('/chats/lasi')
def ielasit_chatu():
    chata_rindas = []
    with open("chats.txt", "r") as f :
        for rinda in f :
            chata_rindas.append(rinda)
    return jsonify({"chats" : chata_rindas})



if __name__ == '__main__' :
    app.run(threaded= True, port= 5000) 
