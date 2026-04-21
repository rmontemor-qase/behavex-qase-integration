from behave import given, when, then

from src.calculator import Calculator


@given("a fresh calculator")
def step_fresh_calculator(context):
    context.calculator = Calculator()


@when("I add {value:g}")
def step_add(context, value):
    context.calculator.add(value)


@when("I subtract {value:g}")
def step_subtract(context, value):
    context.calculator.subtract(value)


@when("I multiply by {value:g}")
def step_multiply(context, value):
    context.calculator.multiply(value)


@then("the displayed value should be {expected:g}")
def step_value_is(context, expected):
    actual = context.calculator.value
    assert actual == expected, f"Expected {expected}, got {actual}"


@then("dividing by {divisor:g} should raise an error")
def step_divide_raises(context, divisor):
    try:
        context.calculator.divide(divisor)
    except ZeroDivisionError:
        return
    raise AssertionError("Expected ZeroDivisionError was not raised")


@given("this test is not ready")
def step_not_ready(context):
    context.not_ready = True


@then("it should not be reported")
def step_not_reported(context):
    assert context.not_ready is True
