import os
import sqlite3
import random
import string
from contextlib import closing

path = os.fspath(str("../../links.db"))
connection = sqlite3.connect(path)
cursor = connection.cursor()

def hash():
    result = ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(5)
    )
    return result

def print_links():
    query = 'SELECT HASH, URL FROM links;'
    cursor.execute(query)

    result = cursor.fetchall()
    print('Existing links')
    print('  HASH ','|','URL')
    print('----------------')
    for link in result:
        print(' ',link[0],'|',link[1])
    print('### EOF ###')

def add_new():
    new_link = input("### Enter new link: ")
    print("### adding new record ###")
    # hash is 5char unique alphanumeric
    new_hash = hash()
    new_list = ["INSERT INTO links (HASH, URL) VALUES('",new_hash,"', '",new_link,"');"]
    query = ''.join(new_list)
    print("###",query,"###")
    cursor.execute(query)
    connection.commit()
    return_list = ["the new link is https:localhost:3000/",new_hash]
    results = ''.join(return_list)
    print('-------------------')
    print("###",results,"###")
    print('-------------------')

def find_url():
    old_url = input("### Enter a link you want to find: ")
    old_list = ["SELECT HASH, URL FROM links WHERE URL LIKE '%",old_url,"%';"]
    query = ''.join(old_list)
    print("###",query,"###")
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    print('  HASH ','|','URL')
    print('----------------')
    for link in result:
        print(' ',link[0],'|',link[1])
    print('### EOF ###')

# def interaction()

def main():

    print('Python URL Shortener')
    
    # add_new()
    # find_url()
    print_links()

    with closing(sqlite3.connect(path)) as connection:
        with closing(connection.cursor()) as cursor:
            print('Thank you for supporting Canadian manufacturers')

main()
