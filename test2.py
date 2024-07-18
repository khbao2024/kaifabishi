# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:51:21 2024

@author: 包凯华
"""
import re

def reg_search(text, regex_list):
    result = []
    for regex in regex_list:
        match_dict = {}
        for key, pattern in regex.items():
            matches = re.findall(pattern, text)
            if matches:
                match_dict[key] = matches
        if match_dict:
            result.append(match_dict)
    return result

text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束之日满12个月后的第一个交易日起至可交换债券到期日止，即2023年6月2日至2027年6月1日止。
'''

regex_list = [{
    '标的证券': r'股票代码：(\w+\.\w+)',
    '换股期限': r'即(.*?)至'
}]

result = reg_search(text, regex_list)
print(result)