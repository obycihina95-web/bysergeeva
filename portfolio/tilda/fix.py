"""Общие исправления для JSON Zero Block.

Кнопки. В автолейауте Тильда ставит кнопке height:auto и игнорирует
заданную высоту, поэтому без вертикальных отступов кнопка сжимается
до высоты строки. Даём кнопкам отступы 14/24 и шрифт 13px.

(Ряды карточек переносились из-за невидимой рамки 3px у групп,
это исправлено в global-code.html.)

Запуск: python3 fix.py in.json out.json
"""
import json
import sys

SCREENS = ['', '-res-960', '-res-640', '-res-480', '-res-360']
BTN_PAD = '14px 24px 14px 24px'


def fix_buttons(d):
    for k, e in d.items():
        if not k.isdigit() or e.get('elem_type') != 'button':
            continue
        e['fontsize'] = '13'
        if e.get('textfit') == 'fixedsize':
            # кнопка во всю ширину: высоту держит сама, отступы только по бокам
            e['padding'] = '0px 24px 0px 24px'
            for s in SCREENS:
                if ('height' + s) in e:
                    e['height' + s] = '48'
        else:
            e['padding'] = BTN_PAD
            for s in SCREENS:
                if ('height' + s) in e:
                    e['height' + s] = '48'


def fix_all(d):
    fix_buttons(d)
    return d


if __name__ == '__main__':
    d = json.load(open(sys.argv[1], encoding='utf-8'))
    fix_all(d)
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, separators=(',', ':'))
