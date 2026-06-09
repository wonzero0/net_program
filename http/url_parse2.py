from urllib import parse
url = 'https://home.sch.ac.kr/sch/06/010100.jsp?mode=view&article_no=20250502144326361065&board_wrapper=%2Fsch%2F06%2F010100.jsp&pager.offset=0&board_no=20090723152156588979'
parsed_url = parse.urlsplit(url)
print(parsed_url)
print('scheme :', parsed_url.scheme)
print('netloc :', parsed_url.netloc)
print('path :', parsed_url.path)
print('query :', parsed_url.query)
print('fragment:', parsed_url.fragment)