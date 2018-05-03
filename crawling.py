# 웹 열어서 데이터 읽어오기
# 설치방법은 윈도우10 기준. cmd 에서 명령어 넣기
# pip install requests 로 설치 가능
import urllib.request
# 가독성있게 파싱
# pip install beautifulsoup4 로 설치 가능
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20180503').read(), 'html.parser')

if __name__ == "__main__":
    soup = BeautifulSoup(urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20180503').read(), 'html.parser')
    res = soup.find_all('div', 'tit5')

# print(res)는 html 코드까지 같이 출력
    for n in res:
        print(n.get_text())
