from flask import Flask, app



@app.route("/", methods=["GET"])
def index():
    return ""

if __name__=='__main__':
    app.run(debug=True)


