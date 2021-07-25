#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#https://github.com/muslimcyber1234

import requests, re , colorama
colorama.init()
print("""

\033[1;31m  _   _            _      _
\033[1;31m | | | | __ _  ___| | __ | | ____ _ _ __ ___   ___ _ __ __ _
\033[1;31m | |_| |/ _` |/ __| |/ / | |/ / _` | '_ ` _ \ / _ \ '__/ _` |
\033[1;31m |  _  | (_| | (__|   <  |   < (_| | | | | | |  __/ | | (_| |
\033[1;31m |_| |_|\__,_|\___|_|\_\ |_|\_\__,_|_| |_| |_|\___|_|  \__,_|

\033[1;37m           _
\033[1;37m   ___ ___| |___   __
\033[1;37m  / __/ __| __\ \ / /
\033[1;37m | (_| (__| |_ \ V /
\033[1;32m  \___\___|\__| \_/

\033[1;33m                      `.--:::::-.`
\033[1;33m                  ``/-y-y:y:y:y:y/+-.`            `  `-`
\033[1;33m :-        `- :/..o:s-y:y:y/y:y/y:y/s-:/:`    +s:-do`:++
\033[1;33m y/`.   `+/`s.+s-o//sosos/y/s/h/h/h:h/y:ys-   :dmshy/`od
\033[1;33m +`+-  .yhs -++:o-oo+s+os+y+h+y/h:y+h:d:y/-    .+hmNs`/N
\033[1;33m   +/ `ssss -y:+o-s++y+ss/y+h/h/s+y/h:s:+/::...+.`.hNh:d
\033[1;33m - .o:/y./s.oo/.``...-/+s+y/y/y+ssy/+..``.-/+-/: ``/Nhmm
\033[1;33m .  .--.::./y/.``.:+ssso+/o/sos+o/:/+++:.:++/-`-:+.`No-y
\033[1;33m /``/+/`ods/o+:`.:-::/oyhdmddhhhyso/:---.-+/+./--+. dd `
\033[1;33m /``.od.`dm+/+-`-/osso+-./ymNNms/.-+sys/..++:.` `:o sN.
\033[1;33m     .d: /d+-/:./omNNNNmh+ymNNdo+hmNNmd+--::-:`-.`. /N/
\033[1;33m o``-+y. `yo:/-.+so+o+++oshmMNhhso++++:-::--:/ohy/..odo
\033[1;33m mosyo.  :ds//-`/yhysoo+osdmNNhho+/++syy+-`://o./yhhdh.
\033[1;33m Nh+-` ./yy +/-`oddmmmmNNNNmMNdmNNmmmmds+---//.  `.-/s-
\033[1;33m d-``./os:`:s/:`/ssydmNNNNNmMNdmNNNNmhs/--/-//`     -yo`
\033[1;33m hyssys/`  :++/`.+///shhmmmmMMddhdhyo+/+://://`     `.`
\033[1;33m `-::.`    `+oo-`-oh--hmNdooddo+dmdo`-s+/+/:/-
\033[1;33m       `.-///os:`-/yh/-:::``/: .:::./yoo+/:::`
\033[1;33m  ``-////+o/--//--/oyhhhhyy+ss+yyysoyooo+/:/-.-/:/++-`
\033[1;33m `:::///++++o:-:::-:oshdmdh+++oddyoho+//-::-.:so+++os+:`
\033[1;33m -.`.//+o//o/o/--:+::/shmNN/  oNmhyo/:-.---.:++ossoosoo+
\033[1;33m :++:///++/+o+o+-:/sso:/hmNs  sNmy:.`-`.../osssooo+++//+
\033[1;33m syhhh+//+//o/y/y/+.s/s+o+hd` hh+/-/+o/o+sooys+/oyyyo+//
\033[1;33m hyyssso/::+:o:++++::/:s:o/+-/s/s+s/s+y+ss/y+syy/:sys+/:
\033[1;33m Nmmdddhy+/s+so+oyoy:+/y/y:y/o:o+sd/os+oyoos+s//:..--..-
\033[1;33m MNmy+syhdsN+yhshyodsshdoNsd:/:m::sh:Nsyyyohym/::::::/sh
\033[1;33m MMMNmh+oooooyyosoydddddddddhso+/:::-/:+:/::///+osyyhNNN
\033[1;33m MMMMNNNdhoo++/smhyosydNNNNNNNNNNNmmmmmddhyhmmNNNNNmNNNN

\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdhhhhdNNNNNNNNNNNNNNNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNNNmhys+++++/////ohNNNNNNNNNNNNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNmhyo+::o///////:::::::/hNNNNNNNNNNN
\033[1;31m NNNNNNNNNNNNNmmhso/:/o///////::::::::::::::/NNNNNNNNNNN
\033[1;31m NNNNNNNmdhysoo++/////////::::::------------:hNNNNNNNNNN
\033[1;31m mdhhyso++++++///////::::::--------------:/+/:mNNNNNNNNN
\033[1;31m Nmmd+::/+++++////:::-----------------++so/:--hNNNNNNNNN
\033[1;31m NNd:.....-:/::::------.........--------------dNNNNNNNNN
\033[1;31m NN+-....`````.-:...............-----..---::/yNNNNNNNNNN
\033[1;31m NN/...+.`.....`::..............-----:::///odNNNNNNNNNNN
\033[1;31m NNo-..-.`....``./-.........----+s:--:/oydmNNNNNNNNNNNNN
\033[1;31m NNd:.........``.--...-----:::--ss-.../mNNNNNNhyyhmNNNNN
\033[1;31m NNNh:...........---:::::----..`+/.-+shNNNNNN+:h-.-:osmN
\033[1;31m NNNNd+-..`.+-...-::::/+/....:so:--sNNNNNNNNm/-:...:s.+N
\033[1;31m NNNNNNdo:-...--:+sydNNNy-.....----yNNNNmhs+/:::-----./N
\033[1;31m NNNNNNNNNdhyyhdNNNNNNNNh.---..--/yymhs+/////::---:---yN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNd/--..---:///:::::---:::::--mNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNo-.......:::------::::::::--/NN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNd:------/y------::::::/+/-./hNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNN/---------------:+ydmNNNmmNNNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNNd:--.------:+shmNNNNNNNNNNNNNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNNNmy+:-:/oydNNNNNNNNNNNNNNNNNNN
\033[1;31m NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

\033[1;32m  _
\033[1;32m | |__  _   _
\033[1;32m | '_ \| | | |
\033[1;32m | |_) | |_| |
\033[1;32m |_.__/ \__, |
\033[1;32m        |___/

\033[1;36m                      _ _                      _
\033[1;36m  _ __ ___  _   _ ___| (_)_ __ ___   ___ _   _| |__   ___ _ __
\033[1;36m | '_ ` _ \| | | / __| | | '_ ` _ \ / __| | | | '_ \ / _ \ '__|
\033[1;36m | | | | | | |_| \__ \ | | | | | | | (__| |_| | |_) |  __/ |
\033[1;36m |_| |_| |_|\__,_|___/_|_|_| |_| |_|\___|\__, |_.__/ \___|_|
\033[1;36m                                         |___/

\033[1;33m _ ____  _____ _  _
\033[1;33m/ |___ \|___ /| || |
\033[1;33m| | __) | |_ \| || |_
\033[1;33m| |/ __/ ___) |__   _|
\033[1;33m|_|_____|____/   |_|
\033[1;31m                                                                        muslimcyber1234
\033[1;31m1) \033[1;37mUnited States                \033[1;31m31) \033[1;37mMexico                \033[1;31m61) \033[1;37mMoldova
\033[1;31m2) \033[1;37mJapan                        \033[1;31m32) \033[1;37mFinland               \033[1;31m62) \033[1;37mNicaragua
\033[1;31m3) \033[1;37mItaly                        \033[1;31m33) \033[1;37mChina                 \033[1;31m63) \033[1;37mMalta
\033[1;31m4) \033[1;37mKorea                        \033[1;31m34) \033[1;37mChile                 \033[1;31m64) \033[1;37mTrinidad And Tobago
\033[1;31m5) \033[1;37mFrance                       \033[1;31m35) \033[1;37mSouth Africa          \033[1;31m65) \033[1;37mSoudi Arabia
\033[1;31m6) \033[1;37mGermany                      \033[1;31m36) \033[1;37mSlovakia              \033[1;31m66) \033[1;37mCroatia
\033[1;31m7) \033[1;37mTaiwan                       \033[1;31m37) \033[1;37mHungary               \033[1;31m67) \033[1;37mCyprus
\033[1;31m8) \033[1;37mRussian Federation           \033[1;31m38) \033[1;37mIreland               \033[1;31m68) \033[1;37mPakistan
\033[1;31m9) \033[1;37mUnited Kingdom               \033[1;31m39) \033[1;37mEgypt                 \033[1;31m69) \033[1;37mUnited Arab Emirates
\033[1;31m10) \033[1;37mNetherlands                 \033[1;31m40) \033[1;37mThailand              \033[1;31m70) \033[1;37mKazakhstan
\033[1;31m11) \033[1;37mCzech Republic              \033[1;31m41) \033[1;37mUkraine               \033[1;31m71) \033[1;37mKuwait
\033[1;31m12) \033[1;37mTurkey                      \033[1;31m42) \033[1;37mSerbia                \033[1;31m72) \033[1;37mVenezuela
\033[1;31m13) \033[1;37mAustria                     \033[1;31m43) \033[1;37mHong Kong             \033[1;31m73) \033[1;37mGeorgia
\033[1;31m14) \033[1;37mSwitzerland                 \033[1;31m44) \033[1;37mGreece                \033[1;31m74) \033[1;37mMontenegro
\033[1;31m15) \033[1;37mSpain                       \033[1;31m45) \033[1;37mPortugal              \033[1;31m75) \033[1;37mEl Salvador
\033[1;31m16) \033[1;37mCanada                      \033[1;31m46) \033[1;37mLatvia                \033[1;31m76) \033[1;37mLuxembourg
\033[1;31m17) \033[1;37mSweden                      \033[1;31m47) \033[1;37mSingapore             \033[1;31m77) \033[1;37mCuracao
\033[1;31m18) \033[1;37mIsrael                      \033[1;31m48) \033[1;37mIceland               \033[1;31m78) \033[1;37mPuerto Rico
\033[1;31m19) \033[1;37mIran                        \033[1;31m49) \033[1;37mMalaysia              \033[1;31m79) \033[1;37mCosta Rica
\033[1;31m20) \033[1;37mPoland                      \033[1;31m50) \033[1;37mColombia              \033[1;31m80) \033[1;37mBelarus
\033[1;31m21) \033[1;37mIndia                       \033[1;31m51) \033[1;37mTunisia               \033[1;31m81) \033[1;37mAlbania
\033[1;31m22) \033[1;37mNorway                      \033[1;31m52) \033[1;37mEstonia               \033[1;31m82) \033[1;37mLiechtenstein
\033[1;31m23) \033[1;37mRomania                     \033[1;31m53) \033[1;37mDominican Republic    \033[1;31m83) \033[1;37mBosnia And Herzegovia
\033[1;31m24) \033[1;37mViet Nam                    \033[1;31m54) \033[1;37mSloveania             \033[1;31m84) \033[1;37mParaguay
\033[1;31m25) \033[1;37mBelgium                     \033[1;31m55) \033[1;37mEcuador               \033[1;31m85) \033[1;37mPhilippines
\033[1;31m26) \033[1;37mBrazil                      \033[1;31m56) \033[1;37mLithuania             \033[1;31m86) \033[1;37mFaroe Islands
\033[1;31m27) \033[1;37mBulgaria                    \033[1;31m57) \033[1;37mPalestinian           \033[1;31m87) \033[1;37mGuatemala
\033[1;31m28) \033[1;37mIndonesia                   \033[1;31m58) \033[1;37mNew Zealand           \033[1;31m88) \033[1;37mNepal
\033[1;31m29) \033[1;37mDenmark                     \033[1;31m59) \033[1;37mBangladeh             \033[1;31m89) \033[1;37mPeru
\033[1;31m30) \033[1;37mArgentina                   \033[1;31m60) \033[1;37mPanama                \033[1;31m90) \033[1;37mUruguay
                                                          \033[1;31m91) \033[1;37mExtra
""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 91+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()
