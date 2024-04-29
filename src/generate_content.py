import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    split_lines = markdown.split("\n")
    title_line = ""
    for line in split_lines:
        if line.startswith("# "):
            title_line = line
            break
    if title_line == "":
        raise Exception("All pages need to have an h1!")
    return title_line.lstrip("# ")
        
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()
 
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        full_file_path = os.path.join(dir_path_content, file)
        new_file_path = os.path.join(dest_dir_path, file)
        new_file_path = new_file_path.replace(".md", ".html")
        if os.path.isfile(full_file_path):
            generate_page(full_file_path, template_path, new_file_path)
        if os.path.isdir(full_file_path):
            generate_pages_recursive(full_file_path, template_path, new_file_path)