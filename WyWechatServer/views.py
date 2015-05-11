# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from wechat_sdk.basic import WechatBasic
from wechat_sdk.exceptions import ParseError
from wy_settings import weixin_appid, weixin_secret
from utils import do_commands_table


def hello(request):
    import json

    return HttpResponse(json.dumps([
        {
            'title': u'【查看报障】',
            'description': '',
            'picurl': '',
            'url': ''
        },
        {
            'title': u'【192.0.0.1(xx网站)】【2015.5.1】\n 故障类型：*** \n 处理进度：未受理 \n 受理人  ：暂无',
            'description': '',
            'picurl': '',
            'url': ''
        },
        {
            'title': u'【192.0.0.1(xx游戏)】【2015.4.30】\n 故障类型：*** \n 处理进度：修理中 \n 受理人  ：**工号',
            'description': '',
            'picurl': '',
            'url': ''
        },
        {
            'title': u'【192.0.0.1(xx后台)】【2015.4.29】\n 故障类型：*** \n 处理进度：已解决 \n 受理人  ：**工号',
            'description': '',
            'picurl': '',
            'url': ''
        },
    ]))


def MyMachine(request):
    return render_to_response('MyMachine.html', '')


def CheckComplaint(request):
    return render_to_response('CheckComplaint.html', '')


@csrf_exempt
def weixin(request):
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    xml = request.body
    wechat_instance = WechatBasic(token='custom_service', appid=weixin_appid, appsecret=weixin_secret)
    if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        return HttpResponseBadRequest('Verify Failed')
    else:
        if request.method == 'GET': return HttpResponse(request.GET.get('echostr'))
    try:
        wechat_instance.parse_data(data=xml)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
    message = wechat_instance.get_message()
    # try:
    if message.type == 'text':
        # response = wechat_instance.response_text(u'文字')
        if do_commands_table.has_key(message.content):
            response = do_commands_table[message.content](wechat_instance, request)
        else:
            response = wechat_instance.response_text(message.content)
    elif message.type == 'image':
        content = message.media_id
        response = wechat_instance.response_text(u'图片')
    elif message.type == 'voice':
        response = wechat_instance.response_text(u'声音')
    elif message.type == 'video' or message.type == 'shortvideo':
        response = wechat_instance.response_text(u'视频')
    elif message.type == 'location':
        response = wechat_instance.response_text(u'地理位置')
    elif message.type == 'link':
        response = wechat_instance.response_text(u'链接')
    elif message.type == 'event':
        response = wechat_instance.response_text(u'事件')
    elif message.type == 'click' or message.type == 'view':
        if do_commands_table.has_key(message.key):
            response = do_commands_table[message.key](wechat_instance, request)
        else:
            response = wechat_instance.response_text(message.key)
    else:
        response = wechat_instance.response_text(u'未知' + message.type)
    # except:
    # response = wechat_instance.response_text(u'服务器错误')

    return HttpResponse(response)