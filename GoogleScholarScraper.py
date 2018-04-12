from urllib2 import urlopen
from bs4 import BeautifulSoup

url = "https://scholar.google.co.in/citations?view_op=search_authors&mauthors=anuja+arora+jiit&hl=en&oi=ao"
base_link = "https://scholar.google.co.in"

def main():
        page = urlib2.urlopen(url)
        soup = BeautifulSoup(page)
        all_anchors = soup.find_all('a')
        print(soup)
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
        print(profile_soup)


if __name__ == "__main__":
    main()
