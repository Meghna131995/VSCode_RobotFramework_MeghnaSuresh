*** Settings ***
Library    SeleniumLibrary
Resource     ../Operations/FramesOps01.robot

*** Variables ***
${URL}    https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html
${broswer}    chrome

*** Test Cases ***
Handling_Frames
    Open Browser    ${URL}    ${broswer}
    Set Selenium Speed    1seconds
    Maximize Browser Window
    Frames_
    #Close Browser


    
