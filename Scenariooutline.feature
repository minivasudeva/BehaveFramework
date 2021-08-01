Feature:scenario outline.

  Scenario Outline: test
    Given I am on home page
    When I click state "<state>"
    And I click district "<district>"
    And I click resource "<resource>"
    Then compare text "<text_value>"
    Examples:
      |state  |district |resource |text_value|
      |Andhra Pradesh |Anantapur |OXYGEN |The scare of running out of oxygen during this pandemic is hitting ATP like all the states across India. URGENT help for OXYGEN supply to Anantapur OxygenShortage Emergency|
      |Andhra Pradesh |Anantapur |OXYGEN |The scare of1 running out of oxygen during this pandemic is hitting ATP like all the states across India. URGENT help for OXYGEN supply to Anantapur OxygenShortage Emergency|

#      |Chandigarh  |Chandigarh |Oxygen |Oxygen available. Oxygen available. Call tel: 9654078988, Chandigarh