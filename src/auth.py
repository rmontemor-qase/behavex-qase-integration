"""In-memory authentication service used as a system-under-test."""

from dataclasses import dataclass, field


class AuthError(Exception):
    """Raised when authentication fails."""


@dataclass
class AuthService:
    _users: dict[str, str] = field(
        default_factory=lambda: {"alice": "wonderland", "bob": "builder"}
    )
    _current_user: str | None = None

    def login(self, username: str, password: str) -> str:
        expected = self._users.get(username)
        if expected is None or expected != password:
            raise AuthError("Invalid credentials")
        self._current_user = username
        return f"Welcome, {username}!"

    def logout(self) -> None:
        self._current_user = None

    @property
    def current_user(self) -> str | None:
        return self._current_user

    @property
    def is_authenticated(self) -> bool:
        return self._current_user is not None
