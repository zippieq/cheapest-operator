from flask import Blueprint, request, current_app

upload_csv_blueprint = Blueprint('upload_csv', __name__)
current_app.register_blueprint(upload_csv_blueprint)

def read_csv_file(file):
    for row in file.read().decode('utf-8').splitlines():
        yield row.split(',')

@upload_csv_blueprint.route('/upload-csv', methods=['POST'])
def upload_csv():
    trie = current_app.trie
    csv_file = request.files['file']
    csv_file.seek(0)
    operator_name = ''
    for row in read_csv_file(csv_file):
        if row[0].startswith('Operator'):
            operator_name = row[0].strip(':')
        else:
            prefix = row[0].strip()
            cost = float(row[1].strip())
            trie.insert(prefix, operator_name, cost)
    return 'CSV uploaded successfully.'
