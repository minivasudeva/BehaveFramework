from behave import *
from selenium import webdriver
from time import sleep

@given(u'I am on mission humane page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C://webdriver//chromedriver.exe')
    context.driver.get("https://app.missionhumane.org")
    context.driver.maximize_window()
    sleep(2)

@when(u'I search for the first state')
def step_impl(context):
    state_xpath = '//*[@class="location-row"][1]'

@then(u'AP is listed')
def step_impl(context):
    state_name = context.driver.find_element_by_xpath('//*[@class="location-row"][1]').text
    print(state_name)
    assert state_name =='Andhra Pradesh'
    context.driver.quit()


@when(u'I click first state')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@class="location-row"][1]').click()
    sleep(2)

@then(u'anatapur is listed as first district')
def step_impl(context):
    dist_name = context.driver.find_element_by_xpath('//*[@class="location-row"][2]').text
    print(dist_name)
    assert dist_name == 'Anantapur'
    context.driver.quit()


@when(u'I click the state "{stname}"')
def step_impl(context,stname):
    all_states = context.driver.find_elements_by_class_name('location-row')
    print(stname)
    for st in all_states:
            if st.text == stname:
                st.click()
                sleep(3)
                break

@then(u'states of AP are listed')
def step_impl(context):
    context.driver.quit()