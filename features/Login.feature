Feature:
  As a Bynder user I want to be able login and logout to Bynder portal

  Scenario: Valid log in
    Given the login page is opened
    When I login with existing username and password
    Then I should be redirected to the dashboard page

  Scenario: Logout
    Given the dashboard page is opened
    When I perform log out
    Then I should be redirected to login page

  Scenario: Log in with non-existing username and password
    Given the login page is opened
    When I login with non-existing username and password
    Then A message of incorrect username or password should be displayed