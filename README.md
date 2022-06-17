# GenesisL1-pbid-search-script
PDB Search script made for GenesisL1 task that searches The Protein Data Bank for a given pdbid and outputs molecule(s) details into a CSV file, if matches are found.

The PDB archive searched can be found here: https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt

Instructions:


Download and Run the Python script in command line

When prompted for input, Input the desired pdbid, this should be a 4 character string that includes letters and numbers. If a string that is not equal to 4 characters in length is input, an error will be raised.

The script will run and look for matches in the database, if 1 or more matches are found, the results will be written to a CSV file with the same name as the pdbid. The CSV file can be found in the same directory as the script.

If no matches are found this will be printed to the console and no CSV file will be written.
