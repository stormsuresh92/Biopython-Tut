from Bio import Medline
import pandas as pd

data = []
with open("pubmed-activating-set.txt", encoding='utf-8') as handle:
    for record in Medline.parse(handle):
        try:
            Article_type = record['PT']
            PMID = record['PMID']
            Title = record["TI"]
            Date = record["DP"]
            Volume = record['VI']
            Issue = record['IP']
            Page = record['PG']
            Doi = record['LID']
            Abstract = record['AB']
            Author = record['AU']
            Affiliation = record['AD']
            dic = {
                'Article_type':Article_type,
                'PMID':PMID,
                'Title':Title,
                'DP':Date,
                'Volume':Volume,
                'Issue':Issue,
                'Page':Page,
                'Doi':Doi,
                'Abstract':Abstract,
                'Author':Author,
                'Affiliation':Affiliation
            }
            data.append(dic)
        except:
            pass

df = pd.DataFrame(data)
df.to_csv('out.csv', index=False)
print('fin')
   