import os
import shutil

from block_processing import markdown_to_html_node

def create_public(destination_path):
    public_exists = os.path.exists(destination_path)
    print(f"Does {destination_path} exists: {public_exists}")

    if (public_exists):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)

def copy_static_to_public(src_path, destination_path):
    folder_content = os.listdir(src_path)
    print(f"Content of '{src_path}' folder: {folder_content}")
    for item in folder_content:
        full_src_path = os.path.join(src_path, item)
        print(full_src_path, os.path.isfile(full_src_path))
        if os.path.isfile(full_src_path):
            shutil.copy(full_src_path, os.path.join(destination_path, item))
        else:
            new_destination_path = os.path.join(destination_path, item)

            os.mkdir(new_destination_path)
            copy_static_to_public(full_src_path, new_destination_path)

def extract_title(markdown):
    lines = markdown.splitlines()
    title_line = next((line for line in lines if line.startswith("# ")), None)
    if title_line is not None:
        return title_line[2:].strip()
    else:
        raise ValueError("Document's missing a title")
    
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_content = ""
    template_content = ""

    with open(from_path, 'r') as markdown_file:
        markdown_content = markdown_file.read()

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title_from_markdown = extract_title(markdown_content)

    html_page = template_content.replace('{{ Title }}', title_from_markdown).replace('{{ Content }}', html_content).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    dir_content = os.listdir(dir_path_content)
    for item in dir_content:
        full_item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(full_item_path) and item.endswith('.md'):
            generate_page(full_item_path, template_path, os.path.join(dest_dir_path, item[:-3] + '.html'), basepath)
        elif os.path.isdir(full_item_path):
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(full_item_path, template_path, new_dest_dir_path, basepath)
