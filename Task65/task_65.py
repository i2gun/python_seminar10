# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы


# Seaborn — библиотека для создания статистических графиков на Python
# разведочный анализ данных (EDA) по заданному дата сету
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import load_dataset, scatterplot, PairGrid, displot

penguins = load_dataset("penguins")


# ● Использовать 2-3 точечных графика
def f_1():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
    plt.show()


# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# hue='sex' - разбивка по полу
# size=island - сгруппировал пингвинов по разному размеру точек
def f_2():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g",
                hue='sex', size='island', style='island')
    plt.show()


# ● Использовать PairGrid с типом графика на ваш выбор
# создадим объект класса PairGrid, в качестве данных передадим ему
# как количественные, так и категориальные переменные
def f_3():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm",
              "flipper_length_mm"]
    y_vars = ['sex']
    g = PairGrid(penguins, x_vars=x_vars, y_vars=y_vars, hue='species')
    g.map(scatterplot)
    plt.show()


# ● Изобразить Heatmap
def f_4():


    data = penguins.pivot_table(index='species', columns='island',
                                values='body_mass_g')
    sns.heatmap(data)
    plt.xlabel('Остров', size=14)
    plt.ylabel('Вид пингвина', size=14)
    plt.show()


# ● Использовать 2-3 гистограммы
def f_5():
    penguins['bill_depth_mm'].hist(bins=10)
    plt.show()


# 4. Изобразить Heatmap
# g = penguins.corr()
# sns.heatmap(g)
# glue = sns.load_dataset("glue").pivot(index="Model",
#                                       columns="Task", values="Score")
# sns.heatmap(glue)
