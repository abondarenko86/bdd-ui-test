from behave import *
from features.page import *


@given(u'the login page is opened')
def step_impl(context):
    if not LoginPage(context).is_open():
        LoginPage(context).open()


@when(u'I login with existing username and password')
def step_impl(context):
    LoginPage(context).login("stan3@bk.ru", "qwerty123")


@then(u'I should be redirected to the dashboard page')
def step_impl(context):
    assert DashboardPage(context).admin_dropdown().is_displayed()


@given(u'the dashboard page is opened')
def step_impl(context):
    if not DashboardPage(context).is_open():
        LoginPage(context).login("stan3@bk.ru", "qwerty123")


@when(u'I perform log out')
def step_impl(context):
    DashboardPage(context).logout()


@then(u'I should be redirected to login page')
def step_impl(context):
    assert LoginPage(context).is_open()


@when(u'I login with non-existing username and password')
def step_impl(context):
    LoginPage(context).login("non-existing username", "password")


@then(u'A message of incorrect username or password should be displayed')
def step_impl(context):
    assert LoginPage(context).message() == 'You have entered an incorrect username or password.'
