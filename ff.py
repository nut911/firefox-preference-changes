from selenium import webdriver
from selenium.webdriver.firefox.options import Options

profile = webdriver.FirefoxProfile()
profile.set_preference('general.warnOnAboutConfig', 'false')

driver = webdriver.Firefox(profile)

driver.get("about:config")

def set_bool_preference(name, value):
    driver.execute_script("""
const { Services } = ChromeUtils.import("resource://gre/modules/Services.jsm");
var prefs = Services.prefs;
prefs.setBoolPref(arguments[0], arguments[1]);
    """, name, value)

def set_string_preference(name, value):
    driver.execute_script("""
const { Services } = ChromeUtils.import("resource://gre/modules/Services.jsm");
var prefs = Services.prefs;
prefs.setStringPref(arguments[0], arguments[1]);
    """, name, value)

def set_int_preference(name, value):
    driver.execute_script("""
const { Services } = ChromeUtils.import("resource://gre/modules/Services.jsm");
var prefs = Services.prefs;
prefs.setIntPref(arguments[0], arguments[1]);
    """, name, value)


elem = driver.find_element_by_xpath("//button[@id='warningButton']")
elem.click()

set_string_preference("browser.download.dir", '~/Downloads')
set_int_preference("browser.download.folderList", "2")

driver.close()
