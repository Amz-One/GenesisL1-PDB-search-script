# GenesisL1-pbid-search-script
PDB Search script made for GenesisL1 task that searches The Protein Data Bank for a given pdbid and outputs molecule(s) details into a CSV file, if matches are found.

The PDB archive searched can be found here: https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt

Instructions:


Download and Run the Python script in command line

When prompted for input, Input the desired pdbid, this should be a 4 character string that includes letters and numbers (Example 12e8 or 6mud). If a string that is not equal to 4 characters in length is input, an error will be raised.

The script will run and look for matches in the database, if 1 or more matches are found, the results will be written to a CSV file with the same name as the pdbid. The CSV file can be found in the same directory as the script.

If no matches are found this will be printed to the console and no CSV file will be written.

Please note due to the size of the database the search may take a few minutes depending on where in the database the id may be found, the lower down the database it is, the longer the search is likely to be. 
However, as soon as all the matches are found, the search stops, preventing the whole file being read and thus saving time.
