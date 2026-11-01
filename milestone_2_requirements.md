# Milestone 2: Requirements

## Capturing Audio

- 01: When the user presses Start, the application must capture playback audio from the computer's default output device.
- 02: When the user presses Stop, the application shall stop capturing audio.
- 03: Capturing audio shall not interrupt normal audio playback.
- 04: The user shall be able to restart capture after stopping it.
- 05: Capturing audio shall not interrupt the original audio playback.
- 06: The application shall display whether capture is stopped, active, or in an error state.
- 07: There will always only be one capture session active so pressing start twice does not create an additional capture session. (EDIT. HAVING MULTIPLE CAPUTRE SESSIONS TO DISPLAY DIFFERENT COLORS AT THE SAME TIME OULD BE THE MOVE BECAUSE IT WOULDN'T BE MUCH HARDER TO IMPLEMENT)
- 08: Closing the application shall release the audio capture resources.

## FFT to Analyze Audio

- 01: The application shall divide captured audio into analysis windows containing N consecutive samples.
- 02: The application shall apply a Hann window function to each complete analysis window before computing its N-point FFT. (EDIT. the reference waves are dependent on the window size. They are infinitely repeating so smoothing the ends of the chunks would prevent distant leakage but this is not a necessity I don't think)
- 03: Each analysis result shall contain frequency and magnitude pairs for bins k = 0 through floor(N / 2).
- 04: The frequency associated with bin k shall be k × fs / N Hz, where fs is the audio sample rate.
- 05: The magnitude associated with each bin shall be sqrt(real² + imaginary²) / N, where real and imaginary are the components of the unnormalized FFT output.

## Color Mapping

- 01: The application shall include all frequency bins produced by the frequency analysis stage in colour conversion. (EDIT. This is going to be very impractical if the user must choose the color value at every (bucket, amplitude) value on the map. One approach to mitigate this risk is probably to remove the option of custom color maps. This is the trivial solution but I think it might limit our score)
- 02: The amplitudes will be normalized and clamped at a max and min value (TBD). The frequencies will also be clamped but our choice of normalization IS NOT DETERMINED.
- 03: The application shall map included frequencies to horizontal colour-map positions using linear mapping. (EDIT. I think that linear mapping is a bit naive because game frequencies likely do not vary over the entire spectrum which would limit color changes in quite games or games with limited audio variation. IDK though I don't really play video games)
- 04: f sigmoid mapping is selected, its centre frequency c and spread parameter s can be determined by the user which would be a good replacement for custom color maps.

## 
