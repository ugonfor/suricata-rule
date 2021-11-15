import requests

urls = dict()

urls['http'] = ['gilgil.net']
urls['https'] = [
    'google.com',
    'naver.com',
    'daum.net',
    'github.com',
    'gitlab.com',
    'portal.korea.ac.kr',
    'yonsei.ac.kr',
    'snu.ac.kr',
    'kaist.ac.kr',
    'kisa.or.kr',
    'kitribob.kr',
    'twitter.com',
    'youtube.com',
    'instagram.com',
    'netflix.com',
    'facebook.com',
    'qt.io',
    'programmers.co.kr',
    'tistory.com',
    'arxiv.org',
]

for url in urls['http']:
    r = requests.get(f'http://{url}')
    
    print(f'{r.url} status code={r.status_code}')
for url in urls['https']:
    r = requests.get(f'https://{url}')
    print(f'{r.url} status code={r.status_code}')
