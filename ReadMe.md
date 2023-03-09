# Clean bib files 

This little script deletes all unused entries in a bib file. It works as follows:

- Extract all citations from the tex file, by matching the inside of the latex commands \cite{} and \citA{}
- go through bib file line by line and stop at lines starting with @ (e.g. @article)
- check if name of citation entry appears in the citations extracted from the text file 
- if it doesn't, discard all lines until next line starting with @

bib and tex file should be in the same directory as the python script. The script will ask to enter file names upon start.

In the command line, simply navigate to the script directory and run the script with: 

    python clean_bibtex.py 
