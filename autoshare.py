

import random
import base64
import json
import os
import platform
import random
import re
import string
import sys
import time
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
reset = "\033[0m"
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;35m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
dark_violet = "\033[38;5;91m"
def clear():
    """Clears the terminal screen based on the operating system."""
    system_name = platform.system().lower()
    if "windows" in system_name:
        os.system("cls")
    else:
        os.system("clear")
def generate_random_ua():

    fbcr_values = [
    "AT&T", "Orange France", "Telia Sweden","Vodafone Italy", "Sky Mobile","Proximus Belgium", "Movistar Spain", "Tele2 Netherlands", "Vodafone Spain", "Telekom Deutschland","Eir Ireland", "KPN Netherlands", "Three Ireland", "Telekom Austria", "Telia Sweden","Vodafone Italy", "Sky Mobile", "Proximus Belgium", "Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland", "KPN Netherlands", "Three Ireland","Telekom Austria", "Telia Sweden", "Vodafone Italy", "Sky Mobile", "Proximus Belgium","Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland","KPN Netherlands", "Three Ireland", "Telekom Austria", "China Mobile", "NTT Docomo", "KT Corporation", "Singtel","AIS Thailand", "Viettel", "Smart Communications", "PTCL Pakistan", "Grameenphone Bangladesh","Nepal Telecom", "MTN Nigeria", "T-Mobile USA", "Verizon Wireless", "Rogers Canada","O2 United Kingdom", "Telstra Australia", "TIM Brazil", "Vivo India", "Telenor Norway","Mobilink Pakistan", "Bell Canada", "Etisalat UAE", "Claro Mexico", "Orange Spain","Vodafone Portugal", "Telkomsel Indonesia","Beeline Russia", "MTS Russia", "Optus Australia","SK Telecom South Korea", "Entel Chile", "MTNL India", "Tigo Ghana", "Idea India","DTAC Thailand", "Zong Pakistan", "Orange Romania", "EE United Kingdom", "Digi Malaysia","Koodo Canada", "Yoigo Spain", "Airtel Nigeria", "Airtel Kenya", "Telekom Malaysia","Cosmote Greece", "Digicel Jamaica", "LIME Caribbean", "Telus Canada", "Sprint USA","Movistar Mexico", "Vodafone Germany", "Optus Australia","Vivo Brazil", "Singtel Singapore", "Airtel India", "Ncell Nepal", "Telenor Sweden","MEO Portugal", "Claro Argentina", "EE Estonia", "Telkom South Africa", "Telenor Norway","Yoigo Spain", "Giffgaff United Kingdom", "Lycamobile France", "A1 Telekom Austria", "Telenor Hungary","Vodafone Greece", "Cosmote Romania", "Telenor Serbia", "Vodafone New Zealand", "Telekom Croatia","Orange Belgium", "Telkomsel Indonesia", "Vivacom Bulgaria", "Orange Poland", "Rogers Canada","Telkom South Africa", "Lycamobile Germany", "M1 Singapore", "DT Mobile Austria", "Claro Colombia","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark","Rakuten Mobile Japan","Ooredoo Qatar","Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","NOS Portugal", "Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico","Orange Moldova", "Telkomsel Indonesia", "Telenor Bulgaria","Vodafone Ukraine", "Cosmote Greece","T-Mobile Czech Republic", "NetOne Zimbabwe", "Glo Nigeria", "MTS Belarus", "Cell C South Africa","Maxis Malaysia", "Fido Canada", "Zain Saudi Arabia", "Telenor Serbia", "Beeline Uzbekistan","A1 Telekom Austria", "Zong Pakistan", "Jazz Pakistan", "Vodafone Portugal", "Telstra Australia","Vodafone Ireland", "Orange Slovakia", "Claro Peru", "Vivo Brazil", "Vodafone Czech Republic","Telenor Montenegro", "Digi Malaysia", "Etisalat Egypt", "Tigo Rwanda", "Robi Bangladesh","MTC Namibia", "AIS Thailand", "Vodafone Greece", "Orange Romania", "T-Mobile Poland","Telenor Hungary", "Telia Latvia", "Ooredoo Oman", "Optus Australia", "Orange Belgium","Telenor Norway", "Lycamobile France", "EE Estonia", "Yoigo Spain", "Giffgaff United Kingdom","Sprint USA", "Telus Canada", "Vodafone Germany", "Movistar Mexico", "Telkomsel Indonesia","Vivo India", "Airtel India", "Ncell Nepal", "Telenor Sweden", "MEO Portugal","Claro Argentina", "Telekom Croatia", "Cosmote Romania", "Orange Poland", "Telenor Serbia","Vodafone New Zealand", "Vivacom Bulgaria", "Telenor Denmark", "T-Mobile Netherlands", "NOS Portugal","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark", "Rakuten Mobile Japan","Ooredoo Qatar", "Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico", "Orange Moldova","Telkomsel Indonesia", "O2 Germany", "Airtel Nigeria", "Orange Kenya","Digicel Jamaica","Unitel Angola", "MobiFone Vietnam", "TMN Portugal", "Grameenphone Bangladesh", "Movitel Mozambique","Telkom South Africa", "Globacom Nigeria", "Nawras Oman", "Vodafone Ghana", "Telenor Pakistan","Yoigo Spain", "SFR France", "Tigo Colombia", "Vodafone Qatar", "Etisalat UAE","Telenor Norway", "Telia Finland", "LIME Caribbean", "EE United Kingdom", "Koodo Canada","TIM Italy", "Telekom Romania", "Jio India", "Ooredoo Kuwait", "Orange Switzerland","Bouygues Telecom France", "Entel Bolivia", "A1 Telekom Austria", "MTN South Africa", "Vodafone Hungary","Zain Jordan", "Ncell Nepal", "Zain Kuwait", "Djezzy Algeria", "Smart Philippines","Telenor Bulgaria", "Cosmote Greece", "Vodafone Portugal", "Telstra Australia", "Three Ireland","Rogers Canada", "Safaricom Kenya", "Orange Luxembourg", "Elisa Finland", "Vodafone Netherlands","KPN Netherlands", "Telia Lithuania", "Vodafone Iceland", "Tigo Ghana", "Idea India","Tata Docomo India", "Aircel India", "Claro Chile", "Movistar Peru", "T-Mobile Croatia","Telkomsel Indonesia", "O2 Czech Republic", "Smartfren Indonesia", "Axiata Malaysia", "Digicel Caribbean","Beeline Kazakhstan", "Moldcell Moldova", "Djezzy Algeria", "Tigo Rwanda", "Vodafone Egypt","COSMOTE Cyprus", "Bell Mobility Canada", "Telenor Sweden", "3 Sweden", "DNA Finland","Zain Bahrain", "Ooredoo Tunisia", "Orange Morocco", "Vivacom Bulgaria", "VIPnet Croatia","Vodafone Greece", "Orange Romania", "T-Mobile Poland", "Telenor Hungary", "AIS Thailand","TrueMove Thailand", "Vodafone Czech Republic", "Digi Malaysia", "XL Axiata Indonesia", "Dialog Sri Lanka","MTN Uganda", "Airtel Bangladesh", "Viva Kuwait", "Wind Italy", "LMT Latvia","Yoigo Spain", "Maroc Telecom Morocco", "Orange Ivory Coast", "Airtel Malawi", "Airtel Zambia", "DITO", "Globe", "GOMO", "TNT", "TM", "O2 Germany", "Orange Kenya", "Digicel Jamaica", "Unitel Angola","MobiFone Vietnam","TMN Portugal","Grameenphone Bangladesh", "Movitel Mozambique", "Telkom South Africa", "Globacom Nigeria"
]
     

    fbmf_fbdv_dict = {

    "asus": ["ZenFone 8", "ROG Phone 5", "ZenFone 7", "ROG Phone 3", "ZenFone 6", "ROG Phone II", "ZenFone 5Z", "ZenFone 5", "ZenFone 4 Pro", "ZenFone 4", "ZenFone 3 Deluxe", "ZenFone 3", "ZenFone 2 Laser", "ZenFone 2", "ZenFone", "ZenFone 6Z", "ZenFone Max Pro (M2)", "ZenFone Max Pro (M1)", "ZenFone 6Z", "ZenFone Max Plus (M2)", "ZenFone Max (M2)", "ZenFone Max (M1)", "ZenFone Live", "ZenFone Zoom", "ZenFone Selfie", "ASUS_Z01RD", "ASUS_Z01QD", "ASUS_I01WD", "ASUS_I01BD", "ASUS_I01HDA"],
    
    "lenovo": ["Legion Phone Duel 2", "Legion Phone Duel", "K12 Note", "K10 Note", "Z6 Pro", "Z5 Pro", "Lenovo Z6 Pro", "Lenovo Z6 Youth", "Lenovo Z5s", "Lenovo Z5 Pro GT", "Lenovo Z5 Pro", "Lenovo Z5", "Lenovo K9", "Lenovo A5", "Lenovo K320t", "Lenovo K8 Note", "Lenovo K6 Note", "Lenovo Vibe K5 Note", "Lenovo Vibe K5", "Lenovo Vibe P1", "Lenovo Vibe X3", "Lenovo Vibe Z2 Pro", "Lenovo Vibe Z2", "Lenovo Vibe Z","A6000", "A6000 Plus", "A7000", "A7000 Turbo", "A2010", "A2010-a", "K3 Note", "Vibe K4 Note", "Vibe K5 Note", "Vibe K5 Plus", "Vibe K5", "Vibe K5 Lite", "Vibe K5 Power", "Vibe K5 S", "Vibe X2", "Vibe X3", "Vibe Z2 Pro", "K6 Power", "K6 Note", "K6", "K6 Plus", "K6 Turbo", "Vibe C", "Vibe C2", "Vibe C2 Power", "Vibe C2 K10a40", "Vibe C2 K10a40C", "Vibe B", "Vibe B A2016a40", "Vibe B A2016b30", "Vibe B A2016b31", "Vibe B A2016b31C", "Vibe B A2016b30A", "Vibe B A2016b30B", "Vibe B A2016b30C", "Vibe B A2016b30D", "Vibe B A2016b30E", "Vibe B A2016b30G", "Vibe B A2016b30J", "Vibe B A2016b30K", "Vibe B A2016b30L", "Vibe B A2016b30M", "Vibe B A2016b30N", "Vibe B A2016b30O", "Vibe B A2016b30Q", "Vibe B A2016b30R", "Vibe B A2016b30T", "Vibe B A2016b30W", "Vibe B A2016b30Y", "Vibe B A2016b31A", "Vibe B A2016b31B", "Vibe B A2016b31C", "Vibe B A2016b31E", "Vibe B A2016b31F", "Vibe B A2016b31G", "Vibe B A2016b31H", "Vibe B A2016b31K", "Vibe B A2016b31L", "Vibe B A2016b31M", "Vibe B A2016b31N", "Vibe B A2016b31O", "Vibe B A2016b31P", "Vibe B A2016b31Q", "Vibe B A2016b31R", "Vibe B A2016b31S", "Vibe B A2016b31T", "Vibe B A2016b31U", "Vibe B A2016b31V", "Vibe B A2016b31W", "Vibe B A2016b31X", "Vibe B A2016b31Y", "Vibe B A2016b31Z", "Vibe B A2016b31AA", "Vibe B A2016b31AB", "Vibe B A2016b31AC", "Vibe B A2016b31AD", "Vibe B A2016b31AE", "Vibe B A2016b31AF", "Vibe B A2016b31AG", "Vibe B A2016b31AH", "Vibe B A2016b31AI", "Vibe B A2016b31AJ", "Vibe B A2016b31AK", "Vibe B A2016b31AL", "Vibe B A2016b31AM", "Vibe B A2016b31AN", "Vibe B A2016b31AO", "Vibe B A2016b31AP", "Vibe B A2016b31AQ", "Vibe B A2016b31AR", "Vibe B A2016b31AS", "Vibe B A2016b31AT", "Vibe B A2016b31AU", "Vibe B A2016b31AV", "Vibe B A2016b31AW", "Vibe B A2016b31AX", "Vibe B A2016b31AY", "Vibe B A2016b31AZ", "Vibe B A2016b31BA", "Vibe B A2016b31BB", "Vibe B A2016b31BC", "Vibe B A2016b31BD", "Vibe B A2016b31BE", "Vibe B A2016b31BF", "Vibe B A2016b31BG", "Vibe B A2016b31BH", "Vibe B A2016b31BI", "Vibe B A2016b31BJ", "Vibe B A2016b31BK", "Vibe B A2016b31BL", "Vibe B A2016b31BM", "Vibe B A2016b31BN", "Vibe B A2016b31BO", "Vibe B A2016b31BP", "Vibe B A2016b31BQ", "Vibe B A2016b31BR", "Vibe B A2016b31BS"],
    
    "sony": ["Xperia 5 III", "Xperia 10 II", "Xperia 1 II", "Xperia 10 Plus", "Xperia 1", "Xperia XZ3", "Xperia 1 III", "Xperia 1 II", "Xperia 1", "Xperia 5 III", "Xperia 5 II", "Xperia 5", "Xperia 10 III", "Xperia 10 II", "Xperia 10", "Xperia Pro", "Xperia L4", "Xperia L3", "Xperia XZ3", "Xperia XZ2 Premium", "Xperia XZ2", "Xperia XZ1 Compact", "Xperia XZ1", "Xperia XZ Premium", "Xperia XZ", "Xperia XA2 Ultra", "Xperia XA2", "Xperia XA1 Ultra", "Xperia XA1 Plus", "Xperia XA1", "Xperia X Compact","C6603", "D6503", "F5121", "F8331", "G3116", "H3113", "J9210", "XQ-AS52", "XQ-AD52", "XQ-BT52", "XQ-BS52", "XQ-AT51", "XQ-AT52", "XQ-AD52", "XQ-AT52", "XQ-AT42", "XQ-AT41", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-BS52", "XQ-BT52", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-AT41", "XQ-BS52", "XQ-BT52", "XQ-AS42", "XQ-BS42", "XQ-AT42", "XQ-BS41", "XQ-AT51", "XQ-AD51", "XQ-AD42", "XQ-AS41", "XQ-BT41", "XQ-BT51", "XQ-BS51", "XQ-BS42", "XQ-AS52", "XQ-AS41", "XQ-BS42", "XQ-BT41", "XQ-AS42", "XQ-AT42", "XQ-AD42", "XQ-BS41", "XQ-AT41", "XQ-BS51", "XQ-BT51", "XQ-AT51", "XQ-AD51", "F8131", "F8132", "G3121", "G3112", "G3123", "G3125", "G8141", "G8142", "G8341", "G8342", "H8216", "H8266", "H8296", "H8416", "H9436", "H9461", "H9436", "H9461", "H9436", "H9493", "H8541", "H8526", "H8116", "H8166", "I4213", "I4293", "I4293", "I4312", "I4332", "I4332", "I4113", "I4193", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213"],
    
    "htc": ["Wildfire E3", "Desire 21 Pro", "U20 5G", "Desire 20 Pro", "Desire 19+", "U12 Life","HTC U20", "HTC U12+", "HTC U11", "HTC U12+", "HTC U12 Life", "HTC U11+", "HTC U11 Life", "HTC U11", "HTC U Ultra", "HTC 10", "HTC One M9", "HTC One M8", "HTC One (M7)", "HTC Desire 820", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Butterfly S", "HTC One Max", "HTC One Mini", "HTC Desire 600", "HTC First", "HTC One X+","HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC U Ultra", "HTC U Play", "HTC Desire 626", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Desire 820", "HTC Desire 626G+", "HTC One X", "HTC One X+", "HTC One S", "HTC One V", "HTC One Mini", "HTC One Mini 2", "HTC One Max", "HTC One E8", "HTC One E9", "HTC One A9", "HTC One E9+", "HTC One M8s", "HTC Desire Eye", "HTC Desire 820s", "HTC Desire 816G", "HTC Desire 626s", "HTC Desire 530", "HTC Desire 828", "HTC 10 Lifestyle", "HTC U11 Life", "HTC U11 Eyes", "HTC U11+"],
    
    "apple": ["iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro", "iPhone 12", "iPhone SE (3rd Gen)", "iPhone 13 Pro Max", "iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro Max", "iPhone 12 Pro", "iPhone 12", "iPhone 12 mini", "iPhone SE (2nd generation)", "iPhone 11 Pro Max", "iPhone 11 Pro", "iPhone 11", "iPhone XR", "iPhone XS Max", "iPhone XS", "iPhone X", "iPhone 8 Plus", "iPhone 8", "iPhone 7 Plus", "iPhone 7", "iPhone SE (1st generation)", "iPhone 6s Plus", "iPhone 6s", "iPhone 6 Plus", "iPhone 6", "iPhone 5s", "iPhone 5c", "iPhone 5", "iPhone 4s", "iPhone 4", "iPhone 3GS", "iPhone 3G", "iPhone","A1549", "A1522", "A1586", "A1633", "A1688", "A1699", "A1700", "A1660", "A1778", "A1661", "A1784", "A1863", "A1901", "A1865", "A1902", "A1920", "A1921", "A2101", "A2102", "A2104", "A1984", "A2103", "A1920", "A1921", "A2160", "A2161", "A2215", "A2217", "A2218", "A2220", "A2221", "A2223", "A2111", "A2229", "A2112", "A2131", "A2106", "A2107", "A2108", "A2162", "A2047", "A2048", "A2049", "A2105", "A2014", "A2015", "A2016", "A1867", "A1868", "A1897", "A1898", "A1899", "A1900", "A1903", "A1923", "A2212", "A2200", "A2202", "A2201", "A2301", "A2223", "A2215", "A1866", "A1993", "A1990", "A2013", "A2012", "A1983", "A1954", "A1953", "A2100", "A2005", "A2114", "A2116", "A2110", "A1920", "A1921", "A1985", "A2115", "A2117", "A2118", "A2003", "A2004", "A2160", "A2161", "A2202", "A2298", "A2299", "A2162", "A2270", "A2271", "A2229", "A2272", "A2273", "A2301", "A2304", "A2324", "A2325", "A2340", "A2341", "A2342", "A2375", "A2376", "A2377", "A2378", "A2406", "A2407", "A2408", "A2451", "A2452", "A2453", "A2600", "A2594", "A2503", "A2571", "A2570", "A2410", "A2402", "A2412", "A2399", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602"],
    
    "oppo": ["Reno 7 Pro", "Reno 7", "Reno 6 Pro+", "A95", "A96", "A93", "Oppo Find X3 Pro", "Oppo Find X2 Pro", "Oppo Find X2", "Oppo Reno 6 Pro+", "Oppo Reno 6 Pro", "Oppo Reno 6", "Oppo Reno 5 Pro+", "Oppo Reno 5 Pro", "Oppo Reno 5", "Oppo A94", "Oppo A74", "Oppo F19 Pro+", "Oppo F19 Pro", "Oppo F19", "Oppo A93", "Oppo A53", "Oppo A33", "Oppo A32", "Oppo A72", "Oppo A52", "Oppo A92", "Oppo A12", "Oppo Reno 3 Pro", "Oppo Reno 3", "Oppo Reno 2", "Oppo Reno", "Oppo K7x", "Oppo K7", "Oppo A9 (2020)", "Oppo A5 (2020)", "CPH1903", "CPH1803", "CPH1859", "CPH1969", "CPH1989", "CPH1919", "CPH1941", "CPH1983", "CPH1963", "CPH1879", "CPH1831", "CPH2035", "CPH2069", "CPH1987", "CPH2071", "CPH2083", "CPH2015", "CPH2019", "CPH2173", "CPH2089", "CPH2067", "CPH2017", "CPH2087", "CPH2205", "CPH2251", "CPH2197", "CPH2235", "CPH2347", "CPH2295", "CPH2249", "CPH2243", "CPH2349", "CPH2359", "CPH2383", "CPH2381", "CPH2239", "CPH2213", "CPH2129", "CPH2195", "CPH2227", "CPH2316", "CPH2353", "CPH2261", "CPH2225", "CPH2269", "CPH2073", "CPH2185", "CPH1877", "CPH2013", "CPH2061", "CPH1955", "CPH1871", "CPH1801", "CPH1873", "CPH1901", "CPH1809", "CPH1853", "CPH1923", "CPH1981", "CPH1833", "CPH1917", "CPH1967", "CPH1937", "CPH1893", "CPH1931", "CPH1921", "CPH1823", "CPH2023", "CPH2021", "CPH2103", "CPH2220", "CPH2127", "CPH2059", "CPH2139", "CPH2253", "CPH2267", "CPH2263", "CPH2247", "CPH2241", "CPH2297", "CPH2357", "CPH2255", "CPH2345", "CPH2329", "CPH2209", "CPH2191", "CPH2199", "CPH2289", "CPH2319", "CPH2343", "CPH2363", "CPH2161", "CPH2163", "CPH1979", "CPH1977", "CPH1973", "CPH1965", "CPH1959", "CPH1951", "CPH1913", "CPH1909", "CPH1905", "CPH1861", "CPH1863", "CPH1967", "CPH1933", "CPH1937", "CPH1921", "CPH1923", "CPH1987", "CPH1919", "CPH1897", "CPH1875", "CPH1874", "CPH1872", "CPH1865", "CPH1863", "CPH1862", "CPH1853", "CPH1852", "CPH1851", "CPH1843", "CPH1841", "CPH1835", "CPH1833", "CPH1832", "CPH1831", "CPH1825", "CPH1823", "CPH1821", "CPH1819", "CPH1813", "CPH1812", "CPH1811", "CPH1809", "CPH1808", "CPH1807", "CPH1805", "CPH1803", "CPH1801"],
    
    "realme": ["Realme GT Master Edition", "Realme 8i", "Realme 8s", "Narzo 30", "Narzo 20", "Realme 7i", "Realme 8", "Realme 7 Pro", "Realme X50 Pro","Realme GT Master Explorer Edition", "Realme GT Master Edition", "Realme GT", "Realme 8 Pro", "Realme 8", "Realme Narzo 30 Pro", "Realme Narzo 30A", "Realme X7 Pro", "Realme X7", "Realme 7 Pro", "Realme 7", "Realme C21", "Realme C20", "Realme C15", "Realme C12", "Realme C11", "Realme 6 Pro", "Realme 6", "Realme X2 Pro", "Realme XT", "Realme 5 Pro", "Realme 5", "Realme 3 Pro", "Realme 3", "Realme 2 Pro", "Realme 2", "Realme 1","RMX2111", "RMX3092", "RMX3161", "RMX3142", "RMX3185", "RMX3186", "RMX3281", "RMX3274", "RMX3361", "RMX3165", "RMX3243", "RMX3242", "RMX3294", "RMX3162", "RMX3241", "RMX3290", "RMX3289", "RMX3270", "RMX3267", "RMX3266", "RMX3263", "RMX3260", "RMX3240", "RMX3280", "RMX3276", "RMX3244", "RMX3121", "RMX3063", "RMX3061", "RMX3090", "RMX3091", "RMX3080", "RMX3211", "RMX3334", "RMX3221", "RMX3295", "RMX3292", "RMX3331", "RMX3383", "RMX3350", "RMX3332", "RMX3300", "RMX3310", "RMX3311", "RMX3385", "RMX3336", "RMX3337", "RMX3338", "RMX3235", "RMX3225", "RMX3124", "RMX3065", "RMX3143", "RMX3201", "RMX3070", "RMX3250", "RMX3246", "RMX3261", "RMX3071", "RMX3150", "RMX3164", "RMX3141", "RMX3063", "RMX3060", "RMX3357", "RMX3223", "RMX3330", "RMX3284", "RMX3362", "RMX3236", "RMX3193", "RMX3191", "RMX3358", "RMX3384", "RMX3262", "RMX3248", "RMX3339", "RMX3283", "RMX3195", "RMX3093", "RMX3098", "RMX3245", "RMX3095", "RMX3064", "RMX3341", "RMX3340", "RMX3365", "RMX3363", "RMX3364", "RMX3366", "RMX3367", "RMX3368", "RMX3369", "RMX3370", "RMX3371", "RMX3372", "RMX3373", "RMX3374", "RMX3375", "RMX3376", "RMX3377", "RMX3378", "RMX3379", "RMX3380", "RMX3381", "RMX3382", "RMX3312", "RMX3249", "RMX3094", "RMX3116", "RMX3187", "RMX3096", "RMX3097", "RMX3171", "RMX3152", "RMX3115", "RMX3081", "RMX3272", "RMX3273", "RMX3264", "RMX3265", "RMX3269", "RMX3268", "RMX3082", "RMX3083", "RMX3084", "RMX3085", "RMX3086", "RMX3087", "RMX3088", "RMX3089", "RMX3099", "RMX309A", "RMX309B", "RMX309C", "RMX309D", "RMX309E", "RMX309F", "RMX309G", "RMX309H", "RMX309I", "RMX309J", "RMX309K", "RMX309L", "RMX309M", "RMX309N", "RMX309O", "RMX309P", "RMX309Q", "RMX309R", "RMX309S", "RMX309T", "RMX309U", "RMX309V", "RMX309W", "RMX309X", "RMX309Y", "RMX309Z", "RMX31ZM", "RMX31ZN", "RMX31ZS", "RMX31ZT", "RMX31ZW", "RMX31ZV", "RMX31ZR", "RMX31ZQ", "RMX31ZP", "RMX31ZO", "RMX31ZN", "RMX31ZM", "RMX31ZL", "RMX31ZK", "RMX31ZJ", "RMX31ZI", "RMX31ZH", "RMX31ZG", "RMX31ZF", "RMX31ZE", "RMX31ZD", "RMX31ZC"],
    
    "motorola": ["Moto G100", "Moto G60", "Moto G40 Fusion", "Moto G30", "Moto G9 Power", "Moto G8", "Moto G Power 2022", "Moto G7", "Moto G Stylus 2022", "Motorola Edge 20 Pro", "Motorola Edge 20", "Motorola Edge 20 Lite", "Motorola Moto G Stylus (2021)", "Motorola Moto G Power (2021)", "Motorola Moto G Play (2021)", "Motorola Moto G9 Plus", "Motorola Moto G9", "Motorola Moto G8 Plus", "Motorola Moto G8 Power", "Motorola Moto G8", "Motorola Moto G7 Plus", "Motorola Moto G7 Power", "Motorola Moto G7 Play", "Motorola Moto G7", "Motorola Moto G6 Plus", "Motorola Moto G6", "Motorola Moto G5S Plus", "Motorola Moto G5 Plus", "Motorola Moto G5", "Motorola Moto G4 Plus", "Motorola Moto G4", "Motorola Moto X4", "Motorola Moto X (2nd Gen)", "Motorola Moto X", "Motorola Moto Z3 Play", "Motorola Moto Z2 Play", "Motorola Moto Z", "Motorola Moto E7 Plus", "Motorola Moto E6 Plus", "Motorola Moto E5 Plus", "Motorola Moto E4 Plus", "Motorola Moto E (2nd Gen)", "Motorola Moto E", "XT2127-2", "XT2127-4", "XT2127-5", "XT2127-6", "XT2127-7", "XT2127-8", "XT2127-10", "XT2127-11", "XT2127-12", "XT2127-13", "XT2127-14", "XT2127-15", "XT2127-16", "XT2127-17", "XT2127-18", "XT2127-19", "XT2127-20", "XT2127-21", "XT2127-22", "XT2127-23", "XT2127-24", "XT2127-25", "XT2127-26", "XT2127-27", "XT2127-28", "XT2127-29", "XT2127-30", "XT2127-31", "XT2127-32", "XT2127-33", "XT2127-34", "XT2127-35", "XT2127-36", "XT2127-37", "XT2127-38", "XT2127-39", "XT2127-40", "XT2127-41", "XT2127-42", "XT2127-43", "XT2127-44", "XT2127-45", "XT2127-46", "XT2127-47", "XT2127-48", "XT2127-49", "XT2127-50", "XT2127-51", "XT2127-52", "XT2127-53", "XT2127-54", "XT2127-55", "XT2127-56", "XT2127-57", "XT2127-58", "XT2127-59", "XT2127-60", "XT2127-61", "XT2127-62", "XT2127-63", "XT2127-64", "XT2127-65", "XT2127-66", "XT2127-67", "XT2127-68", "XT2127-69", "XT2127-70", "XT2127-71", "XT2127-72", "XT2127-73", "XT2127-74", "XT2127-75", "XT2127-76", "XT2127-77", "XT2127-78", "XT2127-79", "XT2127-80", "XT2127-81", "XT2127-82", "XT2127-83", "XT2127-84", "XT2127-85", "XT2127-86", "XT2127-87", "XT2127-88", "XT2127-89", "XT2127-90", "XT2127-91", "XT2127-92", "XT2127-93", "XT2127-94", "XT2127-95", "XT2127-96", "XT2127-97", "XT2127-98", "XT2127-99", "XT2127-100", "XT2127-101", "XT2127-102", "XT2127-103", "XT2127-104", "XT2127-105", "XT2127-106", "XT2127-107", "XT2127-108", "XT2127-109", "XT2127-110", "XT2127-111", "XT2127-112", "XT2127-113", "XT2127-114", "XT2127-115", "XT2127-116", "XT2127-117", "XT2127-118", "XT2127-119", "XT2127-120", "XT2127-121", "XT2127-122", "XT2127-123", "XT2127-124", "XT2127-125", "XT2127-126", "XT2127-127", "XT2127-128", "XT2127-129", "XT2127-130", "XT2127-131", "XT2127-132", "XT2127-133", "XT2127-134", "XT2127-135", "XT2127-136", "XT2127-137", "XT2127-138", "XT2127-139", "XT2127-140", "XT2127-141", "XT2127-142", "XT2127-143", "XT2127-144", "XT2127-145", "XT2127-146", "XT2127-147", "XT2127-148", "XT2127-149", "XT2127-150", "XT2127-151", "XT2127-152", "XT2127-153"],
    
    "nokia": ["Nokia X20", "Nokia X10", "Nokia G20", "Nokia G10", "Nokia 8.3 5G", "Nokia 5.4", "Nokia 3.4", "Nokia 2.4", "Nokia 8.1", "Nokia 7.2", "Nokia 6.2", "Nokia 4.2", "Nokia 3.2", "Nokia 2.2", "Nokia 9 PureView", "Nokia 8 Sirocco", "Nokia 8", "Nokia 7 Plus", "Nokia 7.1", "Nokia 6.1 Plus", "Nokia 6.1", "Nokia 5.1 Plus", "Nokia 5.1", "Nokia 4.1", "Nokia 3.1 Plus", "Nokia 3.1", "Nokia 2.1", "Nokia 1", "TA-1337", "TA-1380", "TA-1395", "TA-1208", "TA-1208", "TA-1334", "TA-1336", "TA-1230", "TA-1239", "TA-1283", "TA-1335", "TA-1234", "TA-1347", "TA-1353", "TA-1340", "TA-1233", "TA-1338", "TA-1386", "TA-1307", "TA-1296", "TA-1281", "TA-1333", "TA-1244", "TA-1235", "TA-1357", "TA-1236", "TA-1339", "TA-1316", "TA-1329", "TA-1343", "TA-1354", "TA-1300", "TA-1303", "TA-1289", "TA-1315", "TA-1287", "TA-1342", "TA-1351", "TA-1331", "TA-1325", "TA-1295", "TA-1240", "TA-1286", "TA-1328", "TA-1284", "TA-1293", "TA-1341", "TA-1292", "TA-1327", "TA-1298", "TA-1323", "TA-1238", "TA-1291", "TA-1345", "TA-1309", "TA-1344", "TA-1324", "TA-1346", "TA-1326", "TA-1304", "TA-1320", "TA-1348", "TA-1318", "TA-1330", "TA-1280", "TA-1246", "TA-1248", "TA-1317", "TA-1299", "TA-1310", "TA-1350", "TA-1332", "TA-1242", "TA-1206", "TA-1294", "TA-1313", "TA-1249", "TA-1241", "TA-1216", "TA-1297", "TA-1285", "TA-1319", "TA-1243", "TA-1356"],
    
    "xiaomi": ["Mi 11", "Mi 10 Pro", "Mi 9T","M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2012K11C","Redmi 6A","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4","Redmi Note 5", "Redmi 4X","Redmi Note 8","Redmi Note 8 Pro","Xiaomi Mi 11 Ultra", "Xiaomi Mi 11 Pro", "Xiaomi Mi 11", "Xiaomi Mi 10 Ultra", "Xiaomi Mi 10 Pro", "Xiaomi Mi 10", "Xiaomi Mi 10T Pro", "Xiaomi Mi 10T", "Xiaomi Mi 9T Pro", "Xiaomi Mi 9T", "Xiaomi Mi 9 Pro 5G", "Xiaomi Mi 9", "Xiaomi Mi 8 Pro", "Xiaomi Mi 8", "Xiaomi Mi 8 Lite", "Xiaomi Mi 8 SE", "Xiaomi Mi Mix 3", "Xiaomi Mi Mix 2S", "Xiaomi Mi Mix 2", "Xiaomi Mi Mix", "Xiaomi Redmi Note 11 Pro+", "Xiaomi Redmi Note 11 Pro", "Xiaomi Redmi Note 11", "Xiaomi Redmi Note 10 Pro", "Xiaomi Redmi Note 10", "Xiaomi Redmi Note 9 Pro", "Xiaomi Redmi Note 9", "Xiaomi Redmi Note 8 Pro", "Xiaomi Redmi Note 8", "Xiaomi Redmi Note 7 Pro", "Xiaomi Redmi Note 7", "Xiaomi Redmi K40 Pro", "Xiaomi Redmi K40", "Xiaomi Redmi K30 Pro", "Xiaomi Redmi K30", "Xiaomi Redmi K20 Pro", "Xiaomi Redmi K20", "Xiaomi Poco X3 Pro", "Xiaomi Poco X3", "Xiaomi Poco X2", "Xiaomi Poco F3", "Xiaomi Poco F2 Pro", "Xiaomi Poco F1"],
    
    "samsung": ["Galaxy S21", "Galaxy A52", "Galaxy S20","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935F","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","SPH-L720","SM-S906E", "Samsung Galaxy S21 Ultra", "Samsung Galaxy S21+", "Samsung Galaxy S21", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy Note 20", "Samsung Galaxy S20 Ultra", "Samsung Galaxy S20+", "Samsung Galaxy S20", "Samsung Galaxy Note 10+", "Samsung Galaxy Note 10", "Samsung Galaxy S10+", "Samsung Galaxy S10", "Samsung Galaxy Note 9", "Samsung Galaxy S9+", "Samsung Galaxy S9", "Samsung Galaxy Note 8", "Samsung Galaxy S8+", "Samsung Galaxy S8", "Samsung Galaxy Note 7", "Samsung Galaxy S7 Edge", "Samsung Galaxy S7", "Samsung Galaxy Note 5", "Samsung Galaxy S6 Edge+", "Samsung Galaxy S6 Edge", "Samsung Galaxy S6", "Samsung Galaxy Note 4", "Samsung Galaxy S5", "Samsung Galaxy S4", "Samsung Galaxy S3", "Samsung Galaxy Note 3", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-A526B", "SM-A516B", "SM-A516N", "SM-A526U", "SM-A716U", "SM-A716V", "SM-A5260", "SM-A526W", "SM-A126U", "SM-A126V", "SM-A016G", "SM-A016B", "SM-A016M", "SM-A025M", "SM-A025F", "SM-A217F", "SM-A217M", "SM-A207F", "SM-A207M", "SM-A102U", "SM-A102U1", "SM-A102W", "SM-A102N", "SM-A1020", "SM-A105F", "SM-A105G", "SM-A105M", "SM-A202F", "SM-A202G", "SM-A202M", "SM-A125U", "SM-A125V", "SM-A022G", "SM-A022M", "SM-A027G", "SM-A027M", "SM-A2170", "SM-A115M", "SM-A107M", "SM-A107F", "SM-A107M", "SM-A0220", "SM-A115F", "SM-A102F", "SM-A1050"],
    
    "vivo": ["Vivo_X60_Pro", "Vivo_X50_Pro", "Vivo_X30_Pro", "Vivo_X27", "Vivo_X23", "Vivo_X21", "Vivo_V21", "Vivo_V17", "Vivo_V15", "Vivo_V11", "Vivo_V9", "Vivo_Y95", "Vivo_Y91", "Vivo_Y81", "Vivo_Y71", "Vivo_S1", "V2056", "V2112A", "V2112", "V2122A", "V2120A", "V2120", "V2116A", "V2114A", "V2112A", "V2010A", "V2019A", "V2010", "V2003A", "V2002A", "V2002", "V1932A", "V1932T", "V1932", "V1929A", "V1928A", "V1928T", "V1928", "V1927A", "V1926A", "V1925A", "V1925", "V1924A", "V1922A", "V1921A", "V1921", "V1920A", "V1919A", "V1916A", "V1916", "V1912A", "V1911A", "V1910A", "V1910", "V1909A", "V1907A", "V1905", "V1903A", "V1901A", "V1901T", "V1901", "V1836", "V1824A", "V1824T", "V1824", "V1818A", "V1818T", "V1813A", "V1813T", "V1813", "V1812A", "V1811A", "V1811T", "V1811", "V1808A", "V1808T", "V1808", "V1801A", "V1801T", "V1801", "V1730T", "V1730F", "V1730A", "V1730", "V1724A", "V1723A", "V1723", "V1721A", "V1720A", "V1720T", "V1720", "V1716A", "V1715A", "V1715", "V1713A", "V1713", "V1712A", "V1712", "V1711T", "V1711A", "V1711", "V1709A", "V1709T", "V1709", "V1708A", "V1708T", "V1707A", "V1707T", "V1706T", "V1706", "V1703A", "V1701A", "V1701", "V1624A", "V1623A", "V1622A", "V1622", "V1621A", "V1619", "V1618A", "V1617A", "V1616", "V1615T", "V1614T", "V1613", "V1611T", "V1611", "V1608A", "V1609", "V1605", "V1604", "V1603", "V1601", "V1570", "V1562", "V1561", "V1550", "V1548", "V1546", "V1543", "V1542", "V1540", "V1530", "V1520", "V1510", "V1500", "V1420", "V1400", "V1310", "V1320"],
    
    "zte": ["ZTE_Axon_10_Pro", "ZTE_Axon_9", "ZTE_Axon_7", "ZTE_Axon_7_Mini", "ZTE_Blade_20", "ZTE_Blade_10", "ZTE_Blade_V10", "ZTE_Blade_V9", "ZTE_Blade_X", "ZTE_Blade_A7", "ZTE_Nubia_Red_Magic", "ZTE_Nubia_Z20", "ZTE_Nubia_X", "ZTE_Nubia_Z18", "ZTE_Nubia_Z17","Axon_10_Pro", "Axon_9", "Axon_7", "Axon_7_Mini", "Blade_20", "Blade_10", "Blade_V10", "Blade_V9", "Blade_X", "Blade_A7", "Nubia_Red_Magic", "Nubia_Z20", "Nubia_X", "Nubia_Z18", "Nubia_Z17"],
    
    "lg": ["LG_G8", "LG_V50", "LG_V40", "LG_G7", "LG_V30", "LG_G6", "LG_V20", "LG_G5", "LG_V10", "LG_G4", "LG_G3", "LG_G2", "LG_G_Flex"],
    
    "huawei": ["Huawei_P40", "Huawei_P30", "Huawei_P20", "Huawei_Mate_30", "Huawei_Mate_20", "Huawei_Mate_10", "Huawei_Nova_5", "Huawei_Nova_4", "Huawei_Nova_3", "Huawei_P10", "Huawei_P9", "Huawei_Honor_9", "Huawei_Honor_8", "Huawei_Y9", "Huawei_Y8"],
    
    "oneplus": ["OnePlus_9_Pro", "OnePlus_9", "OnePlus_8T", "OnePlus_8_Pro", "OnePlus_8", "OnePlus_7T_Pro", "OnePlus_7T", "OnePlus_7_Pro", "OnePlus_7", "OnePlus_6T", "OnePlus_6", "OnePlus_5T", "OnePlus_5", "OnePlus_3T", "OnePlus_3"]
} 
    
    fbcr1 = random.choice(fbcr_values)
    fbcr2 = random.choice(fbcr_values)
    fbcr3 = random.choice(fbcr_values)
    fbcr4 = random.choice(fbcr_values)
    fbcr5 = random.choice(fbcr_values)
    fbcr6 = random.choice(fbcr_values)
    fbcr7= random.choice(fbcr_values)
    fbcr8= random.choice(fbcr_values)
    fbcr9 = random.choice(fbcr_values)
    fbcr10 = random.choice(fbcr_values)


    fbmf1 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf2 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf3 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf4 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf5 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf6 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf7 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf8 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf9 = random.choice(list(fbmf_fbdv_dict.keys()))
    fbmf10 = random.choice(list(fbmf_fbdv_dict.keys()))

    fbdv1 = random.choice(fbmf_fbdv_dict[fbmf1])
    fbdv2 = random.choice(fbmf_fbdv_dict[fbmf2])
    fbdv3 = random.choice(fbmf_fbdv_dict[fbmf3])
    fbdv4 = random.choice(fbmf_fbdv_dict[fbmf4])
    fbdv5 = random.choice(fbmf_fbdv_dict[fbmf5])
    fbdv6 = random.choice(fbmf_fbdv_dict[fbmf6])
    fbdv7 = random.choice(fbmf_fbdv_dict[fbmf7])
    fbdv8 = random.choice(fbmf_fbdv_dict[fbmf8])
    fbdv9 = random.choice(fbmf_fbdv_dict[fbmf9])
    fbdv10 = random.choice(fbmf_fbdv_dict[fbmf10])

    return f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(0,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/en_US;FBRV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBCR/"+fbcr1+";FBMF/"+fbmf1+";FBBD/"+fbmf1+";FBPN/com.facebook.katana;FBDV/"+fbdv1+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:]"



fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))

    
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))  
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])

    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    
    return ua_bgraph
def generate_facebook_cookie(response):
    """
    Generates a properly formatted Facebook cookie string from the login API response.
    """
    cookies = []
    
    # Extract cookies from the session_cookies list
    if "session_cookies" in response:
        for cookie in response["session_cookies"]:
            cookies.append(f"{cookie['name']}={cookie['value']}")
    
    # Add sb= randomly as it is not included in the session_cookies
    import base64, os
    sb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
    cookies.insert(0, f"sb={sb}")  # 'sb' usually appears early in the cookie string

    return ";".join(cookies)


def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    gene = generate_random_ua()
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    
    data = {
        'method': 'auth.login',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': 'fc0a7caa49b192f64f6f5a6d9643bb28',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'credentials_type':'device_based_login_password',
        "source": "device_based_login",
        'error_detail_type':'button_with_disabled',
        'format':'json',
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'generate_machine_id':'1',
        "family_device_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "locale":"fr_DZ","client_country_code":"US",
        "device_id": str(uuid.uuid4()),
        "method": "auth.login",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
    }

    headers = {
        'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Connection-Type': 'WIFI',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=fc0a7caa49b192f64f6f5a6d9643bb28',
        'x-fb-device-group': '5120',
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-connection-quality':'EXCELLENT',
        'user-agent': gene,
        
       
        
        'accept-encoding':'gzip, deflate'
        
    }

    if uid in existing_uids:
        print(f"     {yellow}[INFO] ACCOUNT --> {uid} already exists.")
        print("───────────────────────────────────────────────────────────────")
        return

    try:
        response = requests.post(
            'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true',
            data=data, headers=headers, allow_redirects=False).json()

        
        
        if 'session_key' in response:
            token = response.get('access_token')
            if token:
                # Save token
                with open(path_file, 'a') as f:
                    f.write(f"{uid}|{token}\n")

                # Generate cookie manually
                cookie = generate_facebook_cookie(response)

                # Save cookie
                cookie_path = path_file.replace("ACCOUNT.txt", "ACCOUNTCOOKIE.txt").replace("PAGES.txt", "PAGESCOOKIE.txt")
                with open(cookie_path, 'a') as f_cookie:
                    f_cookie.write(f"{uid}|{cookie}\n")

                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                print(f"     {green}[SUCCESS]: {violet_chu}Extracted Account --> {green}{uid}.")
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                success_count.append(uid)
            else:
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                print(f"     {red}[FAILED]: {violet_chu}TO EXTRACT Account --> {red}{uid}.")
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 

    except Exception as e:
        print(f"     [ERROR] Error extracting account: {uid}. Reason: {str(e)}\n")




def proz(accounts_file, token_output_path, extract_type):
    """Process the accounts and extract tokens concurrently."""
    success_count = []

    # Load existing uids from the output file to avoid duplicates
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        # Process accounts concurrently using a thread pool executor
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print("───────────────────────────────────────────────────────────────")
        print(f"     [SUCCESS]: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("───────────────────────────────────────────────────────────────")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

import requests
import random
import concurrent.futures as thread
import os
import string

fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

import hashlib
import requests

def get_token(username, password):
    url = "https://api.facebook.com/restserver.php"
    ua = generate_random_ua()
    api_key = "882a8490361da98702bf97a021ddc14d"
    secret = "62f8ce9f74b12f84c123cc23437a4a32"

    # Build signature string
    sig_string = (
        f"api_key={api_key}"
        f"email={username}"
        f"format=JSON"
        f"locale=vi_vn"
        f"method=auth.login"
        f"password={password}"
        f"return_ssl_resources=0"
        f"v=1.0"
        f"{secret}"
    )

    sig = hashlib.md5(sig_string.encode('utf-8')).hexdigest()

    payload = {
        "api_key": api_key,
        "email": username,
        "format": "JSON",
        "locale": "vi_vn",
        "method": "auth.login",
        "password": password,
        "return_ssl_resources": "0",
        "v": "1.0",
        "sig": sig
    }

    headers = {
        "user-agent" : ua
    }

    try:
        response = requests.post(url, data=payload, headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data.get("access_token", "Access token not found.")
    except requests.RequestException as e:
        return f"Request failed: {e}"
    except ValueError:
        return "Error parsing response."

def mama(uid, pw, path_file, extract_type, success_count, existing_tokens):
    token = get_token(uid, pw)
    if token == "Access token not found.":
        print(f"{uid}  ─────> {red}FAILED TO EXTRACT TOKEN! ")
        return

    gene = generate_random_ua()

    if uid in existing_tokens:
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
        return

    # Extract Facebook Pages associated with the account token
    pages = extract_fb_pages(token)
    if pages:
        for page in pages:
            page_id = page['id']
            if page_id not in existing_tokens:
                with open(path_file, 'a') as f:
                    f.write(f"{page_id}|{page['accessToken']}\n")
                print(f"{white}{uid}  ─────> {green}Page ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                existing_tokens.add(page_id)
            else:
                print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")
    else:
        print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
    
    success_count.append(uid)

import requests
import random
import string
import os

CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code

def ensure_file_exists():
    """Ensure that the code file exists by creating it if it doesn't exist."""
    open(CODE_FILE, 'a').write('')  # Create the file if it doesn't exist

def generate_code():
    """Generate a unique code in the format BOOSTPHERE-XXX-XXXXX."""
    prefix = "BOOSTPHERE"
    number_part = ''.join(random.choices(string.digits, k=3))
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}-{number_part}-{letters_part}"

def save_code(code):
    """Save the generated code to a file."""
    with open(CODE_FILE, 'w') as file:
        file.write(code.strip())

def load_code():
    """Load the code from the file, if it exists."""
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    """Check if the generated code is approved by fetching the approval list."""
    try:
        url = "https://raw.githubusercontent.com/boostphere/Approval/main/Approval"
        response = requests.get(url)
        response.raise_for_status()

        # Clean and compare
        approved_codes = [
            line.split('#')[0].strip().upper()
            for line in response.text.splitlines()
            if line.strip() != ''
        ]
        return code.strip().upper() in approved_codes
    except requests.RequestException as e:
        print(f"Error fetching the approval list: {e}")
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    red = "\033[91m"
    orange = "\033[33m"
    yellow = "\033[93m"
    green = "\033[92m"
    blue = "\033[94m"
    indigo = "\033[95m"
    violet = "\033[35m"
    reset = "\033[0m"

    rainbow_colors = [red, orange, yellow, green, blue, indigo, violet]

    banner_text = """
██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
██║  ██║██████╔╝██║   ██║██║██║  ██║
██║  ██║██╔══██╗██║   ██║██║██║  ██║
██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
"""

    lines = banner_text.strip("\n").split("\n")
    for i, line in enumerate(lines):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(f"{color}{line}{reset}")

def generate_and_check_code():
    ensure_file_exists()
    code = load_code()

    if not code:
        code = generate_code()
        save_code(code)
        clear_screen()
        banner()
        print(f"      \033[93mYOUR GENERATED CODE \033[0m: \033[91m{code}")
    else:
        clear_screen()
        banner()
        print(f"      \033[93mYOUR CODE \033[0m: \033[91m{code}")

    if is_code_approved(code):
        main()
    else:
        print(f"\033[91m───────────────────────────────────────────────────────────────\033[0m")
        print(f"\033[91mCODE IS NOT APPROVED!\033[0m \033[93mPLEASE SEND IT TO\033[0m \033[97m: \033[93mhttps://www.facebook.com/profile.php?id=61575256934300")

# Stub for main function


def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    pages_data = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        
        url = data.get('paging', {}).get('next')  # Update the URL for the next request

    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(mama, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
def axl3():
    clear_screen()
    banner()
    folder_path = "/sdcard/boostphere/AutoShare"
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    prozc(file_path, token_output_path, extract_type)

import requests
import random
import concurrent.futures as thread
import os
import string

fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # Example token
    gene = generate_random_ua()
    if uid in existing_tokens:
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     {white}ACCOUNT ─────> {red}{uid} {green}ALREADY EXISTS")
        return

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }
    header = {
        'User-Agent': gene,
        'X-FB-Connection-Type': 'WIFI',
    }

    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

    try:
        response = requests.post(url, data=data, header=header, allow_redirects=False).json()
        
        if 'access_token' in response:
            token = response['access_token']

            # Extract Facebook Pages associated with the account token
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f"{white}{uid}  ─────> {green}Page ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f"{white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")

            else:
                print(f"{white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            
            success_count.append(uid)
        else:
            print(f"{white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")

    except Exception as e:
        print(f"[ERROR] Error extracting account: {uid}. Reason: {str(e)}")
import requests
import random
import string
import os

CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code

def ensure_file_exists():
    """Ensure that the code file exists by creating it if it doesn't exist."""
    open(CODE_FILE, 'a').write('')  # Create the file if it doesn't exist

def generate_code():
    """Generate a unique code in the format BOOSTPHERE-XXX-XXXXX."""
    prefix = "BOOSTPHERE"
    number_part = ''.join(random.choices(string.digits, k=3))
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}-{number_part}-{letters_part}"

def save_code(code):
    """Save the generated code to a file."""
    with open(CODE_FILE, 'w') as file:
        file.write(code.strip())

def load_code():
    """Load the code from the file, if it exists."""
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    """Check if the generated code is approved by fetching the approval list."""
    try:
        url = "https://raw.githubusercontent.com/M0koli/approval/refs/heads/main/approval.txt"
        response = requests.get(url)
        response.raise_for_status()

        # Clean and compare
        approved_codes = [
            line.split('#')[0].strip().upper()
            for line in response.text.splitlines()
            if line.strip() != ''
        ]
        return code.strip().upper() in approved_codes
    except requests.RequestException as e:
        print(f"Error fetching the approval list: {e}")
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    red = "\033[91m"
    orange = "\033[33m"
    yellow = "\033[93m"
    green = "\033[92m"
    blue = "\033[94m"
    indigo = "\033[95m"
    violet = "\033[35m"
    reset = "\033[0m"

    rainbow_colors = [red, orange, yellow, green, blue, indigo, violet]

    banner_text = """
██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
██║  ██║██████╔╝██║   ██║██║██║  ██║
██║  ██║██╔══██╗██║   ██║██║██║  ██║
██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
"""
    
    print(f"{red}Owner {yellow}: Connor Louzvendt")
    lines = banner_text.strip("\n").split("\n")
    for i, line in enumerate(lines):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(f"{color}{line}{reset}")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"{red}Owner {yellow}: Connor Louzvendt")
    print(f"{red}Facebook {yellow}: https://www.facebook.com/Connor.Cra1g")
    print(f"{red}Tool {yellow}: Paid")
def generate_and_check_code():
    ensure_file_exists()
    code = load_code()

    if not code:
        code = generate_code()
        save_code(code)
        clear_screen()
        banner()
        print(f"      \033[93mYOUR GENERATED CODE \033[0m: \033[91m{code}")
    else:
        clear_screen()
        banner()
        print(f"      \033[93mYOUR CODE \033[0m: \033[91m{code}")

    if is_code_approved(code):
        main()
    else:
        print(f"\033[91m───────────────────────────────────────────────────────────────\033[0m")
        print(f"\033[91mCODE IS NOT APPROVED!\033[0m \033[93mPLEASE SEND IT TO\033[0m \033[97m: \033[93mhttps://www.facebook.com/profile.php?id=61575256934300")

# Stub for main function

#EAAAAUaZA8jlABO17KRCkGwcVeYlVwtiKSOFIUZA5CdDnlZAY9yDfNRdKFKq0G1hf24LXd7O6LO29APVy1PN4D9zeM319SPOFSVW5SM5QoYyGqZCKEAhCZArrOqZBXs9IVYbnIC0TgicJFCT78SUOBPP1PI79ZBHRISpstZCgUa5MitQX7P0KtFYLitSZAXLXS6oQTVoKZBzwZDZD
def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    pages_data = []
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        
        url = data.get('paging', {}).get('next')  # Update the URL for the next request

    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]

            for future in futures:
                future.result()

        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
def axl1():
    clear_screen()
    banner()
    folder_path = "/sdcard/boostphere/AutoShare"
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    proz(file_path, token_output_path, extract_type)
import requests
import time
import concurrent.futures



def load_tokens(file_path):
    """Loads the tokens from the specified file."""
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        tokens = [line.split('|')[1].strip() for line in lines if len(line.split('|')) > 1]
        return tokens
    except Exception as e:
        print(f"Error loading tokens from {file_path}: {e}")
        return []

def share_post(link, token):
    """Shares a post on the user's feed with 'Only Me' privacy."""
    url = "https://graph.facebook.com/v13.0/me/feed"
    payload = {
        'link': link,
        'published': 'false',
        'privacy': '{"value":"SELF"}',  
        'access_token': token
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            print(f"SUCCESSFULLY SHARED ✅")
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            return True
        else:
            pass
            return False
    except requests.exceptions.RequestException as e:
        pass
        return False

def share_task(link, tokens, total_shares, start_index, end_index):
    """Handles sharing in a range of shares."""
    successful = 0
    for i in range(start_index, end_index):
        token = tokens[i % len(tokens)]  # Cycle through tokens if more shares than tokens
        pass
        if share_post(link, token):
            successful += 1
        time.sleep(1)  # Optional: add delay to avoid spam/blocking
    return successful
def get_combined_data(url):
    """
    Fetch the response from the given URL and extract the `actrs` number and `post_id`.
    Combine these values and return the result.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The combined string of `actrs` number and `post_id`, or an error message.
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }

    try:
        response = requests.get(url, headers=headers).text

        # Extract `actrs` number
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None

        # Extract `post_id`
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None

        if actrs_number and post_id_match:
            return actrs_number, post_id_match
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"

    except Exception as e:
        return f"An error occurred: {str(e)}"
def shareable():
    file_options = {
    1: "/sdcard/boostphere/AutoShare/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/AutoShare/FRAPAGES.txt",
    3: "/sdcard/boostphere/AutoShare/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/AutoShare/PWPAGES.txt"
}
    clear_screen()
    banner()
    print(f"{green}Select a file to load tokens from:")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    for option, path in file_options.items():
        print(f" {red}[{option}]. {green}{path}")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    selected_option = int(input(f"{green}Enter the number of your selected file: "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    if selected_option not in file_options:
        print("Invalid selection.")
        return

    file_path = file_options[selected_option]
    tokens = load_tokens(file_path)
    if not tokens:
        print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")
        print(f"{red}No tokens found in the selected file.")
        return
    
    print(f"\n{green}Found {red}{len(tokens)} {yellow}Tokens")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    num_tokens_to_use = int(input(f"{green}How many tokens would you like to use (max {len(tokens)}): "))
    if num_tokens_to_use > len(tokens):
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        print(f" {red}Enghhhhh!You can't use more tokens than available.")
        return

    selected_tokens = tokens[:num_tokens_to_use]
    print(f"\nSelected {num_tokens_to_use} tokens.")
    
    user_id = input(f"{yellow}Enter the Facebook link : ")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    actrs_number, post_id = get_combined_data(user_id)
    link = f"facebook.com/{actrs_number}/posts/{post_id}"
    
    
    total_shares = int(input(f"{red}How many shares would you like to perform? "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    
    threads = 30
    share_per_thread = total_shares // threads  
    extra_shares = total_shares % threads  

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        start_index = 0
        for i in range(threads):
            end_index = start_index + share_per_thread + (1 if i < extra_shares else 0)
            futures.append(executor.submit(share_task, link, selected_tokens, total_shares, start_index, end_index))
            start_index = end_index
        
        
        total_successful = 0
        for future in concurrent.futures.as_completed(futures):
            total_successful += future.result()

    print(f"\nFinished: {total_successful}/{total_shares} posts shared successfully.")
def extraction():
    clear_screen()
    banner()
    print(f"{blue}[1] {violet_chu}EXTRACT {red}ACCOUNT")
    print(f"{blue}[2] {violet_chu}EXTRACT {red}PAGES")
    print(f"{blue}[3] {violet_chu}EXTRACT {red}ACCOUNT V2")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    elif choice == '3':
        axl3()
    else:
        print(f"     {red}INVALID CHOICE")
def axl2():
    clear_screen()
    banner()
    folder_path = "/sdcard/boostphere/AutoShare"  
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    file_path = input(f"     \033[33mPATH: ").strip()

    prozc(file_path, account_file, extract_type)





    
folder_name = "/sdcard/boostphere/AutoShare"
file_names = ["FRAACCOUNT.txt", "FRAPAGES.txt", "RPWACCOUNT.txt", "RPWPAGES.txt","generated_code.txt"]



if not os.path.exists(folder_name):


    try:
          os.makedirs(folder_name)
    except Exception:
              pass
              


    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)

        if not os.path.exists(file_path):

            try:

                with open(file_path, 'w') as file:

                    pass  
            except Exception:

                pass
import requests
import os

file_map = {
    "1": ("FRAACCOUNTCOOKIE.txt", "FRAACCOUNT.txt"),
    "2": ("FRAPAGESCOOKIE.txt", "FRAPAGES.txt"),
    "3": ("RPWACCOUNTCOOKIE.txt", "RPWACCOUNT.txt"),
    "4": ("RPWPAGESCOOKIE.txt", "RPWPAGES.txt"),
}

base_path = "/sdcard/boostphere/AutoShare"

def get_tokens_from_cookies(input_file, output_file, start_index):
    input_path = os.path.join(base_path, input_file)
    output_path = os.path.join(base_path, output_file)

    
    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if '|' in line]

    print(f"Total cookies found: {len(lines)}")

    if start_index >= len(lines):
        print("Invalid start index.")
        return

   
    existing_tokens = {}
    if os.path.exists(output_path):
        with open(output_path, 'r') as f:
            for line in f:
                if '|' in line:
                    uid, token = line.strip().split('|', 1)
                    existing_tokens[uid] = token

    for line in lines[start_index:]:
        uid, cookie = line.split('|', 1)
        url = f"https://convert-2.onrender.com/index.php?cookie={cookie}"
        try:
            res = requests.get(url, timeout=10)
            data = res.json()

            if data.get("success") and "access_token" in data:
                token = data["access_token"]
                existing_tokens[uid] = token
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                print(f"{green}[✔] {red}{uid} {yellow}-> {green}Token retrieved.")
            else:
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                print(f"{red}[✘] {yellow}{uid} {white}-> {red}Failed to get token.")

        except Exception as e:
            print(f"[!] Error processing {uid}: {e}")

    # Save updated tokens
    with open(output_path, 'w') as f:
        for uid, token in existing_tokens.items():
            f.write(f"{uid}|{token}\n")

    print(f"\n✅ Tokens saved to {output_path}")

def renewableToken():
    clear_screen() 
    banner()
    print(f"{green}Choose a file:")
    print(f"{yellow}[1] {green}FRAACCOUNTCOOKIE")
    print(f"{yellow}[2] {green}FRAPAGESCOOKIE")
    print(f"{yellow}[3] {green}RPWACCOUNTCOOKIE")
    print(f"[{yellow}4] {green}RPWPAGESCOOKIE")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    choice = input(f"{violet_chu}Enter choice (1-4): ").strip()
    if choice not in file_map:
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        print(f"{red}Invalid choice.")
        return

    input_file, output_file = file_map[choice]
    input_path = os.path.join(base_path, input_file)

    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with open(input_path, 'r') as f:
        total_lines = sum(1 for line in f if '|' in line)
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"\n{total_lines} Found ✅ .")

    try:
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        start_index = int(input(f"{green}Enter start index (1 - {total_lines-1}): "))
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    except ValueError:
        print("Invalid input. Must be an integer.")
        return

    get_tokens_from_cookies(input_file, output_file, start_index)
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def matic():
    # File selection input/output paths
    input_files = {
        "1": '/sdcard/boostphere/AutoShare/FRAACCOUNT.txt',
        "2": '/sdcard/boostphere/AutoShare/FRAPAGES.txt',
        "3": '/sdcard/boostphere/AutoShare/RPWACCOUNT.txt',
        "4": '/sdcard/boostphere/AutoShare/RPWPAGES.txt'
    }

    output_files = {
        "1": '/sdcard/boostphere/AutoShare/FRAACCOUNTCOOKIE.txt',
        "2": '/sdcard/boostphere/AutoShare/FRAPAGESCOOKIE.txt',
        "3": '/sdcard/boostphere/AutoShare/RPWACCOUNTCOOKIE.txt',
        "4": '/sdcard/boostphere/AutoShare/RPWPAGESCOOKIE.txt'
    }
    clear_screen()
    banner()
    print(f" {green}Choose a file to process:")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"{red}[1] {green}FRAACCOUNT")
    print(f"{red}[2] {green}FRAPAGES")
    print(f"{red}[3] {green}RPWACCOUNT")
    print(f"{red}[4] {green}RPWPAGES")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    choice = input(f" {green}Enter your choice (1-4): ").strip()

    input_path = input_files.get(choice)
    output_path = output_files.get(choice)

    if not input_path or not os.path.isfile(input_path):
        print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        print(f"{red}Invalid choice or input file not found.")
        return

    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    results = []

    def task(line):
        line = line.strip()
        if '|' not in line:
            return None, None
        uid, token = line.split('|', 1)
        try:
            r1 = requests.get('https://graph.facebook.com/app', params={'access_token': token.strip()}, timeout=10)
            data1 = r1.json()
            if 'error' in data1:
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                return f"{green}[{uid}] {red}Invalid token: {yellow}{data1['error']['message']}", None

            r2 = requests.get(
                'https://api.facebook.com/method/auth.getSessionforApp',
                params={
                    'access_token': token.strip(),
                    'format': 'json',
                    'new_app_id': data1['id'],
                    'generate_session_cookies': '1'
                },
                timeout=10
            )
            data2 = r2.json()

            if 'session_cookies' in data2:
                cookies = ';'.join([f"{c['name']}={c['value']}" for c in data2['session_cookies']])
                return f"{red}[{uid}] {green}Successfully Retrieved Session"
            else:
                return f"{red}[{uid}] {yellow}Failed to retrieve session cookies.", None

        except Exception as e:
            return f"[{uid}] Error: {e}", None

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(task, line): line for line in lines}
        for future in as_completed(futures):
            status, result = future.result()
            if status:
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                print(status)
            if result:
                print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
                results.append(result)

    if results:
        with open(output_path, 'w') as outfile:
            outfile.write('\n'.join(results))
            print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
        print(f"\n{green}Saved {yellow}{len(results)} {red}cookies !")
def verify_tokens():
    files = {
        "1": "/sdcard/boostphere/AutoShare/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/AutoShare/FRAPAGES.txt",
        "3": "/sdcard/boostphere/AutoShare/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/AutoShare/RPWPAGES.txt"
    }

    clear_screen()
    banner()
    print(f" {green}Choose a file to verify tokens:{reset}")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")
    print(f"{red}[1]{green} FRAACCOUNT")
    print(f"{red}[2]{green} FRAPAGES")
    print(f"{red}[3]{green} RPWACCOUNT")
    print(f"{red}[4]{green} RPWPAGES")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")

    choice = input(f" {green}Enter your choice (1-4): {reset}").strip()
    file_path = files.get(choice)

    if not file_path or not os.path.isfile(file_path):
        print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")
        print(f"{red}Invalid choice or file not found.{reset}")
        return

    with open(file_path, "r") as f:
        tokens = [line.strip() for line in f if "|" in line]

    valid_tokens = []

    def check_token(line):
        uid, token = line.split("|", 1)
        try:
            r = requests.get(
                "https://graph.facebook.com/me",
                params={"access_token": token.strip()},
                timeout=10
            )
            data = r.json()

            if "error" in data:
                msg = data["error"].get("message", "Unknown error")
                print(f"{red}[✗]{yellow} {uid} → Invalid: {msg}{reset}")
                return None
            else:
                print(f"{green}[✓]{reset} {uid} → Token is valid.")
                return line

        except Exception as e:
            print(f"{red}[!] {uid} Error: {e}{reset}")
            return None

    print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")
    print(f"{green}Starting token verification... Please wait.{reset}")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")

    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(check_token, line) for line in tokens]
        for future in as_completed(futures):
            result = future.result()
            if result:
                valid_tokens.append(result)

    # Overwrite file with only valid tokens
    with open(file_path, "w") as f:
        f.write("\n".join(valid_tokens))

    print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")
    print(f"{green}Verification complete! {yellow}{len(valid_tokens)}{green} valid tokens saved.{reset}")
    print(f"{red}{len(tokens) - len(valid_tokens)} invalid tokens removed.{reset}")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────{reset}")
def main(): 
    clear_screen()
    banner()
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"{green}[1/A] {blue}Extract Accounts/Pages")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m") 
    print(f"{green}[2/B] {blue}Convert Token to Cookies")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}[3/C] {blue}Convert Cookies to Token")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}[4/D] {blue}Remove Dead Tokens")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m")
    print(f"{green}[5/E] {blue}AutoShare")
    print(f"{dark_violet}───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{green} Choice : ")

    if choice in ['1', 'A', 'a']:
       extraction()
    elif choice in ['2', 'B', 'b']:
        matic()
    elif choice in ['3', 'C', 'c']:
        renewableToken()
    elif choice in ['4', 'D', 'd']:
        verify_tokens()
    elif choice in ['5', 'E', 'e']:
        shareable()
if __name__ == "__main__":
    main()
