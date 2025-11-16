*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  nuuskamuikkunen
    Set Password  nuuskis123
    Set Password Confirmation  nuuskis123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  h
    Set Password  hemuli123
    Set Password Confirmation  hemuli123
    Click Button  Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  hemuli
    Set Password  1
    Set Password Confirmation  1
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  nuuskamuikkunen
    Set Password  nuuskamuikkunen
    Set Password Confirmation  nuuskamuikkunen
    Click Button  Register
    Register Should Fail With Message  Password is invalid


Register With Nonmatching Password And Password Confirmation
    Set Username  nuuskamuikkunen
    Set Password  nuuskis123
    Set Password Confirmation  hemuli123
    Click Button  Register
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  pikkumyy
    Set Password  pikkumyy123
    Set Password Confirmation  pikkumyy123
    Click Button  Register
    Register Should Fail With Message  User with username pikkumyy already exists

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  pikkumyy  pikkumyy123
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}