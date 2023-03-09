import re

# Get bib and tex name
bib_name = input('Enter bib file name: ')
tex_name = input('Enter tex file name: ')

if bib_name == '':
    bib_name = 'references.bib'
if tex_name == '':
    tex_name = 'main.tex'

# Load bib file from local directory
with open(bib_name, 'r') as f:
    bib = f.read()

# Load tex file from local directory
with open(tex_name, 'r') as f:
    tex = f.read()

test = "hallo what is up~\cite{{test}} everything cool man~\citeA{{test2}}? Ok now multiple reference ~\cite{{test3,test4 is a test}}. And an empty citation~\citeA{{}}. What will happen then?"

# Delete emtpy citations from tex file
tex = re.sub(r'\\citeA\{\}', '', tex)
tex = re.sub(r'\\cite\{\}', '', tex)

# Reg exp for matching \cite{...} and \citeA{...} including empty citations
# citations = re.findall(r'\\cite\{(.+?)\}', test)

# Get all citations from tex file
citations = [*re.findall(r'\\cite\{(.+?)\}', tex),*re.findall(r'\\citeA\{(.+?)\}', tex)]

# Split citations that are separated by comma
for citation in citations:
    if ',' in citation:
        citations.remove(citation)
        citations.extend(citation.split(','))

# Remove spaces from citations
citations = [citation.strip() for citation in citations]

# Remove duplicates from citations
citations = list(dict.fromkeys(citations))

# Go through bib file line by line
bib = bib.splitlines()

# Check if line starts with @ and if it does, check if the citation is in the list of citations
deleteFlag = True
cleaned_bib = []
for line in bib:
    if line.startswith('@'):
        citation_name = line.split('{')[1].split(',')[0]
        if citation_name not in citations:
            deleteFlag = True
        else:
            deleteFlag = False
            # Remove entry from citations list
            citations.remove(citation_name)
    if not deleteFlag:
        cleaned_bib.append(line + '\n')

# Join bib file again including line breaks
cleaned_bib = ''.join(cleaned_bib)
# print(bib)

# Save cleaned bib file to local directory
with open('cleaned_' + bib_name, 'w') as f:
    f.write(cleaned_bib)