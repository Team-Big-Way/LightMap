class ColourMapper:
    def __init__(self, settings: dict[str, float]) -> None:
        """
        Preconditions:
            settings satisfies the colour-mapping design specification.
        Postconditions:
            The mapper is configured using a copy of settings.
            The supplied settings are unchanged.
        """
        raise NotImplementedError

    def map_colour(
        self, spectrum: list[tuple[float, float]]
    ) -> tuple[int, int, int]:
        """
        Preconditions:
            spectrum is nonempty.
            Each pair contains a finite, nonnegative frequency
            and a finite, nonnegative magnitude.
        Postconditions:
            Returns (red, green, blue), each an integer from 0 to 255,
            following the colour-mapping requirements.
            spectrum and the mapper's settings are unchanged.
        """
        raise NotImplementedError