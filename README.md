# FRUIT = FIRST Robotics Uploader from an Indiana Teammate
A python script (with GUI) for the automated processing of (long) livestream recordings into (short) match videos.

## How it works
1. Gets information about the matches from FIRST, includes start time and score post time
2. Splits the livestream recording into chucks based on those start & post times
3. Combines those chunks together into match videos
4. Generates a thumbnail using the match number and teams involved
5. Uploads the videos to YouTube

## Upcoming Features
- [ ] Blue Alliance Support
- [ ] Use Twitch instead of a file for input
- [ ] Realtime OBS file for input
- [ ] Better handling of erroneous inputs
- [ ] Cool logo
