import matplotlib.pyplot as plt
import matplotlib.image as mpimg

file_name = "echo_2.dcm"
print("Открываю снимок УЗИ...")

# Этот блок загружает картинку и выводит её на ваш экран
img = mpimg.imread(file_name)
plt.imshow(img)
plt.axis('off')  # Отключаем сетку и пиксельные оси вокруг снимка
plt.title("Ваш УЗИ-снимок в Python")
plt.show()