import sys

from static_files_processing import create_public, copy_static_to_public, generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    print(f"Using basepath: {basepath}")
    static_folder = 'static'
    content_folder = 'content'
    public_folder = 'docs'
    
    create_public(public_folder)
    
    copy_static_to_public(static_folder, public_folder)

    generate_pages_recursive(content_folder, 'template.html', public_folder, basepath)

main()
