def search_pat(df, new_col, pattern):
    col_list = ['Заключение', 'Рекомендации']
    temp_col = df.loc[:, col_list].astype('str').agg('|'.join, axis=1)
    df[new_col] = np.where(temp_col.str.lower().str.contains(pattern, regex=True), 1, 0)
    return df

df_filt \
    .pipe(search_pat, 'Невр', r'невролог') \
    .pipe(search_pat, 'Тер', r'терапевт')