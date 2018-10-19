from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/") #annotation tells the URL that will amek this function run
def render_main():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    return render_template('page1.html')

@app.route("/page2")
def render_page2():
    return render_template('page2.html')

@app.route("/page3")
def render_page3():
    return render_template('page3.html')

@app.route("/responsemc")
def render_responsemc():
    bom = float(request.args['mk'])
    ans = bom * 1.609
    return render_template('responsemc.html', response=str(bom) + 'miles' + ' ' + '=' + ' ' + str(ans) + 'km')

@app.route("/responseUSD")
def render_responseUSD():
    bom = float(request.args['USD'])
    ans = bom * 0.80
    return render_template('responseUSD.html', response=str(bom) + str(ans) + 'EUR')

@app.route("/responseLBKG")
def render_responseLBKG():
    bom = float(request.args['Lbs'])
    ans = bom / 2.205
    return render_template('responseLBKG.html', response=str(bom) + str(ans) + 'kg')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
