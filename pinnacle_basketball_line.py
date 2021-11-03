from selenium import webdriver
import json, unidecode, time

all_items = []

def get_data():
    driver = webdriver.Chrome()
    driver.get('https://www.pinnacle.com/en/basketball/matchups/')
    driver.maximize_window()
    time.sleep(5)
    for data in driver.find_elements_by_class_name('style_row__3q4g_.style_row__3hCMX'):
        item = dict()
        item['FirstTeam'] = data.find_elements_by_class_name('ellipsis.event-row-participant')[0].text
        item['SecondTeam'] = data.find_elements_by_class_name('ellipsis.event-row-participant')[1].text
        item['Time'] = data.find_element_by_class_name('style_matchupDate__1gnX6').text
        item['Team1spread'] = \
        data.find_elements_by_class_name('style_buttons__XEQem')[0].find_elements_by_tag_name('button')[0].text.replace(
            '\n', ' , ')
        item['Team2spread'] = \
        data.find_elements_by_class_name('style_buttons__XEQem')[0].find_elements_by_tag_name('button')[1].text.replace(
            '\n', ' , ')
        item['Team1money'] = \
        data.find_elements_by_class_name('style_buttons__XEQem')[1].find_elements_by_tag_name('button')[0].text
        item['Team2money'] = \
        data.find_elements_by_class_name('style_buttons__XEQem')[1].find_elements_by_tag_name('button')[1].text
        item['total_over'] = \
        data.find_elements_by_class_name('style_buttons__XEQem')[2].find_elements_by_tag_name('button')[0].text.replace(
            '\n', ' , ')
        item['total_under'] = \
        data.find_elements_by_class_name('style_buttons__XEQem')[2].find_elements_by_tag_name('button')[1].text.replace(
            '\n', ' , ')
        all_items.append(item)
    driver.close()

# 

# def insert_data_file():
#     file_ = open('pinnacle.json', 'w')
#     jsondata = json.dumps(all_items, indent=4)
#     jsondata_ = unidecode.unidecode(jsondata)
#     file_.write(jsondata_)


if __name__ == "__main__":
    get_data()
    print(all_items)
#     insert_data_file()
