

class FrequencyAnalyser:

    def __init__(self, window_size: int, hop_size: int) -> None:
        """
        Preconditions:
            0 < hop_size <= window_size.
        Postconditions:
            Window and hop sizes are set to the supplied values.
            No samples or sample rate are stored.
        """
        raise NotImplementedError

    def analyse(
        self, samples: list[float], sample_rate: int
    ) -> list[list[tuple[float, float]]]:
        """
        Preconditions:
            samples contains finite, single-channel audio values
            immediately following the previously supplied samples.
            sample_rate > 0 and is unchanged between reset calls.
        Postconditions:
            Returns one spectrum per completed window, in chronological
            order, following the FFT requirements.
            Each spectrum contains (frequency_hz, magnitude) pairs.
            Returns an empty list if no window is complete.
            Retains samples needed for subsequent windows.
            Stores the sample rate. Does not modify samples.
        """
        raise NotImplementedError

    def reset(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            Clears buffered samples and the stored sample rate.
            Window and hop sizes remain unchanged.
        """
        raise NotImplementedError