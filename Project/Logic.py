from PyQt6.QtWidgets import *
from tv_remote import *

class tv_logic(QMainWindow, Ui_TV_remote):
    def __init__(self) -> None:
        """
        Method to initialize the Television Remote controls
        """
        super().__init__()
        self.setupUi(self)
        #Volume
        self.Volume_bar.setValue(0)
        self.button_volume_up.clicked.connect(self.increase_volume)
        self.button_volume_down.clicked.connect(self.decrease_volume)
        self.button_mute.clicked.connect(self.mute_volume)

        #Power
        self.disable_power()
        self.power_state = False
        self.button_power.clicked.connect(self.toggle_power)
        self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/plain-black-background-02fh7564l8qq4m6d.jpg"))

        #Channels
        self.current_source = 1
        self.button_source_change.clicked.connect(self.toggle_source)

        self.channel_value = 0
        self.Cartoon_Network.clicked.connect(self.img_connection)
        self.button_channel_up.clicked.connect(self.channel_up)
        self.button_channel_down.clicked.connect(self.channel_down)

    # Power Functions
    def toggle_power(self) -> None:
        """
        Method to toggle the power state
        """
        self.power_state = not self.power_state
        if self.power_state:
            self.enable_power()
        else:
            self.disable_power()

    def enable_power(self) -> None:
        """
        Method to enable the power state
        """
        self.button_mute.setEnabled(True)
        self.button_channel_up.setEnabled(True)
        self.button_channel_down.setEnabled(True)
        self.button_volume_up.setEnabled(True)
        self.button_volume_down.setEnabled(True)
        self.Cartoon_Network.setEnabled(True)
        self.Peacock.setEnabled(True)
        self.CNN.setEnabled(True)
        self.ESPN.setEnabled(True)
        self.HBO.setEnabled(True)
        self.HGTV.setEnabled(True)
        self.Free_form.setEnabled(True)
        self.History_Channel.setEnabled(True)
        self.Nickelodeon.setEnabled(True)
        self.MTV.setEnabled(True)
        self.button_netflix.setEnabled(True)
        self.button_youtube.setEnabled(True)
        self.button_spotify.setEnabled(True)
        self.button_source_change.setEnabled(True)

    def disable_power(self) -> None:
        """
        Method to disable the power state
        """
        self.button_mute.setEnabled(False)
        self.button_channel_up.setEnabled(False)
        self.button_channel_down.setEnabled(False)
        self.button_volume_up.setEnabled(False)
        self.button_volume_down.setEnabled(False)
        self.Cartoon_Network.setEnabled(False)
        self.Peacock.setEnabled(False)
        self.CNN.setEnabled(False)
        self.ESPN.setEnabled(False)
        self.HBO.setEnabled(False)
        self.HGTV.setEnabled(False)
        self.Free_form.setEnabled(False)
        self.History_Channel.setEnabled(False)
        self.Nickelodeon.setEnabled(False)
        self.MTV.setEnabled(False)
        self.button_netflix.setEnabled(False)
        self.button_youtube.setEnabled(False)
        self.button_spotify.setEnabled(False)
        self.button_source_change.setEnabled(False)

    def toggle_source(self) -> None:
        """
        Method to toggle the source state
        """
        if self.current_source == 1:
            self.button_source_change.clicked.connect(self.toggle_source)
            self.current_source = 2
        else:
            self.button_mute.clicked.connect(self.toggle_source)
            self.current_source = 1

    def show_cartoon_network(self) -> None:
        """
        Method to show the first channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Cartoon-Network-logo.jpg"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Adult-Swim-Logo.png"))
        self.channel_value = 1
    def show_Peacock(self) -> None:
        """
        Method to show the second channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/1200px-NBC_Peacock_1986.svg.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Paramount-Pictures-logo.png"))
        self.channel_value = 2
    def show_CNN(self) -> None:
        """
        Method to show the third channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/CNN_International_logo.svg.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/abc.png"))
        self.channel_value = 3
    def show_ESPN(self) -> None:
        """
        Method to show the fourth channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/ESPN-logo.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/nba_tv.png"))
        self.channel_value = 4
    def show_HBO(self) -> None:
        """
        Method to show the fifth channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/HBO_logo.svg.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Animal-Planet-logo.png"))
        self.channel_value = 5
    def show_HGTV(self) -> None:
        """
        Method to show the sixth channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/hgtv-logo.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Food_Network_logo.svg.png"))
        self.channel_value = 6
    def show_History_Channel(self) -> None:
        """
        Method to show the seventh channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/History-Channel-logo.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Comedy-Central-logo.png"))
        self.channel_value = 7
    def show_MTV(self) -> None:
        """
        Method to show the eighth channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/MTV-logo-2021.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/everything_entertainment.png"))
        self.channel_value = 8
    def show_Nickelodeon(self) -> None:
        """
        Method to show the ninth channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Nickelodeon_2023_logo_(alternative).svg.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Disney_Channel_logo.svg.png"))
        self.channel_value = 9
    def show_Free_Form(self) -> None:
        """
        Method to show the tenth channel
        """
        if self.current_source == 1:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/untitled-1_364.png"))
        elif self.current_source == 2:
            self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/FX_International_logo.svg.png"))
        self.channel_value = 10
    def show_Netflix(self) -> None:
        """
        Method to show the Netflix application
        """
        self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/netflix-logo.png"))
    def show_Youtube(self) -> None:
        """
        Method to show the Youtube application
        """
        self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/360_F_507468479_HfrpT7CIoYTBZSGRQi7RcWgo98wo3vb7.jpg"))
    def show_Spotify(self) -> None:
        """
        Method to show the Spotify application
        """
        self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/Spotify_logo_with_text.svg.png"))
    def show_power_off(self) -> None:
        """
        Method to show that the power is off
        """
        self.graphicsView_channel.setPixmap(QtGui.QPixmap("img/plain-black-background-02fh7564l8qq4m6d.jpg"))

    #Connecting images to buttons
    def img_connection(self) -> None:
        """
        Method to connect the images to the TV remote buttons
        """
        self.Cartoon_Network.clicked.connect(self.show_cartoon_network)
        self.Peacock.clicked.connect(self.show_Peacock)
        self.CNN.clicked.connect(self.show_CNN)
        self.ESPN.clicked.connect(self.show_ESPN)
        self.HBO.clicked.connect(self.show_HBO)
        self.HGTV.clicked.connect(self.show_HGTV)
        self.History_Channel.clicked.connect(self.show_History_Channel)
        self.MTV.clicked.connect(self.show_MTV)
        self.Nickelodeon.clicked.connect(self.show_Nickelodeon)
        self.Free_form.clicked.connect(self.show_Free_Form)
        self.button_netflix.clicked.connect(self.show_Netflix)
        self.button_youtube.clicked.connect(self.show_Youtube)
        self.button_spotify.clicked.connect(self.show_Spotify)
        self.button_power.clicked.connect(self.show_power_off)

    def channel_up(self) -> None:
        """
        Methos to increase the channel
        """
        self.channel_value += 1
        if self.channel_value==1:
            self.show_cartoon_network()
        elif self.channel_value==2:
            self.show_Peacock()
        elif self.channel_value==3:
            self.show_CNN()
        elif self.channel_value==4:
            self.show_ESPN()
        elif self.channel_value==5:
            self.show_HBO()
        elif self.channel_value==6:
            self.show_HGTV()
        elif self.channel_value==7:
            self.show_History_Channel()
        elif self.channel_value==8:
            self.show_MTV()
        elif self.channel_value==9:
            self.show_Nickelodeon()
        elif self.channel_value==10:
            self.show_Free_Form()
        else:
            self.show_cartoon_network()
    def channel_down(self) -> None:
        """
        Method to decrease the channel
        """
        self.channel_value -= 1
        if self.channel_value==1:
            self.show_cartoon_network()
        elif self.channel_value==2:
            self.show_Peacock()
        elif self.channel_value==3:
            self.show_CNN()
        elif self.channel_value==4:
            self.show_ESPN()
        elif self.channel_value==5:
            self.show_HBO()
        elif self.channel_value==6:
            self.show_HGTV()
        elif self.channel_value==7:
            self.show_History_Channel()
        elif self.channel_value==8:
            self.show_MTV()
        elif self.channel_value==9:
            self.show_Nickelodeon()
        elif self.channel_value==10:
            self.show_Free_Form()
        else:
            self.show_Free_Form()

    #Volume bar functions
    def increase_volume(self) -> None:
        """
        Method to increase the volume
        """
        value = self.Volume_bar.value()
        self.Volume_bar.setValue(min(value + 25, 100))  # Increase by 25, capped at 100
    def decrease_volume(self) -> None:
        """
        Method to decrease the volume
        """
        value = self.Volume_bar.value()
        self.Volume_bar.setValue(max(value - 25, 0))  # Decrease by 25, capped at 0
    def mute_volume(self) -> None:
        """
        Method to mute the volume
        :return:
        """
        self.Volume_bar.setValue(0)
