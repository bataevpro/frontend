import pydicom

# Исправленная строка: параметр force=True теперь строго внутри скобок
ds = pydicom.dcmread('echo_2.dcm.png', force=True)

print("=== МЕТАДАННЫЕ УЗИ-СНИМКА ===")
# Используем getattr, чтобы программа не вылетала, если какого-то тега нет в файле
print(f"Пациент (ID): {getattr(ds, 'PatientID', 'Не указан')}")
print(f"Модальность: {getattr(ds, 'Modality', 'Не указана')}")
print(f"Производитель аппарата: {getattr(ds, 'Manufacturer', 'Не указан')}")
print(f"Модель аппарата: {getattr(ds, 'ManufacturerModelName', 'Не указана')}")
print(f"Дата исследования: {getattr(ds, 'StudyDate', 'Не указана')}")