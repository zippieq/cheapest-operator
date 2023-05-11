Phone Number Routing
Introduction
The Phone Number Routing is a service that finds the lowest cost operator for a given phone number. The service accepts a CSV file containing the operator costs for different phone number prefixes and stores the data in a Trie data structure. The Trie data structure is then used to efficiently search for the lowest cost operator for a given phone number.

Solution Overview
The solution consists of a Flask web application that exposes REST APIs to upload the CSV file and search for the lowest cost operator for a given phone number. The web application uses a Trie data structure to efficiently search for the lowest cost operator for a given phone number.

Running the Application
To run the application, follow these steps:

Install Python 3.11.2 and pip on your machine.
Clone the repository to your local machine.
Install the required Python packages by running pip install -r requirements.txt.
Start the Flask application by running python app.py.
Upload a CSV file by sending a POST request to http://localhost:5000/upload_csv/ with the CSV file in the csv_file parameter.
Search for the lowest cost operator for a given phone number by sending a GET request to http://localhost:5000/find-cheapest-operator?number=<phone_number>

Next Steps
To implement the solution as a scalable solution using AWS API Gateway, Elasticsearch, and Lambda function, S3
