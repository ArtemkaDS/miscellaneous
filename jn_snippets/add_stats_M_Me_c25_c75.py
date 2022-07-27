def f1_stats(x):
    N = x.count()
    M, Me, sd = round(x.mean(), 1), x.median(), round(x.std(), 1)
    
    c25, c75 = round(x.quantile(.25), 1), round(x.quantile(.75), 1)
    if str(x.mean()) == 'nan':
        r = np.nan
    else:
        r = f'{M=}' if len(x) == 1 else f'{N=} {M=}±{sd} | {Me=}[{c25}, {c75}]'
    
    return r


def c25_c75(x):
    c25, c75 = x.quantile(.25), x.quantile(.75)
    return c25, c75