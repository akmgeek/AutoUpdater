import os
import sys

def get_version_path():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Current directory: {current_dir}")

    # Navigate to the most parent directory
    parent_dir = os.path.dirname(current_dir)
    print(f'Parent Dir: {parent_dir}')
    
    # Build the path to the 'src\modules' directory
    version_path = os.path.join(parent_dir, 'src', 'modules')
    print(f'Version Path: {version_path}')
    
    return version_path

def main():
    # Add the calculated path to sys.path
    version_path = get_version_path()
    sys.path.append(version_path)
    
    # Import the get_version function from version module
    from version import get_version
    
    # Print the version information
    print(get_version())

if __name__ == "__main__":
    main()
