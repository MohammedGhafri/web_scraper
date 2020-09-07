import requests
from bs4 import BeautifulSoup as bt
import json
import re

URL='https://en.wikipedia.org/wiki/Solar_cell'
page=requests.get(URL)
# print(page.content)

# Scrap the page
soup=bt(page.content, 'html.parser')


"""
Target div that contain the paragraphs

"""
content=soup.find(id='mw-content-text')


def get_citations_needed_count():

    """
    Report the number of paragraph that need citation

    """
    number_of_citations_needed=content.find_all(class_="noprint Inline-Template Template-Fact")
    return f"Number of citation :{len(number_of_citations_needed)}"

print(get_citations_needed_count())




class citation_needed:
    arr=[]
    def __init__(self,i,p):
        self.index=i
        self.paragraph=p
        
        self.arr.append({'Index Of paragraph': i,'paragraph need for citation':p})

    @classmethod
    def dump(cls):
        """
        cls.arr-{Dictionary}: contain paragraphs that need citation
        """
        return cls.arr



def get_citations_needed_report():

    # relevant passage
    relevant_passage=content.find_all('p')

    for i,p in enumerate(relevant_passage,len(relevant_passage)):

        """
        i-{integer} represent the index of the paragraph
        p-{string}: pragrapgh in div
        """
        # print(p.text.strip()=='citation needed')
        
        try:
            
            """
            Target parent(Relevant Passage) only if '[citation needed]' exist 

            """
            # Target '[citation needed]' in the paragraphs
            a=p.find(class_='noprint Inline-Template Template-Fact')


            if p.find(class_='noprint Inline-Template Template-Fact') != None:
                
                citation_needed(i,p.text.strip())
                # print(p.text)
                x = p.text.split("[citation needed]",)
                print(x)
                # print(len(result))
            
        
        except:
            continue


# get_citations_needed_report()


# # relevant passage
# relevant_passage=content.find_all('p')
# # print(relevant_passage[2].text.strip()=='citation needed')
# for i,p in enumerate(relevant_passage,len(relevant_passage)):

#     """
#     i-{integer} represent the index of the paragraph
#     p-{string}: pragrapgh in div
#     """
#     # print(p.text.strip()=='citation needed')
#     try:
        
#         """
#         Target parent(Relevant Passage) only if '[citation needed]' exist 

#         """
#         # Target '[citation needed]' in the paragraphs
#         a=p.find(class_='noprint Inline-Template Template-Fact')


#         if p.find(class_='noprint Inline-Template Template-Fact') != None:
            
#             citation_needed(i,p.text)
        
      
#     except:
#         continue

a="mohammed ghafri"
# print(a[1:])
        
"""
To write the data that need citaion
"""


if __name__=='__main__':
    get_citations_needed_count()
    get_citations_needed_report()
    with open('citation_needed.json', 'w') as outfile:
        json.dump(citation_needed.dump(), outfile)