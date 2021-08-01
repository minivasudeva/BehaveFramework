Feature: backg feat
  Background: Same steps
    Given I am on mission humane page

  Scenario: test data check
#    Given I am on mission humane page
    When I search for the first state
    Then AP is listed

  Scenario: test district
#    Given I am on mission humane page
    When I click first state
    Then anatapur is listed as first district 