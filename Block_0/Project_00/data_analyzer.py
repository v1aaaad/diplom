"""
Project 00: Анализатор демографических данных
Используй функции из statistics_calculator.py для анализа данных
"""

import pandas as pd
import matplotlib.pyplot as plt

from statistics_calculator import median, mean, standard_deviation

# TODO: Импортируй функции из statistics_calculator.py

def load_demography_data(file_path: str) -> pd.DataFrame|None:
    """Загружает демографические данные из CSV файла"""
    try:
        df = pd.read_csv(file_path)
        print(f"Данные успешно загружены, датафрейм создан")
        return df
    except FileNotFoundError:
        print(f"❌ Ошибка: файл {file_path} не найден")
        return None
    except Exception as e:
        print(f"❌ Ошибка загрузки данных: {e}")
        return None

def analyze_population_data(data):
    """Анализирует данные о населении"""
    if not data:  # ✅ Добавить проверку на пустые данные
        print("Нет данных для анализа")
        return
    print(f"Среднее население: {mean(data):,.0f}") # - Среднее население
    print(f"Медиана населения: {median(data):,.0f}") # - Медиану населения
    print(f"Стандартное отклонение: {standard_deviation(data):,.0f}") # - Стандартное отклонение

def bar_plot(data:pd.DataFrame, x_column: str, y_column: str, title: str = ""):

    # 1. КОНЦЕПЦИЯ: Подготовка данных
    # Извлекаем категории и значения из DataFrame
    categories = data[x_column].tolist()
    values = data[y_column].tolist()

    # 2. КОНЦЕПЦИЯ: Создание фигуры и осей
    # fig - весь "холст", ax - область для рисования
    fig, ax = plt.subplots(figsize=(12, 6)) # Задаем размер графика

    # 3. КОНЦЕПЦИЯ: Построение столбцов
    # bars - объект, содержащий все столбцы (полезно для дальнейшей настройки)
    bars = ax.bar(categories, values, color='skyblue', alpha=0.7, edgecolor='navy')

    # 4. КОНЦЕПЦИЯ: Настройка внешнего вида
    # Заголовок и подписи осей
    ax.set_title(title if title else f"{y_column} по {x_column}", fontsize=14, pad=20)
    ax.set_xlabel(x_column, fontsize=12)
    ax.set_ylabel(y_column, fontsize=12)

    # 5. КОНЦЕПЦИЯ: Настройка осей
    # Поворачиваем подписи категорий для лучшей читаемости
    ax.tick_params(axis='x', rotation=45)

    # 6. КОНЦЕПЦИЯ: Добавление сетки
    ax.grid(True, axis='y', alpha=0.3, linestyle='--')

    # 7. КОНЦЕПЦИЯ: Подписи значений на столбцах (опционально)
    # Показываем числовые значения над каждым столбцом
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + max(values)*0.01,
                f'{height:,.0f}', ha='center', va = 'bottom', fontsize=9)

    # 8. КОНЦЕПЦИЯ: Автоматическая подгонка layout
    plt.tight_layout()    # Предотвращает обрезание подписей

    # 9. КОНЦЕПЦИЯ: Показ графика
    plt.show()

    # 10. КОНЦЕПЦИЯ: Возврат объектов для дальнейшей кастомизации
    return fig, ax

def histogram_plot(data: pd.DataFrame, column: str, title: str = "", bins: int = 10):
    pass

def pie_plot(data: pd.DataFrame, values_column: str, labels_column: str, title: str = ""):
    pass

def scatter_plot(data: pd.DataFrame, x_column: str, y_column: str, title: str = ""):
    pass

def visualize_data(data: pd.DataFrame, plot_type: str, **kwargs):
    """Визуализирует демографические данные"""
    # TODO: Построй график населения по городам
    plot_functions = {
        'bar': bar_plot,
    }
    try:
        plot_function = plot_functions[plot_type]
        return plot_function(data, **kwargs)  # Передаем все дополнительные параметры
    except Exception as e:
        print(f"❌ Ошибка при построении графика '{plot_type}': {e}")
        return None
    pass

if __name__ == "__main__":
    # TODO: Загрузи данные из data/simple_demography.csv
    # Проанализируй и визуализируй их
    print("Анализатор демографических данных")

    df = load_demography_data('data/simple_demography.csv')
    population = df.population.tolist()

    analyze_population_data(population)

    visualize_data(df, 'bar',
                   x_column='city',
                   y_column='population',
                   title='Население городов')
