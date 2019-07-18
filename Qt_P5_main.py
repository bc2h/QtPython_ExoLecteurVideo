import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_Qt_P5_design import Ui_MainWindow #nom de la classe générée
from PySide2.QtCore import QUrl, QTime
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

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

        self.mediaPlayer.durationChanged.connect(self.mediaDurationChanged)
        self.mediaPlayer.positionChanged.connect(self.mediaPositionChanged)
        self.ui.slTimeBarre.valueChanged.connect(self.timeBarreChanged)



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
        self.ui.listFilm.addItem(QFileDialog.getOpenFileName()[0])

    def supprClicked(self):
        print("Supprime")
    def volumeChange(self):
        print("Volume %s" %self.ui.dlVolume.value())
        self.mediaPlayer.setVolume(self.ui.dlVolume.value())
        self.ui.lbVolumePourc.setText(str(self.ui.dlVolume.value())+"%")

    def mediaDurationChanged(self):
        mediaDuration = self.mediaPlayer.duration()
        self.ui.slTimeBarre.setRange(0,mediaDuration)
        totTime = QTime(0,0,0)
        totTime = totTime.addMSecs(mediaDuration)
        self.ui.lbTimeTot.setText(totTime.toString("HH:mm:ss"))

    def mediaPositionChanged(self):
        self.ui.slTimeBarre.valueChanged.disconnect(self.timeBarreChanged)
        mediaPosition = self.mediaPlayer.position()
        self.ui.slTimeBarre.setValue(mediaPosition)
        currentTime = QTime(0,0,0)
        currentTime = currentTime.addMSecs(mediaPosition)
        self.ui.lbTimeReal.setText(currentTime.toString("HH:mm:ss"))
        self.ui.slTimeBarre.valueChanged.connect(self.timeBarreChanged)

    def timeBarreChanged(self):
        self.mediaPlayer.positionChanged.disconnect(self.mediaPositionChanged)
        self.mediaPlayer.setPosition(self.ui.slTimeBarre.value())
        self.mediaPlayer.positionChanged.connect(self.mediaPositionChanged)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
