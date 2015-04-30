from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

Ui_MainWindow, QMainWindow = loadUiType('ui/window.ui')

class AppForm(QMainWindow, Ui_MainWindow):
    def __init__(self, my_dataframe, parent=None):
        super(AppForm, self).__init__()

        self.tweets_list = my_dataframe

        self.setupUi(self)

        self.setWindowTitle('Twitter Mining')
        self.create_main_frame(self.tweets_list)
        self.on_draw(self.tweets_list)

    # Save button on click action
    def on_save(self):
        tweet_lang = str(self.combos.currentText())

        if self.combos.currentIndex() is not 0:
            with open(str(tweet_lang) + '_tweets.txt', 'w') as f:
                f.write(self.text_edit.toPlainText())

    # Display count button on click action
    def on_displaytweets(self):
        self.text_edit.clear()

        java_count = self.tweets_list['java'].value_counts()[True]
        javascript_count = self.tweets_list['javascript'].value_counts()[True]
        php_count = self.tweets_list['php'].value_counts()[True]
        csharp_count = self.tweets_list['csharp'].value_counts()[True]
        cplusplus_count = self.tweets_list['cplusplus'].value_counts()[True]
        python_count = self.tweets_list['python'].value_counts()[True]

        self.text_edit.appendPlainText('TOTAL TWEETS: ' + str(len(self.tweets_list.index)) + '\n')
        self.text_edit.appendPlainText('JAVA: ' + str(java_count))
        self.text_edit.appendPlainText('JAVASCRIPT: ' + str(javascript_count))
        self.text_edit.appendPlainText('PHP: ' + str(php_count))
        self.text_edit.appendPlainText('C#: ' + str(csharp_count))
        self.text_edit.appendPlainText('C++: ' + str(cplusplus_count))
        self.text_edit.appendPlainText('PYTHON: ' + str(python_count) + '\n')

    # Draw the graph
    def on_draw(self, tweets_list):

        self.axes.clear()

        self.axes.set_title('Comparisons of Programming Languages')

        prog_languages = ['java', 'javascript', 'php', 'c++', 'c#', 'python']

        # Store number of tweets a programming language is mentioned
        java_count = tweets_list['java'].value_counts()[True]
        javascript_count = tweets_list['javascript'].value_counts()[True]
        php_count = tweets_list['php'].value_counts()[True]
        csharp_count = tweets_list['csharp'].value_counts()[True]
        cplusplus_count = tweets_list['cplusplus'].value_counts()[True]
        python_count = tweets_list['python'].value_counts()[True]

        lang_counts =[java_count, javascript_count, php_count, csharp_count, cplusplus_count, python_count]

        # X-axis stops at end the number of programming languages
        x_axis = list(range(len(prog_languages)))

        # Set division of elements of x-axis
        self.axes.set_yticks([p + .4 for p in x_axis])
        self.axes.set_yticklabels(prog_languages)

        # Set chart to bar-graph
        self.axes.barh(x_axis, lang_counts)

        # Draw grid on the graph
        self.axes.grid(True)

        self.canvas.draw()

    # Combobox on select action
    def onActivate(self, index):
        self.text_edit.clear()

        # Print tweets mentioning java
        if index is 1:
            for index, row in self.tweets_list.iterrows():
                if(row['java'] is True):
                    self.text_edit.appendPlainText(row['text'])

        # Print tweets mentioning javascript
        if index is 2:
            for index, row in self.tweets_list.iterrows():
                if row['javascript'] is True:
                    self.text_edit.appendPlainText(row['text'])

        # Print tweets mentioning c++
        if index is 3:
            for index, row in self.tweets_list.iterrows():
                if row['cplusplus'] is True:
                    self.text_edit.appendPlainText(row['text'])

        # Print tweets mentioning c#
        if index is 4:
            for index, row in self.tweets_list.iterrows():
                if row['csharp'] is True:
                    self.text_edit.appendPlainText(row['text'])

        # Print tweets mentioning python
        if index is 5:
            for index, row in self.tweets_list.iterrows():
                if row['python'] is True:
                    self.text_edit.appendPlainText(row['text'])

        # Print tweets mentioning php
        if index is 6:
            for index, row in self.tweets_list.iterrows():
                if row['php'] is True:
                    self.text_edit.appendPlainText(row['text'])

        # Print all tweets
        if index is 7:
            for index, row in self.tweets_list.iterrows():
                self.text_edit.appendPlainText(row['text'])


    def create_main_frame(self, tweets_list):
        # self.main_frame = QWidget()

        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)

        self.mplvl.addWidget(self.canvas)

        self.axes = self.fig.add_subplot(111)

        # self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        # self.mplvl.addWidget(self.mpl_toolbar)

        self.combos.addItem("None")
        self.combos.addItem("Java")
        self.combos.addItem("Javascript")
        self.combos.addItem("C++")
        self.combos.addItem("C#")
        self.combos.addItem("Python")
        self.combos.addItem("PHP")
        self.combos.addItem("All")
        self.combos.activated.connect(self.onActivate)

        self.connect(self.display_tweet_count, SIGNAL('clicked()'), self.on_displaytweets)
        self.connect(self.save_button, SIGNAL('clicked()'), self.on_save)