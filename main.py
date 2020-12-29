from flask import Flask

#creating a flask app and naming it "app"
app = Flask('app')

#Creating a route and a function that corresponds to it that will return "Pinging Model Application!!"
@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

