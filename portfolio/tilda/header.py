"""Шапка главной: логотип, меню, часы и общий код сайта (global-code.html).

Запуск: python3 header.py — JSON для update_zero_block появится в out/header.json.
"""
from zb import *

code = open('global-code.html', encoding='utf-8').read()

nav = [('Услуги и цены', '#services'), ('Как работаю', '#process'), ('Обо мне', '#about'),
       ('Вопросы', '#faq'), ('Контакты', '#contact')]
logo = G([T('OS', 9, 700, color=PT, lh=1, w=26, h=26, fit='fixedsize', align='center', valign='middle',
            borderwidth='1px 1px 1px 1px', bordercolor=PT, borderstyle='solid', borderradius='30px 30px 30px 30px'),
          T('Oksana Sergeeva', 14, 700, color=PT, lh=1.2, ls=0.3, upper=True, w='hug', fit='autowidth')],
         dir='row', gap=12, align='center', w='hug', link='#closeallpopup', name='Логотип')
menu = G([T(t, 11, color=PT, lh=1.2, ls=0.44, upper=True, w='hug', fit='autowidth', link=l, cls='os-nav') for t, l in nav],
         dir='row', gap=28, align='center', w='hug', name='Меню', tag='nav', hidden=('n', 'n', 'y', 'y', 'y'))
left = G([logo, menu], dir='row', gap=28, align='center', w='hug', name='Слева', tag='header')
html = N('el', {'elem_type': 'html', 'code': code, 'widthmode': 'fixed', 'heightmode': 'fixed', 'width': '100',
                'height': '14', 'top': '0', 'left': '0', 'layer': 'Код: шрифт, часы, темы, загрузка, окна, кейсы'})
line = SHAPE(100, 1, PT, opacity=0.25, absolute='y', container='window', axisy='bottom', widthunits='%',
             excludefromautoheight='y')

ab = {'ab_title': 'Шапка + общий код сайта', 'ab_flex': 'auto', 'ab_flexcontainer': 'window', 'ab_heightmode': 'hug',
      'ab_flexdirection': 'row', 'ab_flexalignitems': 'center', 'ab_flexjustifycontent': 'space-between',
      'ab_flexgapx': '28', 'ab_bgcolor': BG, 'ab_bgattachment': 'scroll', 'ab_screens': '360,480,640,960,1200'}
put(ab, 'ab_padding', ('14px 32px 14px 32px',) * 2 + ('14px 20px 14px 20px',) + ('14px 16px 14px 16px',) * 2)
for w in SCREENS:
    ab['ab_height' if w == 1200 else f'ab_height-res-{w}'] = '56'

if __name__ == '__main__':
    import os
    os.makedirs('out', exist_ok=True)
    dump(build([left, html, line], '1792164000000', ab), 'out/header.json')
    print(len(open('out/header.json', encoding='utf-8').read()))
