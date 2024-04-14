def get_items(items):
    arrItems = list()
    for item in items:
        item['_id'] = str(item['_id'])
        arrItems.append(item)
    return arrItems

def get_item(item):
    item['_id'] = str(item['_id'])
    return item