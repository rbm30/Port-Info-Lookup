"""
Port Information Lookup Utility
Author: Md. Ariful Islam
GitHub: https://github.com/iamx-ariful-islam
License: MIT
Description: Fetches and looks up port information using the IANA service-names-port-numbers dataset.
"""
# pip install requests

import os
import csv
import requests



DATA_DIR = "data_files"
CSV_FILE = os.path.join(DATA_DIR, "ports_details.csv")
IANA_URL = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"


def download_file(url: str, filename: str) -> None:
    # Download a file from a given URL and save it locally
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total = response.headers.get("content-length")
    chunk_size = max(int(int(total) / 1000), 1024 * 1024) if total else 1024 * 1024

    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)


def ensure_data_file() -> None:
    # Ensure that the data directory and CSV file exist
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.isfile(CSV_FILE):
        print("[INFO] Downloading port details CSV from IANA...")
        download_file(IANA_URL, CSV_FILE)
        print("[INFO] Download completed.")


def port_info(port_no: int):
    """
    Retrieve information about a given port number.

    :param port_no: Port number to look up
    :return: Dictionary containing service name, transport protocol, and description
    """
    ensure_data_file()

    with open(CSV_FILE, newline="", encoding="utf-8", errors="ignore") as file:
        reader  = csv.reader(file)
        headers = next(reader, None)

        for row in reader:
            if len(row) >= 4 and row[1] == str(port_no):
                return {
                    "service_name": row[0],
                    "port_number": row[1],
                    "transport_protocol": row[2],
                    "description": row[3],
                }
    return None


# root
if __name__ == "__main__":
    info = port_info(22)
    if info:
        print(f"Port number        : {info['port_number']}")
        print(f"Transport protocol : {info['transport_protocol']}")
        print(f"Service name       : {info['service_name']}")
        print(f"Description        : {info['description']}")
    else:
        print("No information found for this port.")
        
    
    
    """output:
    
    Port number        : 22
    Transport protocol : tcp
    Service name       : ssh
    Description        : The Secure Shell (SSH) Protocol
    """