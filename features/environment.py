"""Behave / BehaveX environment hooks.

The Qase formatter is plugged in via the `--format` (behave) or
`--formatter` (behavex) CLI flag, so we don't need to register anything
manually here. These hooks only set up the SUT fixtures shared across
scenarios.
"""

from src.auth import AuthService
from src.calculator import Calculator


def before_scenario(context, scenario):
    context.calculator = Calculator()
    context.auth = AuthService()


def after_scenario(context, scenario):
    context.calculator = None
    context.auth = None
