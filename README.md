# BodPlay

Leverages your webcam to identify ongoing motion to play your music as you move. "Jukebox takes dancing as payment"

Inspires people to dance and get rewarded with awesome tunes straight from your own Itunes playlist, but stop dancing and the music stops with you.

We were inspired to create this project after learning about the consequences of sitting for long periods of time. Unfortunately, many office jobs require employees to sit at their desks throughout the entire workday, which has been proven to negatively affect the health of the employees. On the contrary, dancing has been proven to have tons of benefts, including benefits to overall health, confidence, and productivity.

We hope our product can be implemented in 
  - offices, to get employees to have a quick stretch and workout in order to keep the office music playing.
  - dance classes to keep everyone dancing and motivating participants to keep dancing in order to not stop the music.
  - charities such as Dance Marathon which are based on having volunteers dance throughout 24 hours in order to raise money, this product can enforce that the volunteers are consistantly dancing and bring confidence to donators.



BodPlay is powered by Python, using OpenCv to access the webcam, and Itunes commands to power the music.

------------------------------------------------------How it works?------------------------------------------------------
  We are converting every frame to grayscale and comparing each frame with the previous one in order to see if the amount of black pixels changed, if so, that means that there has been a change between frames, which would represent a movement, and would keep the music playing.
  
  To make our product run smoothly, we implemented a counter that checks if there has been no movement during five frames, and then plays music if it has exceeded five frames of no movement, which is equivalent to around 1-2 seconds.
  
  
  
