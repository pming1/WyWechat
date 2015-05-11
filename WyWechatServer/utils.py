#!/usr/bin/env python
# coding: utf-8

from wy_settings import wx_menu, AboutMeWithBindAccount, AboutMeWithoutBindAccount, AboueMechineCommandsInfo, \
    AboutBusinessCommandsInfo, ContactUsInfo, CompanyIntroductionInfo


def getInfo(url=''):
    import requests
    import json

    payload = {'action': 'result'}
    res = requests.get(url, params=payload)
    # print res.text
    return json.loads(res.text)


def error(wechat=None):
    return wechat.response_text(u'绑定账号后方能使用')


def return_news(wechat=None, req=None, content=[]):
    if wechat is None: return wechat.response_news([{'title': u'不知名错误', 'description': '', 'picurl': '', 'url': ''}, ])
    if isBind(req) is True: return wechat.response_news(content)
    return error(wechat)


def isBind(req=None):
    return req.session.get('BindAccount', False)


def AboutMe(wechat=None, req=None):
    if wechat is None: return wechat.response_news([{'title': u'不知名错误', 'description': '', 'picurl': '', 'url': ''}, ])
    if isBind(req) is True:
        return wechat.response_news(AboutMeWithBindAccount)
    else:
        return wechat.response_news(AboutMeWithoutBindAccount)


def AboueMechineCommands(wechat=None, req=None):
    return return_news(wechat, req, AboueMechineCommandsInfo)


def AboutBusinessCommands(wechat=None, req=None):
    return return_news(wechat, req, AboutBusinessCommandsInfo)


def BindAccount(wechat=None, req=None):
    if wechat is None: return wechat.response_news([{'title': u'不知名错误', 'description': '', 'picurl': '', 'url': ''}, ])
    # message = wechat.get_message()
    req.session['BindAccount'] = True
    return wechat.response_news([{'title': u'绑定结果', 'description': '', 'picurl': '', 'url': ''},
                                 {'title': u'绑定成功', 'description': '', 'picurl': '', 'url': ''}])


def UpdateMenu(wechat=None, req=None):
    if wechat is None: return wechat.response_news([{'title': u'不知名错误', 'description': '', 'picurl': '', 'url': ''}, ])
    return wechat.response_text(wechat.create_menu(wx_menu))


def MyMachine(wechat=None, req=None):
    articles = [{
                    'title': u'【我的机器】',
                    'description': '',
                    'picurl': '',
                    'url': ''
                }]
    articles.extend(getInfo('http://test.tunnel.mobi/MyMachine'))
    return return_news(wechat, req, articles)


def CheckComplaint(wechat=None, req=None):
    articles = [{
                    'title': u'【查看报障】',
                    'description': '',
                    'picurl': '',
                    'url': ''
                }]
    articles.extend(getInfo('http://test.tunnel.mobi/CheckComplaint'))
    return return_news(wechat, req, articles)


def ContactCustomerService(wechat=None, req=None):
    if wechat is None: return wechat.response_news([{'title': u'不知名错误', 'description': '', 'picurl': '', 'url': ''}, ])
    return wechat.response_text(u'客服正忙，请稍后再试')


def ContactUs(wechat=None, req=None):
    return return_news(wechat, req, ContactUsInfo)


def CompanyIntroduction(wechat=None, req=None):
    return return_news(wechat, req, CompanyIntroductionInfo)


do_commands_table = {
    'CompanyIntroduction': CompanyIntroduction,
    'ContactUs': ContactUs,
    # 'WyNews':WyNews,
    # 'DataCenter':DataCenter,
    # 'ZuYongTuoGuan':ZuYongTuoGuan,
    # 'JiGuiDaDaiKuan':JiGuiDaDaiKuan,
    # 'WyYunFangHu':WyYunFangHu,
    'BindAccount': BindAccount,
    'MyMachine': MyMachine,
    'CheckComplaint': CheckComplaint,
    'ContactCustomerService': ContactCustomerService,
    'AboutMe': AboutMe,
    '1': AboueMechineCommands,
    '2': AboutBusinessCommands,
    'UpdateMenu': UpdateMenu,

}