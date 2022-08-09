%%time
print(f"Количество файлов = {len([i for i in path_data_source.glob('**/*xls*')])}\n")
df_0 = {
    '-обр': pd.DataFrame(),
    '-конс': pd.DataFrame(),
    '-ли': pd.DataFrame(),
    '-ид': pd.DataFrame(),
    '-опер': pd.DataFrame()
}
for n, f in enumerate(path_data_source.glob('**/*xls*'), start=1):
    mo_name = f.parent.name
    for pref in df_0.keys():
        if '~$' not in str(f.name).lower():
            if pref in str(f.name).lower():
                print(n, f, end='| ')
                df_one = pd.read_excel(io=f)
                df_one = df_one.assign(**{"Мед_организация": mo_name})
                df_0[pref] = pd.concat([df_0[pref], df_one])
                print(df_one.shape)
                del df_one

print('end!')