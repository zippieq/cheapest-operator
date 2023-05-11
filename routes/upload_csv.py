from flask import request, current_app, Blueprint

upload_csv_blueprint = Blueprint('upload_csv', __name__)

@upload_csv_blueprint.route('/upload-csv', methods=['POST'])
def upload_csv():
    trie = current_app.config['trie']
    # Ensure that a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded.', 400
    
    csv_file = request.files['file']
    
    # Read the file into memory
    csv_file.seek(0)
    csv_data = csv_file.read().decode('utf-8').splitlines()
    
    # Update the trie
    try:
        trie.update_from_csv(csv_data)
    except Exception as e:
        return f'Error updating trie: {str(e)}', 500
    
    return 'CSV uploaded successfully.', 200