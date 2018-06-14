from urllib import request
import io
import gzip

__all__ = [
    'get_content_by_url'
]

def get_content_by_url(url):
    page = request.Request(url)
    data = request.urlopen(page)
    encoding = data.getheader('Content-Encoding')
    content = data.read()
    if encoding == 'gzip':
        buf = io.BytesIO(content)
        gf = gzip.GzipFile(fileobj=buf)
        content = gf.read()
    return content.decode("gb2312", 'ignore')