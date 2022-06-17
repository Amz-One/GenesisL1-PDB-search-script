
import re, csv , contextlib
from urllib.request import urlopen

query = input("Please enter 4 character search term\n") #12e8, 6mud
assert len(query) == 4 and re.match("^[1-9]", query) != None, "query input must be 4 characters and start with an integer between 1 and 9"
assert re.match("\d{4}", query) == None, "query cannot be a 4 digit number, it must contain letters"

link = 'https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt'

with contextlib.closing(urlopen(link)) as f:

    row_list = []

    for number, line in enumerate(f, start=1):
        txt = line.decode('utf8')
        if not txt.startswith('>'):
            continue
        if txt.startswith(f'>{query}'):
            global n
            n = number
            reg_list = re.findall(":\w+", txt)
            id = re.search("\w{4}_\w", txt).group()
            mol_name_search = re.search("\s{2}[a-zA-Z\d()*,.'\[\]\-\s]+", txt)
            mol_name = txt[mol_name_search.span()[0] +2: mol_name_search.span()[1] -1]
            seq = f.readline().decode('utf-8').rstrip('\n')
            row_list.append([id, reg_list[0][1::], reg_list[1][1::], mol_name, seq])
        try:
            number > n
        except:
            continue
        else:
            if not txt.startswith(f'>{query}') and number > n:
                break

print(f'Search complete! {len(row_list)} matches found')
if len(row_list) > 0:
    sheet = open(f'{query}.csv', 'w', newline='', encoding='utf8')
    writer = csv.writer(sheet)
    writer.writerow(["id", "Molecule type", "length", "Molecule Name", "Sequence"])
    writer.writerows(row_list)
    sheet.close()
    print(f"Please view results in {query}.csv file, Have a good day!\n")
