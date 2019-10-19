from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

JOB_APP = {
    "first_name": "Spencer",
    "last_name": "Gritton",
    "email": "spencerpgritton@gmail.com",
    "phone": "319-000-0000",
    "org": "Student",
    "linkedin": "https://linkedin.com/in/spencerpgritton/",
    "github": "https://github.com/spencergritton",
    "location": "Iowa City, Iowa, United States",
    "grad_month": '05',
    "grad_year": '2020',
    "university": "University of Iowa"
}

def fillInPageDetails(browser):
    try:
        browser.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_id('email').send_keys(JOB_APP['email'])
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_id('phone').send_keys(JOB_APP['phone'])
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//label[contains(.,'LinkedIn')]").send_keys(JOB_APP['linkedin'])
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[text()='2020']").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[contains(.,'University of Iowa')]").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[contains(.,'Computer Science')]").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//label[contains(.,'Website')]").send_keys(JOB_APP['github'])
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[contains(.,'any employer')]").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[contains(.,'Male')]").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath("//select/option[contains(.,'I am not a protected veteran')]").click()
    except NoSuchElementException:
        pass

    try:
        select = Select(browser.find_element_by_id('#job_application_hispanic_ethnicity'))
        select.select_by_visible_text("No")
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_css_selector("[data-source='attach']").click()
    except NoSuchElementException:
        pass

    try:
        browser.find_elements_by_css_selector("[data-source='attach']")[1].click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_xpath('//*[@id="job_application_answers_attributes_2_answer_selected_options_attributes_0_question_option_id"]').click()
    except NoSuchElementException:
        pass

    try:
        browser.find_element_by_id('disability_status_dropdown_container').click()
    except:
        pass

    # this is turned off currently because this was made quickly just to help speed up the application process
    # Because of this not every input will be filled out so a submit would usually fail
    # if someone else would like to work on this though and complete it then they could do the submit button
    # browser.find_element_by_id("submit_app").click()