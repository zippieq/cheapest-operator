class OperatorTrie:
    def __init__(self):
        self.root = {}

    def update(self, word, operator_name, cost):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        if '$' not in node:
            node['$'] = {'operator': operator_name, 'min_cost': cost}
        elif cost < node['$']['min_cost']:
            node['$']['operator'] = operator_name
            node['$']['min_cost'] = cost

    def search(self, number):
        node = self.root
        min_cost = None
        operator = None
        prefix = ''
        for char in number:
            if char not in node:
                break
            node = node[char]
            prefix += char
            if '$' in node:
                min_cost = node['$']['min_cost']
                operator = node['$']['operator']
        if prefix == '':
            return None, None, None
        return min_cost, operator, prefix
    def update_from_csv(self, csv_data):
        operator_name = ''
        for row in csv_data:
            if row.startswith('Operator'):
                operator_name = row.rstrip(':,')
                print(operator_name)
            else:
                prefix, cost = row.split(',')
                self.update(prefix.strip(), operator_name, float(cost.strip()))