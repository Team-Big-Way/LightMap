## Problem
Individuals with poor hearing cant play video games that make use of important audio ques. These video games become inaccessible or significantly more difficult to play for these individuals. 

## Solution
We want to create a tool where PC audio is captured and processed with a FFT to create a Volume vs Frequency map. In real time, this will correspond to a colour map mapping each peak onto a single colour in which one singular colour is produced. This will then be outputted to either an overlay or an external light.

<img width="955" height="455" alt="image" src="https://github.com/user-attachments/assets/58797190-01c4-4eaa-9415-030f20fd47b4" />
Additionally, the user can create their own custom colour map for whatever scenario and game they want, ideally this should be easy to make but is outside the scope of this project.

For example in a game like Valorant the bomb emits a sound periodically which gets faster as it nears the end of the timer. Not being able to hear that sound is determinantal as can't tell how much time is left so what our software will do is take that sound convert it to a colour and output it to the user. 
