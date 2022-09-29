import json
import base64
from io import BytesIO
from matplotlib.figure import Figure

def lambda_handler(event, context):
    if("x_values" not in list(event.keys())):
        return {
            "statusCode":400,
            'body': json.dumps("x_values has to be provided")
        }
    x = list(event["x_values"])
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
    finalResult = f"<img src='data:image/png;base64,{data}'/>"
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        "finalResult": finalResult
    }
