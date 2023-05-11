from behave import given, when, then
import requests

@given('I have a CSV file located at "{file_path}"')
def step_impl(context, file_path):
    context.csv_path = file_path

@when('I upload the CSV file to the application')
def step_impl(context):
    url = 'http://localhost:5000/upload-csv'
    with open(context.csv_path, 'rb') as file:
        response = requests.post(url, files={'file': file})
    context.response = response

@when('I upload no file to the application')
def step_impl(context):
    url = 'http://localhost:5000/upload-csv'
    response = requests.post(url)
    context.response = response

@then('the application should respond with status code {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('I should be able to search for the lowest cost operator for a given phone number')
def step_impl():
    response = requests.get('http://localhost:5000/find-cheapest-operator/?number=123456789')
    assert response.content == "The cheapest operator for 123456789 is Operator A with cost 1.0 and prefix 1234"
