Feature: Upload CSV file

  Scenario: Successfully upload a valid CSV file
    Given I have a CSV file located at "./features/csv/test.csv"
    When I upload the CSV file to the application
    Then the application should respond with status code 200
    And I should be able to search for the lowest cost operator for a given phone number

  Scenario: Fail to upload an invalid CSV file
    Given I have a CSV file located at "./features/csv/test_invalid"
    When I upload the CSV file to the application
    Then the application should respond with status code 500

  Scenario: No file to upload
    I upload no file to the application
    Then the application should respond with status code 400
