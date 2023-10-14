import requests
import csv

PLACES_ID = [
  "ChIJv-mQ-SZm5kcRZ57eWrOltRA",
  "ChIJdSPq8v8U5kcRIAKGFw-FKJk",
  "ChIJza_ktiOJ5kcR_IoRjLyyLMI",
  "ChIJ4eRKQLsJ5kcRVxMwfe1sdEk",
  "ChIJI87fk_YS5kcRdeA6DE-zNyk",
  "ChIJVYDtVOLZ5UcR5WRTu_qLCPI",
  "ChIJOyh-DMYO5kcRrjpohIMClVY",
  "ChIJqzMWD5SD5kcR3P8JhX8qs_8",
  "ChIJWwDCHu5B5kcRT0_b2PirZNA",
  "ChIJxTngR7AM5kcR61dyHcR11o4",
  "ChIJcSf3Yv_e5UcRtMXb2_2kCxg",
  "ChIJY7TLeLE-5kcR8LfJLi9ew74",
  "ChIJnTbtNfES5kcRFMij69sgzUc",
  "ChIJjXOHBX8M5kcRixhinV_2zKY",
  "ChIJF6ziPX5z5kcRdanokzfKFKs",
  "ChIJTTboGgoV5kcR0DGhO4qNuV0",
  "ChIJR3KS3uh85EcRWNGxuqj0ylY",
  "ChIJM9PIYNhf5kcRuZbWWarJMzk",
  "ChIJsREw4igP5kcRmsB3zdkD8J8",
  "ChIJ9-v8zBcI5kcR_-RqU3lcQzM",
  "ChIJ__9vLZli5kcRp8HUPvv31YQ",
  "ChIJi4Zc2Mjj5UcRTGZNru7hefM",
  "ChIJw8ehe5sL5kcR7VUSbitLokM",
  "ChIJ4Uj1_2Ft5kcReBJJtkfuuqE",
  "ChIJL_VuumQP5kcRxEp0VCEv_L0",
  "ChIJ7wGnLaFb5kcRB8UbQpa-iuI",
  "ChIJD0q3D2MT5kcRmPpPfvljfEM",
  "ChIJe7t36cAZ5kcRzQeUSFBNM7I",
  "ChIJN-dgOCAF5kcRsc4mrvdHUUQ",
  "ChIJhV02sO8i5kcRgmTtmp7Yp5c",
  "ChIJwduFKMMV5kcRjrZvVZg4jaM",
  "ChIJK-ERfb8U5kcRtWpC6WVlE-c",
  "ChIJs8WmgILj5UcRB_4tC2jOR2U",
  "ChIJjU6Mdc4a5kcRLP3dfPuo_u4",
  "ChIJcTcaSSMI5kcR9MMIUWSSJ98",
  "ChIJ28qHQznW5UcRu2fVYAFeVLs",
  "ChIJeVIrNtFq5kcR7-9C-L7EbIU",
  "ChIJjxNBbVjX5UcRhTlFlNBIvmE",
  "ChIJx24ELuRG5kcR07xR90gSIpk",
  "ChIJv8Z_DiPf5UcRgRESEwobrP4",
  "ChIJUa61GjXn5UcRLYpO59XL7fg",
  "ChIJtd3vf7E-5kcRnyHArh15rzc",
  "ChIJH2KgCDeD5kcRujH6HwSAT0U",
  "ChIJzX1_vlB35kcRZz7X6yth0Xk",
  "ChIJNW-LHucK5kcRWp6GuzR4pKo",
  "ChIJrwt71A3e5UcRZsLMdlZajxM",
  "ChIJ8bqjDch35kcRgU7GySF7JoU",
  "ChIJ-dUfXI705kcRzZzAvSej7lM",
  "ChIJYTDrOEQP5kcREO9MYnVs2UY",
  "ChIJVfqc7c9x5kcRS42v9lHAbBk",
  "ChIJQyWPVYPZ5UcRiJ1ngL2gX6k",
  "ChIJDW1OYSxr5kcRzPyZyMekI_o",
  "ChIJleRqSHGA5kcRnEcIxXRpCKs",
  "ChIJn_tiFQNA5kcR4oyNDKSkRSg",
  "ChIJ13IPeFV25kcRN0X8fBlNyEo",
  "ChIJpwGXM50V5kcRIbzKpPUSVrs",
  "ChIJU1NdockV5kcRywokkkMGPqo",
  "ChIJPxpISt9x5kcRXcRcsY2Kimc",
  "ChIJUf6A5ZzZ5UcRW1fiiiygmE8",
  "ChIJn6pQMcZ35kcRSy5ISCbrgto"
]
API_KEY = "AIzaSyApeXWJE5MSQ8mapOkNOgitzfOxhgiOm_o"




# Open CSV file for writing
with open('hotel_reviews.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header to the CSV file
    csv_writer.writerow(['Hotel Address', 'Hotel Name', 'Review'])

    for place_id in PLACES_ID:
        url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Extract relevant information
        if 'result' in data:
            address = data['result'].get('formatted_address', '')
            name = data['result'].get('name', '')

            if 'reviews' in data['result']:
                reviews = [review['text'] for review in data['result']['reviews']]

                # Write data to CSV
                for review in reviews:
                    csv_writer.writerow([address, name, review])
