# for each paper, store top 5 authors, citation, year

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://scholar.google.co.in/citations?view_op=search_authors&mauthors=anuja+arora+jiit&hl=en&oi=ao"
base_link = "https://scholar.google.co.in"
papersInfo = []
papersname = set([])

def main():
        file = open('temp.html', 'w', newline = '')
        page = urlopen(url)
        soup = BeautifulSoup(page)
        all_anchors = soup.find_all('a')
        # print(soup)
        print(all_anchors.__len__())
        # for anchor in all_anchors:
            # print(anchor)
        # temp = soup.select_one("a[href*=/citations?user]")
        # print(temp)
        # print(temp['href'])
        faculty_link = soup.select_one("a[href*=/citations?user]")
        profile_link = base_link + faculty_link['href']
        print(profile_link)
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

        # print(dataTable)
        print(type(dataTable))
        body = dataTable.find_all('body')
        print(body)



if __name__ == "__main__":
    main()
