*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Login_to_application
    
    Click Link    //a[contains(text(),'Log in')]
    Input Text    //input[@id='Email']    suresh.meghna13@gmail.com
    Input Text    //input[@id='Password']    Avengers@13
    Sleep    5
    Click Element    //button[contains(text(),'Log in')]
Login_to_OrangeHRM
    Sleep    7
    #Get Title
    #Title Should Be    Orange
    Input Text    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]    Admin
    Sleep    3
    Input Text    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]    admin123
    Sleep    3
    Click Element    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]
    Sleep    3
    Click Element    xpath://header/div[1]/div[2]/ul[1]/li[1]/span[1]
    Sleep    3
    Click Element    xpath://a[contains(text(),'Logout')]  
    Sleep    5

    ${userbox}    Set Variable    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]
    Sleep    3
    Input Text    ${userbox}    Admin2
    Sleep    8