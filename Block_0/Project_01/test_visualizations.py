"""
Тестирование функций визуализации
"""

from data_visualization_master import visualize_data, load_city_data

def test_all_visualizations():
    """Тестирует все типы визуализаций."""
    df = load_city_data('data/cities_extended.csv')
    
    if df is not None:
        print("🧪 Тестирование визуализаций...")
        
        # TODO: Добавить тесты для каждой функции
        # visualize_data(df, 'bar', x_column='city', y_column='population')
        # visualize_data(df, 'histogram', column='population')
        # и т.д.

if __name__ == "__main__":
    test_all_visualizations()
