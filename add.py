from flask import Flask
from flask import request




app = Flask(__name__)
app.config['SECRET_KEY'] = '1111'


@app.route('/', methods = ['GET','POST'])
def hello():
    return 'hello api works hello'

@app.route('/multiple', methods = ['GET','POST'])

def multiple():
    num1 = request.args.get('n1')
    num2 = request.args.get('n2')
    result = int(num1) * int(num2)
    print(result)
    return str(result)

@app.route('/divide', methods = ['GET','POST'])

def divide():
    num1 = request.args.get('n1')
    num2 = request.args.get('n2')
    result = int(num1) / int(num2)
    print(result)
    return str(result)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)