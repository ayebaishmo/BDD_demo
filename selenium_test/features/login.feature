Feature: Login functionality
  As a registered user
  I want to log in to the system
  So that I can access my personal dashboard and features

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid email and password
    And clicks the login button
    Then the user should be redirected to the dashboard
    And see a welcome message