from behave import given, when, then
from src.is_it_friday import is_it_friday


@given('today is Sunday')
def step_given_today_is(context):
     context.today = "Sunday"

@given('today is Friday')
def step_given_today_is(context):
     context.today = "Friday"

@when("I ask whether it's Friday yet")
def step_when_i_ask_whether_its_friday_yet(context):
    context.actual_answer = is_it_friday(context.today)


@then('I should be told "{expected_answer}"')
def step_then_i_should_be_told(context, expected_answer):
    assert context.actual_answer == expected_answer, \
        f"Expected '{expected_answer}', but got '{context.actual_answer}'"
