from uszipcode import SearchEngine

def generate_zipcode_file(output_filename="zipcodes.txt"):
    """Fetches all US zip codes and writes them to a file."""
    print("Initializing zipcode database (this may take a moment the first time)...")
    # By default, it uses simple_zipcode database
    # To use the comprehensive database, use SearchEngine(db_file_dir="/path/to/your/custom/db")
    # See library docs for download instructions if needed.
    search = SearchEngine()

    print("Fetching all zip codes...")
    # Get all zip codes by querying with returns=0 (no limit)
    all_zipcodes = search.query(returns=0)

    print(f"Writing zip codes to {output_filename}...")
    count = 0
    with open(output_filename, 'w') as f:
        # Iterate over the results from the query
        for zipcode_obj in all_zipcodes:
            f.write(f"{zipcode_obj.zipcode}\n")
            count += 1

    print(f"Successfully wrote {count} zip codes to {output_filename}.")

if __name__ == "__main__":
    generate_zipcode_file()
