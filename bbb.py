from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def redirect_to_app():
    upi_app = request.args.get('upiApp')
    upi_id = request.args.get('upiId')
    # If you want to redirect to an external URL, use `redirect()`
    # return redirect(f"{upi_app}?id={upi_id}")
    return render_template('redirect.html', upi_app=upi_app, upi_id=upi_id)

if __name__ == '__main__':
    app.run(debug=True)
