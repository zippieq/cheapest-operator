from flask import Flask
from utils.trie import OperatorTrie
from routes.cheapest_operator import cheapest_operator_blueprint
from routes.upload_csv import upload_csv_blueprint

app = Flask(__name__)
app.config['trie'] = OperatorTrie()
app.register_blueprint(cheapest_operator_blueprint)
app.register_blueprint(upload_csv_blueprint)
if __name__ == '__main__':
    app.run(debug=True)
