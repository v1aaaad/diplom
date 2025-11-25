"""
Project 01: Мастер визуализации данных
Реализуй различные типы графиков для анализа данных
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_city_data(file_path: str) -> pd.DataFrame | None:
    """Загружает расширенные данные о городах."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Данные загружены: {len(df)} городов")
        return df
    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        return None

# TODO: Реализуй функции визуализации
def bar_plot(data: pd.DataFrame, x_column: str, y_column: str, title: str = "", save_path: str = None):
    """Столбчатая диаграмма для сравнения категорий."""
    pass

def histogram_plot(data: pd.DataFrame, column: str, title: str = "", bins: int = 10, save_path: str = None):
    """Гистограмма для анализа распределения."""
    pass

def pie_plot(data: pd.DataFrame, values_column: str, labels_column: str, title: str = "", save_path: str = None):
    """Круговая диаграмма для отображения долей."""
    pass

def line_plot(data: pd.DataFrame, x_column: str, y_column: str, title: str = "", save_path: str = None):
    """Линейный график для трендов."""
    pass

def scatter_plot(data: pd.DataFrame, x_column: str, y_column: str, title: str = "", save_path: str = None):
    """Точечная диаграмма для корреляций."""
    pass

def visualize_data(data: pd.DataFrame, plot_type: str, **kwargs):
    """Универсальная функция визуализации."""
    plot_functions = {
        'bar': bar_plot,
        'histogram': histogram_plot,
        'pie': pie_plot,
        'line': line_plot,
        'scatter': scatter_plot
    }
    
    if plot_type in plot_functions:
        return plot_functions[plot_type](data, **kwargs)
    else:
        print(f"❌ Неподдерживаемый тип: {plot_type}")
        return None

def create_dashboard(data: pd.DataFrame):
    """Создает дашборд с разными типами визуализаций."""
    print("📊 Создание дашборда...")
    # TODO: Реализовать создание сетки графиков
    pass

if __name__ == "__main__":
    print("🎨 Project 01: Мастер визуализации данных")
    
    # Загрузка данных
    df = load_city_data('data/cities_extended.csv')
    if df is not None:
        print("Первые 5 строк данных:")
        print(df.head())
        
    # TODO: Тестирование функций визуализации
