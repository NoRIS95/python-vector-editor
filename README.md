# Векторный редактор с интерфейсом командной строки (CLI)
С помощью этого редактора можно создавать различные фигуры (точку, отрезок,круг, квадрат), отображать все созданные фигуры, удалять какую-нибудь фигуру по индексу.

## Функционал:
- **Создание фигур**: точка, отрезок, круг, квадрат.
- **Удаление фигуры**: по индексу.
- **Отображение списка фигур**: вывод всех созданных фигур в консоль.
- **Выход из программы**: завершение работы редактора.

## Доступные команды:
- `создать`: создать новую фигуру.
- `удалить`: удалить фигуру по индексу.
- `отобразить`: показать список всех фигур.
- `помощь`: вывести список доступных команд.
- `выход`: завершить работу программы.

## Инструкция по запуску редактора:
1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Клонируйте репозиторий с GitHub и перейдите в директорию проекта:
```bash
git clone https://github.com/NoRIS95/python-vector-editor.git
cd python-vector-editor
```
3. Запустите скрипт
```bash
python3 main.py
```

## Пример использования:
1. Запустите программу:
```bash
python3 main.py
```
2. Создайте фигуру
```bash
Введите команду (создать, удалить, отобразить, помощь или выход):
создать
Какую фигуру хотите создать (введите точка, отрезок, круг или квадрат)?
отрезок
Введите x и y первой точки через пробел: 0 1  
Введите x и y второй точки через пробел: 0 2
Отрезок успешно создан
```
3. Отобразите созданные фигуры
```bash
Введите команду (создать, удалить, отобразить, помощь или выход):
отобразить
0: Отрезок (Точка(0.0, 1.0), Точка(0.0, 2.0))
```
4. Удалите фигуру
```bash
Введите команду (создать, удалить, отобразить, помощь или выход):
удалить
Введите индекс фигуры в списке, которую хотите удалить: 0
Фигура успешно удалена
```

## Требования:
- Python 3.8 или выше.
- Дополнительные зависимости отсутствуют.
