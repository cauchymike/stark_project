from flask import Flask, url_for, render_template, redirect
from forms import JobForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seunmelody-is-my-secret-key'

##################################################################################
#view section
#################################################################################

@app.route('/', methods = ('GET', 'POST'))
def jobformm():
    return  render_template("index.html")

#we can also simply return render_template from the above view function 
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(threaded = True)



