import logging


def cleanup(value: str) -> str:
    return value.lower().strip()


def true(value: str) -> bool:
    return value in ['true', 'True', '1', 'yes', 'on']


def to_list(s, sep=',', filter=(None, '', {}, [])):
    if s in filter:
        return []
    if isinstance(s, str):
        ls = [item.strip() for item in s.split(sep)]
    else:
        ls = list(s)
    return [item for item in ls if item not in filter]


def delimit(l, sep=',', filter=(None, '', {}, [])):
    items = [i for i in to_list(l, sep, filter)]
    return sep.join([str(x) for x in items])


def pluralize(count, singular, plural=None):
    if count == 1:
        return singular
    return plural or (singular + 's')


def get_logger(path):
    return logging.getLogger(path)
