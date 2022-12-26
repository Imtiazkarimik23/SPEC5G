import requests as req
from bs4 import BeautifulSoup
from queue import Queue
import pandas as pd
import os, re, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


address_book = [
    "https://www.techplayon.com/",
    "https://telecompedia.net/"
    ]
unvisited_queue = Queue()
all_visited = []
existing_files = []
SELENIUM = True

if SELENIUM:
    browser = webdriver.Chrome(executable_path="./chromedriver")


def get_next_pages(soup, website_name):
    links = soup.find_all("a")
    page_links = []
    for link in links:
        page = link.get("href")
        try:
            if website_name in page:
                page_links.append(page)
        except:
            continue
    return page_links


def get_paragraphs(soup):
    paragraph = ""
    p_tags = soup.find_all("p")
    for para in p_tags:
        paragraph = paragraph + para.getText() + "\n"
    return paragraph


def update_visited(next_page_links):
    for next_page_link in next_page_links:
        if (next_page_link not in all_visited) and (next_page_link not in unvisited_queue.queue):
            unvisited_queue.put(next_page_link)


def main():
    for i, address in enumerate(address_book):
        website_name = address.split("/")[2].split(".")[-2]
        
        if not os.path.exists(website_name):
            os.mkdir(website_name)
        
        print(website_name)
        existing_files.extend(os.listdir(website_name))
        
        if SELENIUM:
            browser.get(address)
            soup = BeautifulSoup(browser.page_source, "html.parser")
        else:
            wp = req.get(address)
            soup = BeautifulSoup(wp.content, "html.parser")

        all_visited.append(address)
        update_visited(get_next_pages(soup, website_name)) 
        
        while not unvisited_queue.empty():
            link = unvisited_queue.get()
            filename = website_name + "/" + link.split("/")[-2] + ".txt"

            try:
                print("Visited: ", len(all_visited))
                print("Remaining: ", unvisited_queue.qsize())
                if SELENIUM:
                    browser.get(link)
                    soup = BeautifulSoup(browser.page_source, "html.parser")
                else:
                    wp = req.get(link)
                    soup = BeautifulSoup(wp.content, "html.parser")
                time.sleep(0.3)
            except:
                time.sleep(5)
                continue

            all_visited.append(link)
            update_visited(get_next_pages(soup, website_name))
            if (link.split("/")[-2] + ".txt") in existing_files:
                continue 
            paragraph = get_paragraphs(soup)

            with open(filename, "w") as f:
                print(filename)
                try:
                    f.write(paragraph)
                except:
                    continue
            time.sleep(3)

    if SELENIUM:
        browser.close()


if __name__ == "__main__":
    main()
    
        

