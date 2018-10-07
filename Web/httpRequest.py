#coding=utf-8
#!/user/bin/env python
#腾讯视频加复活卡

import random,urllib2,time

if  __name__ == '__main__':
    cardnum = 100
    your_card = "8WN4aT"
    url=r'https://tunnel.video.qq.com/qqlive/revive_card_exchange?vappid=18744662&vsecret=64152c29dd78d368cc5268e250f70d483a7b4c18eff681d7&inviteKey=%s&callback=__jp14'%your_card
    
    for i in range(cardnum):
        j = str(random.randint(0,99999999)).zfill(8)
        print j
        headers={'Host': 'tunnel.video.qq.com',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043808 Mobile Safari/537.36 QQLiveBrowser/6.0.0.14297',
                'Accept': '*/*',
                'Referer': 'https://act.v.qq.com/live/qa/index.html?ovscroll=0&hidestatusbar=1&hidetitlebar=1&style=titlecolor%3D%23ffffff',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,en-US;q=0.8',
                'Cookie': 'gid=1a0013fa-8498-446d-92bd-11dac4d4f2ab; pvid=2065870166; tvfe_boss_uuid=589c8f04ecb53af6; vuserid=%s; vusession=3c80b991cd02cd6774fa; luin=o1142584593; uin=o1142584593; lskey=00030000500e574a68c1e1b61872a6a1e70c767ad3fbdd0acf644977e6fcf32f3f33d7869de4ff98b8af1042; skey=MuFPieSj9z; main_login=qq'%str(j),
                'Q-UA2': 'QV=3&PL=ADR&PR=TRD&PP=com.tencent.qqlive&PPVN=6.0.0.14297&TBSVC=43500&CO=BK&COVC=043808&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MI6 &RL=1080*1920&OS=7.1.1&API=25',
                'Q-GUID': '6365c4428ee26931d6f3d7ad13b788cb',
                'Q-Auth': '31045b957cf33acf31e40be2f3e71c5217597676a9729f1b'
                 }
        request=urllib2.Request(url=url,headers=headers)
        response=urllib2.urlopen(request)
        content= response.read()
        time.sleep(2)
        