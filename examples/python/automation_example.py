import csv

INPUT_CSV = 'data/input.csv'

def transform_row(row):
    # Example transform: normalize email and combine name
    email = row.get('email','').strip().lower()
    name = (row.get('first_name','').strip() + ' ' + row.get('last_name','').strip()).strip()
    return {'name': name, 'email': email}

def main():
    try:
        with open(INPUT_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            out = [transform_row(r) for r in reader]
        for r in out:
            print(r)
    except FileNotFoundError:
        print(f"Place a CSV at {INPUT_CSV} with columns: first_name,last_name,email")

if __name__ == '__main__':
    main()
