import csv
import RAKE

with open('keras_issues.csv', 'rt', encoding='utf-8', errors='replace') as f:
    reader = csv.reader(f)
    row_text = ""
    for row in reader:
        row_text += " "
        row_text += row[22]
    
Rake = RAKE.Rake(RAKE.SmartStopList())
row_text_output = Rake.run(row_text)

with open("output.csv",'w', encoding="utf-8", errors="ignore") as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(row_text_output)
