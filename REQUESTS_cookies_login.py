'''
不发送post请求，直接使用cookie获取登录后的页面
使用情况：
    1、cookie过期时间很长的网站
    2、在cookie过期之前能够拿到所有数据，比较麻烦
    3、配合其他程序一块使用，其他程序专门获取cookie，当前程序专门请求页面
'''

import requests

# post_url = 'https://www.huya.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Cookie":"udb_guiddata=c7804d4a4f3c442aaee67e91d3345fed; udb_deviceid=w_555457535814471680; __yamid_tt1=0.09709432031890874; __yamid_new=C9BEB86BAB9000014D967CBFF9C41D96; game_did=XgG5uDnQpzJlhbaxTvlyKu-8dKaDj7dDKSH; alphaValue=0.80; guid=0adb05fdb2c72d62f0012abe2bbede24; videoBitRate=4000; videoLine=3; isInLiveRoom=; Hm_lvt_51700b6c722f5bb4cf39906a596ea41f=1650361621,1652694535; __yasmid=0.09709432031890874; udb_passdata=3; SoundValue=0.00;nickname=%E4%BD%A0%E5%9C%A8%E6%83%B3%E5%85%A5%E9%9D%9E%E9%9D%9E; partner_uid=88443665559BB2999EB5BCD1BBA65E42; udb_biztoken=AQAyO0_J1HJHsBNYhvvF0ifeTEmw2jMcuIkxbFk5N93vwG3rRss6xFvyvZhuyAffX6VSxwe9YImwLZ2eREwe2OD1nciHciHa9dbWb1tWv1Q-txaGI58a8TQ5FSPmDcKBngUAY2FrASR9746FFoetHI9yZ2wF_qXHeqH_wkJGGkHXpUwyKTHhreuIeiti5L-qoxPM_c20GU8jSOyhwRa8mZsTjC7imU6cdT7mByhkC4b_uZZReVXfEZtmDzKs933syNdbdfcRk5NcZd-l0KIhG8K-zxKvgw5yWkoWEVVIUIXnJUcuAxU2lT2LMREJMxoiQ7mRW1Fu4D39OWKVXHELMUFK; udb_cred=CnCzTOJXpDVRE5q9dis_x0ehj1-vDuqIs779hhS_vKYLcKZiHlUzbnZjRn1uAVaM1cRB8vVIQnFIkI8QGeeD76GWkFsPFeMJw02SpXpHJoiAmjgBv7s-oepjotaT39Kz2fs; udb_openid=88443665559BB2999EB5BCD1BBA65E42; udb_origin=5; udb_other=%7B%22lt%22%3A%221652704574016%22%2C%22isRem%22%3A%221%22%7D; udb_passport=hy_167087240; udb_status=1; udb_uid=1259571444673; udb_version=1.0; username=hy_167087240; yyuid=1259571444673; rep_cnt=41; __yaoldyyuid=1259571444673; _yasids=__rootsid%3DC9D35915B4300001908CAD90D0531EF8; huya_ua=webh5&0.0.1&websocket; PHPSESSID=3802dt9p2pa2n8ab5e1451f343; h_unt=1652772464; huya_flash_rep_cnt=107; Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f=1652772478; huya_web_rep_cnt=204"
}

login_url = 'https://i.huya.com/'

response = requests.get(login_url,headers=headers)

# 保存页面
with open('login_1.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())

'''
cookie也可以作为requests.get()中的一个值
cookies = {键:值}
'''
# 字典引导式
dict = {i:i+10 for i in range(10)}
print(dict)