# LightMap
### Mapping Volume and Frequency to a Colour Map for One Colour Output
A real-time audio visualization system that converts PC audio into a single RGB colour using a customizable 2D colour map.

Capture system audio and compute its frequency spectrum (FFT).

Map frequency and normalized amplitude to RGB values on a 2D colour map.

Combine the sampled colours into one RGB output, updated continuously.

Send the output to a screen, LEDs, or other applications.

## Problem Statement
Many video games rely on important audio ques to inform the player of certain actions or opportunities within games which can make them inaccessible or significantly harder to play for individuals who have poor hearing or are deaf. For example, many tactical shooter's bomb defusal gamemodes make distinct and important audio ques to inform the player of when important objectives like the bomb being planted/defused, or opportunities such as footsteps or audio ques of certain character abilities to take advantage of. This task becomes even harder with games that also have music mixed in with these audio ques. Some games have tried to add visual ques to the game along side these audio ques to try and make the game more accessible however, most of these (especially for competitive games) are very limited and provide very little value in comparison. 



### Other Applications:
Visualize game audio to provide additional feedback for deaf and hard-of-hearing players. The initial RGB output represents the overall audio spectrum; recognizing specific sounds would require further processing.

Other potential applications include music-reactive lighting, desktop visualizations, and RGB device integration.
