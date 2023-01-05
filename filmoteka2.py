from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import sys
import sqlite3
import os

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

FLAG = False


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        super(Ui_MainWindow, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 396)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 10, 471, 361))
        self.tabs.setObjectName("tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.table_films = QtWidgets.QTableView(self.tab1)
        self.table_films.setGeometry(QtCore.QRect(10, 40, 451, 291))
        self.table_films.setObjectName("table_films")
        self.add_film = QtWidgets.QPushButton(self.tab1)
        self.add_film.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.add_film.setFont(font)
        self.add_film.setObjectName("add_film")
        self.new_film = QtWidgets.QPushButton(self.tab1)
        self.new_film.setGeometry(QtCore.QRect(100, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.new_film.setFont(font)
        self.new_film.setObjectName("new_film")
        self.delete_film = QtWidgets.QPushButton(self.tab1)
        self.delete_film.setGeometry(QtCore.QRect(190, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.delete_film.setFont(font)
        self.delete_film.setObjectName("delete_film")
        self.tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.table_genres = QtWidgets.QTableView(self.tab2)
        self.table_genres.setGeometry(QtCore.QRect(10, 40, 451, 291))
        self.table_genres.setObjectName("table_genres")
        self.add_genre = QtWidgets.QPushButton(self.tab2)
        self.add_genre.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.add_genre.setFont(font)
        self.add_genre.setObjectName("add_genre")
        self.new_genre = QtWidgets.QPushButton(self.tab2)
        self.new_genre.setGeometry(QtCore.QRect(100, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.new_genre.setFont(font)
        self.new_genre.setObjectName("new_genre")
        self.delete_genre = QtWidgets.QPushButton(self.tab2)
        self.delete_genre.setGeometry(QtCore.QRect(190, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.delete_genre.setFont(font)
        self.delete_genre.setObjectName("delete_genre")
        self.tabs.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(3)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фильмотека"))
        self.add_film.setText(_translate("MainWindow", "Добавить фильм"))
        self.new_film.setText(_translate("MainWindow", "Изменить фильм"))
        self.delete_film.setText(_translate("MainWindow", "Удалить фильм"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab1), _translate("MainWindow", "Фильмы"))
        self.add_genre.setText(_translate("MainWindow", "Добавить жанр"))
        self.new_genre.setText(_translate("MainWindow", "Изменить жанр"))
        self.delete_genre.setText(_translate("MainWindow", "Удалить жанр"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab2), _translate("MainWindow", "Жанры"))


class AddFilmForm(QMainWindow):
    def setupUi(self, MainWindow):
        super(AddFilmForm, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 175)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 51, 18))
        self.label_name.setObjectName("label_name")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(10, 40, 66, 18))
        self.label_year.setObjectName("label_year")
        self.label_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_genre.setGeometry(QtCore.QRect(10, 80, 35, 12))
        self.label_genre.setObjectName("label_genre")
        self.label_duration = QtWidgets.QLabel(self.centralwidget)
        self.label_duration.setGeometry(QtCore.QRect(10, 110, 35, 12))
        self.label_duration.setObjectName("label_duration")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(210, 130, 91, 21))
        self.add.setObjectName("add")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(10, 130, 191, 21))
        self.error.setText("")
        self.error.setObjectName("error")
        self.name = QtWidgets.QTextEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(80, 10, 231, 24))
        self.name.setObjectName("name")
        self.year = QtWidgets.QTextEdit(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(80, 40, 231, 24))
        self.year.setObjectName("year")
        self.duration = QtWidgets.QTextEdit(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(80, 100, 231, 24))
        self.duration.setObjectName("duration")
        self.genre = QtWidgets.QComboBox(self.centralwidget)
        self.genre.setGeometry(QtCore.QRect(80, 72, 231, 20))
        self.genre.setObjectName("genre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить элемент"))
        self.label_name.setText(_translate("MainWindow", "Название"))
        self.label_year.setText(_translate("MainWindow", "Год выпуска"))
        self.label_genre.setText(_translate("MainWindow", "Жанр"))
        self.label_duration.setText(_translate("MainWindow", "Длина"))
        self.add.setText(_translate("MainWindow", "Добавить"))


class AddGenreForm(QMainWindow):
    def setupUi(self, MainWindow):
        super(AddGenreForm, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 92)
        font = QtGui.QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 20, 191, 21))
        self.textEdit.setObjectName("textEdit")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(180, 50, 71, 21))
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить элемент"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.save.setText(_translate("MainWindow", "Сохранить"))


class Filmotecka(Ui_MainWindow):
    def __init__(self):
        super(Filmotecka, self).setupUi(self)
        self.setFixedSize(489, 402)
        self.setWindowTitle('Фильмотека')
        if os.path.isfile('films_db.sqlite'):
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('films_db.sqlite')
        else:
            app = QApplication(sys.argv)
            bad_exit = DatabaseNotFound()
            bad_exit.show()
            sys.exit(app.exec_())

        self.model_films = QSqlTableModel(self)
        self.model_films.select()

        self.model_genres = QSqlTableModel(self)
        self.model_genres.select()

        self.update_table_films()
        self.update_table_genres()

        self.table_films.setModel(self.model_films)
        self.table_films.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_films.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.add_film.clicked.connect(self.adding_film)
        self.delete_film.clicked.connect(self.deleting_film)
        self.new_film.clicked.connect(self.update_film)

        self.table_genres.setModel(self.model_genres)
        self.table_genres.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_genres.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.add_genre.clicked.connect(self.adding_genre)
        self.delete_genre.clicked.connect(self.deleting_genre)
        self.new_genre.clicked.connect(self.update_genre)

    def update_film(self):
        global FLAG
        if not FLAG:
            if self.table_films.currentIndex().siblingAtColumn(0).data():
                self.form = UpdateFilm(self.table_films.currentIndex().siblingAtColumn(0).data())
                self.form.show()
                FLAG = True

    def update_genre(self):
        global FLAG
        if not FLAG:
            if self.table_genres.currentIndex().siblingAtColumn(0).data():
                self.form = UpdateGenre(self.table_genres.currentIndex().siblingAtColumn(0).data())
                self.form.show()
                FLAG = True

    def deleting_film(self):
        global FLAG
        if not FLAG:
            if self.table_films.currentIndex().siblingAtColumn(0).data():
                sql = f'delete from films where id = {self.table_films.currentIndex().siblingAtColumn(0).data()}'
                self.update_table = QSqlQuery()
                self.update_table.exec(sql)
                self.update_table_films()

    def deleting_genre(self):
        global FLAG
        if not FLAG:
            if self.table_genres.currentIndex().siblingAtColumn(0).data():
                sql = f'delete from genres where id = {self.table_genres.currentIndex().siblingAtColumn(0).data()}'
                self.update_table = QSqlQuery()
                self.update_table.exec(sql)
                self.update_table_genres()

    def adding_film(self):
        global FLAG
        if not FLAG:
            self.form = AddFilm()
            self.form.show()
            FLAG = True
            self.update_table_films()

    def adding_genre(self):
        global FLAG
        if not FLAG:
            self.form = AddGenre()
            self.form.show()
            FLAG = True
            self.update_table_genres()

    def update_table_films(self):
        sql = QSqlQuery('''select films.id as "ID", films.title as "Название", films.year as "Год выпуска", 
                genres.title as "Жанр", films.duration as "Продолжительность" from films 
                join genres on genres.id = films.genre''', self.db)
        self.model_films.setQuery(sql)

    def update_table_genres(self):
        sql = QSqlQuery('''select genres.id as "ID", genres.title as "Жанр" from genres''', self.db)
        self.model_genres.setQuery(sql)


class UpdateFilm(AddFilmForm):
    def __init__(self, id):
        super(UpdateFilm, self).setupUi(self)
        self.id = id
        self.setFixedSize(325, 175)
        self.setWindowTitle('Редактирование записи')
        self.add.setText('Отредактировать')
        self.add.resize(120, 23)
        self.add.move(191, 130)
        con = sqlite3.connect('films_db.sqlite')
        self.cur = con.cursor()
        self.genre.addItems([str(p[0]) for p in self.cur.execute('''select title from genres''').fetchall()])
        self.film = self.cur.execute(f'select * from films where id = {id}').fetchall()[0]
        self.name.setText(self.film[1])
        self.year.setText(str(self.film[2]))
        self.genre.setCurrentText(str(self.cur.execute(f'''select title 
        from genres where id = {self.film[3]}''').fetchone()[0]))
        self.duration.setText(str(self.film[4]))
        self.add.clicked.connect(self.updating_film)

    def updating_film(self):
        if self.name.toPlainText() and self.year.toPlainText().isdigit() and self.duration.toPlainText().isdigit():
            if self.name.toPlainText() not in [p[0] for p in self.cur.execute('select title from films').fetchall()]:
                self.add_table = QSqlQuery()
                self.add_table.exec(f'''update films set title = "{self.name.toPlainText()}", 
                year = {self.year.toPlainText()}, 
                genre = (select id from genres where title = "{self.genre.currentText()}"), 
                duration = {self.duration.toPlainText()} where id = {self.id}''')
                self.close()
            else:
                self.error.setText('Фильм уже добавлен')
        else:
            self.error.setText('Неверно заполнена форма')

    def closeEvent(self, event) -> None:
        global FLAG
        FLAG = False
        global form
        form.update_table_films()


class UpdateGenre(AddGenreForm):
    def __init__(self, id):
        super(UpdateGenre, self).setupUi(self)
        self.id = id
        self.setWindowTitle('Редактирование записи')
        con = sqlite3.connect('films_db.sqlite')
        self.cur = con.cursor()
        self.film = self.cur.execute(f'select * from genres where id = {id}').fetchall()[0]
        self.textEdit.setText(self.film[1])
        self.setFixedSize(262, 92)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.error.setText("")
        self.error.setObjectName("error")
        self.save.clicked.connect(self.updating_genre)

    def updating_genre(self):
        if self.textEdit.toPlainText():
            if self.textEdit.toPlainText() not in [str(p[0]) for p in self.cur.execute('''select title 
            from genres''').fetchall()]:
                self.add_table = QSqlQuery()
                self.add_table.exec(f'''update genres 
                set title = "{self.textEdit.toPlainText()}" where id = {self.id}''')
                self.close()
            else:
                self.error.setText('Жанр уже добавлен')
        else:
            self.error.setText('Неверно заполнена форма')

    def closeEvent(self, event) -> None:
        global FLAG
        FLAG = False
        global form
        form.update_table_genres()


class AddGenre(AddGenreForm):
    def __init__(self):
        super(AddGenre, self).setupUi(self)
        self.setFixedSize(262, 92)
        self.save.clicked.connect(self.adding)
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.error.setText("")
        self.error.setObjectName("error")
        con = sqlite3.connect('films_db.sqlite')
        self.cur = con.cursor()

    def adding(self):
        if self.textEdit.toPlainText():
            if self.textEdit.toPlainText() not in [str(p[0]) for p in self.cur.execute('''select title 
            from genres''').fetchall()]:
                self.add_table = QSqlQuery()
                self.add_table.exec(f'''INSERT INTO genres(title) 
                            VALUES ("{self.textEdit.toPlainText()}")''')
                self.close()
            else:
                self.error.setText('Жанр уже добавлен')
        else:
            self.error.setText('Неверно заполнена форма')

    def closeEvent(self, event) -> None:
        global FLAG
        FLAG = False
        global form
        form.update_table_genres()


class AddFilm(AddFilmForm):
    def __init__(self):
        super(AddFilm, self).setupUi(self)
        self.setFixedSize(325, 175)
        con = sqlite3.connect('films_db.sqlite')
        self.cur = con.cursor()
        self.genre.addItems([str(p[0]) for p in self.cur.execute('''select title from genres''').fetchall()])
        self.add.clicked.connect(self.adding)

    def adding(self):
        if self.name.toPlainText() and self.year.toPlainText().isdigit() and self.duration.toPlainText().isdigit():
            if self.name.toPlainText() not in [p[0] for p in self.cur.execute('select title from films').fetchall()]:
                self.add_table = QSqlQuery()
                self.add_table.exec(f'''INSERT INTO films(title, year, genre, duration) 
                VALUES ("{self.name.toPlainText()}", {self.year.toPlainText()}, 
                (select id from genres where title = "{self.genre.currentText()}"), {self.duration.toPlainText()})''')
                self.close()
            else:
                self.error.setText('Фильм уже добавлен')
        else:
            self.error.setText('Неверно заполнена форма')

    def closeEvent(self, event) -> None:
        global FLAG
        FLAG = False
        global form
        form.update_table_films()


class DatabaseNotFound(QMainWindow, QWidget):
    def __init__(self):
        super(DatabaseNotFound, self).__init__()
        # Создание окна ошибки
        self.setGeometry(500, 500, 250, 50)
        self.setWindowTitle('Ошибка!')
        self.error_layout = QVBoxLayout()
        self.error_label = QLabel('База данных не найдена!', self)
        self.error_label.resize(self.sizeHint())
        self.error_layout.addWidget(self.error_label)
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.error_layout)
        self.setCentralWidget(self.centralWidget)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:  # Закрытие окна
        app.quit()
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    form = Filmotecka()
    form.show()
    sys.exit(app.exec())
