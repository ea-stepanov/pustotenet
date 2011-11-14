# -*- coding: utf-8 -*-
__author__ = 'eduard'

def get_translit(string):

    letters = u'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    table = {u'а':'a', u'б':'b',  u'в':'v', u'г':'g', u'д':'d', u'е':'e', u'ё':'jo', u'ж':'zh', u'з':'z', u'и':'i', u'й':'i', u'к':'k', u'л':'l', u'м':'m', u'н':'n', u'о':'o', u'п':'p', u'р':'r', u'с':'s', u'т':'t', u'у':'u', u'ф':'f', u'х':'h', u'ц':'c', u'ч':'ch', u'ш':'sh', u'щ':'shch', u'ъ':'', u'ы':'i', u'ь':'', u'э':'e', u'ю':'yu', u'я':'ya', ' ':'-'}

    string = string.lower()

    for sign in string:
        if (sign not in letters):
            string = string.replace(sign, '')

    for sign in table.keys():
        string = string.replace(sign, table[sign])

    return string