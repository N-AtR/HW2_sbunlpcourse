
from hazm import *


def myNormalizer(text):
    # ء
    text = text.replace('هء', 'ه‌ی')
    text = text.replace('ي', 'ی')

    # ها
    replace_array = ['ها', 'های', 'هایی', 'هایم', 'هایت',
                     'هایش', 'هایمان', 'هایتان', 'هایشان', 'می', 'نمی']
    for ha in replace_array:
        text = text.replace(' ' + ha + ' ', '‌' + ha + ' ')

    return text


def punctuationOmitter(text):
    replace_array = ['،', '.', '\'', '\"', ':', ';', ',', '?',
                     '!', '؟', '؛', '«', '»', ')', '(', '{', '}', '[', ']']
    for ha in replace_array:
        text = text.replace(ha, '')

    return text
