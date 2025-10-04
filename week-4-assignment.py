   # File Read & Write Challenge 🖋️: Create a program that reads a file
   #  and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors
#  if it doesn’t exist or can’t be read.

def read_and_modify_file():
    """
    Main function that handles file reading, modification, and writing with error handling
    """
    print("📁 File Read & Write Challenge 🖋️")
    print("=" * 50)
    
    # Get filename from user with validation
    while True:
        filename = input("\nPlease enter the filename to read: ").strip()
        
        if not filename:
            print("❌ Error: Filename cannot be empty. Please try again.")
            continue
            
        try:
            # Try to read the file
            content = read_file_safely(filename)
            
            # If successful, process and write the modified content
            if content is not None:
             modified_content = modify_content(content)
                write_modified_file(filename, modified_content)
            
            break
            
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"❌ Error: {e}")
            retry = input("\nWould you like to try another filename? (y/n): ").lower()
            if retry != 'y':
                print("👋 Goodbye!")
                return

def read_file_safely(filename):
    """
    Safely read a file with comprehensive error handling
    
    Args:
        filename (str): Name of the file to read
        
    Returns:
        str: File content if successful, None otherwise
    """