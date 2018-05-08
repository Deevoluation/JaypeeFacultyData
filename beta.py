# for each paper, store top 5 authors, citation, year

from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString
import pandas as pd
import csv


papersInfo = []
papersname = []

def crawl(united_soup):
    #count = 0
    allTables = united_soup.find_all('table')
    try:
        dataTable = allTables[1]
    except IndexError:
        dataTable = allTables[0]
    body = dataTable.find_all('tbody')
    rows = body[0].find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        # print(columns[0].find_all('a')[0].get_text())
        # print(columns[1].get_text())
        # print(columns[2].get_text())
        p_name = columns[0].find_all('a')[0].get_text()
        if  p_name in papersname:
            pos = papersname.index(p_name)
            authors = columns[0].find_all('div')[0].get_text()
            authors = authors.split(',')
            for i in authors:
                if not(i in papersInfo[pos]):
                    papersInfo[pos].append(i)
        else:
            #paper = [columns[0].find_all('a')[0].get_text(), ]
            citation = columns[1].get_text()
            year = columns[2].get_text()
            if(citation == ""):
                citation = "Not found"
            if(year == ""):
                year = "Not found"
            authors = columns[0].find_all('div')[0].get_text()
            authors = authors.split(',')
            #print(authors)
            journal = columns[0].find_all('div')[1].get_text()
            '''
            print("paper: ",p_name)
            print ("cite=",citation,"year =",year)
            print ("authors=",authors,"journal=",journal)
            '''
            paper = [p_name,journal,citation,year] + authors
            #print(paper,"\n")
            papersInfo.append(paper)
            papersname.append(p_name)
    return len(rows)
    
def main():
    
    file = open('temp.html', 'w', newline='')
    excel_file = 'faculty_list.xlsx'
    data = pd.read_excel(excel_file)
    faculty_list = list(data['Faculty Name'])
    for teacher in faculty_list:
        print('teacher = ',teacher)
        fname = teacher.split()[0]
        lname = teacher.split()[1]
        path1 = "https://scholar.google.co.in/citations?view_op=search_authors&mauthors="
        path2 = "+jiit&hl=en&oi=ao"
        url = path1 + fname + "+" + lname + path2
        
        page = urlopen(url)
        soup = BeautifulSoup(page)
        all_anchors = soup.find_all('a')
        base_link = "https://scholar.google.co.in"
        further_link = "&cstart=20&pagesize=80"
        faculty_link = soup.select_one("a[href*=/citations?user]")
        profile_link = base_link + faculty_link['href']
    
        profile_page = urlopen(profile_link + "")
        profile_soup = BeautifulSoup(profile_page)
        
        num1 = 0
        num2 = 0
        
        num1 = crawl(profile_soup)
        
        
        further_page = urlopen(profile_link + further_link)
        further_soup = BeautifulSoup(further_page)
        
        if "There are no articles in this profile." in str(further_soup):
            print("next professor")
            # meaning that only 1 page was there for the current faculty. Move to next faculty
        else:
            num2 = crawl(further_soup)
        print('\nname = '+fname+lname)
        print("num1 = ",num1," num2 = ",num2)
        print("\n",num1+num2," papers found in ",fname+" "+lname)
            
        '''
        for i in range(0,len(papersInfo)):
            print("\n")
            for j in papersInfo[i]:
                print(j+"\n")
    		
        '''
    
    csvfile = "paperlist.csv"   
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(papersInfo)
    
    file.close()
if __name__ == "__main__":
    main()
