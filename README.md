
# Script and CSS Extractor

This Python script extracts all JavaScript and CSS links from an HTML file and outputs them in Markdown format. It categorizes the links into those found in the `<head>` and `<body>` tags.

## Installation

Before running the script, ensure that you have Python installed on your system. Download `main.py`
Then, install the required packages using: 

```bash
pip install beautifulsoup4
lxml
```

## Usage

Run the script from the command line by passing the path to your HTML file as an argument, or if you leave it blank it will look in the default location. The script generates a Markdown file named `scriptsAndCss.md` with the extracted information.

```bash
python scriptExtractor.py ignite\src\main\resources\templates\index.html
```

## Requirements

- Python 3
- BeautifulSoup4

## Output

The script creates a file named `scriptsAndCss.md` in the same directory where the script is run. This file contains the extracted CSS and JavaScript links in Markdown format, categorized by their location in the HTML file (`<head>` or `<body>`).

## Contact
Charl Cronje
Email: charl.cronje@mail.com
Project Link: [https://github.com/charlpcronje/Script-and-CSS-Extract](lhttps://github.com/charlpcronje/Script-and-CSS-Extract)


## License
This project is open-source and available under the MIT License.
