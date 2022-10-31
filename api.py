import requests;

DefaultHeaders = {         
        'Host': 'tt02.altinn.no',
        'Content-Type': 'application/hal+json',
        'Accept': 'application/hal+json',
        'ApiKey': '7A2BA1FE-384E-4793-BD77-58561B15D766', 
}
bodyPassword = {
    "UserName": "brasa1",
    "UserPassword": "passord123"
}

def Login():
    authLogin = requests.post("https://tt02.altinn.no/api/authentication/authenticatewithpassword", headers=DefaultHeaders, json=bodyPassword)

    if (authLogin.status_code == 200):
        
        print("Success cookie stored")
        return authLogin.headers["Set-Cookie"]
    else:
        print("Error Code ", authLogin.status_code)

def GetMessages():
    GetHeaders = {         
        'Host': 'tt02.altinn.no',
        'Content-Type': 'application/hal+json',
        'Accept': 'application/hal+json',
        'ApiKey': '7A2BA1FE-384E-4793-BD77-58561B15D766', 
        'Cookie': loginCookie, 
    }

    messages = requests.get("https://tt02.altinn.no/api/my/messages", headers=GetHeaders)

    if (messages.status_code == 200):
        print("Success messages retrived")
        print(messages.json()["_embedded"])
    else:
        print("Error Code ", messages.status_code)

def PostMessages():
    GetHeaders = {         
        'Host': 'tt02.altinn.no',
        'Content-Type': 'application/hal+json',
        'Accept': 'application/hal+json',
        'ApiKey': '7A2BA1FE-384E-4793-BD77-58561B15D766', 
        'Cookie': loginCookie, 
    }
    msgBody = {
        "message": "Dette er en message"
    }
    messages = requests.get("https://tt02.altinn.no/api/my/Messages?language=1033&complete=false", headers=GetHeaders, json=msgBody)

    if (messages.status_code == 200):
        print("Success messages sent")
        #print(messages.json()["_embedded"])
    else:
        print("Error Code ", messages.status_code)

def GetOrg():

    GetHeaders = {         
        'Host': 'tt02.altinn.no',
        'Content-Type': 'application/hal+json',
        'Accept': 'application/hal+json',
        'ApiKey': '7A2BA1FE-384E-4793-BD77-58561B15D766', 
        'Cookie': loginCookie, 
    }

    messages = requests.get("https://tt02.altinn.no/api/911007118/messages", headers=GetHeaders)

    if (messages.status_code == 200):
        print("Success messages sent")
        print(messages.json())
    else:
        print("Error Code ", messages.status_code)

Run = True
loginCookie = None

while Run:
    action = int(input("Hva vil du gjore? 1 : Logg inn paa altinn, 2 : Sjekk Meldingene dine paa altinn, 3 : Post message, 5 : Avslutt Program:"))

    if (action == 1):
        loginCookie = Login()
    elif (action == 2):
        GetMessages()
    elif (action == 3):
        PostMessages()
    elif (action == 4):
        GetOrg()
    elif (action == 5):
        Run = False
