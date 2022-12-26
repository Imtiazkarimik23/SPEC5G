import textract, os


def extract_text(input_file_name):
    input_file_parts = input_file_name.split("/")
    output_file_name = "/".join(input_file_parts[0:len(input_file_parts)-1]) + "/" + input_file_parts[-1].split(".")[0] + ".txt"
    print("Input: " + input_file_name)
    print("Output: " + output_file_name)
    try:
        lines = '\n'.join(str(textract.process(input_file_name)).split('\\n'))
    except:
        return
    with open(output_file_name, 'w') as f:
        f.write(f'{lines}\n')


def traverse_files(root_folder):    
    releases = os.listdir(root_folder)
    for rel in releases:
        if 'Rel' in rel:
            series = os.listdir(root_folder + rel)
            for ser in series:
                zips = os.listdir(root_folder + rel + "/" + ser)
                for zip_folder in zips:
                    files = os.listdir(root_folder + rel + "/" + ser + "/" + zip_folder)
                    for file in files:
                        extract_text(root_folder + "/" + rel + "/" + ser + "/" + zip_folder + "/" + file )


if __name__ == "__main__":
    root_folder = "Cellular-Dataset/"
    traverse_files(root_folder)

