kleur = input('is de kaas geel?: ')
if kleur == 'ja':
    gaten = input('zitten er gaten in?: ')
    if gaten == 'ja':
        duur = input('is de kaas belachelijk duur?: ')
        if duur == 'ja':
            print('Emmenthaler')
        else:
            print('Leerdammer')
    else:
        hard = input('is de kaas hard als steen?: ')
        if hard == 'ja':
            print('Parmigiano Reggiano')
        else:
            print('Goudse kaas')
else:
    schimmel = input('heeft de kaas blauwe schimmel?: ')
    if schimmel == 'ja':
        korst1 = input('heeft de kaas korst?: ')
        if korst1 == 'ja':
            print('Blue de Rochbaron')
        else:
            print('Foume Dambert')
    else:
        korst2 = input('heeft de kaas korst?: ')
        if korst2 == 'ja':
            print('Camembert')
        else:
            print('Mozarella')