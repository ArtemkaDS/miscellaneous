path_source = Path(f'../data/выгрузка_2023-01-24/')

df_0 = {'-обр': pd.DataFrame(), '-наз': pd.DataFrame()}
df_0['-обр'] = pd.concat([pd.read_excel(f) for f in path_source.glob('**/*xls*') if 'Таблица_1' in f.name])
df_0['-наз'] = pd.concat([pd.read_excel(f) for f in path_source.glob('**/*xls*') if 'Назначения' in f.name])