"""چارشنبه ۰۱ دسامبر ۲۱، ساعات ۲۱:۳۱:۰۲ (+0330)
This module is a module with cool and fun tools  

Tool list : 

    - Dispute                      - shutdown
    - Bank                         -  
    - charge                       - 
    - ip                           -  
    - code Mali                    -  
    - hadis                        - 
    - QUIZ                         - 
    - Short Link                   - 
    - Meaning                      - 
    - info telegram                - 
    - Individual and couple        -  
    - float and integer            - 

-| This library was first a script file, and 
-| after its uses it was not decided to turn this
-| script file into a library (and could help coders 

"""
import requests 
from sys import platform
from os import system

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


    def Hadis(): 
        # Presents a random Islamic hadith
        Had = requests.get("https://api.keybit.ir/hadis/").json() 
        person_1 = Had['result']['person'] 
        persone_2 = Had['result']['text'] 
        persone3 = Had['result']['source'] 

        print(f"""
person : {person_1} 
text : {persone_2} 
source : {persone3} 
""")


    def QUIZ(): 
        # One you know raises  
        Qu = requests.get("https://api.keybit.ir/ayamidanid/").json()
        Qu_2 = Qu['text'] 
        print(F'text : {Qu_2}') 



    def short_link(link):
        links = requests.get(f"https://api.codebazan.ir/shortlink/index.php?url={link}").json()
        link_opthno = links['result']['bitly'] 
        print(f"link short : {link_opthno}") 
        # sample code : 
        # https://www.amazon.com 

    

    def Meaning(Meaning): 
        # This tool is made for the meaning of words
        Meaning_get = requests.get(f"https://api.codebazan.ir/vajehyab/?text={Meaning}").json()
        # Says the sentence in Persian  
        htt = Meaning_get['result']['fa'] 
        # Says the sentence in English 
        htt_1 = Meaning_get['result']['en'] 
        # Explains more  
        htt_2 = Meaning_get['result']['dic'] 
        # Explains more  
        htt_3 = Meaning_get['result']['mani'] 
        # Explains more 
        htt_4 = Meaning_get['result']['Fmoein'] 
        # Explainss more 
        htt_5 = Meaning_get['result']['Fdehkhoda'] 
        # Explaness more 
        htt_6 = Meaning_get['result']['motaradefmotezad']  

        print(F"""
fa : {htt} 
en : {htt_1} 
dic : {htt_2} 
mani : {htt_3} 
fmoein : {htt_4} 
Fdehkhoda : {htt_5} 
motaradefmotezad : {htt_6}

""")

    def info_telegram(id): 
        # telegram info 
        # id : sample = 181391321
        # usernmae : sample = @SI_Developers 
        # frist_name : frist name = Ahura 
        # bio : sample = my name is ahuura ! 

        info = requests.get(f"https://bot.otherapi.tk/telegram/{id}").json() 
        result = info['info']['id'] 
        result_1 = info['info']['username'] 
        result_2 = info['info']['first_name'] 
        result_3 = info['info']['dc_id'] 
        result_4 = info['info']['bio']


        print(f'''

id : {result} 
username : {result_1} 
first name : {result_2}
dc_id : {result_3} 
bio : {result_4} 
''')



    def Individual__couple(number): 
        if number % 2 == 0 : 
            print(F"This is an even number") 
        else: 
            print(F"This is an odd number") 


    def float_int(number): 
        if type(number) == int : 
            print("This is an integer") 
        else: 
            print("This is an float") 


    def shutdown(time): 
        try : 
            if platform == "Windows": 
                system(f'shutdown -s -t {time}')  
            elif platform == "linux":
                system(f'shutdown -h {time} ')  
            elif platform == "darwin": 
                system(f"shutdown -h -t {time} ") 
        except: 
            raise ValueError('Error value !!!') 
    
