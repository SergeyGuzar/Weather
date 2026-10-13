from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QLabel
from modules.app import app
from PyQt6.QtCore import Qt

main_window = QMainWindow()
primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()
WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800
main_window.setGeometry(
    (width_screen//2)-(WIDTH_WINDOW//2),
    (height_screen//2)-(HEIGHT_WINDOW//2),
    WIDTH_WINDOW,
    HEIGHT_WINDOW
)

main_frame = QFrame(main_window)
main_frame.setStyleSheet("background-color: #1a183b")
main_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)
main_layout = QVBoxLayout(main_frame)

frame_H_1 = QFrame(main_frame)
frame_H_1.setStyleSheet("background-color: #1a183b")
frame_H_1.setFixedSize(WIDTH_WINDOW, 225)
main_layout.addWidget(frame_H_1)

frame_H_2 = QFrame(main_frame)
frame_H_2.setStyleSheet("background-color: #1a183b")
frame_H_2.setFixedSize(WIDTH_WINDOW, 225)
main_layout.addWidget(frame_H_2)

frame_H_3 = QFrame(main_frame)
frame_H_3.setStyleSheet("background-color: #1a183b")
frame_H_3.setFixedSize(WIDTH_WINDOW, 225)
main_layout.addWidget(frame_H_3)

layout_Squares_1 = QHBoxLayout(frame_H_1)
layout_Squares_2 = QHBoxLayout(frame_H_2)
layout_Squares_3 = QHBoxLayout(frame_H_3)






orange_frame = QFrame(main_frame)
orange_frame.setStyleSheet("background-color: orange; border-radius: 14px")
orange_frame.setFixedSize(300, 210)
layout_Squares_1.addWidget(orange_frame)

mini_orange_frame_layout = QVBoxLayout(orange_frame)

mini_orange_frame_1 = QFrame(orange_frame)
mini_orange_frame_1.setStyleSheet("background-color: orange")
mini_orange_frame_1.setFixedSize(300,130)
mini_orange_frame_layout.addWidget(mini_orange_frame_1)
orange_label = QLabel("Температура",mini_orange_frame_1 )
orange_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
orange_label.setContentsMargins(10,10,0,0)

mini_orange_frame_2 = QFrame(orange_frame)
mini_orange_frame_2.setStyleSheet("background-color: orange")
mini_orange_frame_2.setFixedSize(300, 50)
orange_label_2 = QLabel("24°C ",mini_orange_frame_2)
orange_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
orange_label_2.setContentsMargins(10,10,0,0)
mini_orange_frame_layout.addWidget(mini_orange_frame_2)

mini_orange_frame_3 = QFrame(orange_frame)
mini_orange_frame_3.setStyleSheet("background-color: orange")
mini_orange_frame_3.setFixedSize(300, 30)
orange_label_3 = QLabel("Сонячно",mini_orange_frame_3)
orange_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
orange_label_3.setContentsMargins(10,0,0,0)
mini_orange_frame_layout.addWidget(mini_orange_frame_3)









blue_frame = QFrame(main_frame)
blue_frame.setStyleSheet("background-color: #0f79db; border-radius: 14px")
blue_frame.setFixedSize(300, 210)
layout_Squares_1.addWidget(blue_frame)

mini_blue_frame_layout = QVBoxLayout(blue_frame)

mini_blue_frame_1 = QFrame(blue_frame)
mini_blue_frame_1.setStyleSheet("background-color: #0f79db")
mini_blue_frame_1.setFixedSize(300,130)
blue_label = QLabel("Вологість",mini_blue_frame_1 )
blue_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
blue_label.setContentsMargins(10,10,0,0)
mini_blue_frame_layout.addWidget(mini_blue_frame_1)

mini_blue_frame_2 = QFrame(blue_frame)
mini_blue_frame_2.setStyleSheet("background-color: #0f79db")
mini_blue_frame_2.setFixedSize(300, 50)
blue_label_2 = QLabel("65% ",mini_blue_frame_2)
blue_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
blue_label_2.setContentsMargins(10,10,0,0)
mini_blue_frame_layout.addWidget(mini_blue_frame_2)

mini_blue_frame_3 = QFrame(blue_frame)
mini_blue_frame_3.setStyleSheet("background-color: #0f79db")
mini_blue_frame_3.setFixedSize(300, 30)
blue_label_3 = QLabel("Комфортно",mini_blue_frame_3)
blue_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
blue_label_3.setContentsMargins(10,0,0,0)
mini_blue_frame_layout.addWidget(mini_blue_frame_3)











purple_frame = QFrame(main_frame)
purple_frame.setStyleSheet("background-color: purple; border-radius: 14px")
purple_frame.setFixedSize(300, 210)
layout_Squares_1.addWidget(purple_frame)

mini_purple_frame_layout = QVBoxLayout(purple_frame)

mini_purple_frame_1 = QFrame(purple_frame)
mini_purple_frame_1.setStyleSheet("background-color: purple")
mini_purple_frame_1.setFixedSize(300,130)
purple_label = QLabel("Швидкість вітру",mini_purple_frame_1 )
purple_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
purple_label.setContentsMargins(10,10,0,0)
mini_purple_frame_layout.addWidget(mini_purple_frame_1)

mini_purple_frame_2 = QFrame(purple_frame)
mini_purple_frame_2.setStyleSheet("background-color: purple")
mini_purple_frame_2.setFixedSize(300, 50)
purple_label_2 = QLabel("12 км/год ",mini_purple_frame_2)
purple_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
purple_label_2.setContentsMargins(10,10,0,0)
mini_purple_frame_layout.addWidget(mini_purple_frame_2)

mini_purple_frame_3 = QFrame(purple_frame)
mini_purple_frame_3.setStyleSheet("background-color: purple")
mini_purple_frame_3.setFixedSize(300, 30)
purple_label_3 = QLabel("Слабкий вітер",mini_purple_frame_3)
purple_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
purple_label_3.setContentsMargins(10,0,0,0)
mini_purple_frame_layout.addWidget(mini_purple_frame_3)











pink_frame = QFrame(main_frame)
pink_frame.setStyleSheet("background-color: #c91010; border-radius: 14px")
pink_frame.setFixedSize(300, 210)
layout_Squares_2.addWidget(pink_frame)

mini_pink_frame_layout = QVBoxLayout(pink_frame)

mini_pink_frame_1 = QFrame(pink_frame)
mini_pink_frame_1.setStyleSheet("background-color: #c91010")
mini_pink_frame_1.setFixedSize(300,130)
pink_label = QLabel("Відчувається як",mini_pink_frame_1 )
pink_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
pink_label.setContentsMargins(10,10,0,0)
mini_pink_frame_layout.addWidget(mini_pink_frame_1)

mini_pink_frame_2 = QFrame(pink_frame)
mini_pink_frame_2.setStyleSheet("background-color: #c91010")
mini_pink_frame_2.setFixedSize(300, 50)
pink_label_2 = QLabel("27°C ",mini_pink_frame_2)
pink_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
pink_label_2.setContentsMargins(10,10,0,0)
mini_pink_frame_layout.addWidget(mini_pink_frame_2)

mini_pink_frame_3 = QFrame(pink_frame)
mini_pink_frame_3.setStyleSheet("background-color: #c91010")
mini_pink_frame_3.setFixedSize(300, 30)
pink_label_3 = QLabel("Тепліше, ніж зазвичай",mini_pink_frame_3)
pink_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
pink_label_3.setContentsMargins(10,0,0,0)
mini_pink_frame_layout.addWidget(mini_pink_frame_3)









light_blue_frame = QFrame(main_frame)
light_blue_frame.setStyleSheet("background-color: #0c438a; border-radius: 14px")
light_blue_frame.setFixedSize(300, 210)
layout_Squares_2.addWidget(light_blue_frame)

light_blue_frame_layout = QVBoxLayout(light_blue_frame)

light_blue_frame_1 = QFrame(light_blue_frame)
light_blue_frame_1.setStyleSheet("background-color: #0c438a")
light_blue_frame_1.setFixedSize(300,130)
light_blue_label = QLabel("Атмосферний тиск",light_blue_frame_1 )
light_blue_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
light_blue_label.setContentsMargins(10,10,0,0)
light_blue_frame_layout.addWidget(light_blue_frame_1)

light_blue_frame_2 = QFrame(light_blue_frame)
light_blue_frame_2.setStyleSheet("background-color: #0c438a")
light_blue_frame_2.setFixedSize(300, 50)
light_blue_label_2 = QLabel("760 ",light_blue_frame_2)
light_blue_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
light_blue_label_2.setContentsMargins(10,10,0,0)
light_blue_frame_layout.addWidget(light_blue_frame_2)

light_blue_frame_3 = QFrame(light_blue_frame)
light_blue_frame_3.setStyleSheet("background-color: #0c438a")
light_blue_frame_3.setFixedSize(300, 30)
light_blue_label_3 = QLabel("мм рт. ст.",light_blue_frame_3)
light_blue_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
light_blue_label_3.setContentsMargins(10,0,0,0)
light_blue_frame_layout.addWidget(light_blue_frame_3)









green_frame = QFrame(main_frame)
green_frame.setStyleSheet("background-color: green; border-radius: 14px")
green_frame.setFixedSize(300, 210)
layout_Squares_2.addWidget(green_frame)

green_frame_layout = QVBoxLayout(green_frame)

green_frame_1 = QFrame(green_frame)
green_frame_1.setStyleSheet("background-color: green")
green_frame_1.setFixedSize(300,130)
green_label = QLabel("Ймовірність дощу",green_frame_1 )
green_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
green_label.setContentsMargins(10,10,0,0)
green_frame_layout.addWidget(green_frame_1)

green_frame_2 = QFrame(green_frame)
green_frame_2.setStyleSheet("background-color: green")
green_frame_2.setFixedSize(300, 50)
green_label_2 = QLabel("20% ",green_frame_2)
green_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
green_label_2.setContentsMargins(10,10,0,0)
green_frame_layout.addWidget(green_frame_2)

green_frame_3 = QFrame(green_frame)
green_frame_3.setStyleSheet("background-color: green")
green_frame_3.setFixedSize(300, 30)
green_label_3 = QLabel("Невелика",green_frame_3)
green_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
green_label_3.setContentsMargins(10,0,0,0)
green_frame_layout.addWidget(green_frame_3)








dark_grey_1_frame = QFrame(main_frame)
dark_grey_1_frame.setStyleSheet("background-color: #293545; border-radius: 14px")
dark_grey_1_frame.setFixedSize(300, 210)
layout_Squares_3.addWidget(dark_grey_1_frame)

dark_grey_frame_layout = QVBoxLayout(dark_grey_1_frame)

dark_grey_1_frame_1 = QFrame(dark_grey_1_frame)
dark_grey_1_frame_1.setStyleSheet("background-color: #293545")
dark_grey_1_frame_1.setFixedSize(280,160)
dark_grey_1_frame_layout = QHBoxLayout(dark_grey_1_frame_1)
dark_grey_1_label = QLabel("Керування погодою",dark_grey_1_frame_1 )
dark_grey_1_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
dark_grey_frame_layout.addWidget(dark_grey_1_frame_1)
dark_grey_1_frame_layout.addWidget(dark_grey_1_label)
dark_grey_1_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


dark_grey_1_frame_2 = QFrame(dark_grey_1_frame)
dark_grey_1_frame_2.setStyleSheet("background-color: #101eb5")
dark_grey_1_frame_2.setFixedSize(280, 50)
dark_grey_1_frame_2_layout = QHBoxLayout(dark_grey_1_frame_2)
dark_grey_1_label_2 = QLabel("Оновити",dark_grey_1_frame_2)
dark_grey_1_label_2.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
dark_grey_frame_layout.addWidget(dark_grey_1_frame_2)
dark_grey_1_frame_2_layout.addWidget(dark_grey_1_label_2)
dark_grey_1_frame_2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)








grey_frame = QFrame(main_frame)
grey_frame.setStyleSheet("background-color: grey; border-radius: 14px")
grey_frame.setFixedSize(300, 210)
layout_Squares_3.addWidget(grey_frame)

grey_frame_layout = QVBoxLayout(grey_frame)

grey_frame_1 = QFrame(grey_frame)
grey_frame_1.setStyleSheet("background-color: grey")
grey_frame_1.setFixedSize(300,130)
grey_label = QLabel("Місто",grey_frame_1 )
grey_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
grey_label.setContentsMargins(10,10,0,0)
grey_frame_layout.addWidget(grey_frame_1)

grey_frame_2 = QFrame(grey_frame)
grey_frame_2.setStyleSheet("background-color: grey")
grey_frame_2.setFixedSize(300, 50)
grey_label_2 = QLabel("Дніпро",grey_frame_2)
grey_label_2.setStyleSheet("font-size: 28px; font-weight: 700; color: white")
grey_label_2.setContentsMargins(10,10,0,0)
grey_frame_layout.addWidget(grey_frame_2)

grey_frame_3 = QFrame(grey_frame)
grey_frame_3.setStyleSheet("background-color: grey")
grey_frame_3.setFixedSize(300, 30)
grey_label_3 = QLabel("Україна",grey_frame_3)
grey_label_3.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
grey_label_3.setContentsMargins(10,0,0,0)
grey_frame_layout.addWidget(grey_frame_3)






dark_grey_2_frame = QFrame(main_frame)
dark_grey_2_frame.setStyleSheet("background-color: #293545; border-radius: 14px")
dark_grey_2_frame.setFixedSize(300, 210)
layout_Squares_3.addWidget(dark_grey_2_frame)

dark_grey_2_frame_layout = QVBoxLayout(dark_grey_2_frame)

dark_grey_2_frame_1 = QFrame(dark_grey_2_frame)
dark_grey_2_frame_1.setStyleSheet("background-color: #293545")
dark_grey_2_frame_1.setFixedSize(280,160)
dark_grey_2_frame_layout_2 = QHBoxLayout(dark_grey_2_frame_1)
dark_grey_2_label = QLabel("Стан погоди",dark_grey_2_frame_1 )
dark_grey_2_label.setStyleSheet("font-size: 16px; font-weight: 500; color: white")
dark_grey_2_frame_layout.addWidget(dark_grey_2_frame_1)
dark_grey_2_frame_layout_2.addWidget(dark_grey_2_label)
dark_grey_2_frame_layout_2.setAlignment(Qt.AlignmentFlag.AlignCenter)


dark_grey_2_frame_2 = QFrame(dark_grey_2_frame)
dark_grey_2_frame_2.setStyleSheet("background-color: #64f590")
dark_grey_2_frame_2.setFixedSize(280, 50)
dark_grey_2_frame_2_layout_2 = QHBoxLayout(dark_grey_2_frame_2)
dark_grey_2_label_2 = QLabel("Змінити колір",dark_grey_2_frame_2)
dark_grey_2_label_2.setStyleSheet("font-size: 12px; font-weight: 400; color: white")
dark_grey_2_frame_layout.addWidget(dark_grey_2_frame_2)
dark_grey_2_frame_2_layout_2.addWidget(dark_grey_2_label_2)
dark_grey_2_frame_2_layout_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

