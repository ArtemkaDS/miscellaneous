%%time

calc_1 = df_ii_0.copy()
calc_1 = calc_1.fillna('-')

calc_1['Патологии не выявлено'] = np.where(calc_1['Результат_исследования'].str.lower().str.contains(r'.атол.+не выявле.+', regex=True), 1, 0)
calc_1['Вазоневральный'] = np.where(calc_1['Результат_исследования'].str.lower().str.contains(r'.+азо.{,3}невраль.+|нейро.{,3}васкуляр.*', regex=True), 1, 0)
calc_1['Опухоль'] = np.where(calc_1['Результат_исследования'].str.lower().str.contains(r'.пухоль|об[ъ,ь]емн|образован', regex=True), 1, 0)
calc_1['Демиелиниз'] = np.where(calc_1['Результат_исследования'].str.lower().str.contains(r'.емиелиниз|рассеянный', regex=True), 1, 0)
calc_1['Инсульт'] = np.where(calc_1['Результат_исследования'].str.lower().str.contains(r'[О,о]чаг|ишеми|.нсульт|наруш.+мозгово.+', regex=True), 1, 0)
calc_1['Травма'] = np.where(calc_1['Результат_исследования'].str.lower().str.contains(r'.равм|.ерелом|.рещин[н]*.', regex=True), 1, 0)