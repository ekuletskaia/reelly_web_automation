# Created by elena.kuletsky at 5/29/2024
Feature: Off-plan tests

  Background:
    Given Open the main page
    When Login into the page with email: e.kuletskaia@gmail.com and password: !cdf9czA@F!zut5

  Scenario: User can filter the off plan products by Unit price range
    When Click on “off plan” at the left side menu
    Then Verify the right page opens
    When Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range (1200000 - 2000000)