# 🔌 Port Info Lookup

A lightweight and reliable Python utility that fetches and displays **port information** (service name, protocol, and description) using the official **IANA service-names-port-numbers** dataset.

---


## 📖 Overview
This tool allows you to easily find which protocol or service runs on a specific port, leveraging the official [IANA](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml) port assignments.

---


## ✨ Features
- Fetch port details directly from the **IANA** official dataset
- Automatically downloads and caches the CSV file
- Lookup service name, port number, transport protocol, and description
- Lightweight and dependency-minimal (only `requests`)

---


## 📦 Installation

```bash
git clone https://github.com/iamx-ariful-islam/port-info-lookup.git
cd port-info-lookup
pip install .
# or
python setup.py install
```


## 📂 Folder / File Structure

```bash
port-info-lookup/
│
├── data_files/
│   │
│   ├── ports_details.csv
│
├── port_info.py
├── README.md
├── requirements.txt
├── setup.py
└── test.py
```


## 🚀 Usage

```python
from port_info import port_info

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
```


## ⚙️ Dependencies

The `requirements.txt` file, lists of all the Python libraries that my "**_port info lookup_**" depends on and installs those packages from the file:

```bash
pip install -r requirements.txt
# or
sudo pip install -r requirements.txt
```


## 📜 Note

Fetches url for port information using the IANA service-names-port-numbers dataset:

```bash
IANA_URL = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"
```

## 💡 Future Enhancements

- Add search by service name or protocol
- Command-line interface (CLI)
- Offline mode with cached dataset validation


## Contributing

Contributions, suggestions, and feedback are always welcome! ❤️
To contribute:

1. Fork the repository
1. Create a new branch (`feature/new-feature`)
1. Commit your changes
1. Push and submit a Pull Request

💬 You can also open an issue if you’d like to discuss a feature or report a bug.


## For more or connect with me

<p align='center'>
  <a href="https://github.com/iamx-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://x.com/mx_ariful_islam"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/iamx-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>


## License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)