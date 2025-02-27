# Пример: goods = [ {'title': 'Ковер', 'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'price': 5300,
# 'color': 'black'} ] field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха' field(goods, 'title',
# 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    res = []
    if len(args) == 1:
        for item in items:
            try:
                yield item[args[0]]
            except:
                continue
    else:
        for item in items:
            yield {args[i]: item[args[i]] for i in range(len(args))}


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    gen_res = field(goods, 'title', 'price')
    for item in gen_res:
        print(item)
