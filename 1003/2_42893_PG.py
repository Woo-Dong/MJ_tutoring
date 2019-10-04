"""
Programmers - 42893번(매칭점수)
https://programmers.co.kr/learn/courses/30/lessons/42893

문제설명
프렌즈 대학교 조교였던 제이지는 허드렛일만 시키는 네오 학과장님의 마수에서 벗어나, 카카오에 입사하게 되었다.
평소에 관심있어하던 검색에 마침 결원이 발생하여, 검색개발팀에 편입될 수 있었고, 대망의 첫 프로젝트를 맡게 되었다.
그 프로젝트는 검색어에 가장 잘 맞는 웹페이지를 보여주기 위해 아래와 같은 규칙으로 검색어에 대한 웹페이지의 매칭점수를 계산 하는 것이었다.

한 웹페이지에 대해서 기본점수, 외부 링크 수, 링크점수, 그리고 매칭점수를 구할 수 있다.
한 웹페이지의 기본점수는 해당 웹페이지의 텍스트 중, 검색어가 등장하는 횟수이다. (대소문자 무시)
한 웹페이지의 외부 링크 수는 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수이다.
한 웹페이지의 링크점수는 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합이다.
한 웹페이지의 매칭점수는 기본점수와 링크점수의 합으로 계산한다.

검색어 word와 웹페이지의 HTML 목록인 pages가 주어졌을 때, 매칭점수가 가장 높은 웹페이지의 index를 구하라. 
만약 그런 웹페이지가 여러 개라면 그중 번호가 가장 작은 것을 구하라.
"""

# Test case 12/20 Accuracy(60%) :(

import re
def solution(word, pages):

    site_idx_Dict = dict()
    basic_score_Dict = dict()
    score_Dict = dict()
    link_Dict = dict()
    linked_Dict = dict()
    word = word.lower()

    for num, page in enumerate(pages):
        site_content = page.split("<meta property=\"og:url\" content=\"")[1]
        site_content = site_content.split("\"/>")[0]

        site_idx_Dict[site_content] = num
        link_Dict[site_content] = list()
        linked_Dict[site_content] = list()
        body = page.split("<body>\n")[1].split("</body>")[0].split("\n")

        score = 0
        link_num = 0

        for line in body:
            string = line
            if "<a" in line:
                a_link_list = line.split("a href=\"")[1:]
                for a_link in a_link_list:
                    a_link = a_link.split("\"")[0]
                    link_Dict[site_content].append(a_link.strip())
                    link_num += 1
                    string = line.split("<a")[0] + line.split("a>")[1]

            string = string.lower()
            string = re.sub('[^a-z]+', ' ', string)
            for elem in string.split(" "):
                if elem.strip() == word:
                    score += 1
        basic_score_Dict[site_content] = score

        if link_num != 0:
            score_Dict[site_content] = score / link_num
        else:
            score_Dict[site_content] = 0

    for elem in site_idx_Dict:
        for link in link_Dict[elem]:
            if not link in linked_Dict:
                continue
            linked_Dict[link].append(elem)
    
    fin_list = list()
    for page, idx in site_idx_Dict.items():
        score = basic_score_Dict[page]
        for elem in linked_Dict[page]:
            score += score_Dict[elem]
        fin_list.append( (score, idx) )
    fin_list.sort(key=lambda x:x[1])    
    fin_list.sort(reverse=True, key=lambda x:x[0])
    # print(fin_list)
    return fin_list[0][1]

word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))
word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word, pages))


