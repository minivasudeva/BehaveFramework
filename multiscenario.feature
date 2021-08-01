Feature: mult scen
  Scenario: test one data
    Given I am on mission humane page
    When I search for the first state
    Then AP is listed

  Scenario: test district samp
    Given I am on mission humane page
    When I click first state
    Then anatapur is listed as first district 