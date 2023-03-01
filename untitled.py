# Задача 1 Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

df[
    (df['population'] > 0) &
    (df['population'] < 500)
].median_house_value.mean()


# Задача 42: Узнать какая максимальная households в зоне минимального значения population
min_population = df.population.min()
df[
    df['population'] == min_population
].households.max()