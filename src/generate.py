from markdown_blocks import extract_title
from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(markdown)
    markdown_html = markdown_to_html_node(markdown)
    content = markdown_html.to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace('''{{ Content }}''', content)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for path in Path(dir_path_content).rglob('*.md'):
        from_path = str(path)
        dest_path = from_path.replace(dir_path_content, dest_dir_path).replace(".md", ".html")
        generate_page(from_path, template_path, dest_path, basepath)



