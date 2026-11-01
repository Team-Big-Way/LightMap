class AppModel:
    """Store application state."""

    def __init__(self) -> None:
        """
        Preconditions: 
            None.
        Postconditions:
            capture_status is "stopped".
            settings is an empty dictionary.
            output_colour is black, represented as (0, 0, 0).
        """
        self.capture_status: str = "stopped"
        self.settings: dict[str, float] = {}
        self.output_colour: tuple[int, int, int] = (0, 0, 0)