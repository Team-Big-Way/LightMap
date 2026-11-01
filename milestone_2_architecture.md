# Milestone 2: Architecture

## Notes

The architecture follows Model–View–Controller, with separate services for audio capture, frequency analysis, and colour conversion. This is a reflection of our requirements and specifications documents so any changes to those documents must also be applied here. 

## Components

### AppModel: Model

**Responsibility:** Store capture status, processing settings, and the latest output colour.

**Location:** Client only.

**Communication:**
- AppController updates capture status, settings, and output colour.
- AppController retrieves these values to update the views.

### AppController: Controller

**Responsibility:** Handle user actions and coordinate the audio processing pipeline.

**Location:** Client only.

**Communication:**
- Receives Start, Stop, and overlay enable/disable requests from ControlView.
- Requests AudioCapture to start or stop capture.
- Receives captured audio samples and their sample rate from AudioCapture.
- Supplies samples and their sample rate to FrequencyAnalyser.
- Supplies the resulting frequency–magnitude pairs to ColourMapper.
- Updates AppModel with capture status, settings, and the latest output colour.
- Supplies capture status and error messages to ControlView.
- Supplies output colours and visibility commands to OverlayView.

### ControlView: View

**Responsibility:** Display application controls, capture status, and error messages.

**Location:** Client only.

**Communication:**
- Sends Start, Stop, and overlay enable/disable requests to AppController.
- Receives capture status and error messages from AppController.

### OverlayView: View

**Responsibility:** Display the latest output colour over the game.

**Location:** Client only.

**Communication:**
- Receives an RGB colour from AppController.
- Receives show and hide commands from AppController.

### AudioCapture: Model

**Responsibility:** Capture playback audio from the computer's default output device.

**Location:** Client only.

**Communication:**
- Receives start and stop requests from AppController.
- Supplies captured samples in chronological order and their sample rate to AppController.
- Reports capture failures to AppController.

### FrequencyAnalyser: Controller

**Responsibility:** Buffer audio samples into analysis windows and compute their frequency spectra using FFT.

**Location:** Client only.

**Communication:**
- Receives audio samples and their sample rate from AppController.
- Receives analysis settings, including window size and hop size, from AppController.
- Returns frequency–magnitude pairs for each completed analysis window to AppController.
- Receives reset requests from AppController to discard buffered samples between capture sessions.

### ColourMapper: Controller

**Responsibility:** Convert frequency–magnitude pairs into colours using the predefined colour map and combine them into one output colour.

**Location:** Client only.

**Communication:**
- Receives frequency–magnitude pairs and colour-mapping settings from AppController.
- Returns one RGB colour per analysis result to AppController.
