Feature: Test

  Scenario: Test my bot
    Given bot
    When is_ticket returns OK
    And is_subject returns OK
    And is_problem returns OK
    And is_module returns OK
    Then everything is fine