import re
def getScore(word, page):
    import re
    return re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())

def solution(word, pages):
    webpages = {}
    for i, page in enumerate(pages):
        pagetitle = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        links = []
        for link_long in page.split('a href=\"')[1:]:
            links.append(link_long.split('\"')[0])
        webpages[pagetitle] = [i, getScore(word, page), links, 0] #3은 링크점수

    for page in webpages.values():
        for target in page[2]:
            try:
                webpages[target][3] += page[1] / len(page[2])
            except:
                pass
    answer = []        
    for page in webpages.values():
        answer.append([page[0], page[1] + page[3]])
    answer.sort(key=lambda x:x[0])
    return sorted(answer, key=lambda x:x[1], reverse=True)[0][0]


