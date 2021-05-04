from django import template

register = template.Library()
bad_words = (
'бля', 'блядь', 'блять', 'b3ъeб', 'cock', 'cunt', 'e6aль', 'ebal', 'eblan', 'eбaл', 'eбaть', 'eбyч', 'eбать', 'eбЄт',
'eблантий', 'fuck', 'fucker', 'fucking', 'xyЄв', 'xyй', 'xy¤', 'xуе,xуй', 'xую', 'zaeb', 'zaebal', 'zaebali', 'zaebat', 'архипиздрит', 'ахуел', 'ахуеть', 'бздение', 'бздеть', 'бздех', 'бздецы', 'бздит', 'бздицы', 'бздло', 'бзднуть', 'бздун', 'бздунь¤', 'бздюха', 'бздюшка', 'бздюшко', 'бл¤', 'бл¤бу', 'бл¤буду', 'бл¤д', 'бл¤ди', 'бл¤дина', 'бл¤дище', 'бл¤дки', 'бл¤довать', 'бл¤дство', 'бл¤дун', 'бл¤дуны', 'бл¤дунь¤', 'бл¤дь', 'бл¤дюга', 'бл¤ть', 'вафел', 'вафлЄр', 'взъебка', 'взьебка', 'взьебывать', 'въеб', 'въебалс¤', 'въебенн', 'въебусь', 'въебывать', 'выбл¤док', 'выбл¤дыш', 'выеб', 'выебать', 'выебен', 'выебнулс¤', 'выебон', 'выебыватьс¤', 'выпердеть', 'высратьс¤', 'выссатьс¤', 'вьебен', 'гавно', 'гавнюк', 'гавнючка', 'гамно', 'гандон', 'гнид', 'гнида', 'гниды', 'говенка', 'говенный', 'говешка', 'говнази¤', 'говнецо', 'говнище', 'говно', 'говноед', 'говнолинк', 'говночист', 'говнюк', 'говнюха', 'говн¤дина', 'говн¤к', 'говн¤ный', 'говн¤ть', 'гондон', 'доебыватьс¤', 'долбоеб', 'долбоЄб', 'долбо¤щер', 'дрисн¤', 'дрист', 'дристануть', 'дристать', 'дристун', 'дристуха', 'дрочелло', 'дрочена', 'дрочила', 'дрочилка', 'дрочистый', 'дрочить', 'дрочка', 'дрочун', 'е6ал', 'е6ут', 'еб твою мать', 'Єб твою мать', 'Єбaн', 'ебaть', 'ебyч', 'ебал', 'ебало', 'ебальник', 'ебан', 'ебанамать', 'ебанат', 'ебана¤', 'Єбана¤', 'ебанический', 'ебанный', 'ебанныйврот', 'ебаное', 'ебануть', 'ебанутьс¤', 'Єбаную', 'ебаный', 'ебанько', 'ебарь', 'ебат', 'Єбат', 'ебатори¤', 'ебать', 'ебать-копать', 'ебатьс¤', 'ебашить', 'ебЄна', 'ебет', 'ебЄт', 'ебец', 'ебик', 'ебин', 'ебись', 'ебическа¤', 'ебки', 'ебла', 'еблан', 'ебливый', 'еблище', 'ебло', 'еблыст', 'ебл¤', 'Єбн', 'ебнуть', 'ебнутьс¤', 'ебн¤', 'ебошить', 'ебска¤', 'ебский', 'ебтвоюмать', 'ебун', 'ебут', 'ебуч', 'ебуче', 'ебучее', 'ебучий', 'ебучим', 'ебущ', 'ебырь', 'елда', 'елдак', 'елдачить', 'жопа', 'жопу', 'заговн¤ть', 'задрачивать', 'задристать', 'задрота', 'зае6', 'заЄ6', 'заеб', 'заЄб', 'заеба', 'заебал', 'заебанец', 'заебаста¤', 'заебастый', 'заебать', 'заебатьс¤', 'заебашить', 'заебистое', 'заЄбистое', 'заебистые', 'заЄбистые', 'заебистый', 'заЄбистый', 'заебись', 'заебошить', 'заебыватьс¤', 'залуп', 'залупа', 'залупатьс¤', 'залупить', 'залупитьс¤', 'замудохатьс¤', 'запизд¤чить', 'засерать', 'засерун', 'засер¤', 'засирать', 'засрун', 'заху¤чить', 'за¤беста¤', 'злоеб', 'злоебуча¤', 'злоебучее', 'злоебучий', 'ибанамат', 'ибонех', 'изговн¤ть', 'изговн¤тьс¤', 'изъебнутьс¤', 'ипать', 'ипатьс¤', 'ипаццо', ' акдвапальцаобоссать', 'конча', 'курва', 'курв¤тник', 'лох', 'лошарa', 'лошара', 'лошары', 'лошок', 'л¤рва', 'малафь¤', 'манда', 'мандавошек', 'мандавошка', 'мандавошки', 'мандей', 'мандень', 'мандеть', 'мандища', 'мандой', 'манду', 'мандюк', 'минет', 'минетчик', 'минетчица', 'мл¤ть', 'мокрощелка', 'мокрощЄлка', 'мразь', 'мудak', 'мудaк', 'мудаг', 'мудак', 'муде', 'мудель', 'мудеть', 'муди', 'мудил', 'мудила', 'мудистый', 'мудн¤', 'мудоеб', 'мудозвон', 'мудоклюй', 'на хер', 'на хуй', 'набздел', 'набздеть', 'наговн¤ть', 'надристать', 'надрочить', 'наебать', 'наебет', 'наебнуть', 'наебнутьс¤', 'наебывать', 'напиздел', 'напиздели', 'напиздело', 'напиздили', 'насрать', 'настопиздить', 'нахер', 'нахрен', 'нахуй', 'нахуйник', 'не ебет', 'не ебЄт', 'невротебучий', 'невъебенно', 'нехира', 'нехрен', 'Ќехуй', 'нехуйственно', 'ниибацо', 'ниипацца', 'ниипаццо', 'ниипет', 'нику¤', 'нихера', 'ниху¤', 'обдристатьс¤', 'обосранец', 'обосрать', 'обосцать', 'обосцатьс¤', 'обсирать', 'объебос', 'обьебать обьебос', 'однохуйственно', 'опездал', 'опизде', 'опизденивающе', 'остоебенить', 'остопиздеть', 'отмудохать', 'отпиздить', 'отпизд¤чить', 'отпороть', 'отъебись', 'охуевательский', 'охуевать', 'охуевающий', 'охуел', 'охуенно', 'охуеньчик', 'охуеть', 'охуительно', 'охуительный', 'оху¤ньчик', 'оху¤чивать', 'оху¤чить', 'очкун', 'падла', 'падонки', 'падонок', 'паскуда', 'педерас', 'педик', 'педрик', 'педрила', 'педрилло', 'педрило', 'педрилы', 'пездень', 'пездит', 'пездишь', 'пездо', 'пезд¤т', 'пердануть', 'пердеж', 'пердение', 'пердеть', 'пердильник', 'перднуть', 'пЄрднуть', 'пердун', 'пердунец', 'пердунина', 'пердунь¤', 'пердуха', 'пердь', 'переЄбок', 'пернуть', 'пЄрнуть', 'пи3д', 'пи3де', 'пи3ду', 'пиzдец', 'пидар', 'пидарaс', 'пидарас', 'пидарасы', 'пидары', 'пидор', 'пидорасы', 'пидорка', 'пидорок', 'пидоры', 'пидрас', 'пизда', 'пиздануть', 'пизданутьс¤', 'пиздарваньчик', 'пиздато', 'пиздатое', 'пиздатый', 'пизденка', 'пизденыш', 'пиздЄныш', 'пиздеть', 'пиздец', 'пиздит', 'пиздить', 'пиздитьс¤', 'пиздишь', 'пиздища', 'пиздище', 'пиздобол', 'пиздоболы', 'пиздобрати¤', 'пиздовата¤', 'пиздоватый', 'пиздолиз', 'пиздонутые', 'пиздорванец', 'пиздорванка', 'пиздострадатель', 'пизду', 'пиздуй', 'пиздун', 'пиздунь¤', 'пизды', 'пиздюга', 'пиздюк', 'пиздюлина', 'пиздюл¤', 'пизд¤т', 'пизд¤чить', 'писбшки', 'писька', 'писькострадатель', 'писюн', 'писюшка', 'по хуй', 'по хую', 'подговн¤ть', 'подонки', 'подонок', 'подъебнуть', 'подъебнутьс¤', 'поебать', 'поебень', 'поЄбываает', 'поскуда', 'посрать', 'потаскуха', 'потаскушка', 'похер', 'похерил', 'похерила', 'похерили', 'похеру', 'похрен', 'похрену', 'похуй', 'похуист', 'похуистка', 'похую', 'придурок', 'приебатьс¤', 'припиздень', 'припизднутый', 'припиздюлина', 'пробзделс¤', 'пробл¤дь', 'проеб', 'проебанка', 'проебать', 'промандеть', 'промудеть', 'пропизделс¤', 'пропиздеть', 'пропизд¤чить', 'раздолбай', 'разху¤чить', 'разъеб', 'разъеба', 'разъебай', 'разъебать', 'распиздай', 'распиздетьс¤', 'распизд¤й', 'распизд¤йство', 'распроеть', 'сволота', 'сволочь', 'сговн¤ть', 'секель', 'серун', 'серька', 'сестроеб', 'сикель', 'сила', 'сирать', 'сирывать', 'соси', 'спиздел', 'спиздеть', 'спиздил', 'спиздила', 'спиздили', 'спиздит', 'спиздить', 'срака', 'сраку', 'сраный', 'сранье', 'срать', 'срун', 'ссака', 'ссышь', 'стерва', 'страхопиздище', 'сука', 'суки', 'суходрочка', 'сучара', 'сучий', 'сучка', 'сучко', 'сучонок', 'сучье', 'сцание', 'сцать', 'сцука', 'сцуки', 'сцуконах', 'сцуль', 'сцыха', 'сцышь', 'съебатьс¤', 'сыкун', 'трахае6', 'трахаеб', 'трахаЄб', 'трахатель', 'ублюдок', 'уебать', 'уЄбища', 'уебище', 'уЄбище', 'уебищное', 'уЄбищное', 'уебк', 'уебки', 'уЄбки', 'уебок', 'уЄбок', 'урюк', 'усратьс¤', 'ушлепок', 'х_у_¤_р_а', 'хyЄ', 'хyй', 'хyйн¤', 'хамло', 'хер', 'херн¤', 'херовато', 'херовина', 'херовый', 'хитровыебанный', 'хитрожопый', 'хуeм', 'хуе', 'хуЄ', 'хуевато', 'хуЄвенький', 'хуевина', 'хуево', 'хуевый', 'хуЄвый', 'хуек', 'хуЄк', 'хуел', 'хуем', 'хуенч', 'хуеныш', 'хуенький', 'хуеплет', 'хуеплЄт', 'хуепромышленник', 'хуерик', 'хуерыло', 'хуесос', 'хуесоска', 'хуета', 'хуетень', 'хуею', 'хуи', 'хуй', 'хуйком', 'хуйло', 'хуйн¤', 'хуйрик', 'хуище', 'хул¤', 'хую', 'хуюл', 'ху¤', 'ху¤к', 'ху¤кать', 'ху¤кнуть', 'ху¤ра', 'ху¤се', 'ху¤чить', 'целка', 'чмо', 'чмошник', 'чмырь', 'шалава', 'шалавой', 'шараЄбитьс¤', 'шлюха', 'шлюхой', 'шлюшка', '¤бывает'
)

@register.filter(name='censor')
def censored(value):
    value = value.split(' ')

    for index, word in enumerate(value):
        if len(word) > 2:
            if word.lower() in bad_words:
                value[index] = "*censored*"
    return ' '.join(map(str, value))