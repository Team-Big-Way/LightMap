"""To be honest the display is probably going to change so this is just
What I thought was a simple placeholder for now."""

class OverlayView:
    def __init__(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            The overlay is hidden and its colour is black.
        """
        raise NotImplementedError

    def set_colour(self, colour: tuple[int, int, int]) -> None:
        """
        Preconditions:
            colour contains three integers from 0 to 255.
        Postconditions:
            The overlay's colour is set to colour.
            Its visibility is unchanged.
        """
        raise NotImplementedError

    def show(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            The overlay is visible and displays its current colour.
        """
        raise NotImplementedError

    def hide(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            The overlay is hidden.
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            The overlay is closed and its resources are released.
        """
        raise NotImplementedError