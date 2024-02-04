import os
import csv
import requests
from urllib.parse import urlparse

def extract_row_column_from_link(link):
    # Extract row and column from the image link
    parsed_url = urlparse(link)
    path_segments = parsed_url.path.split('/')
    row = int(path_segments[-2])
    column = int(path_segments[-1].split('.')[0])
    return row, column

def download_and_sort_images(input_file_path, output_folder):

    tot = 0

    # Create output folders if they don't exist
    for i in range(0, 34):
        folder_path = os.path.join(output_folder, f"column{i}")
        os.makedirs(folder_path, exist_ok=True)

    # Read links from the CSV file
    with open(input_file_path, 'r') as input_file:
        csv_reader = csv.reader(input_file)
        links = next(csv_reader)

        # Download and sort images
        for link in links:
            row, column = extract_row_column_from_link(link)
            output_folder_path = os.path.join(output_folder, f"column{row}")
            output_file_path = os.path.join(output_folder_path, f"row{column}.webp")

            # Download the image
            response = requests.get(link)
            with open(output_file_path, 'wb') as output_file:
                output_file.write(response.content)

            tot += 1
            print(f"Downloaded and sorted {link} to {output_file_path}\n({tot}/1024) - {round((tot/1024)*100, 2)}%")


    return str(tot)

# Specify the input CSV file and output folder
input_file_path = 'input_links.csv'
output_folder = 'output_images'

# Run the function
print("DONE! Downloaded",download_and_sort_images(input_file_path, output_folder),"images")
