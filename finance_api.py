import re

def extract_finance_apis(readme_path="README.md"):
    with open(readme_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Find the Finance section
    finance_section_start = markdown_content.find('## Finance')
    if finance_section_start == -1:
        print("Could not find the Finance section.")
        return None

    # Extract the Finance section content
    finance_section_end = markdown_content.find('##', finance_section_start + 1)
    if finance_section_end == -1:
        finance_section_end = len(markdown_content)

    finance_section_content = markdown_content[finance_section_start:finance_section_end]

    # Extract links from the Finance section
    links = re.findall(r'\[(.*?)\]\((.*?)\)', finance_section_content)

    # Extract just the URLs
    urls = [link[1] for link in links]

    return urls

finance_urls = extract_finance_apis()

if finance_urls:
    for url in finance_urls:
        print(url)
else:
    print("Could not find any URLs in the Finance section.")
