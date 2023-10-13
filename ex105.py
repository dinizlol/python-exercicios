def notas(*n, asd=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if asd:
        if r['média'] >= 7:
           r['Situação'] = 'Boa'
        elif r['média'] >= 5:
             r['Situação'] = 'Razoavel'
        else:
             r['Situação'] = 'RUIM'
    return r

resp = notas(5.5, 2.5, 1.5, 10, 8.7, asd=True)
print(resp)

