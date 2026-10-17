"""Заглушки «кейс в разработке» для С Верой, Вадима Орехова, The Bloom и Brewns.

Повторяют окно с сайта-резюме: папка с искрами, «Кейс ещё собирается»
и кнопка «Ладно, подожду», которая закрывает окно.

Запуск: python3 stub.py — JSON для update_zero_block появятся в out/stub-*.json.
"""
import os
from zb import *

SMALL = (600, 600, 600, 440, 320)

FOLDER = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -12 180 129" fill="none" role="img" aria-label="Папка">'
          '<rect x="3.6" y="0.5" width="172.8" height="103.9" rx="8" fill="#FFF8C7" stroke="#6F8FBE"/>'
          '<path d="M3.6 2V-2a9 9 0 0 1 9-9h55.6a9 9 0 0 1 9 9V2" fill="#FFF8C7" stroke="#6F8FBE"/>'
          '<rect class="os-p1" x="10.8" y="4.6" width="151.2" height="58" rx="10" fill="#F4EBAA" stroke="#6F8FBE" transform="rotate(-2 86.4 33.6)"/>'
          '<rect class="os-p2" x="25.2" y="7" width="147.6" height="58" rx="10" fill="#E9DD8E" stroke="#6F8FBE" transform="rotate(1.5 99 36)"/>'
          '<rect x="0.5" y="44.5" width="179" height="71" rx="10" fill="#FFF8C7" stroke="#6F8FBE"/></svg>')


def spark(fs, delay, top, left):
    # искра мигает так же, как на заставке (osSpark в global-code.html)
    html = f'<span style="display:inline-block;animation:osSpark 1.6s {delay}s ease-in-out infinite">✦</span>'
    return T(html, fs, lh=1, w='hug', fit='autowidth', absolute='y', top=top, left=left)


def icon():
    return G([VEC(FOLDER, 180, 129, 120, cls='os-folder'),
              spark(18, 0, -10, 112), spark(12, 0.5, 26, -14), spark(13, 1, 70, 98)],
             w=120, name='Папка с искрами')


def stub(name):
    body = [
        icon(),
        T('Work in progress', 11, color=MUTED, upper=True, ls=0.44, lh=1.3, align='center', margin='10px 0px 0px 0px'),
        T('Кейс ещё<br />собирается', (44, 44, 40, 34, 30), 700, upper=True, ls=-2, lh=0.92, align='center', tag='h2'),
        T('Я уже раскладываю всё по папочкам. Скоро здесь будет новый проект :)', 14, color=MUTED, lh=1.55,
          align='center', w=(380, 380, 380, 'fill', 'fill')),
        BTN('Ладно, подожду', '#closepopup', blank=False),
    ]
    for i, n in enumerate(body):
        anim(n, 0.12 + i * 0.06)
    win = window(f'Case · {name} · в разработке', body, width=SMALL, gap=14)
    content = win.children[1]
    content.props['flexalignitems'] = 'center'
    for k in [k for k in content.props if k.startswith('padding')]:
        del content.props[k]
    put(content.props, 'padding', ('40px 28px 40px 28px',) * 3 + ('32px 18px 32px 18px',) * 2)
    return win


if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    jobs = [('vera', 'С Верой', '1792170100000'), ('orehov', 'Вадим Орехов', '1792170200000'),
            ('bloom', 'The Bloom', '1792170300000'), ('brewns', 'Brewns', '1792170400000')]
    for key, name, prefix in jobs:
        data = build(stub(name), prefix, popup_artboard(f'Окно кейса: {name}, в разработке (#case-{key})', (640,) * 5))
        dump(data, f'out/stub-{key}.json')
        print(key, len(open(f'out/stub-{key}.json', encoding='utf-8').read()))
