"""Сборщик Zero Block (Tilda) для окон портфолио.

Описываем окно деревом групп и элементов, а скрипт раскладывает его
в JSON для update_zero_block: id, zindex в порядке документа, groupid,
значения по брейкпоинтам (-res-960 и т. д.).

Значение по брейкпоинтам задаётся кортежем из 5 чисел/строк:
(1200, 960, 640, 480, 360). Ключ -res-W пишется, только если значение
отличается от более широкого брейкпоинта.
"""
import json

SCREENS = [1200, 960, 640, 480, 360]

# Цвета голубой темы. Каждый цвет отвечает за свою роль: скрипт тем
# в шапке заменяет их на цвета выбранной темы.
BG, PT, PANEL, INK, MUTED, LINE = '#92ACDD', '#FFF8C8', '#FFF8C7', '#24334C', '#52647C', '#6F8FBE'
F2, F3, ACT, ACTT, AMUTED, HOV = '#F4EBAA', '#E9DD8E', '#24334D', '#FFF8C6', '#C9D6EE', '#3A4D6E'
CARD, SHOT, KITC = '#F2EFCA', '#F2ECC0', '#FFF9CF'
FONT = 'Gilroy'

WIDE = (1120, 920, 600, 440, 320)      # окно .wide
NORMAL = (880, 880, 600, 440, 320)     # обычное окно
WIDE_IN = (1064, 864, 564, 404, 284)   # ширина содержимого широкого окна
BODY_PAD = ('26px 28px 32px 28px',) * 2 + ('20px 18px 26px 18px',) * 3


def bp(v):
    return v if isinstance(v, (tuple, list)) else (v,) * 5


def put(d, key, v):
    """Записать значение по брейкпоинтам."""
    if v is None:
        return
    vals = [None if x is None else str(x) for x in bp(v)]
    d[key] = vals[0]
    prev = vals[0]
    for w, x in zip(SCREENS[1:], vals[1:]):
        if x is not None and x != prev:
            d[f'{key}-res-{w}'] = x
            prev = x


class N:
    """Узел дерева: элемент или группа."""

    def __init__(self, kind, props, children=None):
        self.kind, self.props, self.children = kind, props, children or []


def size(d, w, h):
    # w/h: 'fill' | 'hug' | число | кортеж чисел (fixed)
    for key, v, dflt in (('width', w, 100), ('height', h, 20)):
        mode = key + 'mode'
        if v in ('fill', 'hug'):
            d[mode] = v
            d[key] = str(dflt)
        elif isinstance(v, tuple) and any(x in ('fill', 'hug') for x in v):
            put(d, mode, tuple('fixed' if isinstance(x, (int, float)) else x for x in v))
            put(d, key, tuple(x if isinstance(x, (int, float)) else dflt for x in v))
        else:
            d[mode] = 'fixed'
            put(d, key, v)
    d.setdefault('top', '0')
    d.setdefault('left', '0')


def T(text, fs=14, fw=400, color=INK, lh=1.5, ls=None, upper=False, w='fill', h='hug',
      tag=None, cls=None, link=None, blank=False, align=None, fit='autoheight', **kw):
    d = {'elem_type': 'text', 'text': text, 'textfit': fit, 'fontfamily': kw.pop('font', FONT)}
    size(d, w, h)
    put(d, 'fontsize', fs)
    put(d, 'fontweight', fw)
    put(d, 'lineheight', lh)
    put(d, 'letterspacing', ls)
    d['color'] = color
    if upper:
        d['lettercase'] = 'uppercase'
    if tag:
        d['tag'] = tag
    if cls:
        d['classname'] = cls
    if link:
        d['link'] = link
    if blank:
        d['linktarget'] = '_blank'
    if align:
        put(d, 'align', align)
    for k, v in kw.items():
        put(d, k, v)
    return N('el', d)


def BTN(caption, link, dark=True, cls=None, w='hug', blank=True):
    d = {'elem_type': 'button', 'caption': caption, 'link': link, 'textfit': 'autowidth' if w == 'hug' else 'fixedsize',
         'fontfamily': FONT, 'fontsize': '12', 'fontweight': '400', 'lettercase': 'uppercase', 'letterspacing': '0.36',
         'padding': '0px 16px 0px 16px', 'align': 'center', 'borderradius': '12px 12px 12px 12px', 'speedhover': '0.2'}
    size(d, w if w != 'hug' else 'hug', 40)
    if dark:
        d.update(color=ACTT, bgcolor=ACT, bgcolorhover=HOV)
    else:
        d.update(color=INK, borderwidth='1px 1px 1px 1px', bordercolor=INK, borderstyle='solid', bgcolorhover=CARD)
    if blank:
        d['linktarget'] = '_blank'
    if cls:
        d['classname'] = cls
    return N('el', d)


def IMG(url, fw, fh, w='fill', h=None, fit='auto', pos='center top', alt='', cls=None, **kw):
    d = {'elem_type': 'image', 'img': url, 'filewidth': str(fw), 'fileheight': str(fh),
         'imagefit': fit, 'imageposition': pos, 'alt': alt}
    if h is None:
        size(d, w, 100)
        d['heightmode'] = 'hug'
    else:
        size(d, w, h)
    if cls:
        d['classname'] = cls
    for k, v in kw.items():
        put(d, k, v)
    return N('el', d)


def SHAPE(w, h, bg, **kw):
    d = {'elem_type': 'shape', 'figure': kw.pop('figure', 'rectangle'), 'bgcolor': bg}
    if 'cls' in kw:
        d['classname'] = kw.pop('cls')
    size(d, w, h)
    for k, v in kw.items():
        put(d, k, v)
    return N('el', d)


def VEC(svg, fw, fh, w, cls=None, **kw):
    d = {'elem_type': 'vector', 'vectorsvg': svg, 'vectorjson': '', 'filewidth': str(fw), 'fileheight': str(fh)}
    size(d, w, fh)
    d['heightmode'] = 'hug'
    if cls:
        d['classname'] = cls
    for k, v in kw.items():
        put(d, k, v)
    return N('el', d)


def G(children, dir='column', gap=None, gapx=None, pad='0px 0px 0px 0px', w='fill', h='hug', name='',
      bg=None, border=None, radius=None, align=None, justify=None, overflow=None, link=None, **kw):
    d = {'type': 'physical', 'flex': 'auto', 'name': name}
    put(d, 'flexdirection', dir)
    put(d, 'flexgapy', gap)
    put(d, 'flexgapx', gapx if gapx is not None else gap)
    put(d, 'padding', pad)
    size(d, w, h)
    if bg:
        d['bgcolor'] = bg
    if border:  # (ширина, цвет[, стиль])
        put(d, 'borderwidth', border[0])
        d['bordercolor'] = border[1]
        d['borderstyle'] = border[2] if len(border) > 2 else 'solid'
    if radius is not None:
        d['borderradius'] = f'{radius}px {radius}px {radius}px {radius}px'
    put(d, 'flexalignitems', align)
    put(d, 'flexjustifycontent', justify)
    if overflow:
        put(d, 'overflow', overflow)
    if link:
        d['link'] = link
    for k, v in kw.items():
        put(d, k, v)
    return N('grp', d, [c for c in children if c is not None])


def anim(node, delay, dist=6, style='fadeinup', dur=0.5):
    node.props.update(animstyle=style, animduration=str(dur), animdistance=str(dist),
                      animdelay=f'{delay:.2f}', animmobile='y')
    return node


def build(root, prefix, artboard):
    """Развернуть дерево в JSON Zero Block. prefix — 13 цифр (время в мс)."""
    out = dict(artboard)
    out['timestamp'] = prefix
    groups, elems = [], []
    counter = [0]
    z = [2000]

    def nid():
        counter[0] += 1
        return f'{prefix}{counter[0]:06d}'

    def walk(node, parent):
        d = dict(node.props)
        if parent:
            d['groupid'] = parent
        d['zindex'] = str(z[0])
        z[0] -= 1
        if node.kind == 'grp':
            d['id'] = nid()
            groups.append(d)
            for c in node.children:
                walk(c, d['id'])
        else:
            d['elem_id'] = nid()
            elems.append(d)

    for top in (root if isinstance(root, list) else [root]):
        walk(top, None)
    for i, e in enumerate(elems):
        out[str(i)] = e
    out['groups'] = groups
    return out


def popup_artboard(title, heights):
    ab = {'ab_title': title, 'ab_flex': 'auto', 'ab_heightmode': 'hug', 'ab_flexdirection': 'column',
          'ab_flexalignitems': 'center', 'ab_bgattachment': 'scroll', 'ab_screens': '360,480,640,960,1200'}
    put(ab, 'ab_padding', ('24px 20px 24px 20px',) * 2 + ('16px 20px 16px 20px',) * 3)
    for w, hh in zip(SCREENS, heights):
        ab['ab_height' if w == 1200 else f'ab_height-res-{w}'] = str(hh)
        ab['ab_bgcolor' if w == 1200 else f'ab_bgcolor-res-{w}'] = ''
    return ab


CLOSE_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" fill="none" stroke="#24334C" '
             'stroke-width="1.6" role="img" aria-label="Закрыть"><path d="M3 3l8 8M11 3l-8 8"/></svg>')


def window(label, body_children, width=WIDE, gap=18):
    bar = G([T(label, 11, upper=True, ls=0.44, lh=1.3, w='hug', fit='autowidth'),
             G([VEC(CLOSE_SVG, 14, 14, 14)], dir='row', w=30, h=30, radius=9, border=('1px 1px 1px 1px', LINE),
               align='center', justify='center', link='#closepopup', name='Закрыть')],
            dir='row', gap=12, pad='12px 14px 12px 18px', align='center', justify='space-between',
            border=('0px 0px 1px 0px', LINE), name='Панель окна')
    body = G(body_children, gap=gap, pad=BODY_PAD, align='flex-start', name='Содержимое')
    return G([bar, body], w=width, bg=PANEL, radius=18, border=('1px 1px 1px 1px', LINE), overflow='hidden hidden',
             shadows='0px 30px 80px 0px rgba(0,0,0,0.3)', name='Окно', tag='article')


def dump(obj, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))
