#! /usr/bin/env python3

import os
import sys
import feedparser
import pprint
import datetime
import time


if __name__ == "__main__":

    working_table = {
        'USD/JPY': {
            'URL': 'https://www.fx-exchange.com/usd/rss.xml',
            'title': 'US Dollar(USD)/Japanese Yen(JPY)'
        },
        'EUR/JPY': {
            'URL': 'https://www.fx-exchange.com/eur/rss.xml',
            'title': 'Euro(EUR)/Japanese Yen(JPY)'
        },
        'GBP/JPY': {
            'URL': 'https://www.fx-exchange.com/gbp/rss.xml',
            'title': 'British Pound Sterling(GBP)/Japanese Yen(JPY)'
        },
        'AUD/JPY': {
            'URL': 'https://www.fx-exchange.com/aud/rss.xml',
            'title': 'Australian Dollar(AUD)/Japanese Yen(JPY)'
        },
        'NZD/JPY': {
            'URL': 'https://www.fx-exchange.com/nzd/rss.xml',
            'title': 'New Zealand Dollar(NZD)/Japanese Yen(JPY)'
        },
    }
    # pprint.pprint(working_table)


    if 2 != len(sys.argv):
        print('Need argument')
        sys.exit()


    kbn = ''
    for tmp_key, tmp_value in working_table.items():
        if sys.argv[1] == tmp_key:
            kbn = sys.argv[1]

    if '' == kbn:
        print('Wrong argument')
        sys.exit()


    currency_table = {}
    obj = feedparser.parse(working_table[kbn]['URL'])
    for entry in obj.entries:
        if working_table[kbn]['title'] == entry['title']:
            currency_table.update({ 'kbn': kbn })

            summary = entry['summary']
            currency_table.update({ 'summary': summary })

            tmp1 = summary.split('=')
            tmp2 = tmp1[1].strip(' ').split(' ')
            currency_table.update({ 'rate': tmp2[0] })

            struct_time = entry['published_parsed']
            tmp1 = datetime.datetime.fromtimestamp(time.mktime(struct_time), datetime.timezone.utc)
            tmp2 = tmp1.strftime('%Y-%m-%d %H:%M:%S %Z')
            currency_table.update({ 'published': tmp2 })


    tmp = currency_table['kbn'].split('/')
    print('1 %s = %s %s' % (tmp[0], '{:.2f}'.format(float(currency_table['rate'])), tmp[1]))


    sys.exit()
