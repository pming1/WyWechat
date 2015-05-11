#!/usr/bin/env python
# coding: utf-8

# 微信公众号绑定信息
weixin_appid = u'wx85ddc4617e4400b0'
weixin_secret = u'237dc3cc551b6bac043f660cbab093ca'

# 微信公众号菜单配置
wx_menu = {
    "button": [
        {
            "name": u'走进唯一',
            "sub_button": [
                {
                    "type": "click",
                    "name": u'公司简介',
                    "key": "CompanyIntroduction",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'联系我们',
                    "key": "ContactUs",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'唯一动态',
                    "key": "WyNews",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'数据中心',
                    "key": "DataCenter",
                    "sub_button": []
                },
                {
                    "type": "view",
                    "name": u'唯一招聘',
                    "url": "http://www.wy.com.cn/job.aspx",
                    "sub_button": []
                }
            ]
        },
        {
            "name": u'产品服务',
            "sub_button": [
                {
                    "type": "click",
                    "name": u'租用托管',
                    "key": "ZuYongTuoGuan",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'机柜大带宽',
                    "key": "JiGuiDaDaiKuan",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'唯一云防护',
                    "key": "WyYunFangHu",
                    "sub_button": []
                },
                {
                    "type": "view",
                    "name": u'智能免费DNS',
                    "url": "http://www.51dns.com/",
                    "sub_button": []
                },
                {
                    "type": "view",
                    "name": u'防护宝',
                    "url": "https://www.fanghubao.com",
                    "sub_button": []
                }
            ]
        },
        {
            "name": u'客户中心',
            "sub_button": [
                {
                    "type": "click",
                    "name": u'绑定账号',
                    "key": "BindAccount",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'我的机器',
                    "key": "MyMachine",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'查看报障',
                    "key": "CheckComplaint",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'联系客服',
                    "key": "ContactCustomerService",
                    "sub_button": []
                },
                {
                    "type": "click",
                    "name": u'我的帮助',
                    "key": "AboutMe",
                    "sub_button": []
                }
            ]
        }
    ]
}

#我的帮助
#未绑定帮助信息
AboutMeWithoutBindAccount = [
    {
        'title': u'欢迎关注唯一网络',
        'description': '',
        'picurl': 'http://183.60.143.221/Images/AboutMe.jpg',
        'url': 'http://www.wy.com.cn'
    },
    {
        'title': u'通过【客户中心->绑定账号】来获得更多功能\n详情请登陆我们官方网站:\nhttp://www.wy.com.cn',
        'description': '',
        'picurl': '',
        'url': 'http://www.wy.com.cn'
    },
    {
        'title': u'24小时售后电话：4007-166-188\n有故障请及时与我们联系哦！！',
        'description': '',
        'picurl': '',
        'url': 'http://www.wy.com.cn'
    },
]

#已绑定帮助信息	
AboutMeWithBindAccount = [
    {
        'title': u'欢迎关注唯一网络',
        'description': '',
        'picurl': 'http://183.60.143.221/Images/AboutMe.jpg',
        'url': 'http://www.wy.com.cn'
    },
    {
        'title': u'【1机器相关指令】 ping 重启 备份 释放 报障',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【2业务相关指令】 近期到期 最近账单',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'回复对应数字查看使用方法\n点击按钮 “帮助” 返回本菜单',
        'description': '',
        'picurl': '',
        'url': ''
    },
]

#机器指令说明	
AboueMechineCommandsInfo = [
    {
        'title': u'【机器相关指令】',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【PING操作】\n  机器线路，    发送‘ping  192.168.0.2',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【重启 操作】\n  重启机器，    发送‘重启 192.168.0.2',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【备份 操作】\n  备份机器，    发送‘备份 192.168.0.2',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【释放 操作】\n  释放机器，    发送‘释放 192.168.0.2’',
        'description': '',
        'picurl': '',
        'url': ''
    },
]

#业务指令说明	
AboutBusinessCommandsInfo = [
    {
        'title': u'【业务相关指令】',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【近期到期 操作】\n  查看近期到期，    发送；近期到期’',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【最近账单 操作】\n  查看最近账单，    发送：最近账单',
        'description': '',
        'picurl': '',
        'url': ''
    },
]

#我的机器信息	
MyMachineInfo = [
    {
        'title': u'【我的机器】',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【192.0.0.1(xx网站)】',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【192.0.0.2(xx游戏)】',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【192.0.0.3(xx后台)】',
        'description': '',
        'picurl': '',
        'url': ''
    },
]

#查看报障信息	
CheckComplaintInfo = [
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
]

#联系我们信息	
ContactUsInfo = [
    {
        'title': u'【联系我们】',
        'description': '',
        'picurl': 'http://183.60.143.221/Images/AboutMe.jpg',
        'url': 'http://www.wy.com.cn'
    },
    {
        'title': u'【广东省东莞市唯一网络科技有限公司】\n【WeiYi Network Technology Co., Ltd.】 \n通讯地址：东莞市南城区黄金路1号天安数码城B1区4楼\n邮政编码：523000\n联系电话：0769-23015555  22030330  22030333  22030300\n24H客服电话：4007-166-188\n传真号码：0769-28330000',
        'description': '',
        'picurl': '',
        'url': 'http://www.wy.com.cn'
    },
    {
        'title': u'【厦门分公司】\n通讯地址：厦门市思明区软件园二期望海路57号2楼\n邮政编码：361008\n联系电话：0592-2570000\n传真号码：0592-2952666',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【湛江分公司】\n通讯地址：湛江市赤坎区人民大道北41号京基大厦910\n邮政编码：524022\n联系电话：0759-3372928\n传真号码：0759-3372928',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【深圳分公司】\n通讯地址：深圳市南山区田厦国际中心A座25楼03号\n邮政编码：518000\n联系电话：0755-86706003',
        'description': '',
        'picurl': '',
        'url': ''
    },
    {
        'title': u'【北京分公司】\n通讯地址：北京市朝阳区建国路93号万达广场3号楼1102室\n邮政编码：100022\n联系电话：010-58208558\n传真号码：010-58206266',
        'description': '',
        'picurl': '',
        'url': ''
    },
]

#公司简介信息	
CompanyIntroductionInfo = [
    {
        'title': u'【公司简介】',
        'description': u'东莞市唯一网络科技有限公司（简称“唯一网络”）成立于2005年8月，是国内领先互联网增值业务提供商。为客户提供高品质的服务器租用，服务器托管，机柜大带宽，网络安全，CDN加速等互联网增值业务解决方案',
        'picurl': 'http://183.60.143.221/Images/AboutMe.jpg',
        'url': 'http://mp.weixin.qq.com/s?__biz=MjM5MjM3NTMwMg==&mid=200520472&idx=1&sn=0e0045d856f24d75f923bb7e696a3094&scene=18#rd'
    }
]