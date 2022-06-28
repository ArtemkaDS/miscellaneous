# Сниппеты для jupyter notebook

1. Расширение экрана
```python
# Расширение экрана
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

# Options for pandas
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
pd.options.display.max_columns = 50
pd.options.display.max_rows = 30
pd.set_option('max_colwidth', 200)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)
```

2. Сохранение ноутбука без кода
```shell
jupyter nbconvert --no-input report_DQ_epic_li_2022-05-12 --to html
```

3. Пишем все в один файл Excel
```python
with pd.ExcelWriter(path=Path(path_dir.parent, 'data_calculated', "outliers_3std_2022-04-21.xlsx")) as writer:
    df_only_outliers.to_excel(writer, sheet_name="Выбросы avg_per_day", index=False)
    df_with_outliers_pivot.to_excel(writer, sheet_name="Статистика по стационарам", index=False)
    df_3.to_excel(writer, sheet_name='Статистика по группам', index=False)
```

4. Полезное:
- 
```python
df.assign(**{
    'X-Axis': np.random.rand(len(df)), 
    'Y-Axis': lambda in_: in_['X-Axis'] ** 2
    })
```
