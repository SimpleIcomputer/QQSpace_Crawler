#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import configparser
import sys
# import matplotlib.pyplot as plt
# import matplotlib
# font = {'family': 'MicroSoft YaHei'}
# matplotlib.rc('font', **font)
'operation_file function and saving for contant'
# functions:


def load_inifile():
    # get config_imformations
    # driver_path : driver_path
    # start_url : url for start
    # base_url : baseurl for get text
    # qq_number : qqnumber for scrapy
    # time_start,time_end : time limit
    # js_code : decode js code
    try:
        config_reader = configparser.RawConfigParser()
        config_reader.read("config.ini")
        features = ["driver_path", "start_url",
                    "base_url", "including_forward", "qq_number", "time_start", "time_end", "js_code"]
        config_infor = {}
        for i in range(0, 3):
            config_infor[features[i]] = config_reader.get(
                "settings", features[i])
            if config_infor[features[i]] == "":
                raise Exception(
                    "load_inifile callback: settings must not be NULL!")
        for i in range(3, 7):
            config_infor[features[i]] = config_reader.get(
                "user_config", features[i])
            if config_infor[features[i]] == "":
                raise Exception(
                    "load_inifile callback: user_config must not be NULL!")
        for i in range(7, 8):
            config_infor[features[i]] = config_reader.get(
                "decode_gtk", features[i])
            if config_infor[features[i]] == "":
                raise Exception(
                    "load_inifile callback: decode_gtk must not be NULL!")
        return config_infor
    except Exception as e:
        print(e)
        temp = input()
        sys.exit()


def contant_init():
    try:
        contant = load_inifile()
        return contant
    except Exception as e:
        print(e)
        temp = input()
        sys.exit()


def write2file(dataframe):
    try:
        print("crawling done")
        if dataframe["com_names"] != {}:
            datatemp = sorted(dataframe["com_names"].items(),
                              key=lambda d: d[1], reverse=True)
            datatemplis = []
            for i in range(3):
                datatemplis.append(datatemp[i])
            dataframe["com_names"] = dict(datatemplis)
        print("writing to result.csv")
        if dataframe["content"] == {}:
            print("nothing to write!")
            return
        pd.DataFrame(dataframe).to_csv("result.csv")
        # for name, times in dataframe["com_names"].items():
        #     plt.bar(name, times)
        # plt.legend()
        # plt.xlabel('小可爱们')
        # plt.ylabel("次数")
        # plt.savefig("com_names.png")
        print("done")
        return
    except Exception as e:
        print(e)
        temp = input()
        sys.exit()
