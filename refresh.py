import os
import shutil

# Define the paths
main_dir = "/Users/henrybackman/Documents/weekend_trip_test"
sub_dir = "/Users/henrybackman/Documents/weekend_trip_test/original"

def main():
    # Remove all files in the main directory (not subdirectories)
    for item in os.listdir(main_dir):
        item_path = os.path.join(main_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Removed: {item}")

    # Copy all files from subdirectory to main directory
    for item in os.listdir(sub_dir):
        item_path = os.path.join(sub_dir, item)
        if os.path.isfile(item_path):
            shutil.copy2(item_path, main_dir)
            print(f"Copied: {item}")

    print("Operation completed.")

if __name__ == "__main__":
    main()