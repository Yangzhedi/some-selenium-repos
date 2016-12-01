# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

defalut_url = 'http://192.168.1.109:9000/'

driver = webdriver.Chrome()

driver.get(defalut_url)

time.sleep(3)
driver.find_element_by_id("login").click()

time.sleep(1)
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("BsbV2")
driver.find_element_by_class_name("register-button").click()
# 登录成功
time.sleep(1)
driver.get(defalut_url + '#/person/info/edit')

# 修改/添加 个人信息
editSpan = driver.find_elements_by_xpath("//div[@class='info-edit-info']")
span = (editSpan[1].find_elements_by_tag_name("span"))[2]
span.find_element_by_tag_name("a").click()
span.find_element_by_tag_name("input").send_keys("l")
span.find_element_by_class_name("btn-primary").click()
# for i in editSpan:
print editSpan[1]
# editSpan.find_elements_by_tag_name("a")[1].click()

# 开始创建小队
driver.get(defalut_url + "?#/create-team")
time.sleep(1)
games = driver.find_elements_by_class_name("game")
print len(games)
time.sleep(3)
print len(games)
games[2].find_element_by_tag_name("a").click()

form = driver.find_element_by_class_name("content-form")
form.find_element_by_tag_name("input").send_keys(u'测试team-admin建队')
time.sleep(1)
(form.find_elements_by_tag_name('button')[1]).click()
time.sleep(3)
driver.find_element_by_class_name("sa-confirm-button-container").find_element_by_tag_name("button").click()
time.sleep(3)

# get url
url = driver.current_url
team_num = url.split('/')[-1]
print driver.current_url
print team_num


# # 退出登录
# ul = driver.find_element_by_class_name("navbar-right")
# li = (ul.find_elements_by_tag_name('li'))[3]
# # menu = driver.find_element_by_id('account-menu')
# webdriver.ActionChains(driver).move_to_element(li).perform()
# time.sleep(3)
# # menu.click()
# driver.find_element_by_id('logout').click()

print 'is already print url, now you can logout'

# 退出登录
# 暂时手动，妈的
print 'please logout quickly, you only have 5 seconds !!!'
time.sleep(5)
print 'time is up'
print 'login other users quickly'


def join_team(user):
    # 切换用户
    time.sleep(3)
    driver.find_element_by_id("login").click()
    time.sleep(1)
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").send_keys("BsbV2")
    driver.find_element_by_class_name("register-button").click()

    time.sleep(1)
    driver.get(defalut_url+"#/person/info/edit")
    time.sleep(2)

    # 修改/添加 个人信息
    editSpan = driver.find_elements_by_xpath("//div[@class='info-edit-info']")
    span = (editSpan[1].find_elements_by_tag_name("span"))[2]
    span.find_element_by_tag_name("a").click()
    span.find_element_by_tag_name("input").send_keys("l")
    span.find_element_by_class_name("btn-primary").click()

    new_url = defalut_url+'#/team/info/' + team_num
    driver.get(new_url)
    driver.find_element_by_class_name('team-title') \
        .find_element_by_class_name('team-apply-btn') \
        .find_element_by_tag_name('button').click()

    # 手动退出
    print 'please logout quickly, you only have 5 seconds !!!'
    time.sleep(5)
    print 'time is up'
    print 'login other users quickly'

join_team("user")
join_team("user1")
join_team("user2")
join_team("user3")
join_team("user4")