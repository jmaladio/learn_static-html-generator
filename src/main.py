from static_files_processing import create_public, copy_static_to_public

def main():
    static_folder = 'static'
    public_folder = 'public'
    
    create_public(public_folder)
    
    copy_static_to_public(static_folder, public_folder)

main()
