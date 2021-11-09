from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez

# for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
#     print(seq_record.id)
#     print(seq_record.seq)
#     print(len(seq_record))


# file = open('sequence.txt', 'r')
# lines = file.readlines()
# for index, seqs in enumerate(lines):
#     my = Seq(seqs.strip())
#     print(index, my.translate(table=1))


# seq_record = SeqIO.read("NC_005816.gb", "genbank")
# print(seq_record.id)
# print(seq_record.name)
# print(seq_record.description)
# print(seq_record.letter_annotations)
# print(seq_record.annotations["source"])
# print(seq_record.dbxrefs)
# print(seq_record.features)


# Entrez.email = "suresh66692@gmail.com" # Always tell NCBI who you are
# handle = Entrez.esearch(db="pubmed", term="activating mutation[title]", retmax="200" )
# record = Entrez.read(handle)
# print(record['IdList'])

Entrez.email = "suresh66692@gmail.com" # Always tell NCBI who you are
handle = Entrez.esearch(db="pubmed", term="activating mutation[title]", retmax="10" )
record = Entrez.read(handle)
IdList = record['IdList']
for id in IdList:
    handle = Entrez.esummary(db="pubmed", id=id)
    pm = Entrez.read(handle)
    info = pm[0]["TitleMainList"][0]
    print("Journal info\nid: {}\nTitle: {}".format(pm[0]["Id"], info["Title"]))

