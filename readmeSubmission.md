[LightMap (Main Branch)](https://github.com/loilipopi/LightMap/tree/main)
## Group Members
[Joe Meritt](https://github.com/loilipopi) (Project Manager)\
Robert Hoang (Designer)\
[Lucas Lu](https://github.com/l-lu2007) (Developer)\
[Kevin Wu](https://github.com/isnxnet) (Developer)\
[Taj Sangra](https://github.com/tajsangra) (Developer)

## Problem Statement
Many video games rely on important audio ques to inform the player of certain actions or opportunities within games which can make them inaccessible or significantly harder to play for individuals who have poor hearing or are deaf. For example, many tactical shooter's bomb defusal gamemodes make distinct and important audio ques to inform the player of when important objectives like the bomb being planted/defused, or opportunities such as footsteps or audio ques of certain character abilities to take advantage of. This task becomes even harder with games that also have music mixed in with these audio ques. Some games have tried to add visual ques to the game along side these audio ques to try and make the game more accessible however, most of these (especially for competitive games) are very limited and provide very little value in comparison. 

# Specification 

## Problem
Individuals with poor hearing cant play video games that make use of important audio ques. These video games become inaccessible or significantly more difficult to play for these individuals. 

## Solution
We want to create a tool where PC audio is captured and processed with a FFT to create a Volume vs Frequency map. In real time, this will correspond to a colour map mapping each peak onto a single colour in which one singular colour is produced. This will then be outputted to either an overlay or an external light.

<img width="955" height="455" alt="image" src="https://github.com/user-attachments/assets/58797190-01c4-4eaa-9415-030f20fd47b4" />
Additionally, the user can create their own custom colour map for whatever scenario and game they want, ideally this should be easy to make but is outside the scope of this project.


For example in a game like Valorant, there is an objective emits a sound periodically which gets faster as it nears the end of the timer. Not being able to hear that sound is detrimental as can't tell how much time is left so what our software will do is take that sound convert it to a colour and output it to the user. 
