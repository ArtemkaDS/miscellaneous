calc_1['Отсутствие мимики'] = np.where(calc_1['Жалобы'].str.lower().str.contains(r'отсутств.+мими.*|наруш.+мими.*', regex=True), 1, 0)



calc_2 = calc_1.melt(id_vars=calc_1.columns[:21], 
            value_vars=calc_1.columns[21:], 
            var_name='Параметр', 
            value_name='Значение')
calc_2 = calc_2.query('Значение == 1')
# display(calc_2.head())
calc_2.groupby('Параметр').agg({"Значение": 'sum',
                                "emias_id": 'nunique'
                               })