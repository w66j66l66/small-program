##初稿，下面有正式版

# import requests
# import re
# from bs4 import BeautifulSoup
# # 目标URL
# url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp?cb=news'
# # 发送HTTP请求
# resp = requests.get(url).text
# # 获取响应内容和示例文本的赋值

# text = resp
# # 正则表达式模式
# pattern = r'"url":"(https://news\.cctv\.com/\d{4}/\d{2}/\d{2}/[^"]+)"'
# # 查找所有匹配项
# matches = re.findall(pattern, text)
# #索引结束，匹配结果是matches






# def parse_cctv_article(html):
#     soup = BeautifulSoup(html, 'lxml')

#     # 标题：优先 h1，再 fallback <title>
#     title_tag = soup.find('h1')
#     title = title_tag.get_text(strip=True) if title_tag else (soup.title.string.strip() if soup.title else '')

#     # 发布时间：尝试常见的 meta 属性或页面内文本
#     pub = None
#     for meta_name in ('pubdate', 'publishdate', 'article:published_time', 'ptime'):
#         m = soup.find('meta', attrs={'name': meta_name}) or soup.find('meta', attrs={'property': meta_name})
#         if m and m.get('content'):
#             pub = m['content']
#             break
#     if not pub:
#         # 有时发布时间在一个带时间类名的标签内
#         time_tag = soup.find(class_=re.compile(r'(time|date|pub|ptime)', re.I))
#         if time_tag:
#             pub = time_tag.get_text(strip=True)

#     # 正文：尝试多个常见容器，按找到的第一个且文本足够长的返回
#     candidates = [
#         ('div', {'class': 'cnt_bd'}),
#         ('div', {'class': 'content'}),
#         ('div', {'id': 'content'}),
#         ('div', {'class': re.compile(r'(article|content|main)', re.I)}),
#         ('div', {'id': re.compile(r'(article|content|main)', re.I)}),
#         ('article', {}),
#     ]
#     article_text = ''
#     for name, attrs in candidates:
#         node = soup.find(name, attrs=attrs)
#         if node:
#             # 合并段落文本
#             parts = [p.get_text(strip=True) for p in node.find_all(['p', 'div']) if p.get_text(strip=True)]
#             article_text = '\n\n'.join(parts).strip()
#             if len(article_text) > 50:
#                 break

#     # 最后 fallback：页面里第一个长文本块
#     if not article_text:
#         paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
#         article_text = '\n\n'.join(paragraphs).strip()

#     return {
#         'title': title,
#         'published': pub,
#         'content': article_text
#     }




# for i in matches:
#     url_1 = i
    # resp_1 = requests.get(url=url_1)
    # resp_1.encoding = "utf-8"  
    # html_data = resp_1.text 
    # if __name__ == '__main__':
    #     data = parse_cctv_article(html_data)
    #     print('标题:', data['title'])
    #     print('发布时间:', data['published'])
    #     print('正文预览:\n', data['content'][:1000])






###正式版###
#正式版要安装requests,re,beautifulsoup,os,reportlab这些库
# ...existing code...
import requests
import re
from bs4 import BeautifulSoup
import os

# 目标URL
url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp?cb=news'
# 发送HTTP请求
resp = requests.get(url).text
# 获取响应内容和示例文本的赋值

text = resp
# 正则表达式模式
pattern = r'"url":"(https://news\.cctv\.com/\d{4}/\d{2}/\d{2}/[^"]+)"'
# 查找所有匹配项
matches = re.findall(pattern, text)
#索引结束，匹配结果是matches



def parse_cctv_article(html):
    soup = BeautifulSoup(html, 'lxml')

    # 标题：优先 h1，再 fallback <title>
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else (soup.title.string.strip() if soup.title else '')

    # 发布时间：尝试常见的 meta 属性或页面内文本
    pub = None
    for meta_name in ('pubdate', 'publishdate', 'article:published_time', 'ptime'):
        m = soup.find('meta', attrs={'name': meta_name}) or soup.find('meta', attrs={'property': meta_name})
        if m and m.get('content'):
            pub = m['content']
            break
    if not pub:
        # 有时发布时间在一个带时间类名的标签内
        time_tag = soup.find(class_=re.compile(r'(time|date|pub|ptime)', re.I))
        if time_tag:
            pub = time_tag.get_text(strip=True)

    # 正文：尝试多个常见容器，按找到的第一个且文本足够长的返回
    candidates = [
        ('div', {'class': 'cnt_bd'}),
        ('div', {'class': 'content'}),
        ('div', {'id': 'content'}),
        ('div', {'class': re.compile(r'(article|content|main)', re.I)}),
        ('div', {'id': re.compile(r'(article|content|main)', re.I)}),
        ('article', {}),
    ]
    article_text = ''
    for name, attrs in candidates:
        node = soup.find(name, attrs=attrs)
        if node:
            # 合并段落文本
            parts = [p.get_text(strip=True) for p in node.find_all(['p', 'div']) if p.get_text(strip=True)]
            article_text = '\n\n'.join(parts).strip()
            if len(article_text) > 50:
                break

    # 最后 fallback：页面里第一个长文本块
    if not article_text:
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
        article_text = '\n\n'.join(paragraphs).strip()

    return {
        'title': title,
        'published': pub,
        'content': article_text
    }

# ...existing code...
# { changed code }
# 收集文章
articles = []
for i in matches:
    url_1 = i
    resp_1 = requests.get(url=url_1)
    resp_1.encoding = "utf-8"  
    html_data = resp_1.text 
    if __name__ == '__main__':
        data = parse_cctv_article(html_data)
        print('标题:', data['title'])
        print('发布时间:', data['published'])
        print('正文预览:\n', data['content'][:1000])
        
    try:
        resp_1 = requests.get(url=url_1, timeout=10)
        resp_1.encoding = "utf-8"
        html_data = resp_1.text
        data = parse_cctv_article(html_data)
        articles.append({
            'url': url_1,
            'title': data['title'],
            'published': data['published'],
            'content': data['content']
        })
    except Exception as e:
        print('抓取出错：', url_1, e)

# 生成 PDF
def save_articles_pdf(articles, out_path):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except Exception:
        raise RuntimeError('需要安装 reportlab：pip install reportlab')

    # 找一个系统中文字体（如 msjh.ttf / msyh.ttf / simhei.ttf），如无请修改路径
    possible_fonts = [
        r"C:\Windows\Fonts\msyh.ttf",
        r"C:\Windows\Fonts\msyh.ttf", 
        r"C:\Windows\Fonts\msjh.ttf",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simfang.ttf"
    ]
    font_path = None
    for p in possible_fonts:
        if os.path.exists(p):
            font_path = p
            break
    if not font_path:
        raise RuntimeError('未找到中文字体文件，请将系统字体路径写入 possible_fonts 列表或安装中文字体。')

    font_name = 'UserChinese'
    pdfmetrics.registerFont(TTFont(font_name, font_path))

    doc = SimpleDocTemplate(out_path, pagesize=A4,
                            rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=60)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='MyTitle', fontName=font_name, fontSize=16, leading=20, spaceAfter=6))
    styles.add(ParagraphStyle(name='MyMeta', fontName=font_name, fontSize=10, leading=12, textColor=colors.grey))
    styles.add(ParagraphStyle(name='MyBody', fontName=font_name, fontSize=12, leading=16))

    story = []
    if not articles:
        story.append(Paragraph('未抓取到任何文章。', styles['MyBody']))
    else:
        for idx, art in enumerate(articles, 1):
            title = art.get('title') or ('未命名 第{}篇'.format(idx))
            pub = art.get('published') or ''
            content = art.get('content') or ''
            # Paragraph 需要 html-like 换行
            content = content.replace('&', '&amp;')
            content = content.replace('\r\n', '\n').replace('\r', '\n')
            content = content.replace('\n\n', '<br/><br/>').replace('\n', '<br/>')
            story.append(Paragraph(title, styles['MyTitle']))
            if pub:
                story.append(Paragraph(pub, styles['MyMeta']))
            story.append(Spacer(1, 6))
            story.append(Paragraph(content, styles['MyBody']))
            if idx != len(articles):
                story.append(PageBreak())

    doc.build(story)

# ...existing code...
if __name__ == '__main__':
    # 保存到脚本同目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_pdf = os.path.join(script_dir, '每日新闻.pdf')
    try:
        save_articles_pdf(articles, out_pdf)
        print('已生成 PDF：', out_pdf)
    except Exception as e:
        print('生成 PDF 失败：', e)
# ...existing code...
























    