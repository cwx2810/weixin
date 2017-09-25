from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError

base_url = 'http://weixin.sogou.com/weixin?'

# cookie
headers = {
    'Cookie': 'SUV=007353952BF29AA559B551113681F453; IPLOC=CN6500; SUID=A198F22B2320940A0000000059BF96E7; ld=hlllllllll2Bsib7lllllVu@OmZlllll3@3Yoyllll9lllll9klll5@@@@@@@@@@; LSTMV=473%2C215; LCLKINT=8050; SNUID=AF92FA2308025EFE7CDF4E6C0849F8F8; ABTEST=8|1506302945|v1; weixinIndexVisited=1; sct=3; JSESSIONID=aaaavp8MUNhSu4msndz6v; ppinf=5|1506303941|1507513541|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1NDolRTclQTUlOTYlRTUlOUIlQkQlRTUlOUMlQTglRTYlODglOTElRTUlQkYlODMlRTQlQjglQUR8Y3J0OjEwOjE1MDYzMDM5NDF8cmVmbmljazo1NDolRTclQTUlOTYlRTUlOUIlQkQlRTUlOUMlQTglRTYlODglOTElRTUlQkYlODMlRTQlQjglQUR8dXNlcmlkOjQ0Om85dDJsdUo3aGZLeGhRNGVrWmFCeVo4MHdIM0lAd2VpeGluLnNvaHUuY29tfA; pprdig=kaQl69DTCFKsrAY7v0Zoj6Z12vS6kLK8Gn6nwLR8PmKlp2YQEGBpwzPT4RoCO28Vcpu0tzpuXQAr_DeaAIlQl6Ysos65oXXlkd_iofehOpStMCh1znPNfUeel0tY3GVGwFxS-gzJBfHDeQN5bCeAZ8xlOXzL_g-reGvHrXh58sE; sgid=31-31055541-AVnIX8VsaM6QVy3YLAWegbQ; ppmdig=1506303941000000d8ee449cba43651b19f4698cfb0462dd',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

# 具体获取页面内容
def get_html(url):
    try:
        # 不让requests收到302后跳转，传入cookie以获取100页内容
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            pass
    except ConnectionError:
        return get_html(url)

# 设置关键词和页数，获取搜狗索引页
def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    # 把data解析为url
    queries = urlencode(data)
    # 拼接url
    url = base_url + queries
    html = get_html(url)
    print(html)

if __name__ == '__main__':
    get_index('风景', 1)