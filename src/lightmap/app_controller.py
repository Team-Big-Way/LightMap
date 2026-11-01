from .app_model import AppModel
from .audio_capture import AudioCapture
from .frequency_analyser import FrequencyAnalyser
from .colour_mapper import ColourMapper
from .control_view import ControlView
from .overlay_view import OverlayView


class AppController:
    def __init__(
        self,
        model: AppModel,
        capture: AudioCapture,
        analyser: FrequencyAnalyser,
        mapper: ColourMapper,
    ) -> None:
        """
        Preconditions:
            Components are configured consistently.
            Capture is stopped.
        Postconditions:
            Stores references to the supplied components.
            No views are attached and capture remains stopped.
        """
        raise NotImplementedError

    def set_views(
        self, controls: ControlView, overlay: OverlayView
    ) -> None:
        """
        Preconditions:
            The application has not been closed.
            controls is connected to this controller's callbacks.
        Postconditions:
            Stores references to both views.
            Synchronizes the displayed status with the model.
        """
        raise NotImplementedError

    def start(self) -> None:
        """
        Preconditions:
            Views are attached and the application is not closed.
        Postconditions:
            If already capturing, changes nothing.
            Otherwise, resets the analyser and requests capture
            using on_samples and on_error as callbacks.
            Updates model and displayed status to reflect the outcome.
        """
        raise NotImplementedError

    def stop(self) -> None:
        """
        Preconditions:
            Views are attached and the application is not closed.
        Postconditions:
            Capture is stopped and the analyser is reset.
            Model and displayed capture status are "stopped".
        """
        raise NotImplementedError

    def on_samples(
        self, samples: list[float], sample_rate: int
    ) -> None:
        """
        Preconditions:
            Capture is active.
            Input satisfies FrequencyAnalyser.analyse preconditions.
        Postconditions:
            Samples are passed to the analyser.
            Each returned spectrum is converted to a colour.
            Model and overlay receive the latest resulting colour.
            If no spectrum is returned, the colour is unchanged.
        """
        raise NotImplementedError

    def on_error(self, message: str) -> None:
        """
        Preconditions:
            Views are attached and message is nonempty.
        Postconditions:
            Capture is stopped and the analyser is reset.
            Model and displayed capture status are "error".
            The error message is displayed.
        """
        raise NotImplementedError

    def set_overlay_enabled(self, enabled: bool) -> None:
        """
        Preconditions:
            Views are attached and the application is not closed.
        Postconditions:
            The overlay is visible if enabled, otherwise hidden.
        """
        raise NotImplementedError

    def close(self) -> None:
        """
        Preconditions:
            Views are attached.
        Postconditions:
            Capture is stopped and the analyser is reset.
            Model capture status is "stopped".
            Both views are closed and their resources released.
        """
        raise NotImplementedError