from flask import Flask, render_template, request

app = Flask(__name__)


# Make a homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [ "1. Roses","2. Iris", "3.Carnation", "4. Orchid", "5.Daffodil"]
    
    return render_template('name.html', name=name, nameList = listOfNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

# Add the option to run this file directly
if __name__== "__main__":
    app.run(debug=True)