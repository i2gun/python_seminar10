from pandas import read_csv
from seaborn import scatterplot, relplot, histplot
from matplotlib.pyplot import show

data = read_csv('california_housing_test.csv')


def first():
    scatterplot(data=data, x='households', y='population')
    show()


    # 1. Изобразите отношение households к population с
    # помощью точечного графика
# first()


def second():
    relplot(x="longitude", y="median_house_value", kind="line", data=data)
    show()


    # 2. Визуализировать longitude по отношения к
    # median_house_value, используя линейный график
# second()

# Гистограммы агрегируют числовые данные по группам с равными интервалами,
# которые называют бинами, и отображают частоту
# встречаемости значений в каждом из бинов
# second()
def third():
    histplot(data=data, x="housing_median_age")
    show()


    # 3. Представить гистограмму по housing_median_age
# third()


def fourth():
    histplot(data=data, x="median_house_value", hue="housing_median_age")
    show()


    # 4. Изобразить гистограмму по median_house_value с
    # оттенком housing_median_age
fourth()
