*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    XML
Resource    ../Operations/code1Operations.robot
#Library    RPA.Browser.Selenium    auto_close=${False}


*** Variables ***
${url}    https://demo.nopcommerce.com/
${url2}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome

*** Test Cases ***
Login_Test
    Open Browser    ${url2}    ${browser}
    Maximize Browser Window
    Login_to_OrangeHRM
    Get Title
    
