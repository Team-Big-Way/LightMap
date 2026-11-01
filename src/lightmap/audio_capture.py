from typing import Callable


class AudioCapture:
    def __init__(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            Audio capture is stopped.
        """
        raise NotImplementedError

    def start(
        self,
        on_samples: Callable[[list[float], int], None],
        on_error: Callable[[str], None],
    ) -> None:
        """
        Preconditions:
            Both callbacks are callable.
        Postconditions:
            If already capturing, the existing session is unchanged.
            Otherwise, begins capturing the default output device.

            During capture, on_samples receives chronological,
            single-channel sample batches and their sample rate.
            The sample rate remains constant within the session.

            If capture fails, capture is stopped and on_error
            receives an error message.
            Original audio playback is not interrupted.
        """
        raise NotImplementedError

    def stop(self) -> None:
        """
        Preconditions:
            None.
        Postconditions:
            Capture is stopped and capture resources are released.
            No further callbacks occur after this method returns.
        """
        raise NotImplementedError