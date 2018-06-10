import csv
import RAKE

with open('keras_issues.csv', 'rt', encoding='utf-8', errors='replace') as f:
    reader = csv.reader(f)
    row_text = ""
    for row in reader:
        row_text += row[22]
    
Rake = RAKE.Rake(RAKE.SmartStopList())
print(Rake.run(row_text))
