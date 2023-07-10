# by Muk Chunpongtong
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import random
browser = webdriver.Chrome("D:\Google Drive\Code\Python\chromedriver 108.exe")


search_term = ''
quote_count = 1
quotes = []
search_bar_xpath = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input'
recursion_max = 4


def menu():
    global search_term
    global quote_count
    search_term = str(input("Input your search query for Youtube: "))
    quote_count = int(input("Input number of quotes to find: "))
    search_for_quotes()  # search_term and comment_count are global variables
    if len(quotes) == 0:
        print("No Quotes Found.")
    else:
        for i in range(len(quotes)):
            print(str(i+1) + ". " + str(quotes[i]))


def search_for_quotes():
    #  repeat seeking comments 'comment_count' times
    for i in range(quote_count):
        try_get(0)
    browser.close


def try_get(recursion):
    try:
        get_video()
    except:
        if recursion < recursion_max:
            try_get(recursion+1)
        else:
            print("too many recursions")


def get_video():
    # get to youtube
    browser.get("https://www.youtube.com/")  # open youtube
    search_bar = browser.find_element_by_xpath(search_bar_xpath)  # get the search bar input
    time.sleep(1)  # wait a bit for the page to load
    search_bar.send_keys(search_term)  # input the word
    search_bar.send_keys(u'\ue006')  # press return
    search_bar.send_keys(u'\ue007')  # press enter
    time.sleep(1)  # wait a bit for the page to load

    #  browse for a video
    thumbnails = browser.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')
    # pick one of the videos in the list
    print("Retrieved " + str(len(thumbnails)) + " Video Thumbnails")
    video = thumbnails[random.randrange(0, len(thumbnails))]
    #  click on the video
    action = ActionChains(browser)
    action.click(on_element=video)  # click on the correct image//
    action.perform()
    time.sleep(3)  # wait a bit for the page to load
    get_quotes()


def get_quotes():
    comments = browser.find_elements_by_xpath('//yt-formatted-string[@id="content-text"]')
    print("Retrieved " + str(len(comments)) + " Comments")
    1/len(comments)  # if len comments is 0, then retry

    # get the quote
    quote = comments[random.randrange(0, len(comments))].text
    quotes.append(quote)
    print("Appended: " + str(quote))


menu()
