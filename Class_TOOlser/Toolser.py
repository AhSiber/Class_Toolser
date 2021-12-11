"""چارشنبه ۰۱ دسامبر ۲۱، ساعات ۲۱:۳۱:۰۲ (+0330)
This module is a module with cool and fun tools  

Tool list : 

    - Dispute     - joke
    - Bank        - number 
    - charge      - craet password 
    - ip          - Wikipedia 
    - Date        - Convert text to Morse code 
    - time        -  ping site 
    - req         - qr code 
    - font        - Character 
    - des         - True Code Meli  
    - Download    - Email Verification 
    - voice       - encode 
    - decode      - shutdown 

-| This library was first a script file, and 
-| after its uses it was not decided to turn this
-| script file into a library (and could help coders 

"""
import requests 


class Tools : 

    def __init__(self ,Code , font , ip , download) -> None: # self -> None 
        self.Code = Code 
        self.font = font 
        self.ip =ip 
        self.download = download 


    def dnst():
        try: 
            name = requests.get('https://api.codebazan.ir/danestani/').text  # send requests format(txt) 
            return name 
        except: 
            raise TimeoutError('time out Error! ')

    def who(ip):
        try : 
            name = requests.get(
                f"https://api.codebazan.ir/whois/index.php?type=json&domain={ip}").json() # requests - get - json()
            ip = name['ip'] # show ip 
            address = name['address'] # show addres 
            dns = name['dns']["1"] # show dns - 1 

            return f"IP : {ip} \nadress : {address} \ndns : {dns}" 
        except: 
            raise ValueError(f'Error value ! : {ip} - ') 


    def font_en(font):  
        try: 
            fon_name = requests.get(f"http://api.codebazan.ir/font/?text={font}").json()  # api font -- > json() 
            print(fon_name['result']["1"]) 
            print(fon_name['result']["2"]) 
            print(fon_name['result']["3"]) 
            print(fon_name['result']["4"]) 
            print(fon_name['result']["5"]) 
            print(fon_name['result']["6"]) 
            print(fon_name['result']["7"]) 
            print(fon_name['result']["8"]) 
            print(fon_name['result']["9"]) 
            print(fon_name['result']["10"]) 
            print(fon_name['result']["11"]) 
            print(fon_name['result']["12"]) 
            print(fon_name['result']["13"]) 
            print(fon_name['result']["14"]) 
            print(fon_name['result']["15"]) 
            print(fon_name['result']["16"]) 
            print(fon_name['result']["17"]) 
            print(fon_name['result']["18"]) 
            print(fon_name['result']["19"]) 
            print(fon_name['result']["20"]) 
            print(fon_name['result']["21"]) 
            print(fon_name['result']["21"]) 
            print(fon_name['result']["22"]) 
            print(fon_name['result']["23"]) 
            print(fon_name['result']["23"]) 
            print(fon_name['result']["25"]) 
            print(fon_name['result']["26"]) 
            print(fon_name['result']["27"]) 
            print(fon_name['result']["24"]) 
            print(fon_name['result']["27"]) 
            print(fon_name['result']["28"]) 
            print(fon_name['result']["29"]) 
            print(fon_name['result']["30"]) 
            print(fon_name['result']["33"]) 
            print(fon_name['result']["39"]) 
            print(fon_name['result']["40"]) 
            print(fon_name['result']["41"]) 
            print(fon_name['result']["42"]) 
            print(fon_name['result']["42"]) 
            print(fon_name['result']["44"]) 
            print(fon_name['result']["45"]) 
            print(fon_name['result']["46"]) 
            print(fon_name['result']["47"]) 
            print(fon_name['result']["48"]) 
            print(fon_name['result']["49"]) 
            print(fon_name['result']["50"]) 
            print(fon_name['result']["51"]) 
            print(fon_name['result']["52"]) 
            print(fon_name['result']["53"]) 
            print(fon_name['result']["53"]) 
            print(fon_name['result']["55"]) 
            print(fon_name['result']["56"]) 
            print(fon_name['result']["57"]) 
            print(fon_name['result']["58"]) 
            print(fon_name['result']["59"]) 
            print(fon_name['result']["60"])  # result - 60 - end 

        except : 
            raise ValueError(f'eror input : {font}')

    def req():
        try: 
            Date = requests.get("https://api.codebazan.ir/time-date/?json=en").json() # requstes - get - json()
            Time =  Date['result']['time'] # result - time 
            date = Date['result']['date'] # result date 
            fasl = Date['result']['fasl'] # result  - fas1 
            return f'time iran : {Time} \nDate iran : {date} \nfasl : {fasl}' 
        except: 
            print("error api !")

    
    def jokes():
        try:  
            name = requests.get("http://api.codebazan.ir/jok/").text # requests - txt 
            return name  
        except : 
            print("Error API !" 
            )

    def number(numbers:int): 
        try: 
            name = requests.get(f"https://api.codebazan.ir/adad/?text={numbers}").json() # renumber quests json() -- 
            fa = name["result"]["fa"] # exchange number --> Fa and En 
            fatext = name["result"]["fatext"] # exchange fatext  
            return f"Fa : {fa}\ntext : {fatext}" 
        except : 
            raise ValueError(f"Error value : -- {numbers} type numbers == int !!")
 
    def code_mali(code:int):
        code = str(code) # str code 
        if not code.isnumeric() or len(code) != 10: # if -- len 
            return "The national code is incorrect" # return... 

        total = 0 # zero 
        count = int(code[-1]) #inger (int) > code [-1] 
        for d, index in zip(code, range(10, 1, -1)): # zip code , range(10,1,-1)
            total += int(d) * index # add int(d) * = index 

        remis = total % 11 # totoal % len(11)
        # if , else , return : 
        if remis < 2: 
            if remis == count:
                return "The national code is correct"
        else:
            if 11 - remis == count:
                return "The national code is correct"

            return "The national code is incorrect"

