#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'crawler function'

from selenium import webdriver
import datetime
import execjs
import json
import sys
import re


imformations = {}
browser = None
js_function = None
dataframe = {}
dataframe["cmtnum"] = 0
dataframe["com_names"] = {}
dataframe["content"] = {}
dataframe["postime"] = {}
re_sourcecode = r'{"auth_flag"(.+)}'
re_cnde = '[\u4e00 -\u9fa5]+'


def time_legitimate(time_start, time_end):
    try:
        imformations["time_start"] = datetime.datetime.strptime(
            imformations["time_start"], '%Y-%m-%d')
        imformations["time_end"] = datetime.datetime.strptime(
            imformations["time_end"], '%Y-%m-%d')
        imformations["time_now"] = datetime.datetime.now()
        if imformations["time_end"] > imformations["time_start"]:
            raise Exception("time_legitimate() callback:time error!")
        if imformations["time_end"] > imformations["time_now"]:
            raise Exception("time_legitimate() callback:time error!")
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def get_GTK(str):
    try:
        return js_function.call("getGTK", str)
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def is_start(start_time, now_time):
    try:
        if start_time >= now_time:
            return True
        return False
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def is_end(end_time, now_time):
    try:
        if end_time > now_time:
            return True
        return False
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def trans_TodayorYesterdayorDby(trains_time):
    try:
        if "年" in trains_time:
            return False
        if "昨天" in trains_time:
            return datetime.datetime.now()-datetime.timedelta(days=1)
        if "前天" in trains_time:
            return datetime.datetime.now()-datetime.timedelta(days=2)
        return datetime.datetime.now()-datetime.timedelta(days=0)
    except Exception as e:
        print(e)
        temp = input()
        sys.exit()


def get_cookie():
    try:
        cookies = browser.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'p_skey':
                imformations["hash"] = cookie["value"]
                return True
        browser.quit()
        raise Exception("crawler() callback: p_skey not in coockies!")
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def data_flitter(source):
    try:
        fliter = re.compile(re_sourcecode, re.S | re.M | re.U)
        datas = fliter.search(source)
        datas_dict = json.loads(datas.group(0))
        if "msglist" not in datas_dict.keys() or datas_dict["msglist"] == "null":
            return False
        data_filtereds = []
        for msg in datas_dict["msglist"]:
            if imformations["including_forward"] == "False":
                if "rt_certified" in msg.keys():
                    continue
            data_filtered = {}
            data_filtered["com_names"] = []
            data_filtered["createTime"] = msg["createTime"]
            data_filtered["content"] = msg["content"]
            data_filtered["cmtnum"] = msg["cmtnum"]
            if msg["commentlist"] is None:
                data_filtereds.append(data_filtered)
                continue
            for comments in msg["commentlist"]:
                data_filtered["com_names"].append(comments["name"])
            data_filtereds.append(data_filtered)
        return data_filtereds
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def text_numerical(datas):
    try:
        pat = re.compile(r'[\u4e00-\u9fa5]+')
        temp = pat.findall(datas["content"])
        content = ""
        for words in temp:
            content += words
        datas["content"] = content
        dataframe["cmtnum"] += datas["cmtnum"]
        dataframe["content"][datas["content"]
                             ] = dataframe["content"].get(datas["content"], 0)+1
        dataframe["postime"][imformations["time_now"].strftime("%y-%m-%d")
                             ] = dataframe["postime"].get(
            (imformations["time_now"].strftime("%y-%m-%d")), 0)+1
        if datas["com_names"] is None:
            return
        for name in datas["com_names"]:
            dataframe["com_names"][name] = dataframe["com_names"].get(
                name, 0)+1
        return
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def imformation_init(contant):
    try:
        global imformations, browser, js_function
        imformations = contant
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        browser = webdriver.Chrome(
            executable_path=imformations["driver_path"], chrome_options=option)
        js_function = execjs.compile(imformations["js_code"])
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def crawler_init(contant):
    try:
        imformation_init(contant)
        time_legitimate(imformations["time_start"], imformations["time_end"])
        while True:
            browser.get(imformations["start_url"])
            print("Are you ready? enter y/n")
            temp = input()
            if temp == "y" or temp == "henxin!":
                return get_cookie()
            elif temp is "n":
                browser.quit()
                return False
            elif temp is "q":
                browser.quit()
                sys.exit()
            print("?")
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()


def crawling():
    try:
        base_url = imformations["base_url"].format(
            imformations["qq_number"],
            imformations["qq_number"], "{}", "20", get_GTK(imformations["hash"]))
        browser.set_window_size(0, 0)
        for num in [x*20 for x in range(9999)]:
            browser.get(base_url.format(str(num)))
            data_filtereds = data_flitter(browser.page_source)
            if data_filtereds is False:
                print("interrupt:", imformations["time_now"])
                return dataframe
            for data_filtered in data_filtereds:
                trans_time = trans_TodayorYesterdayorDby(
                    data_filtered["createTime"])
                imformations["time_now"] = trans_time
                if trans_time is False:
                    imformations["time_now"] = datetime.datetime.strptime(
                        data_filtered["createTime"], '%Y年%m月%d日')
                if is_start(imformations["time_start"], imformations["time_now"]):
                    if is_end(imformations["time_end"], imformations["time_now"]):
                        browser.quit()
                        return dataframe
                    text_numerical(data_filtered)
        browser.quit()
        return dataframe
    except Exception as e:
        print(e)
        browser.quit()
        temp = input()
        sys.exit()
