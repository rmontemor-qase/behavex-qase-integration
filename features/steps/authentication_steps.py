from behave import given, when, then

from src.auth import AuthError, AuthService


def _get_service(context) -> AuthService:
    if not hasattr(context, "auth"):
        context.auth = AuthService()
    return context.auth


@given('the user "{username}" with password "{password}"')
def step_user_with_password(context, username, password):
    context.username = username
    context.password = password
    _get_service(context)


@given("they are logged in")
def step_already_logged_in(context):
    _get_service(context).login(context.username, context.password)


@when("they attempt to log in")
def step_attempt_login(context):
    context.login_error = None
    context.login_message = None
    try:
        context.login_message = _get_service(context).login(
            context.username, context.password
        )
    except AuthError as exc:
        context.login_error = str(exc)


@when("they log out")
def step_logout(context):
    _get_service(context).logout()


@then("the login should succeed")
def step_login_succeeds(context):
    assert context.login_error is None, f"Unexpected error: {context.login_error}"
    assert context.login_message is not None


@then('the login should fail with "{message}"')
def step_login_fails_with(context, message):
    assert context.login_error == message, (
        f"Expected error '{message}', got '{context.login_error}'"
    )


@then('the current user should be "{username}"')
def step_current_user_is(context, username):
    actual = _get_service(context).current_user
    assert actual == username, f"Expected {username}, got {actual}"


@then("no user should be authenticated")
def step_no_user(context):
    assert _get_service(context).is_authenticated is False
