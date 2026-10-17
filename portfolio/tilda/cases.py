"""Окна больших кейсов (Баловень, Lara Shell, СКЭНАР-терапия, Нина).

Запуск: python3 cases.py — JSON для update_zero_block появятся в out/.
Тексты и порядок блоков повторяют portfolio/index.html.
"""
import os
from zb import *

CDN = 'https://static.tildacdn.com/'
IMG_ = {
    'baloven': ('tild6631-3035-4463-b133-376530613334/baloven.jpg', 1200, 750),
    'baloven-afisha': ('tild3331-3932-4630-a139-373231336635/baloven-afisha.jpg', 1200, 525),
    'baloven-lunch': ('tild3165-3233-4334-b636-366432643661/baloven-lunch.jpg', 1200, 603),
    'baloven-paths': ('tild6362-6330-4432-a461-393134346165/baloven-paths.jpg', 1200, 330),
    'baloven/full-index': ('tild6664-3839-4362-b438-643764333166/full-index.jpg', 1000, 4509),
    'baloven/full-about': ('tild3731-3332-4034-b361-393835386465/full-about.jpg', 1000, 2714),
    'baloven/full-afisha': ('tild3333-3865-4138-a132-336661633530/full-afisha.jpg', 1000, 4002),
    'baloven/full-banquets': ('tild6531-3165-4762-b439-333330623238/full-banquets.jpg', 1000, 3781),
    'baloven/full-booking': ('tild3264-6664-4161-b962-303232353436/full-booking.jpg', 1000, 1330),
    'baloven/full-kvartirniki': ('tild3932-3835-4138-b330-363564336662/full-kvartirniki.jpg', 1000, 4277),
    'baloven/full-menu': ('tild3066-6532-4732-b639-663835363865/full-menu.jpg', 1000, 7151),
    'baloven/kit-event': ('tild3366-3937-4232-b262-393638303066/kit-event.jpg', 1400, 159),
    'baloven/kit-filters': ('tild3932-6237-4863-b462-653162393066/kit-filters.png', 1692, 88),
    'baloven/kit-format': ('tild3465-6166-4135-a238-666334343033/kit-format.jpg', 572, 802),
    'baloven/mob-afisha': ('tild3339-3762-4436-b565-326463656363/mob-afisha.jpg', 390, 8000),
    'baloven/mob-index': ('tild3034-6339-4333-a562-303632356231/mob-index.jpg', 390, 8000),
    'baloven/mob-menu': ('tild3539-3932-4234-a138-653331373037/mob-menu.jpg', 390, 8000),
    'lara': ('tild6336-3335-4232-a130-626164636230/lara.jpg', 1200, 750),
    'lara/full-index': ('tild6464-6664-4939-a330-303066376365/full-index.jpg', 1000, 8000),
    'lara/full-blog': ('tild3264-6364-4564-a532-396464373239/full-blog.jpg', 1000, 3744),
    'lara/full-children': ('tild6165-6435-4539-a138-323031643264/full-children.jpg', 1000, 5418),
    'lara/full-massage': ('tild3762-6336-4733-b830-396638303764/full-massage.jpg', 1000, 6101),
    'lara/full-obuchenie': ('tild3838-3366-4337-a331-663134636262/full-obuchenie.jpg', 1000, 6500),
    'lara/full-shop': ('tild3931-6437-4938-b931-316539653764/full-shop.jpg', 1000, 4135),
    'lara/mob-index': ('tild3533-6234-4335-b236-613062386664/mob-index.jpg', 390, 8000),
    'lara/mob-massage': ('tild6431-3561-4132-b138-383866636664/mob-massage.jpg', 390, 8000),
    'lara/mob-shop': ('tild3132-3666-4539-a662-373463303138/mob-shop.jpg', 390, 8000),
    'lara/navigator': ('tild3364-6533-4266-a538-646266326435/navigator.jpg', 1100, 943),
    'lara/prices': ('tild6231-6666-4864-b162-633239363635/prices.jpg', 1100, 950),
    'lara/voice': ('tild3862-6265-4061-b539-383530393037/voice.jpg', 1200, 750),
    'nina/mob-index': ('tild3731-3166-4535-b630-646633386363/mob-index.jpg', 430, 2810),
    'nina/sections': ('tild3661-6535-4566-a130-336161323032/sections.jpg', 430, 920),
    'scenar': ('tild6464-6562-4365-b137-643538306164/scenar.jpg', 1200, 750),
    'scenar/full-index': ('tild3661-6333-4835-b733-306337303165/full-index.jpg', 1000, 8000),
    'scenar/full-kontakty': ('tild6432-3635-4930-b136-666165333436/full-kontakty.jpg', 1000, 2017),
    'scenar/full-magazin': ('tild3535-3631-4133-a230-383632643633/full-magazin.jpg', 1000, 3322),
    'scenar/full-o-nas': ('tild3433-3332-4965-b734-666664306662/full-o-nas.jpg', 1000, 3956),
    'scenar/full-otzyvy': ('tild3361-6262-4632-b535-383666343461/full-otzyvy.jpg', 1000, 2801),
    'scenar/full-prajs-list': ('tild3665-3463-4565-b232-653832363763/full-prajs-list.jpg', 1000, 3163),
    'scenar/full-shkola': ('tild6237-3362-4335-b934-363437336432/full-shkola.jpg', 1000, 3757),
    'scenar/full-stati': ('tild3536-3961-4063-a463-396666396232/full-stati.jpg', 1000, 2146),
    'scenar/full-uslugi': ('tild6131-3835-4038-b233-633834383261/full-uslugi.jpg', 1000, 4381),
    'scenar/mob-index': ('tild3764-6135-4533-a630-616436643930/mob-index.jpg', 390, 8000),
    'scenar/mob-magazin': ('tild3362-6362-4531-a139-633165623938/mob-magazin.jpg', 390, 8000),
    'scenar/mob-uslugi': ('tild6634-6432-4138-b364-313763613337/mob-uslugi.jpg', 390, 8000),
    'scenar/navigator': ('tild3035-3833-4430-b064-333436393139/navigator.jpg', 1100, 1188),
    'scenar/prices': ('tild3561-3663-4662-b031-626237626166/prices.jpg', 1100, 812),
    'scenar/route': ('tild3664-6438-4332-b038-386635363036/route.jpg', 1100, 839),
    'scenar/voice': ('tild3263-3933-4462-b233-313839316530/voice.jpg', 1200, 750),
}


def url(k):
    return CDN + IMG_[k][0]


def img(k, **kw):
    u, fw, fh = IMG_[k]
    return IMG(CDN + u, fw, fh, **kw)


INNER = WIDE_IN
TEXT_W = (414, 334, 'fill', 'fill', 'fill')   # колонка текста в решении
SHOT_W = (622, 502, 'fill', 'fill', 'fill')   # колонка картинки в решении
H2 = dict(fs=(60, 48, 34, 34, 34), fw=700, upper=True, ls=(-3.9, -3.1, -2.2, -2.2, -2.2), lh=0.88)
H3_SHOW = (29, 23, 20, 20, 20)
CHIP = 'display:inline-block;border:1px solid #6F8FBE;border-radius:999px;padding:4px 10px;margin:0 6px 6px 0'
KIND = 'display:inline-block;background:#24334D;color:#FFF8C6;border:1px solid #24334D;border-radius:999px;padding:4px 10px;margin:0 6px 6px 0'


def meta(kind, *items):
    html = f'<span style="{KIND}">{kind}</span>' + ''.join(f'<span style="{CHIP}">{i}</span>' for i in items)
    return T(html, 10, upper=True, ls=0.4, lh=1.2, margin='0px 0px -6px 0px')


def caseno(n):
    return T(n, 11, color=MUTED, lh=1.3)


def shot(k, w='fill', radius=12, hero=False, **kw):
    return G([img(k, cls='os-shot', alt='')], w=w, radius=radius, bg=SHOT, border=('1px 1px 1px 1px', LINE),
             overflow='hidden hidden', name='Скриншот',
             **({'shadows': '0px 20px 50px 0px rgba(0,0,0,0.12)'} if hero else {}), **kw)


def pain(p1, p2):
    st = dict(fs=(21, 17, 17, 17, 17), fw=500, lh=1.35, ls=-0.3, w=(600, 600, 'fill', 'fill', 'fill'))
    return G([T(p1, **st), T(p2, color=MUTED, **st)], gap=8, pad='4px 0px 4px 18px',
             border=('0px 0px 0px 3px', ACT), name='Боль')


def sol(n, h3, p, right, flip=False):
    text = G([caseno(n), T(h3, (26, 21, 20, 20, 20), 700, lh=1.05, ls=-0.8), T(p, 14, lh=1.55)],
             gap=8, w=TEXT_W, name='Текст решения', **({'flexorder': ('1', '1', '0', '0', '0')} if flip else {}))
    pic = G([right], w=SHOT_W, name='Картинка решения')
    return G([text, pic], dir=('row', 'row', 'column', 'column', 'column'), gap=(28, 28, 16, 16, 16),
             align=('center', 'center', 'flex-start', 'flex-start', 'flex-start'), name=f'Решение {n}')


def sol_wide(n, h3, p, k):
    text = G([caseno(n), T(h3, (36, 29, 24, 24, 24), 700, lh=1.05, ls=-1.1), T(p, 14, lh=1.55)],
             gap=8, w=(640, 640, 'fill', 'fill', 'fill'), name='Текст решения')
    return G([text, shot(k)], gap=16, name=f'Решение {n}')


def show_head(label, h3, p):
    left = G([caseno(label), T(h3, H3_SHOW, 700, lh=1.05, ls=-0.9, margin='6px 0px 0px 0px')], w='fill', name='Заголовок')
    return G([left, T(p, 13, color=MUTED, lh=1.5, w=(420, 380, 'fill', 'fill', 'fill'))],
             dir=('row', 'row', 'column', 'column', 'column'), gap=(20, 20, 10, 10, 10),
             align=('flex-end', 'flex-end', 'flex-start', 'flex-start', 'flex-start'), name='Шапка раздела')


def site_show(h3, tabs, first_url):
    """tabs: [(подпись, ключ картинки, адрес)]"""
    tab_els = []
    for i, (name, key, addr) in enumerate(tabs):
        tab_els.append(T(name, 12, lh=1.2, w='hug', fit='autowidth', cls='os-tab' + (' os-on' if i == 0 else ''),
                         padding='8px 14px 8px 14px', borderwidth='1px 1px 1px 1px', bordercolor=LINE,
                         borderstyle='solid', borderradius='999px 999px 999px 999px',
                         attributes=f'src={url(key)}&amp;url={addr}'))
    dots = [SHAPE(9, 9, LINE, figure='circle', borderradius='3000px 3000px 3000px 3000px') for _ in range(3)]
    bar = G(dots + [T(first_url, 11, color=MUTED, lh=1.3, w=(340, 340, 'fill', 'fill', 'fill'), cls='os-url',
                      bgcolor=PANEL, padding='4px 10px 4px 10px', borderradius='6px 6px 6px 6px',
                      margin='0px 0px 0px 10px')],
            dir='row', gap=6, pad='10px 12px 10px 12px', align='center', bg=SHOT,
            border=('0px 0px 1px 0px', LINE), name='Строка браузера')
    view = G([img(tabs[0][1], cls='os-view', alt='Страница сайта целиком')], h=(560, 560, 520, 480, 440),
             overflow='hidden auto', name='Окно браузера (листается)')
    browser = G([bar, view], radius=14, bg='#ffffff', border=('1px 1px 1px 1px', LINE), overflow='hidden hidden',
                shadows='0px 20px 50px 0px rgba(0,0,0,0.12)', name='Браузер')
    return G([show_head('Весь сайт', h3, 'Переключайте страницы и листайте внутри окна.'),
              G(tab_els, dir='row', gap=6, pad='0px 0px 10px 0px', overflow='auto hidden', name='Вкладки страниц',
                margin='14px 0px 0px 0px'),
              browser], name='Весь сайт')


PHONE = (230, 230, 200, 200, 200)
PHONE_H = (473, 473, 411, 411, 411)


def phone(key, caption, delay='', w=PHONE, h=PHONE_H):
    inner_w = tuple(x - 16 for x in w)
    notch_w = tuple(round(x * 0.34) for x in inner_w)
    notch = SHAPE(notch_w, 14, ACT, absolute='y', top=6,
                  left=tuple(round((a - b) / 2) for a, b in zip(inner_w, notch_w)),
                  borderradius='999px 999px 999px 999px')
    screen = G([notch, img(key, cls=('os-scroll ' + delay).strip(), alt=caption)], w=w, h=h, radius=30, bg='#ffffff',
               border=('8px 8px 8px 8px', ACT), overflow='hidden hidden',
               shadows='0px 18px 40px 0px rgba(0,0,0,0.15)', name='Экран телефона')
    return G([screen, T(caption, 11, color=MUTED, upper=True, ls=0.55, lh=1.3, w='hug', fit='autowidth')],
             gap=10, align='center', w='hug', name='Телефон')


def mob_show(h3, p, phones, one=False):
    row = G(phones, dir='row', gap=(18, 18, 14, 14, 14),
            justify=('center',) * 5 if one else ('center', 'center', 'flex-start', 'flex-start', 'flex-start'),
            overflow=None if one else ('visible visible', 'visible visible', 'auto hidden', 'auto hidden', 'auto hidden'),
            pad='0px 0px 8px 0px', name='Телефоны')
    return G([show_head('Мобильная версия', h3, p), G([row], name='Ряд телефонов', margin='14px 0px 0px 0px')],
             name='Мобильная версия')


def kit_card(children, w, name, **kw):
    return G(children, gap=12, pad='16px 16px 16px 16px', radius=14, bg=KITC, border=('1px 1px 1px 1px', LINE),
             w=w, name=name, **kw)


def up(t):
    return T(t, 11, upper=True, ls=0.44, lh=1.3)


def swatches(items, sq):
    cols = []
    for name, hexv in items:
        cols.append(G([SHAPE(sq, sq, hexv, cls='os-sw', borderradius='12px 12px 12px 12px',
                             borderwidth='1px 1px 1px 1px', bordercolor='rgba(0,0,0,0.06)', borderstyle='solid'),
                       T(name, 12, 700, lh=1.3, margin='3px 0px 0px 0px'), T(hexv, 10, color=MUTED, lh=1.3)],
                      gap=0, w=sq, name=name))
    return G(cols, dir='row', gap=(10, 10, 10, 6, 6), name='Образцы цветов')


def kit(label_h3, p, rows):
    return G([show_head('UI-кит', label_h3, p), G(rows, gap=12, name='Сетка кита', margin='14px 0px 0px 0px')],
             name='UI-кит')


def kit_row(cards):
    return G(cards, dir=('row', 'row', 'column', 'column', 'column'), gap=12, align='flex-start', name='Ряд кита')


def type_card(w, big, big_style, notes):
    els = [up('Шрифты' if len(notes) > 1 else 'Шрифт'), T(big, 44, **big_style)]
    for n in notes:
        els.append(n)
    return kit_card(els, w, 'Шрифты')


def proof(nums, text):
    cols = []
    numw = (332, 265, 254, 174, 114)
    for b, s in nums:
        cols.append(G([T(b, (41, 33, 28, 28, 28), 700, color=ACTT, lh=0.95, ls=-2),
                       T(s, 11, color=ACTT, upper=True, ls=0.44, lh=1.3, opacity=0.75)], gap=4, w=numw, name='Цифра'))
    return G([G(cols, dir='wrap', gap=12, name='Цифры'),
              T(text, 13, color=ACTT, lh=1.55, opacity=0.85, padding='14px 0px 0px 0px',
                borderwidth='1px 0px 0px 0px', bordercolor=AMUTED, borderstyle='solid')],
             gap=12, pad='22px 22px 22px 22px', radius=16, bg=ACT, name='Цифры')


def gift(h3):
    left = G([up('Подарок'), T(h3, (26, 21, 20, 20, 20), 700, lh=1.1, ls=-0.8, margin='6px 0px 4px 0px'),
              T('Бесплатно покажу 3 места, где вы теряете клиентов.', 14, lh=1.55)], w='fill', name='Текст')
    return G([left, BTN('Прислать ссылку ↗', 'https://t.me/oksergeevadesign', cls='os-nudge')],
             dir=('row', 'row', 'column', 'column', 'column'), gap=20,
             align=('center', 'center', 'flex-start', 'flex-start', 'flex-start'),
             pad='20px 22px 20px 22px', radius=16, border=('1.5px 1.5px 1.5px 1.5px', INK, 'dashed'), name='Подарок')


def stagger(nodes, start=0.12, step=0.06):
    for i, n in enumerate(nodes):
        anim(n, start + i * step)
    return nodes


# ---------- «было / стало» ----------
BA_W = INNER
BA_H = (665, 540, 705, 505, 355)


def before_after(after_key, old_site):
    W, H = BA_W, BA_H
    after = img(after_key, w=W, h=H, fit='cover', pos='center top', absolute='y', top=0, left=0, alt='Новый сайт')
    tag_after = T('стало', 10, color=ACTT, upper=True, ls=0.5, lh=1.2, w='hug', fit='autowidth', absolute='y', top=12,
                  left=tuple(x - 12 - 62 for x in W), bgcolor=ACT, padding='5px 10px 5px 10px',
                  borderradius='999px 999px 999px 999px')
    todo = T('скриншот старого сайта', 10, color='#B0452F', upper=True, ls=0.5, lh=1.2, w='hug', fit='autowidth',
             cls='os-ba-mark', padding='2px 7px 2px 7px', borderwidth='1px 1px 1px 1px', bordercolor='#B0452F',
             borderstyle='dashed', borderradius='6px 6px 6px 6px')
    before = G([todo, T(old_site, 13, color=MUTED, lh=1.3, w='hug', fit='autowidth')], gap=8, align='center',
               justify='center', w=tuple(x // 2 for x in W), h=H, bg=SHOT, overflow='hidden hidden', absolute='y',
               top=0, left=0, name='Было (ширину двигает скрипт)')
    tag_before = T('было', 10, color=ACTT, upper=True, ls=0.5, lh=1.2, w='hug', fit='autowidth', absolute='y', top=12,
                   left=12, bgcolor=ACT, padding='5px 10px 5px 10px', borderradius='999px 999px 999px 999px')
    line = SHAPE(2, H, ACT, cls='os-ba-line', absolute='y', top=0, left=tuple(x // 2 - 1 for x in W))
    knob_svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" fill="none" role="img" aria-label="Сравнить">'
                '<circle cx="20" cy="20" r="20" fill="#24334D"/><path d="M16 14l-6 6 6 6M24 14l6 6-6 6" stroke="#FFF8C6" '
                'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    knob = VEC(knob_svg, 40, 40, 40, cls='os-ba-knob', absolute='y', top=tuple(h // 2 - 20 for h in H),
               left=tuple(x // 2 - 20 for x in W), shadows='0px 6px 18px 0px rgba(0,0,0,0.2)')
    return G([after, tag_after, before, tag_before, line, knob], w=W, h=H, radius=14, bg=PANEL,
             border=('1px 1px 1px 1px', LINE), overflow='hidden hidden', name='Было / стало (тяните)')


# ---------- кейсы ----------
def case_baloven():
    sq = (126, 100, 98, 69, 45)
    colors = kit_card([up('Цвета бренда'), swatches(
        [('Небо', '#75C3FF'), ('Апельсин', '#FD6901'), ('Янтарь', '#E8891D'), ('Персик', '#EAA87A'), ('Вечер', '#1F2938')], sq)],
        (705, 572, 'fill', 'fill', 'fill'), 'Цвета бренда')
    types = type_card((347, 280, 'fill', 'fill', 'fill'), 'Баловень',
                      dict(fw=400, color='#fd6901', upper=True, lh=1, font='Georgia'),
                      [T('Bergamasco · Constantia: заголовки', 10, color=MUTED, upper=True, ls=0.4, lh=1.3),
                       T('Авторская кухня днём, сцена вечером.', 14, lh=1.55),
                       T('TildaSans: текст', 10, color=MUTED, upper=True, ls=0.4, lh=1.3)])
    kb = dict(fs=11, lh=1.2, ls=0.66, upper=True, w='hug', fit='autowidth', font='Arial', padding='11px 18px 11px 18px',
              borderradius='999px 999px 999px 999px')
    btns = G([T('Купить билет ↗', color='#ffffff', bgcolor='#fd6901', **kb),
              T('Забронировать стол', color='#1f2938', bgcolor='#ffffff', borderwidth='1px 1px 1px 1px',
                bordercolor='#1f2938', borderstyle='solid', **kb),
              T('Забронировать', color='#1f2938', bgcolor='#ffffff', shadows='0px 2px 10px 0px rgba(0,0,0,0.1)', **kb)],
             dir='wrap', gap=8, name='Кнопки')
    ui = kit_card([up('Кнопки и фильтры'), btns, img('baloven/kit-filters', alt='Фильтры афиши')],
                  (526, 426, 'fill', 'fill', 'fill'), 'Кнопки и фильтры')
    event = kit_card([up('Карточка события'), img('baloven/kit-event', alt='Карточка события в афише')],
                     (526, 426, 'fill', 'fill', 'fill'), 'Карточка события', justify='center')
    fmt = kit_card([up('Карточка формата'), img('baloven/kit-format', w=(200, 200, 200, 200, 200), alt='Карточка формата вечера')],
                   'fill', 'Карточка формата', dir=('row', 'row', 'column', 'column', 'column'), gapx=18,
                   align=('center', 'center', 'flex-start', 'flex-start', 'flex-start'))
    tabs = [('Главная', 'baloven/full-index', 'baloven-redesign.netlify.app/'),
            ('Меню', 'baloven/full-menu', 'baloven-redesign.netlify.app/menu'),
            ('Афиша', 'baloven/full-afisha', 'baloven-redesign.netlify.app/afisha'),
            ('Квартирники', 'baloven/full-kvartirniki', 'baloven-redesign.netlify.app/afisha/kvartirniki'),
            ('Банкеты', 'baloven/full-banquets', 'baloven-redesign.netlify.app/banquets'),
            ('О нас', 'baloven/full-about', 'baloven-redesign.netlify.app/about'),
            ('Бронирование', 'baloven/full-booking', 'baloven-redesign.netlify.app/booking')]
    body = [
        meta('редизайн', 'арт-кафе · Москва, м. Павелецкая', 'работаем с 2024 года'),
        T('Сайт, на котором «зайду поесть» превращается в «приду на вечер»', tag='h2', **H2),
        before_after('baloven', 'cafe-baloven.com'),
        pain('У кафе две жизни: днём кухня, вечером сцена с квартирниками и театральными ужинами. А сайт показывал всё одной лентой.',
             'Гость, который искал квартирник, натыкался на бизнес-ланч и уходил.'),
        sol('01', 'Каждый гость сразу у своего', 'Три входа на главной: «Вкусно поесть», «Сходить на вечер», «Устроить праздник». Никто не ищет нужное в ленте.', shot('baloven-paths')),
        sol('02', 'Пришёл за билетом, бронирует и ужин', 'В каждой карточке события рядом с «Купить билет» стоит «Забронировать стол». Вечер на сцене приводит гостя за столик.', shot('baloven-afisha'), flip=True),
        sol('03', 'Ланч на сегодня открывается сам', 'Человек в обед видит меню именно этого дня. Не нужно листать и не нужно писать в директ «а что сегодня?».', shot('baloven-lunch')),
        site_show('10 страниц, каждая со своей задачей', tabs, 'baloven-redesign.netlify.app/'),
        mob_show('Удобно с телефона, откуда приходит большинство гостей', 'Каждую страницу я рисую отдельно под экран телефона.',
                 [phone('baloven/mob-index', 'Главная'), phone('baloven/mob-afisha', 'Афиша', 'os-d6'), phone('baloven/mob-menu', 'Меню', 'os-d12')]),
        kit('Дизайн-система, чтобы сайт рос без хаоса', 'Цвета, шрифты и готовые блоки. Новую страницу или событие можно собрать за минуты, и всё будет в одном стиле.',
            [kit_row([colors, types]), kit_row([ui, event]), fmt]),
        proof([('3', 'недели'), ('55 000 ₽', 'стоимость редизайна'), ('с 2024', 'работаем вместе')],
              'Фирменные цвета, шрифты и фото кафе я сохранила: гости узнают своё место, просто им стало удобнее. Клиент одобрил концепцию.'),
        gift('Пришлите ссылку на ваш сайт'),
    ]
    stagger(body)
    return window('/02 · Баловень', body)


def wide_kit(colors_items, type_big, type_style, type_note, img_label, img_key, img_h):
    sq = (126, 100, 98, 69, 45)
    colors = kit_card([up('Цвета бренда'), swatches(colors_items, sq)], (705, 572, 'fill', 'fill', 'fill'), 'Цвета бренда')
    types = type_card((347, 280, 'fill', 'fill', 'fill'), type_big, type_style,
                      [T(type_note, 10, color=MUTED, upper=True, ls=0.4, lh=1.3)])
    wide = kit_card([up(img_label), img(img_key, h=img_h, fit='cover', pos='center top', alt=img_label)], 'fill', img_label)
    return [kit_row([colors, types]), wide]


def case_lara():
    tabs = [('Главная', 'lara/full-index', 'bms-health.ru/'), ('Массаж лица', 'lara/full-massage', 'bms-health.ru/massage'),
            ('Детские занятия', 'lara/full-children', 'bms-health.ru/children'),
            ('Обучение', 'lara/full-obuchenie', 'bms-health.ru/obuchenie'), ('Магазин', 'lara/full-shop', 'bms-health.ru/shop'),
            ('Блог', 'lara/full-blog', 'bms-health.ru/blog')]
    body = [
        meta('редизайн', 'студия БМС-тренировок · Москва', 'работаем сейчас'),
        T('Сайт, который сам спрашивает: «Чем вам помочь?»', tag='h2', **H2),
        shot('lara', hero=True),
        pain('В студии шесть направлений: тренировки, массаж лица, детские занятия, коучинг, обучение и магазин. А человек приходит не за «БМС», а с больной спиной.',
             'Чтобы он не ушёл, сайт должен понять его с полуслова.'),
        sol_wide('01', 'Голосовой поиск: сказал «болит спина», получил ответ', 'Кнопка «Чем вам помочь?» есть на каждой странице. Человек говорит или пишет своими словами, и сайт сразу показывает подходящую услугу, страницу и статью. Это главная идея сайта.', 'lara/voice'),
        sol('02', 'Навигатор по запросу вместо меню из терминов', 'На главной список живых запросов: «Беспокоит спина, шея или суставы», «Нужны занятия для ребёнка». Нажал свой и увидел направление, первый шаг и стоимость.', shot('lara/navigator'), flip=True),
        site_show('6 страниц, каждая со своей задачей', tabs, 'bms-health.ru/'),
        mob_show('Удобно с телефона, откуда приходит большинство клиентов', 'Каждую страницу я рисую отдельно под экран телефона.',
                 [phone('lara/mob-index', 'Главная'), phone('lara/mob-massage', 'Массаж лица', 'os-d6'), phone('lara/mob-shop', 'Магазин', 'os-d12')]),
        kit('Дизайн-система, чтобы сайт рос без хаоса', 'Цвета, шрифты и готовые блоки. Новую услугу или страницу можно собрать быстро, и всё будет в одном стиле.',
            wide_kit([('Слива', '#3F325E'), ('Ночь', '#2B1F36'), ('Золото', '#DEC14A'), ('Лаванда', '#9F85AD'), ('Туман', '#EFEDF3')],
                     'Lara Shell', dict(fw=700, color='#3F325E', lh=1), 'Gilroy: заголовки и текст',
                     'Карточки цен', 'lara/prices', (560, 560, 459, 321, 218))),
        proof([('2', 'недели'), ('70 000 ₽', 'стоимость редизайна'), ('внедрено', 'клиент запустил сайт')],
              'Фирменные цвета, шрифт Gilroy, фото, тексты и цены студии я сохранила. Клиент одобрил концепцию и внедрил её.'),
        gift('Пришлите ссылку на ваш сайт'),
    ]
    stagger(body)
    return window('/03 · Lara Shell', body)


def case_scenar():
    tabs = [('Главная', 'scenar/full-index', 'scenar-dok-s.ru/'), ('Лечение', 'scenar/full-uslugi', 'scenar-dok-s.ru/uslugi'),
            ('Школа', 'scenar/full-shkola', 'scenar-dok-s.ru/shkola'), ('Магазин', 'scenar/full-magazin', 'scenar-dok-s.ru/magazin'),
            ('О центре', 'scenar/full-o-nas', 'scenar-dok-s.ru/o-nas'), ('Отзывы', 'scenar/full-otzyvy', 'scenar-dok-s.ru/otzyvy'),
            ('Прайс-лист', 'scenar/full-prajs-list', 'scenar-dok-s.ru/prajs-list'), ('Статьи', 'scenar/full-stati', 'scenar-dok-s.ru/stati'),
            ('Контакты', 'scenar/full-kontakty', 'scenar-dok-s.ru/kontakty')]
    body = [
        meta('редизайн', 'центр СКЭНАР-терапии · Калининград', 'работаем сейчас'),
        T('Сайт, который сам подбирает лечение под симптом', tag='h2', **H2),
        shot('scenar', hero=True),
        pain('У центра четыре направления: лечение, диагностика, школа и магазин аппаратов. Пациент приходит с болью, а не с названием метода.',
             'Раньше ему приходилось самому разбираться, что такое СКЭНАР и что ему подойдёт.'),
        sol_wide('01', 'Подбор решения: показал, где болит, получил лечение', 'Схема тела с точками. Нажал туда, где беспокоит, и сразу видно систему организма, заболевания и процедуры, которые помогут.', 'scenar/navigator'),
        sol('02', 'Голосовой поиск своими словами', 'Можно сказать или написать «болит спина». Сайт покажет услугу с ценой, систему организма и статью о проблеме.', shot('scenar/voice'), flip=True),
        sol('03', 'Понятный путь пациента', 'Консультация, диагностика, курс лечения и поддержка дома. Человек видит, с чего начать и что будет дальше.', shot('scenar/route')),
        site_show('9 страниц, каждая со своей задачей', tabs, 'scenar-dok-s.ru/'),
        mob_show('Удобно с телефона, откуда приходит большинство клиентов', 'Каждую страницу я рисую отдельно под экран телефона.',
                 [phone('scenar/mob-index', 'Главная'), phone('scenar/mob-uslugi', 'Лечение', 'os-d6'), phone('scenar/mob-magazin', 'Магазин', 'os-d12')]),
        kit('Дизайн-система, чтобы сайт рос без хаоса', 'Цвета, шрифты и готовые блоки. Новую услугу или страницу можно собрать быстро, и всё будет в одном стиле.',
            wide_kit([('Лазурь', '#00A3D3'), ('Глубина', '#073B52'), ('Небо', '#EBF9FF'), ('Зелень', '#6EBE4D'), ('Коралл', '#FF8562')],
                     'СКЭНАР', dict(fw=700, color='#073B52', lh=1, font='Arial'), 'Proxima Nova: заголовки и текст',
                     'Популярные услуги с ценами', 'scenar/prices', (560, 560, 393, 275, 186))),
        proof([('4', 'недели'), ('60 000 ₽', 'стоимость редизайна'), ('внедряют', 'клиент принял концепцию')],
              'Официальный прайс с кодами медицинских услуг, цвета, шрифт и фото центра я сохранила. Клиент принял концепцию и сейчас внедряет её.'),
        gift('Пришлите ссылку на ваш сайт'),
    ]
    stagger(body)
    return window('/04 · СКЭНАР-терапия', body)


def case_nina():
    cols = [('Клиентам', ['Консультирование', 'Семейная терапия', 'Детский психолог', 'Терапевтические группы']),
            ('Психологам', ['Супервизия', 'Обучающая личная терапия', 'Наставничество', 'Группы практики']),
            ('Сообщество', ['Киноклуб для психологов', 'Исследование сказок', 'Вебинары']),
            ('Материалы', ['Чек-листы', 'Схемы и шаблоны']),
            ('Основа', ['Главная', 'Обо мне', 'Политика конфиденциальности'])]
    colw = (195, 403, 253, 'fill', 'fill')
    n = 0
    col_groups = []
    for title, items in cols:
        lis = []
        for it in items:
            n += 1
            li = T(f'<span style="font-size:10px;color:#52647C">{n:02d}</span>  {it}', 12, lh=1.25, w='fill',
                   bgcolor=PANEL, padding='9px 10px 9px 10px', borderradius='10px 10px 10px 10px', cls='os-li')
            anim(li, 0.4 + n * 0.045, style='zoomin', dist=0)
            li.props['animscale'] = '0.6'
            lis.append(li)
        col_groups.append(G([T(title, 11, color=ACTT, upper=True, ls=0.44, lh=1.3, opacity=0.65)] + lis, gap=6,
                            w=colw, name=title))
    smap = G([
        G([T('16', (120, 96, 72, 72, 72), 700, color=ACTT, lh=0.8, ls=(-8.4, -6.7, -5, -5, -5), w='hug', fit='autowidth'),
           G([T('страниц, и у каждой услуги своя', (29, 23, 20, 20, 20), 700, color=ACTT, lh=1.05, ls=-0.9, margin='0px 0px 8px 0px'),
              T('У Нины много направлений: консультации, семейная и детская терапия, группы, супервизия, киноклуб, материалы. Раньше всё это пришлось бы искать в одной ленте. Теперь у каждого направления отдельная страница с описанием, ценой и кнопкой записи.',
                14, color=ACTT, lh=1.55, opacity=0.8)], w='fill', name='Текст')],
          dir=('row', 'row', 'row', 'column', 'column'), gap=20, align=('center',) * 3 + ('flex-start',) * 2, name='Шапка карты'),
        G(col_groups, dir='wrap', gap=10, align='flex-start', name='Карта страниц')],
        gap=20, pad='24px 24px 24px 24px', radius=18, bg=ACT, name='Карта сайта')
    mini_w = (346, 280, 'fill', 'fill', 'fill')
    minis = []
    for num, h, p in [('02', 'Цены видны сразу', 'На 14 страницах цены оформлены карточками с кнопкой «Записаться». Не нужно писать и спрашивать.'),
                      ('03', 'Меню не теряется', 'При прокрутке подсвечивается раздел, в котором сейчас человек.'),
                      ('04', 'Всё на Taplink', 'Тексты и цены легко поменять в редакторе, программист не нужен.')]:
        minis.append(G([caseno(num), T(h, 17, 700, lh=1.3, ls=-0.34), T(p, 13, color=MUTED, lh=1.55)], gap=6,
                       pad='16px 18px 16px 18px', radius=14, border=('1px 1px 1px 1px', LINE), w=mini_w, name=h))
    crop = G([G([img('nina/sections', alt='Разделы главной')], w=(340, 340, 340, 'fill', 'fill'), radius=22, bg=SHOT,
                border=('1px 1px 1px 1px', LINE), overflow='hidden hidden', name='Скриншот')], align='center', name='По центру')
    sq = (198, 158, 98, 69, 45)
    colors = kit_card([up('Цвета'), swatches([('Хлопок', '#F2F3ED'), ('Лён', '#DADAD2'), ('Песок', '#BDB7A7'), ('Лес', '#4C513A'), ('Мох', '#303426')], sq)],
                      'fill', 'Цвета')
    body = [
        meta('сайт на Taplink', 'семейный и детский психолог', 'пришла через Profi'),
        T('16 страниц за 5 дней для психолога, которая устала ждать', tag='h2', **H2),
        smap,
        pain('Нина уже заказывала сайт у другого специалиста. Делали долго, а результат её не устроил.',
             'Ко мне она пришла с двумя просьбами: сделать быстро и не пропасть.'),
        sol('01', 'Клиент и коллега сразу видят своё', 'Главная разделена по людям: «Для вас и вашей семьи», «Психологам», «Профессиональная среда», «Полезные материалы». Никому не нужно разбираться в списке из 16 услуг.', crop),
        G(minis, dir=('row', 'row', 'column', 'column', 'column'), gap=12, align='flex-start', name='Ещё решения'),
        mob_show('Сайт, который открывают из Instagram', 'Taplink живёт в ссылке профиля, поэтому главное здесь телефон. Экран листается сам, наведите, чтобы остановить.',
                 [phone('nina/mob-index', 'Главная', w=(260, 260, 240, 240, 220), h=(535, 535, 493, 493, 452))], one=True),
        kit('Палитра «Хлопок и лесной зелёный»', 'Спокойные природные цвета, в которых не тревожно. Одна палитра на все 16 страниц.', [colors]),
        proof([('5', 'дней'), ('24 000 ₽', 'стоимость'), ('16', 'страниц')],
              'Нина нашла меня на Profi. Всё время работы я была на связи, и сайт был готов за 5 дней.'),
        gift('Пришлите ссылку на ваш сайт или Taplink'),
    ]
    stagger(body)
    return window('/01 · Нина Евстафьева', body)


if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    jobs = [('baloven', case_baloven, '1792163000000', 'Окно кейса: Баловень (#case-baloven)', (6200, 5600, 7400, 6600, 6200)),
            ('lara', case_lara, '1792163100000', 'Окно кейса: Lara Shell (#case-lara)', (6000, 5400, 7000, 6200, 5800)),
            ('scenar', case_scenar, '1792163200000', 'Окно кейса: СКЭНАР-терапия (#case-scenar)', (6400, 5800, 7600, 6800, 6400)),
            ('nina', case_nina, '1792163300000', 'Окно кейса: Нина (#case-nina)', (3800, 3800, 4800, 5200, 5200))]
    for name, fn, prefix, title, hs in jobs:
        data = build(fn(), prefix, popup_artboard(title, hs))
        dump(data, f'out/{name}.json')
        print(name, len(open(f'out/{name}.json', encoding='utf-8').read()), 'символов,',
              sum(1 for k in data if k.isdigit()), 'элементов,', len(data['groups']), 'групп')
