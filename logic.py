from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from gui import *
from pygame import *


class Logic(QMainWindow,Ui_MainWindow):
    """
    A class representing the functions of a music playlist
    """
    def __init__(self) -> None:
        """
        Method to set default values of playlist and connect gui buttons to logic
        """
        super().__init__()
        self.__songTitle = None
        self.setupUi(self)


        self.__album_images = ['Images/evermore.jpg', 'Images/folklore.jpg', 'Images/Lover.jpg',
                             'Images/Red.jpg', 'Images/Reputation.jpg']

        self.__songTitles = ['long story short by Taylor Swift', 'the lakes by Taylor Swift', 'Cornelia Street by Taylor Swift',
                           'Holy ground by Taylor Swift', 'Call it what you want by Taylor Swift']

        self.__songSounds = ['Music/longstoryshort.mp3', 'Music/thelakes.mp3', 'Music/CorneliaStreet.mp3',
                           'Music/HolyGround.mp3', 'Music/CallItWhatYouWant.mp3']

        self.__volume = 0
        self.__song_num = 1
        mixer.init()
        mixer.music.set_volume(self.__volume)
        #https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

        self.playButton.clicked.connect(lambda: self.play())
        self.skipButton.clicked.connect(lambda: self.skip())
        self.reverseButton.clicked.connect(lambda: self.reverse())
        self.Volume_downButton.clicked.connect(lambda: self.volume_down())
        self.Volume_upButton.clicked.connect(lambda: self.volume_up())

    def set_album_image(self, song_num: int) -> None:
        """
        Method to display image of song album
        :param song_num: Represents which song's image should be displayed. Should be between 1 and the length of the
                         album_images list
        """
        if 1 <= song_num <= len(self.__album_images):
            album_image = self.__album_images[song_num - 1]
            pixmap = QPixmap(album_image)
            #https://www.pythonguis.com/faq/adding-images-to-pyqt6-applications/
            self.album_image.setPixmap(pixmap)

    def set_song_title(self, song_num: int) -> None:
        """
        Method to display song title
        :param song_num: Represents which song's title should be displayed. Should be between 1 and the length of the
                         album_images list
        """
        title = self.__songTitles[song_num - 1]
        self.songTitle.setText(title)

    def set_playlist_label(self, song_num: int) -> None:
        """
        Method to display which song the playlist is on
        :param song_num: Represents the place of song in the playlist
        """
        self.Playlist_label.setText(f'Song {song_num}/5')

    def set_volume_label(self, volume: float) -> None:
        """
        Method to change volume label based on the setting of the volume
        :param volume: Represents setting of volume from 0 - 0.75
        """
        self.volume_label.setText(f'Volume: {volume:.2f}')

    def play(self) -> None:
        """
        Method to play the music when 'play' button is clicked
        """
        self.set_album_image(self.__song_num)
        self.set_song_title(self.__song_num)
        self.set_playlist_label(self.__song_num)

        mixer.music.load(self.__songSounds[self.__song_num - 1])
        mixer.music.play()


    def reverse(self) -> None:
        """
        Method to go back in the playlist when reverse 'button' is clicked
        If first song in playlist is reached, it returns to the last song in playlist
        """
        self.__song_num -= 1
        if self.__song_num == 0:
            self.__song_num = 5
        self.play()

    def skip(self) -> None:
        """
        Method to skip over songs in the playlist when 'skip' button is clicked
        If maximum song in playlist is reached, it returns to song one
        """
        self.__song_num += 1
        if self.__song_num > len(self.__songSounds):
            self.__song_num = 1
        self.play()

    def volume_up(self) -> None:
        """
        Method to increase song volume
        """
        if self.__volume < 0.75:
            self.__volume += 0.25
        self.set_volume_label(self.__volume)
        mixer.music.set_volume(self.__volume)

    def volume_down(self) -> None:
        """
        Method to decrease volume
        """
        if self.__volume >= 0.25:
            self.__volume -= 0.25
        self.set_volume_label(self.__volume)
        mixer.music.set_volume(self.__volume)
