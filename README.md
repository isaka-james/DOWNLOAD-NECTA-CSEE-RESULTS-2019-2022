# NECTA-RESULTS-2019-2022
These Python scripts facilitate the downloading of individual school CSEE NECTA results from the years 2019 to 2022, in their respective orders.

## How to Download Files
   + clone the project
```bash
git clone https://github.com/isaka-james/DOWNLOAD-NECTA-CSEE-RESULTS-2019-2022.git
cd DOWNLOAD-NECTA-CSEE-RESULTS-2019-2022
```
   + Run the script
```python
python3 start.py
```
After the program finishes, you will find all school files organized in their respective folders (Years).
The folders format
```yaml
DOWNLOAD-NECTA-CSEE-RESULTS-2019-2022
│
├── 2019
│   ├── School1
│   ├── School2
│   └── ...
│
├── 2020
│   ├── School1
│   ├── School2
│   └── ...
│
├── 2021
│   ├── School1
│   ├── School2
│   └── ...
│
└── 2022
    ├── School1
    ├── School2
    └── ...
```

Please note that the total size of all downloaded files is estimated to be around 990+MB.
   
## Additional Information
The data is scraped from two sources: the official NECTA site and maktaba.tetea.org.


### Contributing
Contributions are welcome! The project is designed to be flexible, allowing easy integration of results from future years. Feel free to contribute and improve the project for upcoming NECTA results.
