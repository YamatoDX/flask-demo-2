from flask import Flask, request
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

if (__name__ == "__main__"):
    app.run(debug = True, port = 5000)
