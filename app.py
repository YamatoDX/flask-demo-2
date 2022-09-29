from flask import Flask, request
import base64
from io import BytesIO
from matplotlib.figure import Figure
app = Flask(__name__)

allData = {
    "D03":{
        "name":"Shadman Martin Piyal",
        "roll":"D03",
        "totalMarks":450
    },
    "D02":{
        "name":"Tanbeer Islam Shukhan",
        "roll":"D02",
        "totalMarks":500
    },
    "D01":{
        "name":"Jariful Ahmed",
        "roll":"D01",
        "totalMarks":700
    }
}

@app.route("/")
def HomePage():
    return f'<h1 style="color:red;text-align:center;">This is the home page </p>'

@app.route("/getAllStudents", methods = ["GET"])
def getStudents():
    return allData

@app.route('/getStudentInfo', methods = ["GET"])
def getStudentInfo():
    if("studentId" not in list(request.args)):
        return "studentId has to be provided in the query string"
    studentId = request.args["studentId"]
    if(studentId == "" or isinstance(studentId, str) == False):
        return "The provided studentId is invalid"
    if(studentId not in list(allData.keys())):
        return {}
    return allData[studentId]

@app.route("/postStudentInfo", methods = ["POST"])
def postStudentInfo():
    requestBody = request.get_json()
    allRequiredFields = ["name","roll", "totalMarks"]
    allinputFields = list(requestBody.keys())
    for each in allRequiredFields:
        if(each not in allinputFields):
            return "name, roll, totalMarks has to be provided" 
    name = requestBody["name"]
    roll = requestBody["roll"]
    totalMarks = requestBody["totalMarks"]
    if(isinstance(name, str) == False or isinstance(roll, str) == False or isinstance(totalMarks, int) == False):
        return "name, roll has to be string and totalMarks has to be integer value"
    if(name == "" or roll == "" or totalMarks <= 0):
        return "name , roll cannot be empty string and totalMarks has to greater than zero"
    allData[roll] = {
        "name": name,
        "roll": roll,
        "totalMarks": totalMarks
    }
    return allData

@app.route("/getImage")
def getImage():
    fig = Figure()
    ax = fig.subplots()
    x = [i for i in range(1,100,1)]
    y = list(map(lambda current: current ** 3, x))
    ax.plot(x,y, color = "red", label = "heat Values")
    ax.set_title("Hello world")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    fig.legend()
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

@app.route("/getImageByData", methods = ["POST"])
def getImageByData():
    requestBody = request.get_json()
    if("x_values" not in list(requestBody.keys())):
        return "x_values has to be provided"
    x = requestBody["x_values"]
    y = list(map(lambda each: each ** 3, x))
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x,y, color = "red", label = "heat Values")
    ax.set_title("Hello world")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    fig.legend()
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

def graphFunction(functionType, inputValue):
    if(functionType == "linear"):
        return inputValue
    elif(functionType == "square"):
        return int(inputValue) ** 2
    else:
        return int(inputValue) ** 3

@app.route("/getGraph", methods = ["POST"])
def getGraph():
    requestBody = request.get_json()
    print(f'requestBody is {requestBody}')
    start = requestBody["start"]
    end = requestBody["end"]
    increment = requestBody["increment"]
    inputFunctionType = requestBody["inputFunction"]
    x = [i for i in range(start, end + 1, increment)]
    y = list(map(lambda each: graphFunction(inputFunctionType, each), x))
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x,y, color = "red", label = "heat Values")
    ax.set_title("Hello world")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    fig.legend()
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data;
    # return f"<img src='data:image/png;base64,{data}'/>"

if (__name__ == "__main__"):
    app.run(debug = True, port = 5000)
