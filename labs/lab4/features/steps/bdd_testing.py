from behave import *
from unit_testing import *

@given('lab')
def step_first(context):
    context.a = TestBisquare()


@when('discriminant calculates alright')
def check_discriminant(context):
    context.a.test_discriminant()


@when('solve_square gives correct roots')
def check_square(context):
    context.a.test_solve_square()


@when('solve_bisquare gives correct roots')
def check_bisquare(context):
    context.a.test_solve_bisquare()


@then('everything is fine')
def step_last(context):
    pass
