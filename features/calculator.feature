Feature: Calculator
  As a user of the calculator
  I want to perform basic arithmetic operations
  So that I can trust the results

  Background:
    Given a fresh calculator

  @qase.id:1
  @qase.suite:Calculator
  @qase.fields:{"severity":"normal","priority":"high","layer":"unit"}
  Scenario: Adding two positive numbers
    When I add 2
    And I add 3
    Then the displayed value should be 5

  @qase.id:2
  @qase.suite:Calculator
  @qase.fields:{"severity":"normal","priority":"medium","layer":"unit"}
  Scenario: Subtracting a number
    When I add 10
    And I subtract 4
    Then the displayed value should be 6

  @qase.id:3
  @qase.suite:Calculator
  @qase.fields:{"severity":"critical","priority":"high","layer":"unit"}
  Scenario: Dividing by zero raises an error
    When I add 8
    Then dividing by 0 should raise an error

  @qase.id:4
  @qase.suite:Calculator
  Scenario Outline: Multiplication with several inputs
    When I add <start>
    And I multiply by <factor>
    Then the displayed value should be <result>

    Examples:
      | start | factor | result |
      | 2     | 3      | 6      |
      | 5     | 4      | 20     |
      | 7     | 0      | 0      |

  @qase.ignore
  Scenario: Work-in-progress scientific mode
    Given this test is not ready
    Then it should not be reported
