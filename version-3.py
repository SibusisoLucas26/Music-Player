from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton, MDFloatingActionButton
from kivy.core.window import Window
import webbrowser

import os



Builder.load_string('''
<MainScreen>:
    play_button: play_button
    next_button: next_button
    prev_button: prev_button
    current_song_label: current_song_label
    position_slider: position_slider
    position_label: position_label
    timer_label: timer_label
    volume_slider: volume_slider
    song_image_layout: song_image_layout
    song_image: song_image

    ###################################################################################
    MDBoxLayout:                           #Mainscreen layout
        orientation: 'vertical'
        spacing: "4dp"
        padding: "4dp"
        md_bg_color: "#212121"
        size: "300dp", "600dp"
        size_hint: None, None
        ##############################################################################

        MDBoxLayout:
            size: "190dp", "45dp"                               #Layout buttonIcon for Files, Spotify
            size_hint_y: None
           # height: "2dp"
            padding: "0dp"
            md_bg_color: "#1ed760"

            MDIconButton:
                icon: "/home/lucas/Documents/Coding-Projects/Muziq Player/src/spotify.png"
                on_release: root.spotify_link()
                user_font_size: "36sp"
                pos_hint: {"right": 1}

            MDIconButton:
                icon: "/home/lucas/Documents/Coding-Projects/Muziq Player/src/fm.png"
                #on_release: root.spotify_link()
                user_font_size: "36sp"
                pos_hint: {"right": 1}

            MDIconButton:
                size_hint_y: None
                icon: "/home/lucas/Documents/Coding-Projects/Muziq Player/src/library.png"
                user_font_size: "36sp"
                size_hint: None, None
            #    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release: root.show_directory_selection_popup()
        #########################################################################
        MDBoxLayout:
            id: song_image_layout
            size_hint_y: None
            height: "400dp"
            padding: "5dp"
            md_bg_color: "#212121"
            Image:
                id: song_image
                source: "/home/lucas/Documents/Coding-Projects/Muziq Player/src/cd.jpg"
             #   source: "/home/lucas/Downloads/cd.jpg"  # Replace with the path to the default song image
                allow_stretch: True
                keep_ratio: True
        #########################################################################

        MDBoxLayout:                      #Second_layout
            id: button_layout
            padding: "0dp"  # Set padding to zero
            #md_bg_color: "#212222"
            #md_bg_color: "green"
            size: "0dp", "50dp"
            size_hint: 0.5, None
            pos_hint: {"center_x": 0.5, "center_y": 0.5}


            MDIconButton:
                id: prev_button
                text: ""
                icon: "/home/lucas/Documents/Coding-Projects/Muziq Player/src/b.png"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: None, None  # Disable automatic size hint
                size: dp(38), dp(38)
                on_release: root.play_previous_song()
                md_bg_color: 0, 0, 0, 0

            MDIconButton:
                id: play_button
                theme_text_color: "Custom"
                size_hint: None, None  # Disable automatic size hint
                size: dp(38), dp(38)
                icon: "play"
                on_release: root.toggle_play_pause()  # Use a single method to toggle play/pause
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 20}
                md_bg_color: 0, 0, 0, 0



            MDIconButton:
                id: next_button
                text: ""
                icon: "/home/lucas/Documents/Coding-Projects/Muziq Player/src/n.png"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: None, None  # Disable automatic size hint
                size: dp(38), dp(38)
                on_release: root.play_next_song()
                md_bg_color: 0, 0, 0, 0



        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "24dp"
            padding: "4dp"
            md_bg_color:"#535353"

            Label:
                id: current_song_label
                size_hint_y: None
                height: "24dp"

       ################################################### Timer
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "24dp"
            padding: "-44dp"
            md_bg_color: 0, 0, 0, 0

            Label:
                id: position_label
                text: root.format_time(position_slider.value)
                #text: "0:00"
                text_color: 0, 0, 0, 1
                md_bg_color: 0, 0, 0, 0


            Slider:
                id: position_slider
                min: 0
                max: 1
                value: 0
                #value: root.sound.get_pos() if root.sound else 0
                step: 0.01
                size_hint_x: 1  # Set the slider to take up the available horizontal space
                padding: "-35dp"
                on_value_normalized: root.on_slider_change(self.value_normalized)

            Label:
                id: timer_label
                text: '-' + root.format_time(position_slider.max - position_slider.value)
                #text: '0:00'
                text_color: 0, 0, 0, 1
                md_bg_color: 0, 0, 0, 0

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "24dp"
            padding: "4dp"
            md_bg_color:0, 0, 0, 0
        #    size_hint: 0.5, 4
        #    pos_hint: {"center_x": 0.5, "center_y": 4}

        #    Image:
        #        id: song_image
        #        source: "/home/sibusiso/eclipse-workspace/Muziq-Player/music custom/volume.png"
        #        padding: "4dp"
            #    size: "10dp", "25dp"                               #Layout buttonIcon for Files, Spotify
            #    size_hint_y: None

            Slider:
                id: volume_slider
                padding: "4dp"
                size_hint_y: None
                height: "24dp"
                min: 0
                max: 1
                value: 0.5
                step: 0.01
                on_value_normalized: root.on_volume_change(self.value_normalized)



''')

Window.size = (300, 600)


class MainScreen(Screen):
    play_button = ObjectProperty(None)
    pause_button = ObjectProperty(None)
    next_button = ObjectProperty(None)
    prev_button = ObjectProperty(None)
    current_song_label = ObjectProperty(None)
    position_slider = ObjectProperty(None)
    position_label = ObjectProperty(None)
    timer_label = ObjectProperty(None)
    volume_slider = ObjectProperty(None)
    current_song_index = 0

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.directory = None
        self.sound = None
        self.timer = None
        self.mp3_files = []
        self.current_song_index = 0
        self.is_playing = False  # Track the state of the music
        self.last_position = 0  # Track the last position of the music when paused

    def spotify_link(self):
        spotify_link = "https://open.spotify.com/"
        webbrowser.open(spotify_link)

######################################################################### music buttons

    def toggle_play_pause(self):
        if self.sound:
            if self.is_playing:
                self.pause_music()
            else:
                self.play_music()

    def play_music(self):
        if self.directory is None:
            self.show_directory_selection_popup()
        else:
            if len(self.mp3_files) > 0:
                song_path = os.path.join(self.directory, self.mp3_files[self.current_song_index])
                self.sound = SoundLoader.load(song_path)

                if self.sound:
                    if not self.is_playing:
                        #Resume from the last position if it was paused
                        self.sound.seek(self.last_position)


                    self.sound.play()
                    self.is_playing = True
                    self.play_button.icon = "pause"  # Change icon to pause
                    self.current_song_label.text = self.mp3_files[self.current_song_index]
                    self.position_slider.max = self.sound.length
                    self.start_position_update()
                    self.start_timer()

                    self.sound.bind(on_stop=self.play_next_song) ## auto play next song

    def play_next_song(self, instance=None):
        if len(self.mp3_files) > 0:
            self.pause_music()
            self.current_song_index = (self.current_song_index + 1) % len(self.mp3_files)
            self.play_music()

    def play_previous_song(self, instance=None):
        if len(self.mp3_files) > 0:
            self.pause_music()
            self.current_song_index = (self.current_song_index - 1) % len(self.mp3_files)
            self.play_music()

    def pause_music(self):
        if self.sound and self.is_playing:
            self.sound.unbind(on_stop=self.play_next_song)
            self.last_position = self.sound.get_pos()  # Save the current position
            self.sound.stop()
            self.is_playing = False
            self.play_button.icon = "play"  # Change icon to play
            self.stop_timer()

############################################################################# Directory buttons
    def load_mp3_files(self):
        if self.directory:
            self.mp3_files = os.listdir(self.directory)

    def show_directory_selection_popup(self):
        file_chooser = FileChooserListView()
        file_chooser.path = os.path.expanduser('~')

        def select_directory(instance):
            self.directory = file_chooser.path if file_chooser.selection else None
            self.popup.dismiss()
            self.load_mp3_files()
            self.play_music()

        def cancel_selection(instance):
            self.popup.dismiss()

        def back_directory(instance):
            if file_chooser.path != '/':  # Avoid going back beyond the root directory
                file_chooser.path = os.path.dirname(file_chooser.path)

        buttons_layout = BoxLayout(orientation='horizontal')
        select_button = MDFillRoundFlatButton(text="Select", on_release=select_directory, size_hint=(0.1, 0.1))
        cancel_button = MDFillRoundFlatButton(text="Cancel", on_release=cancel_selection, size_hint=(0.1, 0.1))
        back_button = MDFillRoundFlatButton(text="Back", on_release=back_directory, size_hint=(0.1, 0.1))

        buttons_layout.add_widget(select_button)
        buttons_layout.add_widget(cancel_button)
        buttons_layout.add_widget(back_button)

        content = BoxLayout(orientation='vertical')
        content.add_widget(file_chooser)
        content.add_widget(buttons_layout)

        self.popup = Popup(title='Select Music Directory', content=content, size_hint=(0.8, 0.8))
        self.popup.open()
###############################################################################

    def set_song_image(self, image_path):
        self.song_image.source = image_path

############################################################################### Timer def
    def start_position_update(self):
        self.position_update_event = Clock.schedule_interval(self.update_position, 0.1)

    def update_position(self, dt):
     if self.sound and self.is_playing:
        current_position = self.sound.get_pos()
        self.position_slider.value = current_position
        elapsed_time = current_position
        remaining_time = self.sound.length - current_position
        self.update_timer_labels(elapsed_time, remaining_time)
       # self.position_label.text = self.format_time(current_position) ##
        if remaining_time <= 0:
            self.play_next_song()
       # self.update_timer(dt)##

    def on_slider_change(self, value_normalized):
     if self.sound:
        self.sound.seek(value_normalized * self.sound.length)
        current_position = self.sound.get_pos()
        remaining_time = self.sound.length - current_position
        self.update_timer_labels(current_position, remaining_time)

    def start_position_update(self):
        self.position_update_event = Clock.schedule_interval(self.update_position, 0.1)

    def start_timer(self):
        self.stop_timer()
        self.timer = Clock.schedule_interval(self.update_timer, 0.5)

    def check_song_state(self, dt):
        if self.sound and self.sound.state == 'stop':
           self.play_next_song()

    def update_timer(self, dt):
     if self.sound and self.sound.state == 'play':
        current_position = self.sound.get_pos()
        elapsed_time = current_position
        remaining_time = self.sound.length - current_position
        self.update_timer_labels(elapsed_time, remaining_time)

    def update_timer_labels(self, elapsed_time, remaining_time):
        self.position_label.text = self.format_time(elapsed_time)
        self.timer_label.text = "-" + self.format_time(remaining_time)

    #def update_timer_labels(self, elapsed_time, remaining_time):
     #   self.position_label.text = self.format_time(elapsed_time)
      #  self.timer_label.text = self.format_time(remaining_time)

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes}:{seconds:02d}"

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

    def update_timer(self, dt):
        if self.sound and self.sound.state == 'play':
            self.timer_label.text = self.format_time(self.sound.get_pos())

################################################################ volume

    def on_volume_change(self, value):
        if self.sound:
            self.sound.volume = value

#################################################################3 main method
class MusicPlayerApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MusicPlayerApp().run()

