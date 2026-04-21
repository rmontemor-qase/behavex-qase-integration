Feature: Authentication
  As a registered user
  I want to log in and out of the system
  So that I can access protected resources

  @qase.id:5
  @qase.suite:Authentication
  @qase.fields:{"severity":"critical","priority":"high","layer":"e2e"}
  Scenario: User can log in with valid credentials
    Given the user "alice" with password "wonderland"
    When they attempt to log in
    Then the login should succeed
    And the current user should be "alice"

  @qase.id:6
  @qase.suite:Authentication
  @qase.fields:{"severity":"critical","priority":"high","layer":"e2e"}
  Scenario: User cannot log in with invalid credentials
    Given the user "alice" with password "not-my-password"
    When they attempt to log in
    Then the login should fail with "Invalid credentials"

  @qase.id:7
  @qase.suite:Authentication
  @qase.fields:{"severity":"normal","priority":"medium","layer":"e2e"}
  Scenario: Logged-in user can log out
    Given the user "bob" with password "builder"
    And they are logged in
    When they log out
    Then no user should be authenticated
