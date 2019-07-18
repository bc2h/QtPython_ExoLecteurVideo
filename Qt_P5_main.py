import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_Qt_P5_design import Ui_MainWindow #nom de la classe générée
from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent #QTime()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   #permet de charger tous les composants graphiques coder dans un autre fichier
# partir du fichier .py (au lieu du .ui) permet d'accéder à la complétion cad la liste des fonctions, widgets...

        self.ui.pbLect.clicked.connect(self.lectClicked)
        self.ui.pbPause.clicked.connect(self.pauseClicked)
        self.ui.pbStop.clicked.connect(self.stopClicked)
        self.ui.pbPreced.clicked.connect(self.precedClicked)
        self.ui.pbSuiv.clicked.connect(self.suivClicked)
        self.ui.pbAjout.clicked.connect(self.ajoutClicked)
        self.ui.pbSuppr.clicked.connect(self.supprClicked)
        self.ui.dlVolume.valueChanged.connect(self.volumeChange)

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.ui.videoScreen)

        self.temps = QTime()


        mediaContent = QMediaContent(QUrl.fromLocalFile("big_buck_bunny.avi"))
        self.mediaPlayer.setMedia(mediaContent)

    def lectClicked(self):
        print("Lecture!!")
        self.mediaPlayer.play()

    def pauseClicked(self):
        print("Pause")
        self.mediaPlayer.pause()

    def stopClicked(self):
        print("Stop")
        self.mediaPlayer.stop()

    def precedClicked(self):
        print("Précédent")
    def suivClicked(self):
        print("Suivant")
    def ajoutClicked(self):
        print("Ajout")
    def supprClicked(self):
        print("Supprime")
    def volumeChange(self):
        print("Volume %s" %self.ui.dlVolume.value())
        self.mediaPlayer.setVolume(self.ui.dlVolume.value())
        self.ui.lbVolumePourc.setText(str(self.ui.dlVolume.value())+"%")

    #def tempTot(self:
        self.mediaPlayer.durationChanged()
        self.mediaPlayer.positionChanged()

        # self.temps = QTime()
        # self.temps.setMinimumTime(QTime(0, 0, 0));
        # self.temps->setMaximumTime(QTime(16, 0, 0));
        # self.temps->setDisplayFormat(QString("hh:mm:ss"));

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
