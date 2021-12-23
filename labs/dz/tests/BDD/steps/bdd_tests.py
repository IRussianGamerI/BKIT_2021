from behave import *

from tests.TDD.tdd_tests import *


@given('bot')
def step_first(context):
    context.a = Test()


@when("is_ticket returns OK")
def test_is_ticket(context):
    context.a.test_ticket()


@step("is_subject returns OK")
def test_is_subject(context):
    context.a.test_subject()


@step("is_problem returns OK")
def test_is_problem(context):
    context.a.test_problem()


@step("is_module returns OK")
def step_impl(context):
    context.a.test_module()


@then("everything is fine")
def step_last(context):
    pass
