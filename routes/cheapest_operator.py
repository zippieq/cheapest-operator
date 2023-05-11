from flask import request, Blueprint, current_app
cheapest_operator_blueprint = Blueprint('cheapest_operator', __name__)

@cheapest_operator_blueprint.route('/find-cheapest-operator', methods=['GET'])
def find_cheapest_operator():
    number = request.args.get('number')
    trie = current_app.config['trie']
    min_cost, operator, prefix = trie.search(number)
    if operator:
        return f'The cheapest operator for {number} is {operator} with cost {min_cost} and prefix {prefix}'
    else:
        return f'No operator found for {number}.'
