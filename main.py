from flask import Flask,jsonify,request

#constructor of the flask
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'number':u'9493249084',
        'name':u'bobby',
        'done':False,
    },
    {
        'id':2,
        'number': u'8082692542',
        'name': u'chrissy',
        'done': False,
    }
]

@app.route("/lani")
def helloWorld():
    return "Hello World"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'number':request.json['number'],
        'name':request.json.get('name',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({"data":tasks})

if __name__=="__main__":
    app.run()
