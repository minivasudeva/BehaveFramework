from behave import *
from selenium import webdriver
from time import sleep

@given(u'I am on home page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C://webdriver//chromedriver.exe')
    context.driver.get("https://app.missionhumane.org")
    context.driver.maximize_window()

@when(u'I click state "{state}"')
def step_impl(context,state):
    sleep(2)
    all_states = context.driver.find_elements_by_class_name('location-row')
    for st in all_states:
        if st.text == state:
            st.click()
            sleep(3)
            break

@when(u'I click district "{district}"')
def step_impl(context,district):
    sleep(2)
    all_district = context.driver.find_elements_by_class_name('location-row')
    for dist in all_district:
        if dist.text == district:
            dist.click()
            sleep(3)
            break

@when(u'I click resource "{resource}"')
def step_impl(context,resource):
    sleep(2)
    no_res = len(context.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[3]/div'))
    for r in range(1, no_res+1):
        res_xpath = '//*[@id="root"]/div/div/div[3]/div[' + str(r) + ']/div[1]'
        all_res = context.driver.find_elements_by_xpath(res_xpath)
        # print(all_res.text)
        for res in all_res:
            # print(res.text)
                if res.text == resource:
                    print(res.text)
                res.click()
                sleep(3)
                break

@then(u'compare text "{text_value}"')
def step_impl(context,text_value):
    no_data_rows = len(context.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div'))
    out = False
    for data in range(4, no_data_rows - 1):
        data_xpath = '//*[@id="root"]/div/div/div[' + str(data) + ']/div/p[2]'
        check_val = context.driver.find_element_by_xpath(data_xpath).text
        print(check_val)
        print(text_value)
        if check_val == text_value:
            out=True
            break
    context.driver.quit()
    assert out == True
    print(out) 