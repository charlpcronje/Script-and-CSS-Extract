import sys
from bs4 import BeautifulSoup

def extract_and_write_to_markdown(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    head_css = soup.head.find_all('link', {'rel': 'stylesheet'})
    body_scripts = soup.body.find_all('script')

    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write('# CSS and JavaScript\n\n')
        md_file.write('## In `<head>` tag\n')
        md_file.write('```html\n')
        for link in head_css:
            md_file.write(str(link) + '\n')
        md_file.write('```\n\n')
        md_file.write('## In `<body>` tag\n')
        md_file.write('```html\n')
        for script in body_scripts:
            md_file.write(str(script) + '\n')
        md_file.write('```\n')

if __name__ == '__main__':
    default_path = 'ignite\\src\\main\\resources\\templates\\index.html'
    file_path = sys.argv[1] if len(sys.argv) == 2 else default_path
    output_file = 'scriptsAndCss.md'
    extract_and_write_to_markdown(file_path, output_file)
    print(f"Markdown file '{output_file}' has been created.")
