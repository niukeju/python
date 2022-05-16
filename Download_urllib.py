# 调用urllib.request
import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# urlretrieve(url,filename) -- url指下载的路径，filename指文件的名字
urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
url_img = 'https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=lisa&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=910999065,3961346066&os=1308061232,3801347634&simid=910999065,3961346066&pn=11&rn=1&di=7077213605308923905&ln=1242&fr=&fmq=1651764488088_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fc-ssl.duitang.com%252Fuploads%252Fitem%252F202005%252F20%252F20200520193446_lmsge.thumb.1000_0.jpg%26refer%3Dhttp%253A%252F%252Fc-ssl.duitang.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1654356488%26t%3D4bcfa36cc4e483825d7adffcca64c1ce&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwzLDYsNCw1LDcsOCwxLDIsOQ%3D%3D'
urllib.request.urlretrieve(url_img,'lisa.jpg')

# 下载视频
url_video = '<video class="" autoplay="" playsinline="true" x5-playsinline="true" webkit-playsinline="true" tabindex="2" mediatype="video"><source class="" src="//v26-web.douyinvod.com/9d881e89b0ec10c880fb92f4150e5363/62740d09/video/tos/cn/tos-cn-ve-15/34dbb221b1c348a1a8543f42b85e6440/?a=6383&amp;ch=4&amp;cr=0&amp;dr=0&amp;lr=all&amp;cd=0%7C0%7C0%7C0&amp;br=233&amp;bt=233&amp;cs=0&amp;ds=6&amp;ft=X1nbLXvvBQapUqey78Z.BOMzJ4lcNSzKF2bLL9sYv8Zm&amp;mime_type=video_mp4&amp;qs=0&amp;rc=N2U0OGZnOGc8OTY3ZGg6O0BpM21wZGgzNztydjMzOmkzM0BeLTY2Xi4yXzQxNl4tY2E2YSMvcTJpMTYzZm1fLS0zLTBzcw%3D%3D&amp;l=202205060030290101381721970B43EAB6" type=""><source class="" src="//v3-web.douyinvod.com/fbd42c50712a052a98de15774ca48782/62740d09/video/tos/cn/tos-cn-ve-15/34dbb221b1c348a1a8543f42b85e6440/?a=6383&amp;ch=4&amp;cr=0&amp;dr=0&amp;lr=all&amp;cd=0%7C0%7C0%7C0&amp;br=233&amp;bt=233&amp;cs=0&amp;ds=6&amp;ft=X1nbLXvvBQapUqey78Z.BOMzJ4lcNSzKF2bLL9sYv8Zm&amp;mime_type=video_mp4&amp;qs=0&amp;rc=N2U0OGZnOGc8OTY3ZGg6O0BpM21wZGgzNztydjMzOmkzM0BeLTY2Xi4yXzQxNl4tY2E2YSMvcTJpMTYzZm1fLS0zLTBzcw%3D%3D&amp;l=202205060030290101381721970B43EAB6" type=""><source class="" src="//www.douyin.com/aweme/v1/play/?video_id=v0300f670000bspoi864904ela5mtj20&amp;line=0&amp;file_id=98d7fe0aa4934679bd551dac95910ba4&amp;sign=b18855a303dab95ac0c3a2839ce06686&amp;is_play_url=1&amp;source=PackSourceEnum_FAVORITE&amp;aid=6383" type=""></video>'
urllib.request.urlretrieve(url_video,'video.mp4')