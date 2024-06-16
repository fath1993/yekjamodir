def fetch_data_from_http_get(request, item: str, context):
    try:
        result_item = str(request.GET[item])
        if result_item == '':
            result_item = None
    except:
        result_item = None
    print(f'{item}: {result_item}')
    context[item] = result_item
    return result_item


def fetch_data_from_http_post(request, item: str, context):
    try:
        result_item = str(request.POST[item])
        if result_item == '':
            result_item = None
    except:
        result_item = None
    print(f'{item}: {result_item}')
    context[item] = result_item
    return result_item


def fetch_datalist_from_http_post(request, item: str, context):
    try:
        result_item = request.POST.getlist(item)
        if result_item == '':
            result_item = None
    except:
        result_item = None
    print(f'{item}: {result_item}')
    context[item] = result_item
    return result_item


def fetch_files_from_http_post_data(request, item, context):
    try:
        result_item = request.FILES.getlist(f'{item}')
        if len(result_item) == 0:
            result_item = None
        else:
            for item in result_item:
                context[f'{item}'] = item
    except:
        result_item = None
    print(f'{result_item}')
    return result_item


def fetch_single_file_from_http_file(request, item: str, context):
    try:
        result_item = request.FILES[item]
        if result_item == '':
            result_item = None
    except:
        result_item = None
    print(f'{item}: {result_item}')
    context[item] = result_item
    return result_item


def fetch_multiple_files_from_http_file(request, item: str, context):
    try:
        result_item = request.FILES.getlist(item)
        if result_item == '':
            result_item = None
    except:
        result_item = None
    print(f'{item}: {result_item}')
    context[item] = result_item
    return result_item