import io
import os
import pandas as pd
import requests
import zipfile
from bs4 import BeautifulSoup


def get_dir_links(parent_dir_link, dir_identifier):
    archive_soup = requests.get(parent_dir_link)
    soup = BeautifulSoup(archive_soup.content, "html.parser")
    all_links = soup.find_all("a")
    directory_links = []
    for link in all_links:
        extracted_link = link.get("href")
        if dir_identifier in extracted_link:
            directory_links.append(extracted_link)
    return directory_links


def make_dir_structure(directory_lvl1_links, dir_structure_df):
    for directory_lvl1 in directory_lvl1_links:
        directory_lvl2_links = get_dir_links(directory_lvl1, "Rel-")
        for directory_lvl2 in directory_lvl2_links:
            zip_folder_links = get_dir_links(directory_lvl2, "_series")
            for zip_folder in zip_folder_links:
                dir_structure_df.loc[len(dir_structure_df.index)] = [directory_lvl1, directory_lvl2, zip_folder, 0]


def download_and_extract_zipped_folder(path, zip_folder):
    r = requests.get(zip_folder)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    folder_name = zip_folder.split("/")[-1].split(".")[0]
    path = path + "/" + folder_name
    if not os.path.exists(path):
        os.mkdir(path)
    z.extractall(path)


def main(dir_structure_df):
    not_downloaded = dir_structure_df[dir_structure_df["Downloaded"] == 0]
    not_downloaded = not_downloaded.reset_index()
    i = 0
    for index, row in not_downloaded.iterrows():
        path = row['DirLevel1'].split("/")[-1] + "/" + row['DirLevel2'].split("/")[-1]

        if not os.path.exists(path):
            os.makedirs(path)

        download_and_extract_zipped_folder(path, row['ZipFolder'])

        idx = dir_structure_df[dir_structure_df['ZipFolder'] == row['ZipFolder']].index[0]
        dir_structure_df.loc[idx].at['Downloaded'] = 1

        i = i + 1
        if i == 10:
            dir_structure_df.to_csv("DirectoryStructure.csv")
            i = 0


if __name__ == "__main__":

    if not os.path.exists("DirectoryStructure.csv"):
        spec_root_link = "https://www.3gpp.org/ftp/Specs/2022-09"
        dir_structure_df = pd.DataFrame(columns=['DirLevel1', 'DirLevel2', 'ZipFolder', 'Downloaded'])
        directory_lvl1_links = get_dir_links(spec_root_link, "Rel-")

        make_dir_structure(directory_lvl1_links, dir_structure_df)
        dir_structure_df.to_csv("DirectoryStructure.csv")
    else:
        dir_structure_df = pd.read_csv("DirectoryStructure.csv")

    main(dir_structure_df)
