import requests

class TiebaSpider:
    def __init__(self,Tieba_name):
        self.tieba_name = Tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?ie=utf-8&kw='+Tieba_name+'&pn={}'.format()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }

    # 1、构建url列表
    def get_url_list(self):
        url_list = []
        for i in range(1000):
            url_list.append(self.url_temp.format(i*50))
        return url_list

    # 发送请求，获取响应
    def parse_url(self,url):
        
        response = requests.get(url,headers=self.headers)
        return response.content.decode()




    def run(self):
        # 实现主要逻辑
        # 1、构建url列表
        url_list =  self.get_url_list()

        # 2、遍历、发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)

        # 保存字符串
        def save_html(self,html_str,page_num):
            # 保存的格式：'李毅-第一页.html' '李毅-第二页.html' '……'
            file_path = '{}-第{}页.html'.format(self.tieba_name,page_num)
            with open(file_path,'w') as f:
                f.write(html_str)

            # 3、保存
            self.save_html(html_str)
            page_num = url_list.index(url)+1    # 页码数
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    Tieba_Spider = TiebaSpider('李毅')
    Tieba_Spider.run()