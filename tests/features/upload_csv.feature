Feature: Upload CSV file

  Scenario: Successfully upload a valid CSV file
    Given I have a CSV file located at "./tests/features/csv/test.csv"
    When I upload the CSV file to the application
    Then the application should respond with status code 200
    Then I should be able to search for number 123456789 the lowest cost is 1.0 for operator Operator A and prefix 1234

  Scenario: Fail to upload an invalid CSV file
    Given I have a CSV file located at "./tests/features/csv/test_invalid"
    When I upload the CSV file to the application
    Then the application should respond with status code 500

  Scenario: No file to upload
    When I upload no file to the application
    Then the application should respond with status code 400
