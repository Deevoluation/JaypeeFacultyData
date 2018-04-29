# for each paper, store top 5 authors, citation, year

from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString

url = "https://scholar.google.co.in/citations?view_op=search_authors&mauthors=anuja+arora+jiit&hl=en&oi=ao"
further_link = "&cstart=20&pagesize=80"
base_link = "https://scholar.google.co.in"
papersInfo = []
papersname = set([])


def main():
    file = open('temp.html', 'w', newline='')
    page = urlopen(url)
    soup = BeautifulSoup(page)
    all_anchors = soup.find_all('a')
    # print(soup)
    print(all_anchors.__len__())

    faculty_link = soup.select_one("a[href*=/citations?user]")
    profile_link = base_link + faculty_link['href']
    # print(profile_link)
    profile_page = urlopen(profile_link + "")
    profile_soup = BeautifulSoup(profile_page)
    print("\n")
    # print(profile_soup)
    # file.write(str(profile_soup))

    # from this point, work flow is as follows :
    # pick a paper. if it does not exists in current data (papersname), create a new papersInfo.
    # else add an additional column in the papersInfo

    allTables = profile_soup.find_all('table')
    dataTable = allTables[1]
    body = dataTable.find_all('tbody')
    rows = body[0].find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        # print(columns[0].find_all('a')[0].get_text())
        # print(columns[1].get_text())
        # print(columns[2].get_text())
        if columns[0].find_all('a')[0].get_text() in papersname:
            pos = papersname.index(columns[0].find_all('a'[0]))
            papersInfo[pos].append("add name of current professor as a co-author to this paper")
        else:
            paper = [columns[0].find_all('a')[0].get_text(), ]
            papersInfo.append(paper)

    print(papersInfo.__len__())

    further_page = urlopen(profile_link + further_link)
    further_soup = BeautifulSoup(further_page)

    if "There are no articles in this profile." in str(further_soup):
        print("next professor")
        # meaning that only 1 page was there for the current faculty. Move to next faculty
    else:
        allTables = profile_soup.find_all('table')
        dataTable = allTables[1]
        body = dataTable.find_all('tbody')
        rows = body[0].find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            # print(columns[0].find_all('a')[0].get_text())
            # print(columns[1].get_text())
            # print(columns[2].get_text())
            if columns[0].find_all('a')[0].get_text() in papersname:
                pos = papersname.index(columns[0].find_all('a'[0]))
                papersInfo[pos].append("add name of current professor as a co-author to this paper")
            else:
                paper = [columns[0].find_all('a')[0].get_text(), ]
                papersInfo.append(paper)

    print(papersInfo.__len__())


if __name__ == "__main__":
    main()
