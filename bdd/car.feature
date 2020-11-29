# Created by ansumanroy at 28/11/20
Feature: Speed
  # Checking Speed validation of the Car Object

  Scenario: Valid speed
    Given Speed is less than 160
    When Accelerated
    Then Speed is valid

  Scenario: Invalid speed
    Given Speed is more than 160
    When Accelerated
    Then Speed is invalid