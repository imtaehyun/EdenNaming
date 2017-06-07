#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sqlite3

from bs4 import BeautifulSoup
from requests import get
"""
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "hanja" char(1) NULL,
    "strokes" integer NULL,
    "add_strokes" integer NULL,
    "is_naming_hanja" char(1) NULL,
    "meaning" text NULL,
"""
REMOVE_ID = [24, 28, 42, 51, 53, 172, 206, 293, 303, 405, 427, 428, 654, 658, 669, 698, 711, 717, 742, 746, 803, 804, 806, 818, 833, 852, 884, 885, 906, 924, 931, 947, 949, 964, 988, 999, 1062, 1101, 1123, 1125, 1132, 1164, 1178, 1181, 1199, 1279, 1281, 1314, 1393, 1520, 1524, 1538, 1539, 1556, 1656, 1723, 1833, 1841, 1919, 1920, 1961, 1977, 1992, 2013, 2014, 2071, 2089, 2092, 2110, 2114, 2128, 2129, 2186, 2215, 2223, 2345, 2346, 2393, 2439, 2444, 2501, 2513, 2547, 2553, 2621, 2775, 2798, 2802, 2803, 2938, 2967, 3024, 3038, 3046, 3047, 3051, 3248, 3250, 3270, 3282, 3299, 3307, 3311, 3316, 3319, 3364, 3388, 3402, 3413, 3429, 3432, 3437, 3439, 3441, 3493, 3501, 3550, 3571, 3593, 3642, 3683, 3686, 3746, 3747, 3856, 3876, 3888, 3890, 3968, 3970, 3994, 4080, 4133, 4166, 4191, 4355, 4483, 4489, 4507, 4539, 4643, 4646, 4676, 4702, 4724, 4762, 4791, 4792, 4846, 4850, 4863, 4875, 4908, 4920, 4921, 4931, 5039, 5040, 5063, 5093, 5140, 5246, 5287, 5290, 5322, 5354, 5384, 5399, 5429, 5477, 5536, 5558, 5716, 5731, 5757, 5771, 5779, 5844, 5879, 5882, 5899, 5915, 6060, 6063, 6071, 6118, 6134, 6159, 6170, 6189, 6197, 6199, 6207, 6208, 6240, 6244, 6260, 6296, 6318, 6319, 6387, 6410, 6632, 6636, 6664, 6665, 6671, 6760, 6768, 6771, 6801, 6912, 6994, 7014, 7052, 7134, 7299, 7529, 7531, 7758, 7791, 7826, 7833, 7853, 7947, 7951, 7959, 7987, 8058, 8179,]


def update_naming_flag(flag, hanja, conn):
    update_flag = conn.cursor()
    update_flag.execute(query)
    conn.commit()


def set_detail_info(conn):
    s = conn.cursor()
    for i in range(len(REMOVE_ID)):
        #query = 'UPDATE naming_hanja SET is_naming_hanja=0 WHERE id=%d' % REMOVE_ID[i]
        #s.execute(query)
        query = 'select id,hanja,reading,is_naming_hanja from naming_hanja where id=%d' % REMOVE_ID[i]
        for row in s.execute(query):
            print(row)

    #conn.commit()

def main():
    conn = sqlite3.connect('naming_korean.db')
    set_detail_info(conn)

    conn.close()  # sqlite3 close


if __name__ == '__main__':
    main()