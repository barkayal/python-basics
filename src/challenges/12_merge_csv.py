import csv


def merge_csv(csv_list, output_filename):
    fieldnames = []
    for input_filename in csv_list:
        input_path = '../../f.input/'+input_filename
        with open(input_path, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    output_path = '../../f.output/'+output_filename
    # write data to output file based on field names
    with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for input_filename in csv_list:
            input_path = '../../f.input/'+input_filename
            with open(input_path, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')