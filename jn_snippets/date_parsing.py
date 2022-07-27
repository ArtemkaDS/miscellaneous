#dd.mm.yyyy

def date_parser(dataframe, colname, new_colname, new_col_position):
    
    """
    In:
        dataframe: pandas.DataFrame - датасет,
        colname: str - имя столбца, из которого нужно достать дату
        new_col_position: int - позиция нового столбца в датасете
    Out:
        dataFrame с новым столбцом с именем `new_colname` - датой в формате `dd.mm.yyyy`
    """
    
    dataframe['temp1'] = dataframe[colname].str.findall(r'\d+\.\d+\.\d*18|\d+\.\d+\.\d*19|\d+\.\d+\.\d*20|\d+\.\d+\.\d*21|\d+\.\d+\.\d*22')
    dataframe['temp2'] = [','.join(map(str, l)) for l in dataframe['temp1']]
    dataframe.insert(new_col_position, new_colname, (df['temp2'].str.partition(',')[0]))
    dataframe.drop(['temp1', 'temp2'], axis=1, inplace=True)
    return dataframe.head(2)


#ДНЕЙ, СУТОК

def days_parser(x):
    x = re.findall(r'\d+.{,5}суток|\d.{,5}сутки|\d.{,5}дня|\d+.{,5}дней', x)
    if len(x) == 1:
        x = x[0]
        x = re.sub(r'\D+', '', x)
        x = float(x)
        return x
    else:
        return np.nan

#days_comp = (df['Жалобы']).astype('str').apply(days_parser)
#days_anam = (df['Анамнез_заболевания']).astype('str').apply(days_parser)

#df.insert(15, 'Дни из Жалоб', days_comp)
#df.insert(15, 'Дни из Анамнеза', days_anam)

#ВЧЕРА, СЕГОДНЯ

def yesterday_parser(y):
    y = re.findall(r'.чера|.егодня|.уток|.утки', y)
    if len(y) > 0:
        return float(1)
    else:
        return np.nan
    
zhal = (df['Жалобы']).astype('str').apply(yesterday_parser)
anam = (df['Анамнез_заболевания']).astype('str').apply(yesterday_parser)

#df.insert(11, 'tod_yest_zhaloby', zhal)
#df.insert(12, 'tod_yest_anamnez', anam)

#НЕДЕЛЬ

def weeks_parser(x):
    x = re.findall(r'\d+.{,5}недел|\d+.{,5}месяц', x)
    if len(x) == 1:
        x = x[0]
        x = re.sub(r'\D+', '', x)
        x = float(x)
        return x
    else:
        return np.nan

weeks_comp = (df_newmid['Жалобы']).astype('str').apply(weeks_parser)
weeks_anam = (df_newmid['Анамнез_заболевания']).astype('str').apply(weeks_parser)

#df_newmid.insert(10, 'нед_мес из Жалоб', weeks_comp)
#df_newmid.insert(10, 'нед_мес из Анамнеза', weeks_anam)

