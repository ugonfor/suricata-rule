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
print(len(urls['https']) + len(urls['http']))


f = open("test.rules", "wt")

idx = 0
for url in urls['http']:
    f.write(f'alert tcp any any -> any 80 (msg:"HTTP {url} access"; content:"GET /"; content:"Host: "; content:"{url}"; nocase; sid:{10001 + idx}; rev:1;)\n')
    idx += 1
for url in urls['https']:
    f.write(f'alert tcp any any -> any 443 (msg:"HTTPS {url} access"; tls.sni; content:"{url}"; nocase; sid:{10001 + idx}; rev:1;)\n')
    idx += 1

    
f.close()