from flask import Flask
from utils.trie import Trie

app = Flask(__name__)
app.config['trie'] = Trie()

if __name__ == '__main__':
    app.run(debug=True)
