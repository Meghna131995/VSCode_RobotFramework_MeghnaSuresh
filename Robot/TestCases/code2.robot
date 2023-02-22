*** Settings ***
Library    SeleniumLibrary
Library    XML
#Library    RPA.Browser.selenium     auto close=${False}
*** Variables ***
${url}    https://rahulshettyacademy.com/dropdownsPractise/
${browser}    chrome
*** Keywords ***
Flights_check
    Sleep    6
    Click Element    xpath://input[@id='ctl00_mainContent_rbtnl_Trip_1']

Currency_dropdown    
    Sleep    3
    # Select From List By Label    ctl00_mainContent_DropDownListCurrency    AED
    Select From List By Index   //select[@id='ctl00_mainContent_DropDownListCurrency']    2
    Sleep    3
    Select From List By Index    //select[@id='ctl00_mainContent_DropDownListCurrency']    3
    Sleep    3
Check_box
    Select Checkbox    xpath://input[@id='ctl00_mainContent_chk_friendsandfamily']
    Sleep    3
    Select Checkbox    xpath://input[@id='ctl00_mainContent_chk_SeniorCitizenDiscount']
    Sleep    3
    Select Checkbox    xpath://input[@id='ctl00_mainContent_chk_IndArm']
    Sleep    3
    Select Checkbox    xpath://input[@id='ctl00_mainContent_chk_StudentDiscount']
    Sleep    3
    Select Checkbox    xpath://input[@id='ctl00_mainContent_chk_Unmr']
    Sleep    3

From_to
    Sleep    6
    Click Element    xpath://input[@id='ctl00_mainContent_ddl_originStation1_CTXT']
    Sleep    3
    Click Element    xpath://a[contains(text(),'Goa (GOI)')]
    Sleep    3
    Click Element    xpath://body[1]/form[1]/div[4]/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[3]/div[1]/div[1]/ul[1]/li[5]/a[1]
    Sleep    3
*** Test Cases ***

Test
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Flights_check
    Currency_dropdown
    Check_box
    From_to
    