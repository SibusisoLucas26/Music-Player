# Music-Player
Music Player App Readme
Introduction

This is a Python-based music player app built using the Kivy framework and KivyMD for the user interface. The app allows you to play local MP3 files, control playback, and adjust volume.
Features

    Play, pause, skip forward, and skip backward controls.
    Seek slider for adjusting the playback position.
    Timer display showing the elapsed and remaining time.
    Volume slider for adjusting the audio volume.
    Ability to select a directory containing MP3 files to play.
    Spotify and file library links for easy access to music sources.

How to Use

    Launching the App:
        Ensure you have Python installed on your system.
        Run the Python script main.py.
        The app window will appear with controls and an image display.

    Loading Music:
        Click the folder icon in the top right corner to load your music directory.
        Navigate to the directory containing your MP3 files and select it.
        The app will load the MP3 files from the selected directory.

    Controlling Playback:
        Click the play button to start playback.
        Click the pause button to pause playback.
        Click the forward and backward buttons to skip to the next and previous songs, respectively.

    Adjusting Playback Position:
        Use the slider below the timer to adjust the playback position.

    Adjusting Volume:
        Use the volume slider at the bottom to adjust the audio volume.

    Viewing Song Information:
        The name of the currently playing song is displayed at the top.
        The app also displays an image related to the song (if available).

    Timer Display:
        The timer displays the elapsed time on the left and remaining time on the right.

    Accessing Music Sources:
        Click the Spotify icon to open Spotify in your default web browser.
        Click the file library icon to access your local file system.

    Exiting the App:
        Close the app window to exit the application.

Notes

    Make sure you have valid MP3 files in your selected directory for the app to function properly.
    The app uses Kivy for the GUI and SoundLoader for audio playback. Ensure you have the necessary dependencies installed.
    The is a bug with music slider and function to load mp3 display art

Requirements

    Python
    Kivy
    KivyMD

Acknowledgements

This app was created using the Kivy framework and KivyMD library. Special thanks to the developers of these libraries for providing the tools to build this application.
License

This Music Player App is open-source and available under the MIT License. Feel free to modify and use it for your own projects.
