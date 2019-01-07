# Created by rajeevnair at 2018-12-22
Feature: Philips User Registration in reference app
  # Enter feature description here

  Scenario: Navigate to user registration screen skipping on-boarding screen
    # Enter steps here
    # Given I set app environment as "testing"
    Then I skip product tour


  Scenario: Set the environment and verify the product tour screens
    Given I set app environment as "staging"
    Then I navigate and verify the product tour
