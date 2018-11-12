from urllib import request
import io
import gzip

__all__ = [
    'get_content_by_url'
]

def get_content_by_url(url):
    page = request.Request(url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    data = request.urlopen(page,headers=headers)
    encoding = data.getheader('Content-Encoding')
    content = data.read()
    if encoding == 'gzip':
        buf = io.BytesIO(content)
        gf = gzip.GzipFile(fileobj=buf)
        content = gf.read()
    return content.decode("gb2312", 'ignore')