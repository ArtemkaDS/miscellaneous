def show_hist(df):
    figure(figsize=(25, 5), dpi=80)
    sns.histplot(data=df, x='Срок_заболевания', 
                 binwidth=3,
                 shrink=.8
                )
    # lines
    y=np.linspace(0,500,100)
    n_std = 1

    target_mean = df['Срок_заболевания'].mean()
    target_median = df['Срок_заболевания'].median()
    target_mode = df['Срок_заболевания'].mode().tolist()
    target_std = df['Срок_заболевания'].std()
    target_std_3_0 = target_mean - df['Срок_заболевания'].std() * n_std
    target_std_3_1 = target_mean + df['Срок_заболевания'].std() * n_std

    plt.plot([target_mean]*100,y,label=f'Среднее значение = {round(target_mean, 1)}', linewidth=2, c='r')
    plt.plot([target_median]*100,y,label=f'Медиана = {round(target_median, 1)}',linestyle='--', linewidth=2, c='y')
    plt.plot([target_std_3_1]*100,y,label=f'Среднее значение + {n_std} sd = {round(target_std_3_1, 1)}', linewidth=2, c='b')

    plt.legend(fontsize=13, frameon=False, loc=5)
    plt.grid(alpha=0.2)
    plt.title(f"Диагноз = {df['Диагноз_code'].unique().tolist()[0]}")
    plt.xticks(ticks=range(0,370, 20))
    plt.show()

    
for x in df_filt['Диагноз_code'].sort_values().unique().tolist():
    show_hist(df=df_filt.loc[df_filt['Диагноз_code'] == x])