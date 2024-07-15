import os

directory = "/Users/henrybackman/Documents/weekend_trip"


def main():
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        print(f"Checking: {filename}")
        if not filename.startswith("GH0"):
            continue
        namepart, ext = os.path.splitext(filename)
        clipno = namepart[3:4]
        print(f"Clip number: {clipno}")
        if clipno == "1":
            continue
        
        new_filename = "GH01" + namepart[4:] + clipno + ext
        
        # Get the full file paths
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed: {filename} to {new_filename}")

    print("Renaming process completed.")

if __name__ == "__main__":
    main()