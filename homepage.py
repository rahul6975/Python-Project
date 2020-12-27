import tkinter
from tkinter import *
from tkinter import messagebox
import tkcalendar
from tkcalendar import DateEntry
import time
import mysql.connector
import random
#database connection
cu=mysql.connector.connect(user="root",password="root",host="localhost",database="GARV")
con=cu.cursor()

####Profile Start############################################################################################################################################################

def teaching():
    b30={"Sericulture is:":["art of silkworm breeding","science of the various kinds of serum","artificial rearing of fish","art of silkworm breeding","study of various cultures of a community"]}
    b1={"Which of the following dams is not on Narmada river?":["Koyna Power Project","Indira-Sagar Project"," Maheshwar Hydel Power Project","Jobat Project","Koyna Power Project"]}
    b2={"Photosphere is described as the:":["Visible surface of the sun from which radiation emanates","Lower layer of atmosphere","Visible surface of the sun from which radiation emanates","Wavelength of solar spectrum","None of the above"]}
    b3={"Location of sugar industry in India \nis shifting from north to south because of:":["high yield and high sugar content in sugarcane","cheap labour","expanding regional market","cheap and abundant supply of power","high yield and high sugar content in sugarcane"]}
    b4={"The area covered by forest in India is about:":["23%","46%","33%","23%","19%"]}       
    b5={"India's Oil bearing areas are mostly \nassociated with the:":["Sedimentary rocks","Plutonic rocks","Volcanic rocks","Sedimentary rocks","Metamorphic rocks"]}
    b6={"Which one of the following pairs \nis not correctly matched?":["Bhubaneshwar -- Mahanadi"," Kota —Chambal","Bhubaneshwar -- Mahanadi","Jabalpur — Narmada","Surat --- Tapti"]}
    b7={"Nagarjunasagar Project is situated on the river:":["Krishna","Tungabhadra","Cauvery","Krishna","Godavari"]}
    b8={"Through which States does Cauvery River flow? ":[" M.P. Tamil Nadu","Gujarat, M.P. Tamil Nadu","Karnataka, Kerala, Tamil Nadu","Karnataka, Kerala, Andhra Pradesh","M.P., Maharashtra, Tamil Nadu"]}
    b9={"The world is divided into:":["24 time zones","12 time zones","20 time zones","24 time zones","36 time zones"]}
    b10={"Atmosphere exists because:":["The Gravitational force of the Earth","The Gravitational force of the Earth","Revolution of the Earth","Rotation of the Earth","Rotation of the Earth"]}
    b11={"Laterite soil develop as a result of:":["leaching","deposits of alluvial","deposition of loess","leaching","continued vegetation cover"]}
    b12={"Which of the following rivers is not a tributory of the Indus?":["Bhagirathi","Sutlej","Jhelum","Bhagirathi","Chenab"]}
    b13={"Different seasons are formed because":["because earth is tilted when it revolves around sun.","Sun is moving around the earth","of revolution of the earth around the Sun on its orbit","of rotation of the earth around its axis","because earth is tilted when it revolves around sun."]}
    b14={"The natural vegetation of Savana consists of: ":["Tall grass","Tall grass","Scrub jungle","Short grass","Trees"]}
    b15={"The much discussed Tehri Dam Project is \nlocated in which of the following states?":["Uttaranchal","Madhya Pradesh","Rajasthan","Haryana","Uttaranchal"]}
    b16={" Which of the following is the biggest \nfresh water lake' in India?":["Wular Lake","Dal Lake","Sukhna Lake","Loktak Lake","Wular Lake"]}
    b17={"The difference between the Indian Standard Time \nand the Greenwich mean Time is:":["+ 5 * 1/2 hours","-3 * 1/2 hours","+ 3 * 1/2 hours","- 3 * 1/4 hours","+ 5 * 1/2 hours"]}
    b18={"The biggest reserves of thorium are in:":["India","India","China","The Soviet Union","U.S.A"]}
    b19={"The term 'Regur' refers to:":["Black Cotton soils","Laterite soils","Black Cotton soils","Red soils","Deltaic Alluvial soils"]}
    b20={"Where are most of the earth's active \nVolcanoes concentrated?":["Pacific Ocean","Europe","Pacific Ocean","Africa","South America"]}
    b21={"The fertility of the soil can be \nincreased by growing :":["Legumes","Cereals","Fibre Crops","Legumes","Root Crops"]}
    b22={"The coldest place on the earth is:":["Verkhoyansk (Antarctica)","Halifax","Chicago","Siachen","Verkhoyansk (Antarctica)"]}
    b23={"When does the moon come between the sun \nand the earth?":["solar eclipse","Lunar eclipse","solar eclipse","side real day","full moon day"]}
    b24={"Turpentine oil used in medicine' is obtained from:":["Chir pin","Acacia","Chir pin","Myrobalans","Kusum"]}
    b25={"Which of the following is cold stream?":["Labrador","Curasia","Labrador","Gulf of stream","Hakuna Hatata"]}
    b26={"Which of the following is the smallest \nocean of the world?":["Arctic","Pacific","Indian","Atlantic","Arctic"]}
    b27={"Which of the following soil is very \nhard to cultivate? ":["Red","Alluvial","Red","Black","Sandy"]}
    b28={"The southern tip of India is:":["Indira Point in Nicobar Islands","Cape Comorin","Point Calimere","Indira Point in Nicobar Islands","Kovalam in Trivandrum"]}
    b29={"The rock material carried by a \nglacier is called":["moraines","alluvium","meanders","nodules","moraines"]}
    d=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30]
    dic=[]
    while(len(dic)!=15):
         m=random.choice(d)
         if m not in dic:
              dic.append(m)
    return dic

def gov():
    c1={"World Tourism Day is celebrated on- ":["September 27","September 12","September 25","September 27","September 29"]}
    c2={"Where is Bose Institute ?":["Kolkata","Dispur","Kolkata","Mumbai","New Delhi"]}
    c3={"When is the International Yoga Day celebrated ?":["June 21","June 21","March 21","April 22","May 31"]}
    c4={"The motif of 'Hampi with Chariot' is printed \non the reverse of which currency note ?":["Rs. 50 note","One Rupee Note"," Rs. 500 note","Rs. 50 note","Rs. 1000 note"]}
    c5={"'Line of Blood' is a book written by whom? ":["Bairaj Khanna","Bairaj Khanna","Ursula Vernon","Amal EI-Mohtar","Diksha Basu"]}
    c6={"........... is the first woman to head\n a public sector bank. ":["Arundhati Bhattacharya","Arundhati Bhattacharya","Shikha Sharma","Chanda Kochar","Usha Ananthasubramanyan"]}
    c7={"The Insurance Regulatory and Development \nAuthority (IRDA) is a -":["Statutory Body","Statutory Body"," Constitutional Body","agricultural irrigation","domestic use"]}
    c8={"Who among the following Scientists got two \nNobel prizes of which one was in Peace?":["Linus Pauling","Albert Einstein","H. G. Khorana","Linus Pauling","Paul Berg"]}
    c9={"The first Indian State to go wholley organic is -":["Sikkim","Meghalaya","Sikkim","Manipur","Kerala"]}
    c10={"Which among the following cities in India, is not \nlocated in Golden Quadrilateral Road Network?":["Chandigarh","Kolkata","Mumbai","New Delhi","Chandigarh"]}
    c11={"What is the name of Indira Gandhi's Samadhi?":["Shakti Sthal","Shanti Ghat","Shakti Sthal","Shanti Van","Shanti Sthal"]}
    c12={"According to Census 2011, the district of Madhya Pradesh \nwith highest female-male ratio is -":["Balaghat","Jhabua","Dindor","Mandla","Balaghat"]}
    c13={"What is the approximate present irrigation potential, \nin lakh hectares, of Madhya Pradesh?":["33","68.20","44.94","78.20","33"]}
    c14={"Madhya Pradesh State was constituted on -":["1st November, 1956","1st November, 1959","1st September, 1956","1st November, 1956","1st September, 1951"]}
    c15={"Who introduced 'Green Army' for environment conservation?":["Australia","Japan","China","Australia","Egypt"]}
    c16={"According to the World Health Organization the most \naffected country by Ebola was -":["Liberia","Nigeria","Mali","Liberia","Senegal"]}
    c17={"Prime Minister Narendra Modi launched \n'Swachha Bharat Mission' officially on -":["Gandhi Jayanti","Independence Day","Republic Day","Gandhi Jayanti","Environment Day"]}
    c18={"'Kyoto Protocol' is related to -":["Climate change","Air pollution","Green House gases","Climate change","Water pollution"]}
    c19={"102nd Indian Science Congress was held at-":["Mumbai","Mumbai","Jammu","Kolkata","Ahmedabad"]}
    c20={"Who was sworn in as the first Chief Minister\n of Telangana State?":["K. Chandrashekhar Rao","Jayalalitha","Chandrababu","K. Chandrashekhar Rao","None of these"]}
    c21={"'Ozone Layer Preservation Day' is celebrated on -":["16th September","16th September","5th June","23rd March","21st April"]}
    c22={"Organization related to 'Red Data Book' or \n'Red List' is -":["I.U.C.N.","U.T.E.S.","I.U.C.N.","I.B.W.C."," W.W.F."]}
    c23={"Who among the following is regarded as \nthe leader of 'Chipko Movement'?":["Sundarlal Bahuguna","Medha Patkar","Baba Amte","Sundarlal Bahuguna","Kiran Bedi"]}
    c24={"'Montreal Protocol' is related to -":["Chlorofluorocarbon","White Tiger","Chlorofluorocarbon","Water pollution","Agriculture"]}
    c25={"What is the rank of India in silk production in the world?":["Second","First","Second","Third","Fourth"]}
    c26={"According to Census 2011, of the total population \nof Madhya Pradesh the percentage of rural population is -":["72.4","72.4","67.8","75.4","62.8"]}
    c27={" Birsinghpur Hydel Power Station is situated in \nwhich of the following districts?":["Umaria","Umaria","Jabalpur","Balaghat","Shahdol"]}
    c28={"National Rural Health Mission has been\n launched in the country in ":["2005","2003","2005","2007","2009"]}
    c29={"July 11, every year is observed as the -":["World Population Day","World Population Day","World Literacy Day","World Heart Day","Malala Day"]}
    c30={"The currency of the 'Republic of Maldives' is -":["Rufiyaa","Riyal","Rupee","Ringgit","Rufiyaa"]}
    d=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30]
    dic=[]
    while(len(dic)!=15):
         m=random.choice(d)
         if m not in dic:
              dic.append(m)
    return dic
               
def bank():
    d1={"Banking functions centrally controlled by the :":["RBI","Central Bank","RBI","SBI","Both [B] and [C]"]}
    d2={"The ratio between cash in hand and total \nassets maintained by the banks is called :":["SLR (Statutory Liquid Ratio)","SBR (Statutory Bank Ratio)","SLR (Statutory Liquid Ratio)","CBR (Central Bank Reserve)","CLR (Central Liquid Reserve)"]}
    d3={"What is ‘Repo rate’?":["is the rate at which \nthe RBI lends to banks","is the rate at which \nthe RBI lends to State Government","is the rate at which \nthe International aid agencies lend to RBI","is the rate at which \nthe RBI lends to banks","is the rate at which the \nbanks lends to RBI"]}
    d4={"What is the apex organisation of \nIndustrial Finance in India ?":["Industrial Development Bank of India","Industrial Finance Corporation","Industrial Credit and Investment corporation of India","Industrial Development Bank of India","None of these"]}
    d5={"Which of the following is called \na ‘banker’s cheque’ ?":["Banker's draft","Demand draft","Debit card","Pay order","Banker's draft"]}
    d6={"The place where bankers meet and \nsettle their mutual claims and accounts is known as :":["Clearing House","Treasury","Clearing House","Collecting Centre","Dumping Ground"]}
    d7={"What is the ideal of designing \nRegional rural Banks ?":["Help the targetted \ngroups","Work on basics of \ncommercial banks","Help the targetted \ngroups","Keep lending rates lower \nthan cooperative institutions","Work on innovative and \nadaptive ideals"]}
    d8={"Identify the punishable offence \nby a Bank Account holder ?":["If a cheque drawn by him is dishonoured \nfor insufficiency of funds in his account","If a cheque is not crossed","If a post dated cheque is issued","If a cheque drawn by him is dishonoured \nfor insufficiency of funds in his account","Issuing a cheque \nwithout signature"]}
    d9={"What is a Cross cheque ?":["which can be encashed \nonly through a bank","which can be encashed \nonly by the drawee","which can be encashed \nonly through a bank","which can be encashed \nonly at the State Bank of India","which can be encashed \nonly after it has been transferred to \nanother person"]}
    d10={"Which of the following rural \nbank is named after a river ?":["Varada Grameen Bank","Prathama Bank","Varada Grameen Bank","Thar Anchalik Grameen Bank","Aravali Kshetriya Grameen Bank"]}
    d11={"What is Scheduled Bank in India ?":["It is included in the II Schedule \nof Reserve Bank of India Act"," It is included in the II Schedule \nof Banking Regulation Act.","It is included in the II Schedule \nof Constitution","It is included in the II Schedule of \nReserve Bank of India Act","None of these above"]}
    d12={"What is the animal on the \ninsignia of the RBI ?":["Tiger","Lion","Tiger","Panther","Elephant"]}
    d13={"The number of Banks nationalised since 1969 is :":["14","8","12","14","20"]}
    d14={"Which of the following is the Banker's Bank :":["RBI","RDBI","RBI","SBI","UBI"]}
    d15={"What is the largest Public Sector Bank in India ?":["SBI","Central Bank","SBI","Punjab National Bank","None of these above"]}
    d16={"In which year the Reserve Bank of \nIndia was taken over by the Government ?":["1948","1945","1948","1952","1956"]}
    d17={"In Capital Market SRO stands for :":["Self-Regulatory Organisations","Self-Regulatory Organisations","Small Revenue Operations","Securities Roll-back Operations","Securities Regulatory Organisations"]}
    d18={"Terms Bull market and Bear market is \nassociated with which branch of commercial activity ?":["Share Market","Foreign Trade","Banking","Share Market","Manufacturing"]}
    d19={"Which of the following is not an \naffiliate of the Reserve Bank of India ?":["Unit Trust Of India","Unit Trust Of India","Deposit insurance Corporation","Agricultural Refinance Corporation","The Industrial Development Bank of India"]}
    d20={"Which of the following is not \nan asset held by commercial banks ?":["Current account deposits","Bills of exchange","Current account deposits","Money lent at short notice","Credit balances with the Reserve Bank"]}
    d21={"Which of the following provides the largest \npart of the demand for loanable funds in India ?":["Corporate businesses","Farmers","Private-house purchasers","Hire-purchase borrowers","Corporate businesses"]}
    d22={"Who amongst the following was never a \nGovernor of the RBI ?":["Arup Roy Choudhury","Y. V. Reddy","Bimal Jalan","Arup Roy Choudhury","Rangarajan"]}
    d23={"Private Sector Mutual Funds in \nIndia were permitted in":["1993","2001","1994","1993","1964"]}
    d24={"Which one of the following is not a \nfeature of Limited Liability Partnership firm ?":["Partners should be \nless than 20","Partnership and management need \nnot be separate","Partners should be \nless than 20","It is a corporate body \nwith perpetual succession","Internal governance may be \ndecided by mutual agreement among partners"]}
    d25={"Stock Exchanges play a role in an \neconomy which may be termed as":["Useful but need strict \nregulation","Hardly useful","Harmful to proper \ncapital markets","Useful but need strict \nregulation","A very important segment to \nregulate inflation"]}
    d26={"The oldest stock exchange of India is :":["Bombay Stock Exchange","Bombay Stock Exchange","Bangalore Stock Exchange","Hyderabad Stock Exchange","Ahmadabad Stock Exchange"]}
    d27={"In 1921, the Presidency Banks of Bengal, Madras and \nBombay were nationalized to give birth to:":["State Bank of India""Syndicate Bank","Punjab and Sindh Bank","Punjab National Bank","State Bank of India"]}
    d28={"Which bank gives long term loan to famers ?":["Land Development Bank","SBI","NABARD","Rural Banks","Land Development Bank"]}
    d29={"Which of the following combinations are correct ?":["RRB --- Agricultural finance","NABARD --- Industrial Loans","RBI --- Long term finance","RRB --- Agricultural finance","IDBI --- Short term loans"]}
    d30={"Debenture holders of company are its:":["Creditors","Creditors","Debtors","Directors","Shareholders"]}
    d=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30]
    dic=[]
    while(len(dic)!=15):
         m=random.choice(d)
         if m not in dic:
              dic.append(m)
    return dic
               
def defence():
    a30={"Which company conferred with the title of world's \nbiggest planemaker for the seventh straight year?":["Boeing","Bombardier","Boieng","Airbus","Tupolev"]}
    a1={"India successfully test-fired its nuclear-capable \nlong-range ballistic missile Agni-IV,with a strike range of":["4,000 km","1,800 km","2,200 km","3,600 km","4,000 km"]}
    a2={"For which country, US has regulator Federation of Aviation\n Administration (FAA) retained the highest aviation safety rank?":["India","Spain","Canada","India","Turkey"]}
    a3={"Information Fusion Centre (IFC) for the Indian \nOcean Region (IOR) will be inagurated by":["Indian Navy","India Air Force","Indian Army","Indian Navy","Indian Coast Guard"]}
    a4={"Which aircraft was tested by Indian Air Force \n(IAF) and flew with blended bio-jet fuel?":["An-32 transport aircraft","An-32A transport aircraft","An-32G transport aircraft","An-32 transport aircraft","An-34A transport aircraft"]}       
    a5={"The Nigerian military has recently lifted ban on\n this UN agency operations in ravaged northeast.":["UNICEF","UNICEF","UNIDO","WHO","UNESCO"]}
    a6={"Which of the following system was launched by \nIndian Navy to rescue crew members from submarines?":["Deep Submergence Rescue Vehicle (DSRV)","Long Submergence Rescue Vehicle (LSRV)","Medium Submergence Rescue Vehicle (MSRV)","Deep Submergence Rescue Vehicle (DSRV)","Ultrasonic Submergence Rescue Vehicle (USRV)"]}
    a7={"Who conducted an exercise Cross Bow 18 ?":["Indian Air Force","Indian Army","Indian Air Force","Indian Navy","Indian Coast Guard"]}
    a8={"2018 Military Literature Festival\n was held in __________.":["Chandigarh","Pune","Hyderabad","New Delhi","Chandigarh"]}
    a9={"The 10th Edition of the bilateral exercise between \nthe Indian Navy and Russian Federation Navy begins in __________.":["Visakhapatnam","Visakhapatnam","Kolkata","Cochin","Chennai"]}
    a10={"Which of the following is the India's \nSecond Inland Water Transport origin destination pair for containerized \ncargo movement on National Waterway-1?":["Kolkata-Patna","Paradip-Cuttack","Kolkata-Patna","Mumbai-Chennai","Panaji-Kochi"]}
    a11={"The Indian Coast Guard has conducted \nthe Regional Level Marine Oil Pollution \nResponse Exercise titled 'Clean Sea - 2018' __________.":["Port Blair","Kolkata Port","Kandla Port","Port Blair","Paradip Port"]}
    a12={"Which of the following theatre level\n maritime war exercise will be conducted \nby Indian Navy?":["TROPEX","Sagar Kavach,Avardhan","Sea Vigil","TROPEX"]}
    a13={"SHINYUU Maitri-18 is a bilateral air \nexercise between India and this country.":["Japan","Japan","Singapore","Brunei","Thailand"]}
    a14={"The 7th India and China joint military \nexercises - 'Hand in Hand' will commence from _______.":["December 10","December 8","December 10","December 13","December 18"]}
    a15={"KONKAN is a Naval exercise between \nwhich two countries?":["India and the United Kingdom","India and Bangladesh","Bangladesh and Myanmar","United Kingdom and China","India and the United Kingdom"]}
    a16={"With which country, India signed USD \n500 million deal for construction of two missile frigates \nin Goa for the Indian Navy?":["Russia","France","Russia","Japan","Germany"]}
    a17={"The joint military exercise between India and the \nUnited States which commenced in Jaipur \non 19 November 2018 is;":["Vajra Prahar","Ajeta Warrior","Vajra Prahar","Hand in Hand","Sampriti"]}
    a18={"The joint military exercise between India and \nRussia EXERCISE INDRA 2018 was conducted in __________, Uttar Pradesh.":["Jhansi","Jhansi","Lucknow","Kanpur","Allahabad"]}
    a19={"2018 is decided as the Year of the Disabled Soldier by;":["Indian Army","Indian Army","Indian Navy","Indian Air Force","Indian Coast Guard"]}
    a20={"Samudra Shakti is a Bilateral Exercise between which two countries?":["India and Indonesia","South Korea and India","China and France","India and Indonesia","Russia and Japan"]}
    a21={"SIMBEX, the 25th edition of the India-Singapore \nbilateral naval exercise is being held in which port?":["Port Blair","Lakshadweep","Neil Island","Port Blair","Visakhapatnam"]}
    a22={"US has granted a waiver from sanctions for New Delhi's \nrole in the development of Chabahar port in __________.":["Iran","China","Japan","Iran","Maldives"]}
    a23={"The Indian Army will induct a new artillery guns and equipment, \nincluding K9 Vajra and M777 howitzers at __________, in Maharashtra.":["Nashik","Thane","Pune","Nagpur","Nashik"]}
    a24={"Which port plans to host an edible oil refinery to \nmaximise revenue and ensure captive cargo?":["Jawaharlal Nehru Port Trust","Jawaharlal Nehru Port Trust","Kandla Port","Mormugao Port","Paradip Port"]}
    a25={"European Intervention Initiative a joint military \nforce was launched in __________.":["Paris","Paris","Rome","London","Berlin"]}
    a26={"Indian Coast Guard has launched a new offshore \npatrol vessel in Chennai, recently. It was named as;":["ICGS Varaha","ICGS Samudra","ICGS Rani Abbaka","ICGS Aadesh","ICGS Varaha"]}
    a27={"India's first nuclear-powered submarine \ncompleted its first deterrence patrol recently. \nThe name of the Submarine is;":["INS Arihant","INS Arihant","INS Kalvari","INS Sindhuvijay","INS Arighat"]}
    a28={"The world's largest marine sanctuary planned to be built in __________.":["Antarctica","Netherland","Iceland","Antarctica","Cyprus"]}
    a29={"The 2nd successful night trial of Agni-1 ballistic \nmissile was conducted in which coast?":["Odisha Coast","Odisha Coast","Andhra coast","Malabar Coast","Konkan coast"]}
    d=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30]
    dic=[]
    while(len(dic)!=15):
         m=random.choice(d)
         if m not in dic:
              dic.append(m)
    return dic

def govtvalidate(idno):
     screen("Government Jobs Exam","govtjobs.png",gov(),idno,"govt")
def teachingvalidate(idno):
     screen("Teaching Exam","teaching.png",teaching(),idno,"teaching")
def bankvalidate(idno):
     screen("Bank Exam","bank&insurance.png",bank(),idno,"bank")
def defencevalidate(idno):
     screen("Defence Exam","defence.png",defence(),idno,"defence")

def checkanswers(qn,ans,idno,exm):
     global stp
     stp=1
     for i in range(0,len(ans)):
          ans[i]=ans[i].get()
     mrk=0
     for i in range(0,len(qn)):
          if ans[i]==0:
               mrk=mrk
          elif list(qn[i][list(qn[i].keys())[0]])[0]==list(qn[i][list(qn[i].keys())[0]])[ans[i]]:
               mrk=mrk+1
          else:
               mrk=mrk
     con.execute("update garv set "+exm+"="+str(mrk)+" where id="+idno)
     cu.commit()
     messagebox.showinfo("GARV","Record Stored Sucessfully.")
     profilpg(idno)
               
qno=0
def nxtbtn(qn,r1,r2,r3,r4,lf,qlst,nxt,bk,ans,sub):
     global qno
     if qno==len(qlst)-1:
          nxt.config(state="disable")
          bk.config(state="active")
          sub.config(state="active")
     else:
          nxt.config(state="active")
          bk.config(state="active")
          sub.config(state="disable")
          qno=qno+1
     #q=qlst[qno]
     qn.config(text=str(qno+1)+". "+list(qlst[qno].keys())[0])
     r1.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[1],variable=ans[qno],value=1)
     r2.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[2],variable=ans[qno],value=2)
     r3.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[3],variable=ans[qno],value=3)
     r4.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[4],variable=ans[qno],value=4)
    
def bkbtn(qn,r1,r2,r3,r4,lf,qlst,bk,nxt,ans,sub):
     global qno
     if qno==0:
          bk.config(state="disable")
          nxt.config(state="active")
          sub.config(state="disable")
     else:
          bk.config(state="active")
          nxt.config(state="active")
          sub.config(state="disable")
          qno=qno-1
     #q=qlst[qno]
     qn.config(text=str(qno+1)+". "+list(qlst[qno].keys())[0])
     r1.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[1],variable=ans[qno],value=1)
     r2.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[2],variable=ans[qno],value=2)
     r3.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[3],variable=ans[qno],value=3)
     r4.config(text=list(qlst[qno][list(qlst[qno].keys())[0]])[4],variable=ans[qno],value=4)
    
stp=0
def start(ti,ll,t,qlst,ans,idno,exm):
    global stp
    ll.config(text=str(ti))
    if ti==0:
        messagebox.showwarning("Alert","Times Up...!!!")
        checkanswers(qlst,ans,idno,exm)
        profilpg()
    elif stp==1:
        messagebox.showinfo("GARV","OK DONE...")
        stp=0
    else:
        t.after(1000,start,ti-1,ll,t,ans,qlst,idno,exm)
def screen(name,pic,qlst,idno,exm):
    t=Toplevel()
    f3=Frame(t)
    f4=Frame(t)
    f5=Frame(t)
    t.title("GARV Online Exam")
    c=Canvas(f5,height=100,width=200)
    tl=Label(c,text="Seconds",font=("Geometr415 Blk BT",40),fg="red")
    tl.grid(row=0)
    c.grid(row=0)
    count=Label(f5,text="Countdown",font=("Geometr415 Blk BT",15),fg="red").grid(row=1)
    exnm=Label(f4,text=name,font=("Geometr415 Blk BT",30)).grid(row=0)
    exlogo=tkinter.PhotoImage(file=pic)
    exlog=Label(f3,image=exlogo).grid(row=0)
    f3.grid(row=0)
    f4.grid(row=0,column=1)
    f5.grid(row=0,column=2)
    #qlst=govt()
    lf=LabelFrame(t,text="Attemp all Questions",font=("Geometr415 Blk BT",20))
    global qno
    ans=[]
    for i in range(0,len(qlst)):
         ans.append(IntVar())
    qn=Label(lf,text=str(qno+1)+". "+list(qlst[qno].keys())[0],font=("Geometr415 Blk BT",22))
    qn.grid(row=0,columnspan=2,stick=W)
    r1=Radiobutton(lf,text=list(qlst[qno][list(qlst[qno].keys())[0]])[1],font=("Geometr415 Blk BT",22),variable=ans[qno],value=1)
    r1.grid(row=1,stick=W)
    r2=Radiobutton(lf,text=list(qlst[qno][list(qlst[qno].keys())[0]])[2],font=("Geometr415 Blk BT",22),variable=ans[qno],value=2)
    r2.grid(row=1,column=1,stick=W)
    r3=Radiobutton(lf,text=list(qlst[qno][list(qlst[qno].keys())[0]])[3],font=("Geometr415 Blk BT",22),variable=ans[qno],value=3)
    r3.grid(row=2,stick=W)
    r4=Radiobutton(lf,text=list(qlst[qno][list(qlst[qno].keys())[0]])[4],font=("Geometr415 Blk BT",22),variable=ans[qno],value=4)
    r4.grid(row=2,column=1,stick=W)
    lf.grid(row=3,columnspan=3)
    nextpic=tkinter.PhotoImage(file="next.png")
    prepic=tkinter.PhotoImage(file="pre.png")
    f2=Frame(t,bd=0,width=700)
    submit=tkinter.PhotoImage(file="submit.png")
    sub=Button(f2,text="Submit",image=submit,bd=0,state="disable",command=lambda:checkanswers(qlst,ans,idno,exm))
    sub.grid(row=0,column=1,padx=10,pady=10)
    bk=Button(f2,text="Back",image=prepic,bd=0,command=lambda:bkbtn(qn,r1,r2,r3,r4,lf,qlst,bk,nxt,ans,sub))
    bk.grid(row=0,stick=E,padx=10,pady=10)
    nxt=Button(f2,text="Next",image=nextpic,bd=0,command=lambda:nxtbtn(qn,r1,r2,r3,r4,lf,qlst,nxt,bk,ans,sub))
    nxt.grid(row=0,column=2,stick=W,padx=10,pady=10)
    f2.grid(row=4,columnspan=3)
    t.geometry("800x400")
    start(120,tl,t,qlst,ans,idno,exm)
    t.mainloop()
#Exam Selection
def exmopt(idno):
     t=Toplevel()
     t.title("GARV Exams")
     teaching=tkinter.PhotoImage(file="teaching.png")
     medical=tkinter.PhotoImage(file="medical.png")
     govt=tkinter.PhotoImage(file="govtjobs.png")
     jee=tkinter.PhotoImage(file="jee.png")
     bank=tkinter.PhotoImage(file="bank&insurance.png")
     defence=tkinter.PhotoImage(file="defence.png")
     l2=Label(t,text="Select the Exam You want to give",font=("Geometr415 Blk BT",20),fg="blue")
     l2.grid(row=0,columnspan=4)
     tb=Button(t,text="Teaching",image=teaching,bd=0,command=lambda:teachingvalidate(idno))
     tb.grid(row=1,padx=10)
     lt=Label(t,text="Detail of Teaching Exams")
     lt.grid(row=1,column=1,padx=10)
     mb=Button(t,text="Medical Entrance",image=medical,bd=0)
     mb.grid(row=1,column=2,padx=10)  
     mt=Label(t,text="Detail of Medical Exams")
     mt.grid(row=1,column=3,padx=10)
     gb=Button(t,text="Govt Exams",image=govt,bd=0,command=lambda:govtvalidate(idno))
     gb.grid(row=2,padx=10)
     gt=Label(t,text="Detail of Govt Exams")
     gt.grid(row=2,column=1,padx=10)
     db=Button(t,text="Defence",image=defence,bd=0,command=lambda:defencevalidate(idno))
     db.grid(row=2,column=2,padx=10)
     dt=Label(t,text="Detail of Defence Exams")
     dt.grid(row=2,column=3,padx=10)
     bb=Button(t,text="Bank",image=bank,bd=0,command=lambda:bankvalidate(idno))
     bb.grid(row=3,padx=10)
     bt=Label(t,text="Detail of Bank Exams")
     bt.grid(row=3,column=1,padx=10)
     jb=Button(t,text="JEE",image=jee,bd=0)
     jb.grid(row=3,column=2,padx=10)
     jt=Label(t,text="Detail of JEE Exams")
     jt.grid(row=3,column=3,padx=10)
     t.mainloop()
def contactus():
     t5=tkinter.Tk()
     ll=Label(t5,text="email=garv@gmail.com\nmob=9876543210",font=("Geometr415 Blk BT",12))
     ll.grid(row=0)
     t5.mainloop()
def aboutus():
     t4=tkinter.Tk()
     l=Label(t4,text="""\tGARV Competitive Exams\n\tThis Is Desktop application created by 4 college Students as their group Project.\nThey are Gaurav S. ,Aditya S. ,Rahul Y. & Viren M. In this Aplication \nStudents can be able to give their Online Exams Directly \nThough the Home From their PC & with direct Registeration """,justify="left",font=("Geometr415 Blk BT",12))
     l.grid(row=0)
     t4.mainloop()
def profilpg(idn):
     con.execute("select * from garv where id="+idn)
     data=con.fetchall()[0]
     t3=Toplevel()
     t3.title("Welcome to GARV")
     profile=tkinter.PhotoImage(file="profile.png")
     l=Label(t3,image=profile).grid(row=0)
     ilab=Label(t3,text=data[1]+" "+data[2]+" "+data[3]+"\nID No:-"+data[0]+"\nDoB:-"+data[4]+"\nEmail ID:-"+data[5]+"\nContact No:-"+str(data[6]),justify=LEFT,font=("Geometr415 Blk BT",18)).grid(row=1)
     
     #Option Menu
     option=tkinter.PhotoImage(file="option.png")
     ob=Menubutton(t3,image=option,bd=0)
     ob.menu=Menu(ob,tearoff=0)
     ob["menu"]=ob.menu
     ob.menu.add_checkbutton(label="About Us",command=aboutus)
     ob.menu.add_checkbutton(label="Contact Us",command=contactus)
     ob.grid(row=0,column=2,stick=NE)

     #list of Already appeared exams
     exmlf=LabelFrame(t3,text="Performance",font=("Geometr415 Blk BT",18))
     d={"Teaching Exam":data[9],"Medical Exam":data[10],"Government Job Exam":data[11],"Defence Exam":data[12],"Banking":data[13],"JEE & BITSAT":data[14]}
     b=0
     for i in d:
         if not(d[i]):
             continue
         else:
             Label(exmlf,text=i,font=("Geometr415 Blk BT",18)).grid(row=b)
             Label(exmlf,text=str(d[i])+"/15 Marks",font=("Geometr415 Blk BT",18)).grid(row=b,column=1)
             b=b+1
     exmlf.grid(row=2,columnspan=3)
     #Button to give more exam
     givexm=tkinter.PhotoImage(file="giveexm.png")
     eg=Button(t3,text="Give Exam",image=givexm,bd=0,command=lambda:exmopt(data[0]))
     eg.grid(row=5)
     t3.mainloop()
#idn=5717
#profilpg(str(idn))



####################################profile page end##########################################################################################################################################

#Login Validation
def loginvalidate(un,ps):
    con.execute("select id from garv where email='"+un+"' and pswrd='"+ps+"';")
    messagebox.showinfo("Welcome","Login Sucessfull")
    #print(con.fetchall()[0][0])
    profilpg(con.fetchall()[0][0])

#show hide Validation for Login Page
def unhide(pe,sh,show):
     show.config(file="hide.png")
     pe.config(show="")
     sh.config(command=lambda:lhide(pe,sh,show))

def lhide(pe,sh,show):
     show.config(file="show.png")
     pe.config(show="*")
     sh.config(command=lambda:unhide(pe,sh,show))
#validate Forget Password
def fpvalidate(usn,idn):
    if len(usn)!=0 or len(idn)!=0:
        try:
            con.execute("select email from garv where email='"+usn+"';")
            em=con.fetchall()[0][0]
            print(em)
            if len(em)!=0:
                con.execute("select pswrd from garv where id='"+idn+"';")
                pss=con.fetchall()[0][0]
                messagebox.showinfo("Alert","Your Password is "+pss)
                pss=0
            else:
                messagebox.showinfo("Alert","Invalid Email")
        except mysql.connector.Error:
            messagebox.showerror("Alert","Invalid Email ID")
    else:
        messagebox.showerror("Alert","No values Inserted")


#Forget Password
def frgtpswd():
     tt=Toplevel()
     tt.title("GARV")
     username=tkinter.PhotoImage(file="username.png")
     lab=Label(tt,image=username)
     lab.grid(row=0)
     lfusn=LabelFrame(tt,text="Username")
     usn=Entry(lfusn,bd=0)
     usn.grid(row=0)
     lfusn.grid(row=0,column=1)
     lfid=LabelFrame(tt,text="ID Number")
     idn=Entry(lfid,bd=0)
     idn.grid(row=0)
     lfid.grid(row=1,column=1)
     submit=tkinter.PhotoImage(file="submit.png")
     sb=Button(tt,text="Submit",image=submit,bd=0,command=lambda:fpvalidate(usn.get(),idn.get()))
     sb.grid(row=2)
     tt.mainloop()
#Login Page
def loginf():
     t1=Toplevel()
     t1.title("Login in GARV")
     logo=tkinter.PhotoImage(file="loginlogo.png")
     forget=tkinter.PhotoImage(file="forget.png")
     login=tkinter.PhotoImage(file="loginmini.png")
     show=tkinter.PhotoImage(file="show.png")
     back=tkinter.PhotoImage(file="back.png")
     username=tkinter.PhotoImage(file="username.png")
     password=tkinter.PhotoImage(file="pswrd.png")
     ln=Label(t1,image=logo)
     ln.grid(row=0,columnspan=3)
     ul=Label(t1,text="User Name",font=("Geometr415 Blk BT",16),image=username)
     ul.grid(row=1)
     lfue=LabelFrame(t1,text="Username",font=("Geometr415 Blk BT",12))
     ue=Entry(lfue,bd=0);ue.grid(row=0)
     lfue.grid(row=1,column=1)
     pl=Label(t1,text="Password",font=("Geometr415 Blk BT",16),image=password)
     pl.grid(row=2)
     lfpe=LabelFrame(t1,text="Password",font=("Geometr415 Blk BT",12))
     pe=Entry(lfpe,bd=0,show="*");pe.grid(row=0)
     lfpe.grid(row=2,column=1)
     sh=Button(t1,bd=0,image=show,command=lambda:unhide(pe,sh,show))
     sh.grid(row=2,column=2)
     fp=Button(t1,bd=0,text="Forget Password",image=forget,command=frgtpswd)
     fp.grid(row=3,columnspan=3)
     b=Button(t1,text="Login",bd=0,image=login,command=lambda:loginvalidate(ue.get(),pe.get()))
     b.grid(row=4,column=1,columnspan=2)
     bb=Button(t1,text="Back",bd=0,image=back)
     bb.grid(row=4)
     #t1.geometry("500x500")
     t1.mainloop()

#show hide functions for register page
def show2(pe,pe2,sh,show):
     show.config(file="hide.png")
     pe.config(show="")
     pe2.config(show="")
     sh.config(command=lambda:hide(pe,pe2,sh,show))

def hide(pe,pe2,sh,show):
     show.config(file="show.png")
     pe.config(show="*")
     pe2.config(show="*")
#show hide Validation for Login Page
def unhide(pe,sh,show):
     show.config(file="hide.png")
     pe.config(show="")
     sh.config(command=lambda:lhide(pe,sh,show))

def lhide(pe,sh,show):
     show.config(file="show.png")
     pe.config(show="*")
     sh.config(command=lambda:unhide(pe,sh,show))
#home page
c=0
def home():
     global c
     t=tkinter.Tk()
     t.iconbitmap(r'icon.ico')
     t.title("Welcome to GARV")
     #Importing images
     img=tkinter.PhotoImage(file="g2.png")
     login=tkinter.PhotoImage(file="login.png")
     register=tkinter.PhotoImage(file="register.png")
     #Logo
     la=Label(t,image=img)
     la.grid(row=0)
     nul1=Label(t,text="\n").grid(row=1)
     lb=Button(t,text="Login",bd=0,image=login,command=loginf)       #Login Button
     lb.grid(row=2,sticky=W+E)
     nul1=Label(t,text="\n").grid(row=3)
     #import registerpg as r
     lr=Button(t,text="Register",bd=0,image=register,command=regpg)    #Registor Button
     lr.grid(row=4,sticky=W+E)
     t.geometry("500x500")
     t.mainloop()
#show hide functions for register page
def show2(pe,pe2,sh,show):
     show.config(file="hide.png")
     pe.config(show="")
     pe2.config(show="")
     sh.config(command=lambda:hide(pe,pe2,sh,show))

def hide(pe,pe2,sh,show):
     show.config(file="show.png")
     pe.config(show="*")
     pe2.config(show="*")
     sh.config(command=lambda:show2(pe,pe2,sh,show))
#Data Validation at the time of registrationw="*")
     sh.config(command=lambda:show2(pe,pe2,sh,show))
#Data Validation at the time of registration
#Id generate
def generateid():
    idlst=[]
    con.execute("select id from GARV;")
    ids=con.fetchall()
    for i in ids:
        idlst.append(i)
    idno=random.randint(0000,9999)
    idno=str(idno)
    if len(idno)<4:
        for i in range(0,(4-len(idno))):
            idno="0"+idno
    if idno not in idlst:
        return idno
    else:
        idlst.clear()
        generateid()
#Registor validation
def datavalidate(name,middle,surname,dob,email,cont,ps1,ps2,qlfn):
     sysdate=time.strftime("%y")
     if len(name)!=0 and len(middle)!=0 and len(surname)!=0 and len(email)!=0 and len(qlfn)!=0:
          if len(ps1)>5:
               if ps1==ps2:
                   if dob[-2:]!=sysdate:
                       if len(cont)==10:
                            try:
                                cont=int(cont)
                                messagebox.askyesno("Alert","Are you sure that you have Inserted Correct Data\nBecause once inserted cannot be changed & same data will be shown on your Result.")
                                if messagebox.askyesno!=False:
                                    try:
                                        idn=generateid()
                                        con.execute("insert into GARV values('"+idn+"','"+name+"','"+middle+"','"+surname+"','"+dob+"','"+email+"',"+str(cont)+",'"+ps1+"','"+qlfn+"',NULL,NULL,NULL,NULL,NULL,NULL);")
                                        cu.commit()
                                        messagebox.showinfo("Alert","Registration Sucessfully.\n Your ID number is "+idn)
                                    except mysql.connector.Error:
                                        messagebox.showerror("Alert","Opps something went wrong....!!!!\n Try again")                
                                else:
                                    messagebox.showinfo("Alert","Registration Cancled Sucessfully.")
                            except ValueError:
                                messagebox.showerror("Alert","Invalid Contact Number.")
                       else:
                            messagebox.showerror("Alert","Contact number should be of 10 Digits only.")
                   else:
                        messagebox.showerror("Alert","Please Select Correct Date of Birth.")
               else:
                    messagebox.showerror("Alert","Password does'nt Match.")
          else:
               messagebox.showerror("Alert","Password should Contain atleast 6 Characters")
     else:
          messagebox.showerror("Alert","There should not be any Empty Data")
#Register page
def regpg():
     t2=Toplevel()
     t2.title("GARV Registor")
     l=Label(t2,text="Enter the Following Detail to Registor :-",font=("Cooper Black",20),fg="Brown")
     l.grid(row=0,columnspan=3)
     #Name Details
     l1=LabelFrame(t2,text="Your Name",font=("Geometr415 Blk BT",12),width=250)
     l1.grid(row=1)
     l2=LabelFrame(t2,text="Middle Name",font=("Geometr415 Blk BT",12),width=250)
     l2.grid(row=1,column=1)
     l3=LabelFrame(t2,text="Surname",font=("Geometr415 Blk BT",12),width=250)
     l3.grid(row=1,column=2)
     r1=Entry(l1,bd=0)
     r1.grid(row=0)
     r2=Entry(l2,bd=0)
     r2.grid(row=0)
     r3=Entry(l3,bd=0)
     r3.grid(row=0)
     #Date of Birth
     frm=Frame(t2,bd=2)
     l4=Label(frm,text="Select Date of Birth ",font=("Geometr415 Blk BT",20));l4.grid(row=0)
     dt=DateEntry(frm)
     dt.grid(row=0,column=1)
     frm.grid(row=3,columnspan=3)
     #Email
     email=tkinter.PhotoImage(file="email.png")
     elab=Label(t2,text="E-mail ID",font=("Geometr415 Blk BT",50),image=email).grid(row=4)
     lfee=LabelFrame(t2,text="Email ID",font=("Geometr415 Blk BT",12),width=250)
     ee=Entry(lfee,bd=0);ee.grid(row=0)
     malst=["@gmail.com","@yahoo.com","@hotmail.com","@orchat.com"]
     extmal=StringVar();extmal.set(malst[0])
     malopt=OptionMenu(lfee,extmal,*malst);malopt.grid(row=0,column=1)
     lfee.grid(row=4,column=1)
     #Contact
     contact=tkinter.PhotoImage(file="contact.png")
     clab=Label(t2,text="Contact",font=("Geometr415 Blk BT",20),image=contact).grid(row=5)
     lfce=LabelFrame(t2,text="Contact",font=("Geometr415 Blk BT",12),width=250)
     cel=Label(lfce,text="+91");cel.grid(row=0)
     ce=Entry(lfce,bd=0);ce.grid(row=0,column=1)
     lfce.grid(row=5,column=1)
     #Password
     create=tkinter.PhotoImage(file="createprd.png")
     p1lab=Label(t2,text="Create New Password",font=("Geometr415 Blk BT",20),image=create).grid(row=6)
     lfp1e=LabelFrame(t2,text="Create New Password",font=("Geometr415 Blk BT",12),width=250)
     p1e=Entry(lfp1e,show="*",bd=0);p1e.grid(row=0)
     lfp1e.grid(row=6,column=1)
     #Confirm Password
     confirm=tkinter.PhotoImage(file="confmpswrd.png")
     p2lab=Label(t2,text="Confirm Password",font=("Geometr415 Blk BT",20),image=confirm).grid(row=7)
     lfp2e=LabelFrame(t2,text="Confirm Password",font=("Geometr415 Blk BT",12),width=250)
     p2e=Entry(lfp2e,show="*",bd=0);p2e.grid(row=0)
     lfp2e.grid(row=7,column=1)
     #Show Hide Password
     show=tkinter.PhotoImage(file="show.png")
     sohid=Button(t2,text="Show",image=show,command=lambda:show2(p1e,p2e,sohid,show),bd=0);sohid.grid(row=6,rowspan=2,column=2)
#Qualification
     qualification=tkinter.PhotoImage(file="qualification.png")
     l5=Label(t2,text="Select Qualification ",font=("Geometr415 Blk BT",20),image=qualification)
     l5.grid(row=8)
     lfqmnu=LabelFrame(t2,text="Qualification",font=("Geometr415 Blk BT",12),width=250)
     qlfc=["10th Pass","12th Commers Pass","12th Science","12th Arts","B.COM","BSc.IT","BSc.CS","BAF"]
     dflt=StringVar();dflt.set(qlfc[0])
     qmnu=OptionMenu(lfqmnu,dflt,*qlfc);qmnu.grid(row=0)
     lfqmnu.grid(row=8,column=1)
     #notice
     lfno=LabelFrame(t2,text="Notice",font=("Geometr415 Blk BT",10),highlightcolor="red",fg="red")
     notl=Label(lfno,text="1.Enter the Correct Detail.\n2.Once Registration done cannot change Details.\n3.Same detail will come on Result.\n4.Username is Email ID while Loging In.",font=("Geometr415 Blk BT",10),fg="red",justify=LEFT)
     notl.grid(row=0)
     lfno.grid(row=9,columnspan=3)
     #Final Buttons
     submit=tkinter.PhotoImage(file="submit.png")
     b=Button(t2,text="Submit",bd=0,image=submit,command=lambda:datavalidate(r1.get(),r2.get(),r3.get(),dt.get(),ee.get()+extmal.get(),ce.get(),p1e.get(),p2e.get(),dflt.get()))
     b.grid(row=10,column=2)
     back=tkinter.PhotoImage(file="back.png")
     b1=Button(t2,text="Back",bd=0,image=back);b1.grid(row=10)
     t2.geometry("590x500")
     t2.mainloop()
     
home()
