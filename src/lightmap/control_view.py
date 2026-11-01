"""again this is a view that is probably going to change so these are just
loose placeholders for now."""

from typing import Callable


class ControlView:
    def __init__(
        self,
        on_start: Callable[[], None],
        on_stop: Callable[[], None],
        on_overlay_toggle: Callable[[bool], None],
        on_close: Callable[[], None],
    ) -> None:
        """
        Preconditions:
            All callbacks are callable.
        Postconditions:
            The controls are connected to their callbacks.
            Overlay changes pass True for enabled, False for disabled.
            The window is initially hidden and status is "stopped".
        """
        raise NotImplementedError

    def show(self) -> None:
        """
        Preconditions:
            The view has not been closed.
        Postconditions:
            The control window is visible.
        """
        raise NotImplementedError

    def set_status(self, status: str) -> None:
        """
        Preconditions:
            status is "stopped", "active", or "error".
            The view has not been closed.
        Postconditions:
            The displayed capture status is status.
        """
        raise NotImplementedError

    def show_error(self, message: str) -> None:
        """
        Preconditions:
            message is nonempty.
            The view has not been closed.
        Postconditions:
            The error message is displayed to the user.
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            The window is closed and its resources are released.
            Does not invoke on_close again.
        """
        raise NotImplementedError