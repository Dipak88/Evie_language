import pyttsx3
import speech_recognition as sr
import datetime
from datetime import datetime
import os 
import re
from PIL import Image
from time import sleep
import ecapture as ec
from gtts import gTTS
import playsound
from googletrans import Translator

d1 = datetime.now()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('voice',50)


#def trans(audio):
    #engine.say(audio)
    #engine.runAndWait()
    
def speak(audioString):
    print(audioString)
    date_string = d1.strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts = gTTS(text=audioString, lang='hi')
    tts.save(filename)
    playsound.playsound(filename)
    #os.system("start audio.mp3")
    sleep(1)
    print(filename)
    os.remove(filename)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5, phrase_time_limit=20)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def trans(text):
    t1=Translator()
    r=t1.translate(text,dest='hindi')
    print(r.text)
    speak(r.text)



#########################

class SelectProfession:
    trans("please select your profession")
    def employee(self):
        trans("please enter the personal details")
        trans("please enter your Name")
        name =takeCommand().lower()
        name = input("Enter the name : " +name)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please enter the residential address")
        address = takeCommand().lower()
        address = input("enter the residential address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip  code")
        zip_code = takeCommand().lower()
        zip_code = input("enter the zip code" + zip_code)
        trans("please enter pan card number")
        Pancard = takeCommand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)

        trans("please enter adhar card number")
        adharcard = takeCommand().lower()
        if len(adharcard) == 12 :
            adharcard = int(input("Enter the adharcard number : "+adharcard))
        trans("sorry sir adhar card number is invalid please check it")    
        trans("please enter email")
        email = takeCommand().lower()
        email = input("Enter the email : "+email)
        trans("please enter the employer details")
        trans("please enter the employment name")
        employer_name = takeCommand().lower()
        employer_name = input("Enter the Employer Name : "+employer_name)
        trans("please enter the office address")
        address = takeCommand().lower()
        address = input("enter the office address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip code")
        zip_code = takeCommand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        trans("please enter your designation")
        designation = takeCommand().lower()
        designation = input("Enter the designation : "+designation)
        trans("please enter the department")
        department = takeCommand().lower()
        department = input("Enter the Department name : "+department)
        trans("please enter the email id")
        email = takeCommand().lower()
        Email = input("Enter the  email id : "+email)
        trans("please enter the offical contact number : ")
        Official_number = takeCommand().lower()
        Official_number = input("Enter official contact number : " +Official_number)

    def professionals(self):
        trans("please enter the personal details")
        trans("please enter your Name")
        name =takeCommand().lower()
        name = input("Enter the name : " +name)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please enter the residential address")
        address = takeCommand().lower()
        address = input("enter the residential address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip code")
        zip_code = takeCommand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        trans("please enter pan card number")
        Pancard = takeCommand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        trans("please enter adhar card number")
        adharcard = takeCommand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        trans("please enter email")
        email = takeCommand().lower()
        email = input("Enter the email : "+email)
        pr.businessname()
        trans("do you want to list your business on preferred online store yes or no")
        print("do you want to list your business on preferred online store yes / no")

        trans("do you want to add more business yes or no")
        businessname = takeCommand().lower()
        if "yes" in businessname:
            pr.businessname()

        if "no" in businessname:
            trans("thank you selecting business")    

    def retailers(self):
        trans("please enter your Name")
        name =takeCommand().lower()
        name = input("Enter the name : " +name)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please enter the residential address")
        address = takeCommand().lower()
        address = input("enter the residential address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip code")
        zip_code = takeCommand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        trans("please enter pan card number")
        Pancard = takeCommand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        trans("please enter adhar card number")
        adharcard = takeCommand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        if len(adharcard) == 12 :
            adharcard = int(input("Enter the adharcard number : "+adharcard))
        trans("sorry sir adhar card number is invalid please check it")    
        trans("please enter email")
        email = takeCommand().lower()
        email = input("Enter the email : "+email)
        pr.businessname()
        trans("do you want to list your business on preferred online store yes or no")
        print("do you want to list your business on preferred online store yes / no")
        trans("do you want to add more business yes or no")
        businessname = takeCommand().lower()
        if "yes" in businessname:
            pr.businessname()

        if "no" in businessname:
            trans("thank you selecting retailer")  
  
    def others(self):
        trans("please enter the personal details")
        trans("please enter your Name")
        name =takeCommand().lower()
        name = input("Enter the name : " +name)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please enter the residential address")
        address = takeCommand().lower()
        address = input("enter the residential address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip code")
        zip_code = takeCommand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        trans("please enter pan card number")
        Pancard = takeCommand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        trans("please enter adhar card number")
        adharcard = takeCommand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        if len(adharcard) == 12 :
            adharcard = int(input("Enter the adharcard number : "+adharcard))
        trans("sorry sir adhar card number is invalid please check it")    
        trans("please enter email")
        email = takeCommand().lower()
        email = input("Enter the email : "+email)
        trans("please enter the employer details")
        trans("please enter the employment name")
        employer_name = takeCommand().lower()
        employer_name = input("Enter the Employer Name : "+employer_name)
        trans("please enter the office address")
        address = takeCommand().lower()
        address = input("enter the office address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip code")
        zip_code = takeCommand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        trans("please enter your designation")
        designation = takeCommand().lower()
        designation = input("Enter the designation : "+designation)
        trans("please enter the department")
        department = takeCommand().lower()
        department = input("Enter the Department name : "+department)
        trans("please enter the email id")
        email = takeCommand().lower()
        Email = input("Enter the  email id : "+email)
        trans("please enter the offical contact number : ")
        Official_number = takeCommand().lower()
        Official_number = input("Enter official contact number : "+Official_number)
    
    def businessname(self):
        trans("please Enter business name")
        business_name = takeCommand().lower()
        business_name = input("Enter the business name : ")
        trans("Please Select business type")
    
        business_name = ["business advisors","finance adviors","Mutual fund advisors",'Electricals store',"insurance advisors","technical consultants",
        "software developers","mobile app developers","Digital marketing","tax consultants","project consultants","legal consultants","others"]
        print(business_name)
        select_business_name = input(business_name)
        trans("thank you for selecting the business"+business_name)
        
        trans("do you have GST Registration yes or no ")
        print("do you have GST Registration yes / no")
        GST_registration = takeCommand().lower()
        if "yes" in GST_registration:
            trans("Enter the GST Number")
            GST_number = input("Enter the GST number : ")
        elif "no" in GST_registration:
            pass
        trans("please enter the residential address")
        address = takeCommand().lower()
        address = input("enter the residential address : "+address)
        trans("please enter city name")
        city = takeCommand().lower()
        city = input("enter the city name : "+city)
        trans("please enter state name")
        state = takeCommand().lower()
        state = input("Enter the state name : "+state)
        trans("please enter the country name")
        country = takeCommand().lower()
        country = input("Enter the country name : "+country)
        trans("Please enter zip code")
        zip_code = takeCommand().lower()
        zip_code = input("Enter the zip code : "+zip_code)    
        trans("please enter email")
        offcial_email = takeCommand().lower()
        offcial_email = input("Enter the email : "+offcial_email)
        trans("please enter the official contact number")
        offcial_number = takeCommand().lower()
        Official_number = input("Enter official contact number : "+ offcial_number)
        trans("do you want to list your business on preferred online store yes or no")
        print("do you want to list your business on preferred online store yes / no")

class ManageBudget:

    def income(self):
        trans("please select the options for income")
        income = ["salary","interest","rental","dividend","gift","gain on sale of shares","gain on sale mutual fund","others"]
        print(income)
        income = takeCommand().lower()
        if re.search("salary|interest|rental|dividend|gift|gain on sale of shares|gain on sale mutual fund|others",income):
            select_income = input(income)
            trans("selected option has" +    select_income)
            trans("please enter the name ")
            name = takeCommand().lower()
            name = input("Enter the name : "+name)
            trans("thank you for choosing income"   +        select_income)    
        trans("please select correct option in income")
        mr.income()
    def expense(self):
        trans("please select the options for expense")
        expense = ["Rent & Electricity","holidays & outgoing",
                    "loan obligations","insurance","fees & bills","car",
                    "education","Entertainment","family & personal",
                    "contigencies","mobile & internet","saving & investment","home",
                    "groceries","beauty","food & drinks","gifts","healthcare","shopping",
                    "sports & hobbies","transport","work","charities"]
        print(expense)
        expence = takeCommand().lower()
        if re.search("Rent & Electricity|holidays & outgoing|loan obligations|insurance|fees & bills|car|education|Entertainment|family & personal|contigencies|mobile & internet|saving & investment|home|groceries|beauty|food & drinks|gifts|healthcare|shopping|sports & hobbies|transport|work|charities",expence):
            select_expense = input(expense)
            trans("selected option has" +     select_expense)
            trans("please enter the name ")
            name = takeCommand().lower()
            name = input("Enter the name : "+name)
            trans("thank you for choosing expense"+      select_expense)
        trans("please select correct option in expense")
        mr.expense()

class Digitalbankingservices:
    def retailerbanking(self):
        trans("cash disbursal")
        trans("cash collection")
        trans("cheque collection")
        trans("E M I collection")

        retailers = ["cash disbursal","cash collecion","cheque collection","emi collection"]
        print(retailers)
        retailers = takeCommand().lower()
        if re.search("cash disbursal|cash collecion|cheque collection|emi collection",retailers):
            if "cash disbursal" or "cash collection" or "cheque collection" in retailers:
                trans("Verifying the all details and to proceed to action")
                trans("Enter the OTP ")
                otp = int(input("Enter the otp : "))
            elif "emi collection" in retailers:
                trans("please select financial institution")
                trans("please enter the loan account number")
                loan_number = takeCommand().lower()
                loan_number = input("Enter the loan account number : "+loan_number)
        trans("please select correct option")
        digi.retailerbanking()

        retailers = input(retailers)
        retailers = retailers.lower()
        if "cash disbursal" in retailers :
            trans("Verifying the all details and to proceed to action")
            trans("Enter the OTP ")
            otp = int(input("Enter the otp : "))
            trans("your cash has been dibursed")
        elif "cash collecion" in retailers:
            trans("Verifying the all details and to proceed to action")
            trans("Enter the OTP ")
            otp = int(input("Enter the otp : "))
            trans("your cash has been dibursed")
        elif "cheque collection" in retailers:
            trans("Verifying the all details and to proceed to action")
            trans("Enter the OTP ")
            otp = int(input("Enter the otp : "))
            trans("your cash has been dibursed")
        elif "emi collection" in retailers:
            trans("please select financial institution")
            trans("please enter the loan account number")
            loan_number = takeCommand().lower()
            loan_number = input("Enter the loan account number : "+loan_number)

    def digitalBankingServices(self):
        trans("active accounts")
        trans("money transfer")
        trans("cash withdrawal")
        trans("cash desposite")
        trans("cheque clearing")
        trans("virtual multipurpose")
        trans("loan e m i payments")

    def open_account(self):
        trans("you want to new account then click on new account form")
        trans("please enter the first name")
        first_name = takeCommand().lower()
        first_name = input("Enter the first name : "+first_name)
        trans("please enter the last name")
        last_name = takeCommand().lower()
        last_name = input("Enter the last name : "+last_name)
        trans("please enter the Email")
        email = takeCommand().lower()
        email = input("enter the Email : "+email)
        trans("please enter the mobile number")
        mobile = takeCommand().lower()
        mobile = input("Enter the mobile number : "+mobile)
        trans("please enter date of birth")
        DOB = input("Enter the DOB : ")
        trans("please enter father name")
        father = takeCommand().lower()
        father = input("Enter the father name : "+father)
        trans("please enter the mother name")
        mother = takeCommand().lower()
        mother = input("Enter the mother name : "+mother)
        trans("please enter the nationality")
        nationality = takeCommand().lower()
        nationality = input("Enter the Nationality : "+nationality)
        trans("please attached the scan adharcard file")
        adharcard = input("attached adhar card : ")
        trans("please attached the pancard file")
        pancard = input("attached pan card : ")
        trans("please select scan photograph")
        photograph = input("attached photograph : ")

class Evoicing:
    def einvoicing(self):
        trans("welcome to e invoicing")
        trans("Do you want to  record new sale yes or no")
        evoice = takeCommand().lower()
        if "yes" in evoice: 
            trans("please enter client name")
            client_name = takeCommand().lower()
            client_name = input("Enter the client name : "+client_name)

            trans("do you want to create new item yes or no")
            new_item = takeCommand().lower()
            if "yes" in new_item:
                trans("please the add category name")
                add_category = takeCommand().lower()
                add_category = input("enter the category name : "+add_category)
                trans("please enter the name")
                name = takeCommand().lower()
                name = input("Ente the name : "+name)
                trans("please select the packing type")
                packing_type = input("please select packing type : ")
                trans("Please enter the packing size")
                packing_size = takeCommand().lower()
                packing_size = input("Enter the packing size : "+packing_size)
                trans("Please enter purchase cost")
                purhase_cost = takeCommand().lower()
                purhase_cost = input("Enter the purhase cost : "+purhase_cost)
                trans("Please enter the maximum retail price")
                max_retailer = takeCommand().lower()
                max_retailer = input("Enter the maximum retailer price : "+max_retailer)
                trans("Please enter the offer price")
                offer_price = takeCommand().lower()
                offer_price = input("Enter the offer price : "+offer_price)
                trans("Please enter the stock Quantity")
                stock_QTY = takeCommand().lower()
                stock_QTY = input("Enter the stock quanlity : "+stock_QTY)
                trans("Please select the stocks")
                trans("Please enter minimum level")
                minimum_level = takeCommand().lower()
                minimum_level = input("Enter the minimum level : "+minimum_level)
                trans("Please stock update on date")
                trans("Please upload product image")
                trans("Please select tax")
                trans("Please enter the HSN code")
                hsn_code = takeCommand().lower()
                hsn_code = input("Enter the hsn code : "+hsn_code)
                trans("Please select gst") 
            if "no" in new_item:
                trans("previous item list please check it below")  
        if "no" in evoice:
            trans("thank you for choosing e invoice") 

class Manage_stoks:
    def manage_stocks(self):
        trans("welcome to e manage stock")
        trans("Do you want to  add stocks yes or no")  
        manage_stocks = takeCommand().lower()
        if "Yes" in manage_stocks: 
            trans("please the add category name")
            trans("please the add category name")
            add_category = takeCommand().lower()
            add_category = input("enter the category name : "+add_category)
            trans("please enter the name")
            name = takeCommand().lower()
            name = input("Ente the name : "+name)
            trans("please select the packing type")
            packing_type = input("please select packing type : ")
            trans("Please enter the packing size")
            packing_size = takeCommand().lower()
            packing_size = input("Enter the packibg size : "+packing_size)
            trans("Please enter purchase cost")
            purhase_cost = takeCommand().lower()
            purhase_cost = input("Enter the purhase cost : "+purhase_cost)
            trans("Please enter the maximum retail price")
            max_retailer = takeCommand().lower()
            max_retailer = input("Enter the maximum retailer price : "+max_retailer)
            trans("Please enter the offer price")
            offer_price = takeCommand().lower()
            offer_price = input("Enter the offer price : "+offer_price)
            trans("Please enter the stock Quantity")
            stock_QTY = takeCommand().lower()
            stock_QTY = input("Enter the stock quanlity : "+stock_QTY)
            trans("Please select the stocks")
            trans("Please enter minimum level")
            minimum_level = takeCommand().lower()
            minimum_level = input("Enter the minimum level : "+minimum_level)
            trans("Please stock update on date")
            trans("Please upload product image")
            trans("Please select tax")
            trans("Please enter the HSN code")
            hsn_code = takeCommand().lower()
            hsn_code = input("Enter the hsn code : "+hsn_code)
            trans("Please select gst")     

        if "no" in manage_stocks:
            trans("thank you for selecting manage stocks check privious stocks")

class Manageotherexpenses :
    def manageotherexpenses(self):
        trans("welcome to e manage  other expenses")
        trans("Do you want to record new expenses yes or no ")
        Manage_expenses = takeCommand().lower()
        if "yes" in Manage_expenses: 
            trans("please enter client name")
            client_name = takeCommand().lower()
            client_name = input("Enter the client name : "+client_name)
            trans("do you want to create new services yes or no")
            new_service = takeCommand().lower()
            if "yes" in new_service:  
                trans("Please enter the expenses name")
                expense_name = takeCommand().lower()
                expense_name = input("Enter the expenses name : "+expense_name)
                trans("Please enter the amount")
                amount = takeCommand().lower()
                amount = input("Enter the amount : "+amount)
                trans("Please select the option")

            if "no" in new_service:
                trans("please check all previous services")
        if "no" in Manage_expenses:
            trans("thank you for choosing manage expenses") 

class Manageorders:
    def manageorders(Self):
        trans("welcome to manage  orders")
    def salesorder(self):
        trans("Do you want to add orders yes or no")
        sales = takeCommand().lower()
        if "yes" in sales:
            trans("please enter client name")
            client_name = takeCommand().lower()
            client_name = input("Enter the client name : "+client_name)
            trans("do you want to add items yes or no")
            new_items = takeCommand().lower()
            if "yes" in new_items:
                trans("Please enter the name")
                name = takeCommand().lower()
                name = input("Enter the name : "+name)
                trans("Please enter the quantity")
                QTY = takeCommand().lower()
                QTY = input("Enter the QTY : "+QTY)
                trans("Please enter the unit")
                unit = takeCommand().lower()
                unit = input("Enter the unit : "+unit )
                trans("Please add packing type")
            if "no" in new_items:
                trans("thank you for selecting sales")    
        if "no" in sales:
            trans("please check all previous records")

    def purchaseorder(self):
        trans("Do you want to add orders yes or no")
        purhase = takeCommand().lower()
        if "yes" in purhase:
            trans("Enter the client name ")
            client_name = takeCommand().lower()
            client_name = input("Enter the client name : "+client_name)
        if "no" in purhase:
            trans("check all purhase record below")

class Managereturn:
    def managereturn(self):
        trans("welcome to manage  return")
        sales = takeCommand().lower()
        if "yes" in sales:
            trans("please enter client name")
            client_name = takeCommand().lower()
            client_name = input("Enter the client name : "+client_name)
	
        if "no" in sales:
            trans("please check all previous recors\d")

    def purchaseorder(self):
        trans("Do you want to add orders yes or no")
        purhase = takeCommand().lower()
        if "yes" in purhase:
            trans("Enter the client name ")
            client_name = takeCommand().lower()
            client_name = input("Enter the client name : "+client_name)
        if "no" in purhase:
            trans("check all purhase record below")

class Managestaffsalary:
    def managestaffsalary(self):
        trans("welcome to manage staff salary")
        trans("do you want to add staff")
        staff = takeCommand().lower()
        if "yes" in staff:
            trans("Please enter the staff full name")
            fullname = takeCommand().lower()
            fullname = input("Enter the full name : "+fullname)
            trans("Please enter the mobile number")
            mobile = takeCommand().lower()
            mobile = input("Enter the mobile number : "+mobile)
            trans("Select the type of salary payment")

            trans("Please add salary details") 
            trans("Please enter the monthly salary ")
            month_salary = takeCommand().lower()
            month_salary = input("Enter the month salary : "+month_salary)
            trans("Please add  overtime rate")
            overtime = takeCommand().lower()
            overtime = input("Enter the overtime details : "+overtime)

            trans("Please add late fine rate")
            fine_late = takeCommand().lower()
            fine_late = input("Enter the fine late amount : ")

            trans("Please select payment cycle ")

            trans("Please enter the pending salary ")
            pending = takeCommand().lower()
            pending = input("Enter the pending salary : "+pending)
            trans("Please select month of salary")
            trans("Please enter the pending overtime")
            pending_ov = takeCommand().lower()
            pending_ov = input("Enter the pending overtime : "+pending_ov)
            trans("Please select month of overtime salary")
            trans("Please add the advances")
            advance = takeCommand().lower()
            advance = input("enter the advance : "+advance) 
        if "no" in staff:
            trans("thank you for selecting manage staff salary")

class Scorecard:
    def scorecard():
        trans("please update the credit score")
        trans("please enter your Name")
        name = takeCommand().lower()
        name = input("Enter the name : "+name)
        trans("please enter the mobile number")
        mobile = takeCommand().lower()
        mobile = input("Enter the Mobile number : "+mobile)
        trans("please enter email")
        email = takeCommand().lower()
        email = input("Enter the email : "+email)
        trans("please enter pancard number")
        Pancard = takeCommand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        trans("please enter adharcard number")
        adharcard = takeCommand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please enter the address")
        address = takeCommand().lower()
        address = input("enter the address : "+address)
    
    def investmentRiskScore(self):
        trans("please update the investment risk score")
    def personaldetails(self):
        trans("please Fill the personal details")
        trans("please Enter the name")
        name = takeCommand().lower()
        name = input("Enter the name : "+name)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please choose the professional ")
        trans("profession 1")
        trans("profession 2")
        trans("professional 3") 
        profession = input("please choose the profession")
        trans("please enter the monthly income")
        monthly_income = takeCommand().lower()
        monthly_income = input("Enter the monthly income : "+monthly_income)
        trans("please enter monthly expense")
        monthly_expense = takeCommand().lower()
        monthly_expense = input("Enter the monthly expense : "+monthly_expense)
        trans("please enter the monthly loan obligation")
        loan_obligation = takeCommand().lower()
        loan_obligation = input("Enter the monthly loan obligation : "+loan_obligation)

    def familydetails(self):
        trans("please fill the family details")
        trans("please enter the name")
        name = takeCommand().lower()
        name = input("enter the name : "+ name)
        trans("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        trans("please choose the qualification")
        trans("qualification 1 ")
        trans("qualification 2 ")
        trans("qualification 3 ")
        qualification = input("please choose the qualification : ")
        trans("please choose the professional ")
        trans("profession 1")
        trans("profession 2")
        trans("professional 3") 
        profession = input("please choose the profession")
        trans("please enter the monthly income")
        monthly_income = takeCommand().lower()
        monthly_income = input("Enter the monthly income : "+monthly_income)
        trans("please choose the relation")
        trans("relation 1 ")
        trans("relation 2 ")
        trans("relation 3 ")
        relation = input("please choose the relation : ")

    def educationdetails(self):
        trans("please fill the education Details")
        trans("please enter the name")
        name = takeCommand().lower()
        name = input("Enter the name : "+name)
        trans("please enter the relationship")
        relationship = takeCommand().lower()
        relationship = input("Enter the relationship : "+relationship)
        trans("please enter the nature of obligation")
        nature_obligation = takeCommand().lower()
        nature_obligation = input("Enter the nature of obligation : "+nature_obligation)
        trans("please enter the expected expense")
        expected_expense = takeCommand().lower()
        expected_expense = input("Enter the expected expense : "+expected_expense)
        trans("please enter the expected date year")
        expected_date_year = input("Enter the expected date/year : ")

    def socialobligationdetails(self):    
        trans("please enter the name")
        name = takeCommand().lower()
        name = input("Enter the name : "+name)
        trans("please enter the relationship")
        relationship = takeCommand().lower()
        relationship = input("Enter the relationship : "+relationship)
        trans("please enter the nature of obligation")
        nature_obligation = takeCommand().lower()
        nature_obligation = input("Enter the nature of obligation : "+nature_obligation)
        trans("please enter the expected expense")
        expected_expense = takeCommand().lower()
        expected_expense = input("Enter the expected expense : "+expected_expense)
        trans("please enter the expected date year")
        expected_date_year = input("Enter the expected date/year : ")

    def retirementdetails(self):
        trans("please enter retirement details")
        trans("please enter the retirement age")
        retirement_age = takeCommand().lower()
        retirement_age = input("Enter the  retirement age : "+retirement_age)
        trans("please choose the fund type")
        trans("fund 1 ")
        trans("fund 2 ")
        trans("fund 3 ")
        relation = input("please choose the funds : ")

    def contigencydetails():
        trans("please enter the contigency plan details")
        trans("Please enter the amount")
        amount = takeCommand().lower()
        amount = input("Enter the amount : "+amount)
        trans("please enter the frequency")
        frequency = takeCommand().lower()
        frequency  = input("Enter the frequency : "+frequency)

    def behaviorscore():
        pass
    def overallscore():
        pass
    
    def scorecard(self):
        trans("welcome in scorecard")
        trans("credit score")
        trans("investment risk score")
        trans("behavior score")
        trans("overall score")
        scorecard = takeCommand().lower()
        if re.search("credit score|investment risk score|behavior score |overall score ",scorecard):
            if "credit score" in scorecard:
                sc.creditscore()
            elif "investment risk score" in scorecard:
                sc.investmentRiskScore()    
                sc.personaldetails()
                sc.familydetails()
                sc.educationdetails
                sc.socialobligationdetails()
                sc.retirementdetails()
                sc.contigencydetails()
            elif "behavior score" in scorecard:
                sc.behaviorscore()
            elif "overall score" in scorecard:
                sc.overallscore()        

        trans("please select the correct option")
        sc.scorecard()
class Rewards:
    def rewards(self):
        trans("welcome to reward")
        trans("rewards here tap to scratch")
        trans("please used this code to claim now")

class Referandearn:
    def referandearn(self):
        trans("welcome to refer and earn")
        trans("Earn 100 rupees every time a referred friends makes their 1st payment on payment from bank A/C")

class Documentmanager:
    def documentmanager(self):
        trans("welcome to documents manager")
        trans("do you want to add documents yes or no")
        Documentmanager = takeCommand().lower()
        if "yes" in Documentmanager: 
            trans("please upload the documents")
            trans("please add notes")
            trans("please voice data")
        elif "No" in Documentmanager:
            trans("thank you")
        trans("do you want add folder yes or no ")
        folder = takeCommand().lower()
        if "yes" in folder:
            trans("please add the documents folder")
        elif "No" in folder:
            trans("thank you")

class Passwordmanager:
    def passwordmanager(self):
        trans("welcome to password manager")
        trans("please enter the security password")

class TaxReturn:
    def incometaxreturn(self):
        trans("please add new data")
        trans("please enter the assesment year")
        assessment_year = input("enter the assessment_year : ")
        trans("please select type of return")
        trans("original")
        print("original")
        trans("modified")
        print("modified")
        type_of_return = input("please choose the type of return : ")
        trans("please enter the due date")
        due_date = input("enter the due date : ")
        trans("please enter the submitted date on")
        submitted_date = input("Enter the submitted date on : ")
        trans("please enter the taxable income")
        texable_income = takeCommand().lower()
        taxable_income = input("Enter the taxable income : "+texable_income)

        trans("please enter liability(refund)")
        refund = takeCommand().lower()
        refund = input("Enter the liability(refund) : "+refund)
        trans("please enter the status")
        status = takeCommand().lower()
        status = input("Enter the Status : "+status)
    
    def gstReturn(self):
        trans("please add new data")
        trans("please choose return type")
        gst_type = ["GSTR-1","GSTR-2","GSTR-3","GSTR_3B","GSTR-4","GSTR-5","GSTR-6","GSTR-7","GSTR-8","GSTR-9","GSTR-9A","GSTR-9C","GSTR-10","GSTR-11"]
        print(gst_type)
        select_gst = input(gst_type)
        trans("thank you for select "   +      select_gst)
        trans("please select recurrence")
        print("Anually")
        trans("anullay")
        print("quartely")
        trans("quartely")
        print("monthly")
        trans("monthly")
        trans("please enter the assesment year")
        assessment_year = input("enter the assessment_year : ")
        trans("please enter the due date")
        due_date = input("enter the due date : ")
        trans("please enter the submitted date on")
        submitted_date = input("Enter the submitted date on : ")
        trans("please enter the sales value")
        sales_value = takeCommand().lower()
        sales_value = input("Enter the sales value : "+sales_value)
        trans("please enter liability(refund)")
        refund = takeCommand().lower()
        refund = input("Enter the liability(refund) : "+refund)
        trans("please enter the status")
        status = takeCommand().lower()
        status = input("Enter the Status : "+status)

class Mutual_fund:
    def highlystablefunds(self):
        funds = ["liquid funds","debt funds","gold funds"]
        print(funds)
        funds = takeCommand().lower()
        if re.search("liquid funds|debt funds|gold funds",funds):
            trans("thank you for selected funds is "  +    funds)
            trans("check all details above and continue it")
        
            trans("please select the investment type")
            trans("money sip")
            trans("one time")
            a = ["money sip" , "one time"]
            a = input(a)
            trans("so you have selected"   +     a)

            trans("please enter the investment amount")
            investment_amount = int(input("Enter the amount : "))

            trans("please enter scedule investment on every")
            ddmmyy = input("Enter the date month year : ")
            
            trans("please setup your investment account")
            trans("please enter the pancard number")
            pancard = input("Enter PAN to create account : ")

            trans("please select the ADF pay terms and condition")
        trans("please select correct option")
        mf.highlystablefunds()

    def balancedfunds(self):
        funds = ["super funds","aggressive hybrid","dynamic asset allocation"]
        print(funds)
        if re.search("super funds|aggressive hybrid|dynamic asset allocation",funds):
            trans("thank you for selected fund is " +   funds)
            trans("check all details above and continue it")

            trans("please select the investment type")
            trans("money sip")
            trans("one time")
            a = ["money sip" , "one time"]
            a = input(a)
            trans("so you have selected"   +      a)

            trans("please enter the investment amount")
            investment_amount = int(input("Enter the amount : "))

            trans("please enter scedule investment on every")
            ddmmyy = input("Enter the date month year : ")

            trans("please setup your investment account")
            trans("please enter the pancard number")
            pancard = input("Enter PAN to create account : ")

            trans("please select the ADF pay terms and condition")

        trans("please select correct option")
        mf.balancedfunds()

    def highgrowthfunds(self):
        funds = ["tax saving funds","large cap funds","diversified funds","mid & small cap","index funds"]
        funds = takeCommand().lower()
        if re.search("tax saving funds|large cap funds|diversified funds|mid & small cap|index funds",funds):
            trans("thank you for selected fund is "+      funds)
            trans("check all details above and continue it")
        
            trans("please select the investment type")
            trans("money sip")
            trans("one time")
            a = ["money sip" , "one time"]
            a = input(a)
            trans("so you have selected" + a)

            trans("please enter the investment amount")
            investment_amount = int(input("Enter the amount : "))

            trans("please enter scedule investment on every")
            ddmmyy = input("Enter the date month year : ")

            trans("please setup your investment account")
            trans("please enter the pancard number")
            pancard = input("Enter PAN to create account : ")

            trans("please select the ADF pay terms and condition")
        trans("please select correct option")
        mf.highgrowthfunds()
class StockMarket:
    pass

class FixedDeposite:
    pass

class InstantLoan:
    def instantloan(self):
        trans("welcome to instant loan services")

class BusinessLoan:
    pass

class OnlineStore:
    def onlinestore(self):
        trans("Welcome to online Stores")

        online_store = ["provisional store","fruit & vegetable store","sweet & confectionery","electrical store","mechanics & repair","fintness & health supplement","electronics appliance","fashion store","gold & jeweleries","mobile & accessories","book & stationary","computer accessories","games & gift","kitchen appliances","medical store","health clinic","personal & baby care","home furnishing","home appliances","makeup artist","beauty parlour & saloon","travel agent","restaurants","others"]
        print(online_store)

        online_store = takeCommand().lower()
        if re.search("provisional store|fruit & vegetable store|sweet & confectionery|electrical store|mechanics & repair|fintness & health supplement|electronics appliance|fashion store|gold & jeweleries|mobile & accessories|book & stationary|computer accessories|games & gift|kitchen appliances|medical store|health clinic|personal & baby care|home furnishing|home appliances|makeup artist|beauty parlour & saloon|travel agent|restaurants|others",online_store):
            trans("thank you for selected"  +     online_store)

        trans("please select corrct option")    
class OnlineServices:
    
    def onlineServices(self):
        trans("welcome to online services")
        online_services = ["saloon for woment","saloon for Men","makeup artists","ac service & repair","appliance repair","painter","cleaning & disinfection","electrician","plumber","carpenters","pest control","car mechanics","fitness centres","web developer","mobile app developer","IT services","computer repair","networking services","financial consultants","legal consultants","financial advisor","tax advisors","baby care","house keeping","others"]
        print(online_services)
        if re.search("saloon for woment|saloon for Men|makeup artists|ac service & repair|appliance repair|painter|cleaning & disinfection|electrician|plumber|carpenters|pest control|car mechanics|fitness centres|web developer|mobile app developer|IT services|computer repair|networking services|financial consultants|legal consultants|financial advisor|tax advisors|baby care|house keeping|others",online_services):
            trans("thank you for selected" +        online_services)
        trans("please select correct option")

########################################
now = datetime.now()

def greeting():
    hour = int(now.hour)
    if hour>=0 and hour<12:
        trans("Good Morning!")
        print("Good Morning!")
    elif hour>=12 and hour<18:
        trans("Good Afternoon!")
        print("Good Afternoon!")
    else:
        trans("Good Evening!")
        print("Good Evening!")
    trans("Welcome to ADF PAY!")
    print("Welcome to ADF PAY!")
    sleep(3)

def language():
    print('Please Select your Language:')
    print('1) English')
    print('2) Hindi')
    print('3) Marathi')
    trans('Please Select your Language:')
    lang = takeCommand().lower()
    if 'english' in lang:
        print("You have selected to proceed in English language")
        trans("You have selected to proceed in English language")
    elif 'hindi' in lang:
        print("You have selected to proceed in Hindi language")
        trans("You have selected to proceed in Hindi language")
    elif 'marathi' in lang:
        print("You have selected to proceed in Hindi language")
        trans("You have selected to proceed in Hindi language")
    sleep(1)
    print(" \n ")

def welcome():
    print('Sign Up to register yourself!')
    trans('Sign Up to register yourself!')
    sleep(1)

    print('Please Enter your Mobile Number')
    trans('Please Enter your Mobile Number')
    mobile=takeCommand().lower()


    print('Please enter 6 digit Otp sent to your mobile no')
    trans('Please enter 6 digit Otp sent to your mobile no')
    otp= takeCommand().lower()
    sleep(1)

    print('Thanks for signing up!')
    trans('Thanks for signing up.. ')
    sleep(3)

def home():
    print("Welcome to ADFPAY. We have varirty of products to explore!!")
    trans("Welcome to ADFPAY. We have varirty of products to explore!!")
    sleep(1)

    print("You may update your profile by visiting the side menu and also update the settings !")
    trans("You may update your profile by visiting the side menu and also update the settings !")
    sleep(1)

    print("Please select the products from below : ")
    trans("Please select the products from below")
#####################

class Networth:
    def Networth(self):
        print('Hi, Welcome to check your Networth!')
        trans('Hi, Welcome to check your Networth!')
        sleep(1)

        Networth= "450000"

        print('Your Current Networth is '+ Networth)
        trans('Your Current Networth is '+ Networth)
        sleep(1)

        print('Please select the following that you want to proceed with : ')
        trans('Please select the following that you want to proceed with : ')
        print('1) Assets')
        print('2) Liabilities')
        opt= takeCommand().lower()
        if 'assets' in opt:
            print("You have selected to assets")
            trans("You have selected to assets")
            Networth.assets()
        elif 'Liabilities' in opt:
            print("You have selected to Liabilities")
            trans("You have selected to Liabilities")
            Networth.Liabilities()
        sleep(1)

    def assets():
        investment= 10000
        current_value= 11000
        Gain= (current_value-investment)/investment
        print('Your Current value of your investment is '+ str(current_value) + ' with a gain of ' + str(Gain))
        trans('Your Current value of your investment is '+ str(current_value) + ' with a gain of ' + str(Gain))
        trans("You may also check your assests as segmented below:")
        sleep(3)

        print("Do you want to add new records to your assets?")
        trans("Do you want to add new records to your assets?")
        print("1) Yes")
        print("2) No")
        New_record_ass= takeCommand().lower()
        if 'yes' in New_record_ass:
            Networth.asset_add_record()
        elif 'no' in New_record_ass:
            exit()

    def Liabilities():
        total_Liabilities= 3000
        current_balance= 5000
        Gain= (current_balance-total_Liabilities)/total_Liabilities
        print('Your Current value of your investment is '+ str(current_balance) + ' with a gain of ' + str(Gain))
        trans('Your Current value of your investment is '+ str(current_balance) + ' with a gain of ' + str(Gain))
        trans("You may also check your Liabilities as segmented below:")
        sleep(3)

        print("Do you want to add new records to your liabilities?")
        trans("Do you want to add new records to your liabilities?")
        print("1) Yes")
        print("2) No")
        New_record_lia= takeCommand().lower()
        if 'yes' in New_record_lia:
            Networth.liabilities_add_record()
        elif 'no' in New_record_lia:
            exit()

    def asset_add_record():
        print("You have selected to add new asset record ")
        trans("You have selected to add new asset record ")
        sleep(1)

        print("Please select the below assets that you want to add to your networth : ")
        trans("Please select the below assets that you want to add to your networth : ")
        print('1) Fixed Deposit')
        print('2) Insurance Policy')
        print('3) Mutual Fund')
        print('4) Shares and Debentures')
        print('5) Security & Bonds')
        print('6) Crypto')
        print('7) Property Details')
        print('8) Gold & Jewellery')
        print('9) Vehicles')
        print('10) Saving Certificates')
        print('11) Other Assets')

        assets= takeCommand().lower()
        sleep(1)
        if 'fixed deposit' in assets:
            print("You have selected Fixed Deposit")
            trans("You have selected Fixed Deposit")
            sleep(1)
            print("You may proceed to edit fixed deposit from below or add new Fixed Deposit details : ")
            trans("You may proceed to edit fixed deposit from below or add new Fixed Deposit details : ")
            sleep(1)

            print("Do you want to add new records to FD?")
            trans("Do you want to add new records to FD?")
            print("1) Yes")
            print("2) No")
            New_record_FD= takeCommand().lower()
            if 'yes' in New_record_FD:
                Networth.Fixed_Deposit()
            elif 'no' in New_record_FD:
                exit()
            
        elif 'insurance policy' in assets:
            print("You have selected Insurance Policy")
            trans("You have selected Insurance Policy")
            sleep(1)
            print("You may proceed to edit Insurance Policy from below or add new Insurance Policy details : ")
            trans("You may proceed to edit Insurance Policy from below or add new Insurance Policy details : ")
            sleep(1)

            print("Do you want to add new records to Insurance Policy?")
            trans("Do you want to add new records to Insurance Policy?")
            print("1) Yes")
            print("2) No")
            New_record_pol= takeCommand().lower()
            if 'yes' in New_record_pol:
                Networth.insurance_policies()
            elif 'no' in New_record_pol:
                exit()

        elif 'mutual fund' in assets:
            print("You have selected Mutual Fund")
            trans("You have selected Mutual Fund")
            sleep(1)
            print("You may proceed to edit Mutual Fund from below or add new Mutual Fund details : ")
            trans("You may proceed to edit Mutual Fund from below or add new Mutual Fund details : ")
            sleep(1)

            print("Do you want to add new records to Mutual Fund?")
            trans("Do you want to add new records to Mutual Fund?")
            print("1) Yes")
            print("2) No")
            New_record_fund= takeCommand().lower()
            if 'yes' in New_record_fund:
                Networth.Mutual_Fund()
            elif 'no' in New_record_fund:
                exit()

        elif 'shares and debentures' in assets:
            print("You have selected Shares and Debentures")
            trans("You have selected Shares and Debentures")
            sleep(1)
            print("You may proceed to edit Shares and Debentures from below or add new Shares and Debentures details : ")
            trans("You may proceed to edit Shares and Debentures from below or add new Shares and Debentures details : ")
            sleep(1)

            print("Do you want to add new records to Shares and Debentures?")
            trans("Do you want to add new records to Shares and Debentures?")
            print("1) Yes")
            print("2) No")
            New_record_shares= takeCommand().lower()
            if 'yes' in New_record_shares:
                Networth.Shares()
            elif 'no' in New_record_shares:
                exit()

        elif 'security and bonds' in assets:
            print("You have selected Security & Bonds")
            trans("You have selected Security & Bonds")
            sleep(1)
            print("You may proceed to edit Security & Bonds from below or add new Security & Bonds details : ")
            trans("You may proceed to edit Security & Bonds from below or add new Security & Bonds details : ")
            sleep(1)

            print("Do you want to add new records to Security & Bonds?")
            trans("Do you want to add new records to Security & Bonds?")
            print("1) Yes")
            print("2) No")
            New_record_bonds= takeCommand().lower()
            if 'yes' in New_record_bonds:
                Networth.security()
            elif 'no' in New_record_bonds:
                exit()

        elif 'crypto' in assets:
            print("You have selected Crypto")
            trans("You have selected Crypto")
            sleep(1)
            print("You may proceed to edit Crypto from below or add new Crypto details : ")
            trans("You may proceed to edit Crypto from below or add new Crypto details : ")
            sleep(1)

            print("Do you want to add new records to Crypto?")
            trans("Do you want to add new records to Crypto?")
            print("1) Yes")
            print("2) No")
            New_record_Crypto= takeCommand().lower()
            if 'yes' in New_record_Crypto:
                Networth.Crypto()
            elif 'no' in New_record_Crypto:
                exit()

        elif 'property details' in assets:
            print("You have selected Property Details")
            trans("You have selected Property Details")
            sleep(1)
            print("You may proceed to edit Property Details from below or add new Property Details : ")
            trans("You may proceed to edit Property Details from below or add new Property Details : ")
            sleep(1)

            print("Do you want to add new records to Property Details?")
            trans("Do you want to add new records to Property Details?")
            print("1) Yes")
            print("2) No")
            New_record_property= takeCommand().lower()
            if 'yes' in New_record_property:
                Networth.Property_Details()
            elif 'no' in New_record_property:
                exit()

        elif 'gold & jewellery' in assets:
            print("You have selected Gold & Jewellery")
            trans("You have selected Gold & Jewellery")
            sleep(1)
            print("You may proceed to edit Gold & Jewellery from below or add new Gold & Jewellery details : ")
            trans("You may proceed to edit Gold & Jewellery from below or add new Gold & Jewellery details : ")
            sleep(1)

            print("Do you want to add new records to Gold & Jewellery?")
            trans("Do you want to add new records to Gold & Jewellery?")
            print("1) Yes")
            print("2) No")
            New_record_gold= takeCommand().lower()
            if 'yes' in New_record_gold:
                Networth.Gold()
            elif 'no' in New_record_gold:
                exit()
            
        elif 'vehicles' in assets:
            print("You have selected Vehicles")
            trans("You have selected Vehicles")
            sleep(1)
            print("You may proceed to edit Vehicles from below or add new Vehicles details : ")
            trans("You may proceed to edit Vehicles from below or add new Vehicles details : ")
            sleep(1)

            print("Do you want to add new records to vehicles?")
            trans("Do you want to add new records to vehicles?")
            print("1) Yes")
            print("2) No")
            New_record_veh= takeCommand().lower()
            if 'yes' in New_record_veh:
                Networth.Vehicles()
            elif 'no' in New_record_veh:
                exit()
            
        elif 'saving certificates' in assets:
            print("You have selected Saving Certificates")
            trans("You have selected Saving Certificates")
            sleep(1)
            print("You may proceed to edit Saving Certificates from below or add new Saving Certificates details : ")
            trans("You may proceed to edit Saving Certificates from below or add new Saving Certificates details : ")
            sleep(1)

            print("Do you want to add new records to saving certificates?")
            trans("Do you want to add new records to saving certificates?")
            print("1) Yes")
            print("2) No")
            New_record_cer= takeCommand().lower()
            if 'yes' in New_record_cer:
                Networth.Saving_Certificates()
            elif 'no' in New_record_cer:
                exit()

        elif 'other Assets' in assets:
            print("You have selected Other Assets")
            trans("You have selected Other Assets")
            sleep(1)
            print("You may proceed to edit Other Assets from below or add new Other Assets details : ")
            trans("You may proceed to edit Other Assets from below or add new Other Assets details : ")
            sleep(1)

            print("Do you want to add new records to other Assets?")
            trans("Do you want to add new records to other Assets?")
            print("1) Yes")
            print("2) No")
            New_record_other= takeCommand().lower()
            if 'yes' in New_record_other:
                Networth.Other_Assets()
            elif 'no' in New_record_other:
                exit()
            sleep(1)

    def liabilities_add_record():
        print("You have selected to add new Liabilities record ")
        trans("You have selected to add new Liabilities record ")
        sleep(1)

        print("Please select the below Liabilities that you want to add to your networth : ")
        trans("Please select the below Liabilities that you want to add to your networth : ")
        print('1) Credit Cards')
        print('2) Loans ')
        print('3) Monthly Obligations')
        print('4) Others')

        Liabilities= takeCommand().lower()
        sleep(1)
        if 'credit cards' in Liabilities:
            print("You have selected Credit Cards")
            trans("You have selected Credit Cards")
            sleep(1)
            print("You may proceed to edit Credit Cards from below or add new Credit Cards details : ")
            trans("You may proceed to edit Credit Cards from below or add new Credit Cards details : ")
            sleep(1)

            print("Do you want to add new records to credit cards?")
            trans("Do you want to add new records to credit cards?")
            print("1) Yes")
            print("2) No")
            New_record_credit= takeCommand().lower()
            if 'yes' in New_record_credit:
                Networth.Credit_Cards()
            elif 'no' in New_record_credit:
                exit()
            
        elif 'loans' in Liabilities:
            print("You have selected Loans")
            trans("You have selected Loans")
            sleep(1)

            print("Please select the below loans that you want to add to your networth : ")
            trans("Please select the below loans that you want to add to your networth : ")
            print('1) Financial Institutions')
            print('2) Private Lenders ')
            print('3) Friends & Relatives')
            l1= takeCommand().lower()
            if 'financial institutions' in l1:
                print("You have selected to Financial Institutions")
                trans("You have selected to Financial Institutions")
                
                print("You may proceed to edit Financial Institutions loans from below or add new details : ")
                trans("You may proceed to edit Financial Institutions loans from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to credit cards?")
                trans("Do you want to add new records to credit cards?")
                print("1) Yes")
                print("2) No")
                New_record_credit= takeCommand().lower()
                if 'yes' in New_record_credit:
                    Networth.Financial_Institutions()
                elif 'no' in New_record_credit:
                    exit()

            elif 'private lenders' in l1:
                print("You have selected to Private Lenders")
                trans("You have selected to Private Lenders")
                
                print("You may proceed to edit Private Lenders Loans from below or add new details : ")
                trans("You may proceed to edit Private Lenders Loans from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to private lenders?")
                trans("Do you want to add new records to private lenders?")
                print("1) Yes")
                print("2) No")
                New_record_lend= takeCommand().lower()
                if 'yes' in New_record_lend:
                    Networth.Private_Lenders()
                elif 'no' in New_record_lend:
                    exit()
                
            elif 'friends & relatives' in l1:
                print("You have selected to Friends & Relatives")
                trans("You have selected to Friends & Relatives")
                Liabilities()
                print("You may proceed to edit Friends & Relatives Loans from below or add new details : ")
                trans("You may proceed to edit Friends & Relatives Loans from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to friends & relatives?")
                trans("Do you want to add new records to friends & relatives?")
                print("1) Yes")
                print("2) No")
                New_record_fri= takeCommand().lower()
                if 'yes' in New_record_fri:
                    Networth.Friends()
                elif 'no' in New_record_fri:
                    exit()

        elif 'monthly Obligations' in Liabilities:
            print("You have selected Monthly Obligations")
            trans("You have selected Monthly Obligations")
            sleep(1)
            print("Please select the below Monthly Obligations loans that you want to add to your networth : ")
            trans("Please select the below Monthly Obligations loans that you want to add to your networth : ")
            print('1) Insurance Premium')
            print('2) SIP Instalments')
            print('3) Recurring deposits')
            m1= takeCommand().lower()
            if 'insurance premium' in m1:
                print("You have selected to Insurance Premium")
                trans("You have selected to Insurance Premium")
                
                print("You may proceed to edit Insurance Premium from below or add new details : ")
                trans("You may proceed to edit Insurance Premium from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to insurance premium?")
                trans("Do you want to add new records to insurance premium?")
                print("1) Yes")
                print("2) No")
                New_record_pre= takeCommand().lower()
                if 'yes' in New_record_pre:
                    Networth.insurance_policies()
                elif 'no' in New_record_pre:
                    exit()

            elif 'sip instalments' in m1:
                print("You have selected to SIP Instalments")
                trans("You have selected to SIP Instalments")
                
                print("You may proceed to edit SIP Instalments from below or add new details : ")
                trans("You may proceed to edit SIP Instalments from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to SIP Instalments?")
                trans("Do you want to add new records to SIP Instalments?")
                print("1) Yes")
                print("2) No")
                New_record_sip= takeCommand().lower()
                if 'yes' in New_record_sip:
                    Networth.SIP_Instalments()
                elif 'no' in New_record_sip:
                    exit()

            elif 'recurring deposits' in m1:
                print("You have selected to Recurring deposits")
                trans("You have selected to Recurring deposits")
                
                print("You may proceed to edit Recurring deposits from below or add new details : ")
                trans("You may proceed to edit Recurring deposits from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to recurring deposits?")
                trans("Do you want to add new records to recurring deposits?")
                print("1) Yes")
                print("2) No")
                New_record_recc= takeCommand().lower()
                if 'yes' in New_record_recc:
                    Networth.Recurring()
                elif 'no' in New_record_recc:
                    exit()
            
        elif 'Others' in Liabilities:
            print("You have selected Others")
            trans("You have selected Others")
            sleep(1)
            print("You may proceed to edit Others from below or add new Others details : ")
            trans("You may proceed to edit Others from below or add new Others details : ")
            sleep(1)

            print("Do you want to add new records to Others?")
            trans("Do you want to add new records to Others?")
            print("1) Yes")
            print("2) No")
            New_record_otherr= takeCommand().lower()
            if 'yes' in New_record_otherr:
                Networth.Other()
            elif 'no' in New_record_otherr:
                exit()

    def Fixed_Deposit():
        print("You have selected to enter new Fixed Deposit")
        trans("You have selected to enter new Fixed Deposit")
        sleep(1)

        trans("Please Select your institution Type :")
        inst_type = str(input("Please Select your institution Type :"))
        sleep(1)
        
        trans("Please enter your FD Type :")
        FD_type = str(input("Please enter your FD Type :"))
        sleep(1)

        trans("Please enter your Invested Value :")
        Invested = str(input("Please enter your Invested Value :"))
        sleep(1)

        trans("Please enter your Annual Rate of Insterest :")
        Ann_rate = str(input("Please enter your Annual Rate of Insterest :"))
        sleep(1)

        trans("Please enter your Interest compounding Frequency :")
        Com_fre= str(input("Please enter your Interest compounding Frequency :"))
        sleep(1)

        trans("Please enter your Investing period :")
        period = str(input("Please enter your Investing period :"))
        sleep(1)

        trans("Please enter your Current Value :")
        curr_val = str(input("Please enter your Current Value :"))
        sleep(1)

        trans("Please enter your start Date :")
        start_date = str(input("Please enter your start Date :"))
        sleep(1)

        trans("Please enter your Note :")
        Note = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def insurance_policies():
        print("You have selected to enter new Insurance Policies")
        trans("You have selected to enter new Insurance Policies")
        sleep(1)

        trans("Please Select your insurance Policies :")
        ins_pol = str(input("Please Select your insurance Policies :"))
        sleep(1)
        
        trans("Please enter your Company Name :")
        com_name = str(input("Please enter your Company Name :"))
        sleep(1)

        trans("Please enter your Policy Name :")
        Pol_name = str(input("Please enter your Policy Name :"))
        sleep(1)

        trans("Please enter your Policy Number :")
        pol_no = str(input("Please enter your Policy Number :"))
        sleep(1)

        trans("Please enter your Start Date :")
        srt_date= str(input("Please enter your Start Date :"))
        sleep(1)

        trans("Please enter your Premium Amount :")
        amount = str(input("Please enter your Premium Amount :"))
        sleep(1)

        trans("Please enter your Recurrence :")
        rec = str(input("Please enter your Recurrence :"))
        sleep(1)

        trans("Please enter your premium due :")
        due = str(input("Please enter your premium due :"))
        sleep(1)

        trans("Please enter your Sum Assured :")
        sum_assured = str(input("Please enter your Sum Assured :"))
        sleep(1)

        trans("Please enter your Maturity Date :")
        mat_date = str(input("Please enter your Maturity Date :"))
        sleep(1)

        trans("Please enter your Maturity Value :")
        mat_val = str(input("Please enter your Maturity Value :"))
        sleep(1)

        trans("Please enter your Note :")
        Note1 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Mutual_Fund():
        print("You have selected enter to new Mutual Fund")
        trans("You have selected enter to new Mutual Fund")
        sleep(1)

        trans("Please enter the Company Name :")
        com = str(input("Please enter the Company Name :"))
        sleep(1)
        
        trans("Please enter your Scheme Name :")
        scheme = str(input("Please enter your scheme Name :"))
        sleep(1)

        trans("Please enter your scheme type :")
        sch_type = str(input("Please enter your scheme type :"))
        sleep(1)

        trans("Please enter your fund class :")
        fund_class = str(input("Please enter your fund class :"))
        sleep(1)

        trans("Please enter your Portfolio Number :")
        port_no = str(input("Please enter your Portfolio Number :"))
        sleep(1)

        trans("Please enter your purchase Date :")
        pur_date= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter units :")
        units = str(input("Please enter units :"))
        sleep(1)

        trans("Please enter Rate :")
        rate = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter your Invested Value :")
        invest_value = str(input("Please enter your invested Value :"))
        sleep(1)

        trans("Please enter current value :")
        curr_vall = str(input("Please enter your current value :"))
        sleep(1)

        trans("Please enter Gain/Loss :")
        mat_val = str(input("Please enter Gain/Loss :"))
        sleep(1)

        trans("Please enter your Note :")
        Note2 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Shares():
        print("You have selected to enter new Shares")
        trans("You have selected to enter new Shares")
        sleep(1)

        trans("Please enter the Script type :")
        Script = str(input("Please enter the Script type :"))
        sleep(1)
        
        trans("Please enter your Company Name :")
        c1 = str(input("Please enter your Company Name :"))
        sleep(1)

        trans("Please enter your Demat account Number :")
        Demat_no = str(input("Please enter your Demat account Number :"))
        sleep(1)

        trans("Please enter your Demat Holding Company :")
        fund_class = str(input("Please enter your Demat Holding Company :"))
        sleep(1)

        trans("Please enter your purchase Date :")
        pur_date1= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter your Number of shared/Debentures :")
        no_shares = str(input("Please enter your Number of shared/Debentures :"))
        sleep(1)

        trans("Please enter Rate :")
        rate1 = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter your Invested Value :")
        invest_value1 = str(input("Please enter your invested Value :"))
        sleep(1)

        trans("Please enter current market value :")
        curr_vall1 = str(input("Please enter your current market value :"))
        sleep(1)

        trans("Please enter Gain/Loss :")
        Gain1 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        trans("Please enter your Note :")
        Note3 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def security():
        print("You have selected to enter Security & Bonds")
        trans("You have selected to enter Security & Bonds")
        sleep(1)

        trans("Please enter the Script type :")
        Script1 = str(input("Please enter the Script type :"))
        sleep(1)
        
        trans("Please enter institution Name :")
        i1 = str(input("Please enter your institution Name :"))
        sleep(1)

        trans("Please enter Instrument Number :")
        Demat_no = str(input("Please enter Instrument Number :"))
        sleep(1)

        trans("Please enter your purchase Date :")
        pur_date2= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter your Number of units :")
        units1 = str(input("Please enter your Number of units :"))
        sleep(1)

        trans("Please enter Rate :")
        rate2 = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter your Invested Value :")
        invest_value2 = str(input("Please enter your invested Value :"))
        sleep(1)

        trans("Please enter current value :")
        curr_vall2 = str(input("Please enter your current  value :"))
        sleep(1)

        trans("Please enter Gain/Loss :")
        Gain2 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        trans("Please enter your Note :")
        Note4 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Crypto():
        print("You have selected to enter Cryptocurrency")
        trans("You have selected to enter Cryptocurrency")
        sleep(1)

        trans("Please enter the Currency Name :")
        Script2 = str(input("Please enter the Currency Name :"))
        sleep(1)
        
        trans("Please enter Wallet Name :")
        i2 = str(input("Please enter your Wallet Name :"))
        sleep(1)

        trans("Please enter purchase Date :")
        pur_date3= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter Number of units :")
        units2 = str(input("Please enter your Number of units :"))
        sleep(1)

        trans("Please enter Rate :")
        rate3 = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter your Invested Value :")
        invest_value3 = str(input("Please enter your invested Value :"))
        sleep(1)

        trans("Please enter current market value :")
        curr_vall3 = str(input("Please enter your current market value :"))
        sleep(1)

        trans("Please enter Gain/Loss :")
        Gain3 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        trans("Please enter your Note :")
        Note5 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Property_Details():
        print("You have selected to enter Property Details")
        trans("You have selected to enter Property Details")
        sleep(1)

        trans("Please enter the Property Type:")
        Script2 = str(input("Please enter the Property Type :"))
        sleep(1)
        
        print("Please fill property details :")
        trans("Please fill property details :")
        sleep(1)
        trans("Please enter your property :")
        property = str(input("Please enter your property :"))
        sleep(1)

        trans("Please enter your property Name :")
        Pro_name = str(input("Please enter your property Name :"))
        sleep(1)

        trans("Please enter your property Status :")
        Pro_status = str(input("Please enter your property status :"))
        sleep(1)

        trans("Please enter BHK No :")
        BHK = str(input("Please enter your BHK No :"))
        sleep(1)

        trans("Please enter your Size :")
        size = str(input("Please enter your Size :"))
        sleep(1)

        trans("Please enter Property Location country :")
        country = str(input("Please enter Property Location country :"))
        sleep(1)

        trans("Please enter state :")
        state= str(input("Please enter state :"))
        sleep(1)

        trans("Please enter city :")
        city= str(input("Please enter city :"))
        sleep(1)

        trans("Please enter sector :")
        sector= str(input("Please enter sector :"))
        sleep(1)

        trans("Please enter Gain/Loss :")
        Gain4 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        trans("Please enter your Note :")
        Note5 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Gold():
        print("You have selected to enter Gold & Jewellery")
        trans("You have selected to enter Gold & Jewellery")
        sleep(1)

        trans("Please enter the Jewellery type :")
        jewel = str(input("Please enter the Jewellery type :"))
        sleep(1)
        
        trans("Please enter Name :")
        namee = str(input("Please enter Name :"))
        sleep(1)

        trans("Please enter purchase Date :")
        pur_date5= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter purity in the scale of 1 karat to 24 karat:")
        purity = str(input("Please enter purity :"))
        sleep(1) 

        trans("Please enter weight :")
        weight = str(input("Please enter your weight :"))
        sleep(1)

        trans("Please enter Rate :")
        rate5 = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter your Invested Value :")
        invest_value5 = str(input("Please enter your invested Value :"))
        sleep(1)

        trans("Please enter current market value :")
        curr_vall5 = str(input("Please enter your current market value :"))
        sleep(1)

        trans("Please enter Gain/Loss :")
        Gain5 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        trans("Please enter your Note :")
        Note7 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Vehicles():
        print("You have selected to enter Vehicles")
        trans("You have selected to enter Vehicles")
        sleep(1)

        trans("Please enter the Vehicles Name :")
        vel_name = str(input("Please enter the Vehicles Name :"))
        sleep(1)
        
        trans("Please enter model :")
        model = str(input("Please enter Model :"))
        sleep(1)

        trans("Please enter Year :")
        year = str(input("Please enter Year :"))
        sleep(1)

        trans("Please enter purchase Date :")
        pur_date6= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter insurance till :")
        insure_till = str(input("Please enter insurance till :"))
        sleep(1) 

        trans("Please enter Registration till :")
        reg_till = str(input("Please enter Registration till :"))
        sleep(1)

        trans("Please enter Purchase Cost :")
        cost = str(input("Please Purchase Cost :"))
        sleep(1)

        trans("Please enter current Price :")
        curr_vall6 = str(input("Please enter your current Price :"))
        sleep(1)

        trans("Please enter your Note :")
        Note8 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Saving_Certificates():
        print("You have selected to enter Saving Certificates")
        trans("You have selected to enter Saving Certificates")
        sleep(1)

        trans("Please enter the Certificate type :")
        cer_type = str(input("Please enter the Certificate type :"))
        sleep(1)
        
        trans("Please enter Institution Name :")
        ist_name = str(input("Please enter Institution Name :"))
        sleep(1)

        trans("Please enter purchase Date :")
        pur_date7= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter No of Units :")
        units2 = str(input("Please enter No of Units :"))
        sleep(1)

        trans("Please enter Rate :")
        ratee = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter Invested Value :")
        cost1 = str(input("Please enter Invested Value :"))
        sleep(1)

        trans("Please enter current Value :")
        curr_vall7 = str(input("Please enter your current Value :"))
        sleep(1)

        trans("Please enter Gain :")
        Gainn = str(input("Please enter Gain :"))
        sleep(1)

        trans("Please enter your Note :")
        Note9 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Other_Assets():
        print("You have selected to enter Other Assets")
        trans("You have selected to enter Other Assets")
        sleep(1)

        trans("Please enter the Asset Type :")
        ast_type = str(input("Please enter the Asset Type :"))
        sleep(1)
        
        trans("Please enter Asset Name :")
        ast_name = str(input("Please enter Asset Name :"))
        sleep(1)

        trans("Please enter purchase Date :")
        pur_date8= str(input("Please enter your purchase Date :"))
        sleep(1)

        trans("Please enter No of Units :")
        units3 = str(input("Please enter No of Units :"))
        sleep(1)

        trans("Please enter Rate :")
        ratee1 = str(input("Please enter Rate :"))
        sleep(1)

        trans("Please enter Invested Value :")
        inv_value = str(input("Please enter Invested Value :"))
        sleep(1)

        trans("Please enter current Value :")
        curr_vall8 = str(input("Please enter your current Value :"))
        sleep(1)

        trans("Please enter Gain :")
        Gain1 = str(input("Please enter Gain :"))
        sleep(1)

        trans("Please enter your Note :")
        Note10 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Credit_Cards():
        print("You have selected to enter Credit Cards")
        trans("You have selected to enter Credit Cards")
        sleep(1)

        trans("Please enter the Bank :")
        Bank1 = str(input("Please enter the Bank :"))
        sleep(1)
        
        trans("Please enter Card Number :")
        card_no = str(input("Please enter Card Number :"))
        sleep(1)

        trans("Please enter Card Limit :")
        card_limit= str(input("Please enter your Card Limit :"))
        sleep(1)

        trans("Please enter Outstanding :")
        outstanding = str(input("Please enter Outstanding :"))
        sleep(1)

        trans("Please enter minimum value :")
        min_value = str(input("Please enter minimum value :"))
        sleep(1)

        trans("Please enter billing Cycle :")
        bii_cycle = str(input("Please enter your billing Cycle :"))
        sleep(1)

        trans("Please enter billing Date :")
        bill_date = str(input("Please enter billing Date :"))
        sleep(1)

        trans("Please enter your Due Date :")
        Due_date = str(input("Please enter your Due Date :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Financial_Institutions():
        print("You have selected to enter Financial Institutions")
        trans("You have selected to enter Financial Institutions")
        sleep(1)

        trans("Please enter the Financial Institutions Name :")
        Bank1 = str(input("Please enter the Financial Institutions Name :"))
        sleep(1)
        
        trans("Please enter Loan Facility :")
        loan_fac = str(input("Please enter Loan Facility :"))
        sleep(1)

        trans("Please enter Loan account Number :")
        loan_no= str(input("Please enter Loan account Number :"))
        sleep(1)

        trans("Please enter Start Date :")
        start_date = str(input("Please enter Start Date :"))
        sleep(1)

        trans("Please enter minimum value :")
        min_value1 = str(input("Please enter minimum value :"))
        sleep(1)

        trans("Please enter Loan Amount :")
        Loan_amt = str(input("Please enter your Loan Amount :"))
        sleep(1)

        trans("Please enter No of EMI :")
        No_emi = str(input("Please enter No of EMI :"))
        sleep(1)

        trans("Please enter your EMI Cycle :")
        emi_cyc = str(input("Please enter your EMI Cycle :"))
        sleep(1)

        trans("Please enter your EMI Amount :")
        emi_amount = str(input("Please enter your EMI Amount :"))
        sleep(1)

        trans("Please enter your EMI Due On :")
        Due_date1 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Private_Lenders():
        print("You have selected to enter Private Lenders")
        trans("You have selected to enter Private Lenders")
        sleep(1)

        trans("Please enter the Private Lender Name :")
        lender = str(input("Please enter the Private Lender Name :"))
        sleep(1)
        
        trans("Please enter Loan Facility :")
        loan_fac1= str(input("Please enter Loan Facility :"))
        sleep(1)

        trans("Please enter Start Date :")
        start_date1 = str(input("Please enter Start Date :"))
        sleep(1)

        trans("Please enter Loan Amount :")
        Loan_amt1 = str(input("Please enter your Loan Amount :"))
        sleep(1)

        trans("Please enter No of EMI :")
        No_emi1 = str(input("Please enter No of EMI :"))
        sleep(1)

        trans("Please enter your EMI Cycle :")
        emi_cyc1 = str(input("Please enter your EMI Cycle :"))
        sleep(1)

        trans("Please enter your EMI Amount :")
        emi_amount1 = str(input("Please enter your EMI Amount :"))
        sleep(1)

        trans("Please enter your EMI Due On :")
        Due_date2 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Friends():
        print("You have selected to enter Friends & Relatives")
        trans("You have selected to enter Friends & Relatives")
        sleep(1)

        trans("Please enter the Name :")
        lender1 = str(input("Please enter the Private Lender Name :"))
        sleep(1)

        trans("Please enter the relationship with the lender :")
        relationship = str(input("Please enter the relationship :"))
        sleep(1)
        
        trans("Please enter Loan Facility :")
        loan_fac2= str(input("Please enter Loan Facility :"))
        sleep(1)

        trans("Please enter Start Date :")
        start_date2 = str(input("Please enter Start Date :"))
        sleep(1)

        trans("Please enter Loan Amount :")
        Loan_amt2 = str(input("Please enter your Loan Amount :"))
        sleep(1)

        trans("Please enter No of EMI :")
        No_emi2 = str(input("Please enter No of EMI :"))
        sleep(1)

        trans("Please enter your EMI Cycle :")
        emi_cyc2 = str(input("Please enter your EMI Cycle :"))
        sleep(1)

        trans("Please enter your EMI Amount :")
        emi_amount2 = str(input("Please enter your EMI Amount :"))
        sleep(1)

        trans("Please enter your EMI Due On :")
        Due_date3 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def insurance_policies():
        print("You have selected to enter new Insurance Policies")
        trans("You have selected to enter new Insurance Policies")
        sleep(1)

        trans("Please Select your insurance Policies :")
        ins_pol1 = str(input("Please Select your insurance Policies :"))
        sleep(1)
        
        trans("Please enter your Company Name :")
        com_namee1 = str(input("Please enter your Company Name :"))
        sleep(1)

        trans("Please enter your Policy Name :")
        Pol_name1 = str(input("Please enter your Policy Name :"))
        sleep(1)

        trans("Please enter your Policy Number :")
        pol_no1 = str(input("Please enter your Policy Number :"))
        sleep(1)

        trans("Please enter your Start Date :")
        srt_datee1= str(input("Please enter your Start Date :"))
        sleep(1)

        trans("Please enter your Premium Amount :")
        amountt1 = str(input("Please enter your Premium Amount :"))
        sleep(1)

        trans("Please enter your Recurrence :")
        rec1 = str(input("Please enter your Recurrence :"))
        sleep(1)

        trans("Please enter your premium due :")
        due1 = str(input("Please enter your premium due :"))
        sleep(1)

        trans("Please enter your Sum Assured :")
        sum_assured1 = str(input("Please enter your Sum Assured :"))
        sleep(1)

        trans("Please enter your Maturity Date :")
        mat_date1 = str(input("Please enter your Maturity Date :"))
        sleep(1)

        trans("Please enter your Maturity Value :")
        mat_val1 = str(input("Please enter your Maturity Value :"))
        sleep(1)

        trans("Please enter your Note :")
        Note11 = str(input("Please enter your Note :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def SIP_Instalments():
        print("You have selected to enter SIP Instalments")
        trans("You have selected to enter SIP Instalments")
        sleep(1)

        trans("Please enter the company Name :")
        n2 = str(input("Please enter the company Name :"))
        sleep(1)

        trans("Please enter the scheme name :")
        Scheme1 = str(input("Please enter the scheme name :"))
        sleep(1)

        trans("Please enter Start Date :")
        start_date4 = str(input("Please enter Start Date :"))
        sleep(1)

        trans("Please enter End Date :")
        End_date1 = str(input("Please enter End Date :"))
        sleep(1)

        trans("Please enter SIP Amount :")
        SIP_amt2 = str(input("Please enter your SIP Amount :"))
        sleep(1)

        trans("Please enter your EMI Due On :")
        Due_date5 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Recurring():
        print("You have selected to enter Recurring Deposits")
        trans("You have selected to enter Recurring Deposits")
        sleep(1)

        trans("Please enter the bank Name :")
        b2 = str(input("Please enter the bank Name :"))
        sleep(1)

        trans("Please enter the scheme name :")
        Scheme2 = str(input("Please enter the scheme name :"))
        sleep(1)

        trans("Please enter Start Date :")
        start_date5 = str(input("Please enter Start Date :"))
        sleep(1)

        trans("Please enter Maturity Date :")
        Maturity_date1 = str(input("Please enter Maturity Date :"))
        sleep(1)

        trans("Please enter Deposit Amount :")
        dep_amt2 = str(input("Please enter your Deposit Amount :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Other():
        print("You have selected to enter Other Details ")
        trans("You have selected to enter Other Details")
        sleep(1)

        trans("Please enter the Type :")
        Type1 = str(input("Please enter the Type :"))
        sleep(1)

        trans("Please enter the name :")
        n3 = str(input("Please enter the name :"))
        sleep(1)

        trans("Please enter Amount Payable :")
        payable = str(input("Please enter Amount Payable :"))
        sleep(1)

        trans("Please enter Recurrence :")
        rec2 = str(input("Please enter Recurrence :"))
        sleep(1)

        trans("Please enter Due Date :")
        due_date2 = str(input("Please enter Due Date :"))
        sleep(1)

        trans("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

#######################################
class Bank_balance:
    def bank_balance():
        print('Hi, Welcome! You have selected to check your Bank Balance!')
        trans('Hi, Welcome! You have selected to check your Bank Balance!')
        sleep(1)

        Bank_Balance= 450000
        cash_balance= 400000

        Total_bal= Bank_Balance + cash_balance

        print('Your Current Bank Balance is ' + str(Bank_Balance) + " & your cash balance is " + str(cash_balance))
        trans('Your Current Bank Balance is ' + str(Bank_Balance) + " & your cash balance is " + str(cash_balance))
        sleep(1)

    def Newrecord():
        print('Hi, Welcome! You have selected to add new record to your bank balance!')
        trans('Hi, Welcome! You have selected to add new record to your bank balance!')
        sleep(1)

        print('Please select the following that you want to proceed with : ')
        trans('Please select the following that you want to proceed with : ')
        print('1) Bank Balance')
        print('2) Cash Balance')
        bal= takeCommand().lower()

        if 'bank balance' in bal:
            print('Hi, Welcome! You have selected to add new record to your bank balance!')
            trans('Hi, Welcome! You have selected to add new record to your bank balance!')
            sleep(1)

            print("You may proceed to edit bank balance from below or add new bank balance details : ")
            trans("You may proceed to edit bank balance from below or add new bank balance details : ")
            sleep(1)
            Bank_balance.bank_bal_record()
        elif 'cash balance' in bal:
            print('Hi, Welcome! You have selected to add new record to your cash balance!')
            trans('Hi, Welcome! You have selected to add new record to your cash balance!')
            sleep(1)

            print("You may proceed to edit cash balance from below or add new cash balance details : ")
            trans("You may proceed to edit cash balance from below or add new cash balance details : ")
            sleep(1)
            Bank_balance.cash_bal_record()
        sleep(1)

    def bank_bal_record():
        trans("Please enter the Bank :")
        Bank1 = str(input("Please enter the Bank :"))
        sleep(1)

        trans("Please enter the Account Type :")
        acc_type = str(input("Please enter the Account Type :"))
        sleep(1)

        trans("Please enter the Account Number :")
        acc_no = str(input("Please enter the Account Number :"))
        sleep(1)

        trans("Please enter the Balance :")
        bal1 = str(input("Please enter the Balance :"))
        sleep(1)

        trans("Please enter the Date Updated :")
        date_upt = str(input("Please enter the Date Updated :"))
        sleep(1)

        print('Thanks you have successfully updated your bank balance!')
        trans('Thanks you have successfully updated your bank balance!')
        sleep(1)

    def cash_bal_record():
        trans("Please enter the Balance Amount :")
        bal1 = str(input("Please enter the Balance Amount :"))
        sleep(1)

        trans("Please enter the Date Updated :")
        date_upt = str(input("Please enter the Date Updated :"))
        sleep(1)

        print('Thanks you have successfully updated your cash balance!')
        trans('Thanks you have successfully updated your cash balance!')
        sleep(1)

#######################################
class Wallet:
    def Wallet():
        print('Hi, Welcome! You have selected to check your Wallet!')
        trans('Hi, Welcome! You have selected to check your Wallet!')
        sleep(1)

        Wallet_bal= 450000

        print('Your Current Wallet Balance is ' + str(Wallet_bal))
        trans('Your Current Wallet Balance is ' + str(Wallet_bal))
        sleep(1)
        while True:
            print('Do you want to TopUp your wallet or do Payment transfer your balance : ')
            trans('Do you want to TopUp your wallet or do Payment transfer your balance : ')
            print('1) Yes')
            print('2) No')
            sleep(1)
            in1= takeCommand().lower()
            if 'yes' in in1:
                print('Hi, You have selected to do transaction in your Wallet!')
                trans('Hi, You have selected to do transaction in your Wallet!')
                sleep(1)
                while True:
                    print('Please select the following that you want to proceed with : ')
                    trans('Please select the following that you want to proceed with : ')
                    print('1) Top-Up Wallet')
                    print('2) Wallet to Wallet Transfer')
                    print('3) Own Bank Transfer')
                    trans= takeCommand().lower()
                    if 'topup wallet' in trans or 'top up wallet' in trans or '1' in trans:
                        print("You have selected to topup your wallet!")
                        trans("You have selected to topup your wallet!")
                        sleep(1)

                        trans("Please enter the amount that you want to topup with : ")
                        topup_amt = str(input("Please enter the amount that you want to topup with : "))
                        sleep(1)
                        Wallet.Payment()
                        break
                    elif 'wallet to wallet transfer' in trans or 'wallet to wallet transfer' in trans:
                        print("You have selected to topup your wallet!")
                        trans("You have selected to topup your wallet!")
                        sleep(1)

                        trans("Please enter the contact number linked to other wallet that you want to transfer to : ")
                        contact_no = str(input("Please enter the the contact number linked to other wallet : "))
                        sleep(1)

                        trans("Please enter the name of the person that you want to transfer to : ")
                        topup_amt = str(input("Please enter the the name of the person to : "))
                        sleep(1)

                        trans("Please enter the amount that you want to transfer to other wallet : ")
                        topup_amt = str(input("Please enter the amount that you want to transfer : "))
                        sleep(1)

                        print('Thanks you have successfully transfered your payment to other wallet')
                        trans('Thanks you have successfully transfered your payment to other wallet')
                        sleep(1)
                        break
                    elif 'Own Bank Transfer' in trans:
                        print("You have selected to Transfer to your Own Bank!")
                        trans("You have selected to Transfer to your Own Bank!")
                        sleep(1)

                        trans("Please enter the account number : ")
                        acc_no1 = str(input("Please enter the account number : "))
                        sleep(1)

                        trans("Please enter the account type : ")
                        acc_type = str(input("Please enter the account type : "))
                        sleep(1)

                        trans("Please enter the IFSC Code : ")
                        IFSC = str(input("Please enter the IFSC Code : "))
                        sleep(1)

                        trans("Please enter the MICR Code : ")
                        MICR = str(input("Please enter the IFSC Code : "))
                        sleep(1)

                        trans("Please enter the amount that you want to transfer : ")
                        trans_amt = str(input("Please enter the amount that you want to transfer : "))
                        sleep(1)

                        print('Thanks you have successfully transfered your payment to your bank')
                        trans('Thanks you have successfully transfered your payment to your bank')
                        sleep(4)
                        break
                break
            elif 'no' in in1:
                break
                sleep(4)

    def Payment():
        print("Please select the following options to proceed with payment :")
        trans("Please select the following options to proceed with payment :")
        sleep(1)
        while True:
            print('1) UPI')
            print('2) Debit Card')
            print('3) Credit Card')
            payment= takeCommand().lower()
            if 'u p i' in payment:
                print("You have selected to proceed with UPI")
                trans("You have selected to proceed with UPI")
                sleep(1)

                trans("Please enter the phone number :")
                phone_no = str(input("Please enter the phone number :"))
                sleep(1)

                trans("Please enter the beneficiary name :")
                bene_name = str(input("Please enter the beneficiary name :"))
                sleep(1)

                print('Thanks you have successfully done payment with UPI')
                trans('Thanks you have successfully done payment with UPI')
                sleep(1)
                break
            elif 'debit card' in payment:
                print("You have selected to proceed with debit card")
                trans("You have selected to proceed with debit card")
                sleep(1)

                trans("Please enter the card number :")
                card_no = str(input("Please enter the card number :"))
                sleep(1)

                trans("Please enter the beneficiary name :")
                bene_name1 = str(input("Please enter the beneficiary name :"))
                sleep(1)

                trans("Please enter the expiry date :")
                exp_date = str(input("Please enter the expiry date :"))
                sleep(1)

                trans("Please enter the CVV Code :")
                cvv_code = str(input("Please enter the CVV Code :"))
                sleep(1)

                print('Thanks you have successfully done payment with your debit card! ')
                trans('Thanks you have successfully done payment with your debit card!')
                sleep(1)
                break
            elif 'credit card' in payment:
                print("You have selected to proceed with Credit Card")
                trans("You have selected to proceed with Credit Card")
                sleep(1)

                trans("Please enter the Credit card number :")
                card_no1 = str(input("Please enter the Credit card number :"))
                sleep(1)

                trans("Please enter the beneficiary name :")
                bene_name2 = str(input("Please enter the beneficiary name :"))
                sleep(1)

                trans("Please enter the expiry date :")
                exp_date1 = str(input("Please enter the expiry date :"))
                sleep(1)

                trans("Please enter the CVV Code :")
                cvv_code1 = str(input("Please enter the CVV Code :"))
                sleep(1)

                print('Thanks you have successfully done payment with your Credit card! ')
                trans('Thanks you have successfully done payment with your Credit card!')
                sleep(1)
                break

#######################################
class Money_Transfer:
    def Money_Transfer():
        print('Hi, Welcome! You have selected to money transfer section')
        trans('Hi, Welcome! You have selected to money transfer section')
        sleep(1)

        print('Please select the following that you want to proceed with : ')
        trans('Please select the following that you want to proceed with : ')
        print('1) Send Money')
        print('2) Receive Money')
        money_trans= takeCommand().lower()
        if 'send money' in money_trans:
            payables=2000
            money_sent=500
            print('Your payables are ' + payables + "& your total money sent is " + money_sent)
            trans('Your payables are ' + payables + "& your total money sent is " + money_sent)
            sleep(1)

            print('Do you want to send money : ')
            trans('Do you want to send money : ')
            print('1) Yes')
            print('2) No')
            sleep(1)
            send_money= takeCommand().lower()
            if 'yes' in send_money:
                print('You have selected to send money : ')
                trans('You have selected to send money : ')
                sleep(1)
                trans("Please enter the amount that you want to send : ")
                amount_send = str(input("Please enter the amount that you want to send : "))
                sleep(1)
                print('Thanks you have successfully sent money')
                trans('Thanks you have successfully sent money')
                sleep(1)
            elif 'no' in send_money:
                print('You do want to send money!')
                trans('You do want to send money!')
        elif 'receive money' in money_trans:
            print('Hi, Welcome! You have selected to receive money')
            trans('Hi, Welcome! You have selected to receive money')
            sleep(1)
            
################################
class Bill_payment:
    def Bill_payment():
        print('Hi, Welcome! You have selected to Bill Payments')
        trans('Hi, Welcome! You have selected to Bill Payments')
        sleep(1)

        while True:
            print('Please select the following that you want to proceed with : ')
            trans('Please select the following that you want to proceed with : ')
            print('1) Recharge Mobile')
            print('2) Postpaid Mobile Bill')
            print('3) DTH')
            print('4) Broadband/ landline bill')
            print('5) Cable TV')
            print('6) Electricity Bills')
            print('7) Gas Bills')
            print('8) Water Bill')
            print('9) EMI Payments')
            print('10) Card Payments')
            bill_pay= takeCommand().lower()
            if "recharge mobile" in bill_pay:
                print('Hi, Welcome! You have selected to Recharge Mobile')
                trans('Hi, Welcome! You have selected to Recharge Mobile')
                sleep(1)

                trans("Please enter the mobile no that you want to recharge : ")
                rech_mob = str(input("Please enter the mobile no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your mobile!')
                trans('Thanks you have successfully recharged your mobile!')
                sleep(1)
                break
            elif 'postpaid  mobile bill' in bill_pay:
                print('Hi, Welcome! You have selected to Postpaid Mobile Bill')
                trans('Hi, Welcome! You have selected to Postpaid Mobile Bill')
                sleep(1)

                trans("Please enter the mobile no that you want to recharge : ")
                postpaid_mob = str(input("Please enter the mobile no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your postpaid mobile!')
                trans('Thanks you have successfully recharged your postpaid mobile!')
                sleep(1)
                break
            elif 'dth' in bill_pay:
                print('Hi, Welcome! You have selected to DTH Recharge')
                trans('Hi, Welcome! You have selected to DTH Recharge')
                sleep(1)

                trans("Please enter the DTH Operator that you use : ")
                dth_op = str(input("Please enter the DTH Operator that you use: "))
                sleep(1)

                trans("Please enter your DTH subscriber no that you want to recharge : ")
                dth_sub = str(input("Please enter your DTH subscriber no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your DTH!')
                trans('Thanks you have successfully recharged your DTH!')
                sleep(1)
                break
            elif 'broadband bill' in bill_pay:
                print('Hi, Welcome! You have selected to Broadband/ landline bill')
                trans('Hi, Welcome! You have selected to Broadband/ landline bill')
                sleep(1)

                trans("Please enter the broadband no that you want to recharge : ")
                brodband_no = str(input("Please enter the broadband or landline no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your postpaid mobile!')
                trans('Thanks you have successfully recharged your postpaid mobile!')
                sleep(1)
                break
            elif 'cable tv' in bill_pay:
                print('Hi, Welcome! You have selected to Cable TV')
                trans('Hi, Welcome! You have selected to Cable TV')
                sleep(1)

                trans("Please enter the cable tv Operator that you use : ")
                cable_op = str(input("Please enter the cable tv Operator that you use: "))
                sleep(1)

                trans("Please enter your cable tv subscriber no that you want to recharge : ")
                cable_sub = str(input("Please enter your Dcable tvTH subscriber no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your cable tv!')
                trans('Thanks you have successfully recharged your cable tv!')
                sleep(1)
                break        
            elif 'electricity bills' in bill_pay:
                print('Hi, Welcome! You have selected to Electricity Bills')
                trans('Hi, Welcome! You have selected to Electricity Bills')
                sleep(1)

                trans("Please enter your State : ")
                ele_state = str(input("Please enter your State "))
                sleep(1)

                trans("Please enter your City : ")
                ele_city = str(input("Please enter your city "))
                sleep(1)

                trans("Please enter your electricity distributer : ")
                ele_dis = str(input("Please enter your electricity distributer  "))
                sleep(1)

                trans("Please enter your connection type : ")
                ele_conn = str(input("Please enter your connection type  "))
                sleep(1)

                trans("Please enter your CA Number : ")
                ele_CA = str(input("Please enter your CA Number : "))
                sleep(1)

                print('Thanks you have successfully paid your electricity bills!')
                trans('Thanks you have successfully paid your electricity bills!')
                sleep(1)
                break
            elif 'gas bills' in bill_pay:
                print('Hi, Welcome! You have selected to Gas Bills')
                trans('Hi, Welcome! You have selected to Gas Bills')
                sleep(1)

                trans("Please enter your State : ")
                gas_state = str(input("Please enter your State "))
                sleep(1)

                trans("Please enter your City : ")
                gas_city = str(input("Please enter your city "))
                sleep(1)

                trans("Please enter your Gas Supplier : ")
                gas_sup = str(input("Please enter your Gas Supplier  "))
                sleep(1)

                trans("Please enter your customer ID : ")
                gas_ID = str(input("Please enter your customer ID :  "))
                sleep(1)

                print('Thanks you have successfully paid your Gas bills!')
                trans('Thanks you have successfully paid your Gas bills!')
                sleep(1)
                break
            elif 'water bill' in bill_pay:
                print('Hi, Welcome! You have selected to proceed with water Bill')
                trans('Hi, Welcome! You have selected to proceed with water Bill')
                sleep(1)

                trans("Please enter your State : ")
                water_state = str(input("Please enter your State : "))
                sleep(1)

                trans("Please enter your City : ")
                water_city = str(input("Please enter your city : "))
                sleep(1)

                trans("Please enter your Board : ")
                water_sup = str(input("Please enter your Board : "))
                sleep(1)

                trans("Please enter your customer ID : ")
                water_ID = str(input("Please enter your customer ID :  "))
                sleep(1)

                print('Thanks you have successfully paid your water bills!')
                trans('Thanks you have successfully paid your water bills!')
                sleep(1)
                break
            elif 'emi payments' in bill_pay:
                print('Hi, Welcome! You have selected to EMI Payments')
                trans('Hi, Welcome! You have selected to EMI Payments')
                sleep(1)

                trans("Please enter your Financial Institution : ")
                Fin_Ins = str(input("Please enter your Financial Institution : "))
                sleep(1)

                trans("Please enter your loan Account No : ")
                loan_acc_no = str(input("Please enter your loan Account No :  "))
                sleep(1)

                print('Thanks you have successfully paid your EMI Payments!')
                trans('Thanks you have successfully paid your EMI Payments!')
                sleep(1)
                break
            elif 'card payments' in bill_pay:
                print('Hi, Welcome! You have selected to card payments')
                trans('Hi, Welcome! You have selected to Card Payments')
                sleep(1)
            trans('Please select the correct product options')
    ################################

class Insurance:
    def Insurance():
        print('Hi, Welcome! You have selected to Insurance section')
        trans('Hi, Welcome! You have selected to Insurance section')
        sleep(1)
        print("Please select the insurance that you want to proceed with : ")
        trans("Please select the insurance that you want to proceed with : ")
        print('1) Life Insurance')
        print('2) Health Insurance')
        print("3) Vehicle insurance")
        print('2) Other Insurance')
        print("3) Investment Plans")
        insurance = takeCommand().lower()
        if 'life insurance' in insurance:
            sleep(1)
        elif 'health insurance' in insurance:
            sleep(1)
        elif 'vehicle insurance' in insurance:
            sleep(1)
        elif 'other insurance' in insurance:
            sleep(1)
        elif 'investment plans' in insurance:
            sleep(1)

###############################
class Managerevenue:
    def manage_revenue():
        print('Hi, Welcome! You have selected to manage revenue')
        trans('Hi, Welcome! You have selected to manage revenue')
        sleep(1)

        Total_Revenue = 450000
        Total_receivables= 20000
        Overdue= 900
        Projects=1

        print('Your Current total revenue balance is ' + str (Total_Revenue) + ' from which total receivables is ' + str(Total_receivables) + ' and Overdue is ' + Overdue )
        trans('Your Current total revenue balance is ' + str (Total_Revenue) + ' from which total receivables is ' + str(Total_receivables) + ' and Overdue is ' + Overdue )

        print('Please check the following detail of your generated revenue and other important metrics:')
        trans('Please check the following detail of your generated revenue and other important metrics:')
        while True:
            print("Do you want to add revenue record? :")
            trans("Do you want to add revenue record? :")
            print('1) Yes')
            print('2) No')
            t1= takeCommand().lower()
            if 'yes' in t1:
                print('You have selected to add revenue record!')
                trans('You have selected to add revenue record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    trans("Please select the following option that you want to proceed with:")
                    print('1) Record Revenue')
                    print('2) view revenue')
                    r1=takeCommand().lower()
                    if 'record revenue' in r1:
                        print("You have selected to proceed to record revenue : ")
                        trans("You have selected to proceed to record revenue : ")
                        Managerevenue.record_revenue()
                    elif 'view revenue' in r1:
                        print("You have selected to proceed to view revenue : ")
                        trans("You have selected to proceed to view revenue : ")
                        sleep(1)
                        print("You may view your revenue record from below and also share the receipt : ")
                        trans("You may view your revenue record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add revenue record!')
                trans('You have selected to not add revenue record!')
                break
            
    def record_revenue():
        print('You have selected to add revenue record for your client :')
        trans('You have selected to add revenue record for your client :')

        print('You may edit your invoice no and date from below : ')
        trans('You may edit your invoice no and date from below : ')

        print('Please enter your client name :')
        trans('Please enter your client name :')
        Managerevenue.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        trans('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new service record? :")
            trans("Do you want to add new service record? :")
            print('1) Yes')
            print('2) No')
            ser1=takeCommand().lower()
            if 'yes' in ser1:
                print("Please enter your item category : ")
                trans("Please enter your item category : ")

                print("Please enter your item Name :")
                trans("Please enter your item Name :")

                print("Please enter the listed rate: :")
                trans("Please enter the listed rate: :")

                print("Please enter the offer rate: :")
                trans("Please enter the offer rate: :")

                print("Please select the following to proceed :")
                trans("Please select the following to proceed :")
                print("Include Tax :")
                print("Exclude Tax :")

                print("Please enter HSN Code :")
                trans("Please enter HSN Code :")

                print("Please enter GST Rate: :")
                trans("Please enter GST Rate: :")

                print("Thanks, you have successfully added your service :")
                trans("Thanks, you have successfully added your service :")
            elif 'no' in ser1:
                print('You have selected to not add revenue record!')
                trans('You have selected to not add revenue record!')
                break
###############################

class Manageexpenses:
    def manage_Expenses():
        print('Hi, Welcome! You have selected to manage Expenses')
        trans('Hi, Welcome! You have selected to manage Expenses')
        sleep(1)

        Total_Expenses = 450000
        Total_payables= 20000
        Overdue= 900
        Projects=1

        print('Your Current total Expenses balance is ' + str (Total_Expenses) + ' from which total receivables is ' + str(Total_payables) + ' and Overdue is ' + Overdue )
        trans('Your Current total Expenses balance is ' + str (Total_Expenses) + ' from which total receivables is ' + str(Total_payables) + ' and Overdue is ' + Overdue )

        print('Please check the following detail of your generated Expenses and other important metrics:')
        trans('Please check the following detail of your generated Expenses and other important metrics:')
        while True:
            print("Do you want to add Expenses record? :")
            trans("Do you want to add Expenses record? :")
            print('1) Yes')
            print('2) No')
            t1= takeCommand().lower()
            if 'yes' in t1:
                print('You have selected to add Expenses record!')
                trans('You have selected to add Expenses record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    trans("Please select the following option that you want to proceed with:")
                    print('1) Record Expenses')
                    print('2) view Expenses')
                    r1=takeCommand().lower()
                    if 'record Expenses' in r1:
                        print("You have selected to proceed to record Expenses : ")
                        trans("You have selected to proceed to record Expenses : ")
                        Manageexpenses.record_Expenses()
                    elif 'view Expenses' in r1:
                        print("You have selected to proceed to view Expenses : ")
                        trans("You have selected to proceed to view Expenses : ")
                        sleep(1)
                        print("You may view your Expenses record from below and also share the receipt : ")
                        trans("You may view your Expenses record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add Expenses record!')
                trans('You have selected to not add Expenses record!')
                break
            
    def record_Expenses():
        print('You have selected to add Expenses record for your client :')
        trans('You have selected to add Expenses record for your client :')

        print('You may edit your invoice no and date from below : ')
        trans('You may edit your invoice no and date from below : ')

        print('Please enter your client name :')
        trans('Please enter your client name :')
        Manageexpenses.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        trans('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new Expenses record? :")
            trans("Do you want to add new Expenses record? :")
            print('1) Yes')
            print('2) No')
            ser2=takeCommand().lower()
            if 'yes' in ser2:
                print("Please enter your Expenses Name :")
                trans("Please enter your Expenses Name :")

                print("Please enter the Expenses amount: :")
                trans("Please enter the Expenses amount: :")

                print("Please enter the offer rate: :")
                trans("Please enter the offer rate: :")

                print("Please select the following to proceed :")
                trans("Please select the following to proceed :")
                print("Price with GST :")
                print("Price without GST")

                print("Thanks, you have successfully added your service :")
                trans("Thanks, you have successfully added your service :")
            elif 'no' in ser2:
                print('You have selected to not add Expenses record!')
                trans('You have selected to not add Expenses record!')
                break

###############################
class Manageorder:
    def manage_orders():
        print('Hi, Welcome! You have selected to manage Orders')
        trans('Hi, Welcome! You have selected to manage Orders')
        sleep(1)

        Total_Orders = 450000
        pending_Orders= 20000
        Cancelled= 900
        closed_orders=100

        print('Your Current total Orders is ' + str (Total_Orders) + ' from which pending orders is ' + str(pending_Orders) + ' and closed order is ' + closed_orders )
        trans('Your Current total Orders is ' + str (Total_Orders) + ' from which total receivables is ' + str(pending_Orders) + ' and Overdue is ' + closed_orders )

        print('Please check the following detail of your generated Orders and other important metrics:')
        trans('Please check the following detail of your generated Orders and other important metrics:')
        while True:
            print("Do you want to add Orders record? :")
            trans("Do you want to add Orders record? :")
            print('1) Yes')
            print('2) No')
            t1= takeCommand().lower()
            if 'yes' in t1:
                print('You have selected to add Orders record!')
                trans('You have selected to add Orders record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    trans("Please select the following option that you want to proceed with:")
                    print('1) Record Orders')
                    print('2) view Orders')
                    r1=takeCommand().lower()
                    if 'record orders' in r1:
                        print("You have selected to proceed to record Orders : ")
                        trans("You have selected to proceed to record Orders : ")
                        Manageorder.record_Expenses()
                    elif 'view orders' in r1:
                        print("You have selected to proceed to view Orders : ")
                        trans("You have selected to proceed to view Orders : ")
                        sleep(1)
                        print("You may view your Orders record from below and also share the receipt : ")
                        trans("You may view your Orders record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add Orders record!')
                trans('You have selected to not add Orders record!')
                break
            
    def record_Orders():
        print('You have selected to add Orders record for your client :')
        trans('You have selected to add Orders record for your client :')

        print('You may edit your Orders no and date from below : ')
        trans('You may edit your Orders no and date from below : ')

        print('Please enter your client name :')
        trans('Please enter your client name :')
        Manageorder.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        trans('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new Orders record? :")
            trans("Do you want to add new Orders record? :")
            print('1) Yes')
            print('2) No')
            ser2=takeCommand().lower()
            if 'yes' in ser2:
                print("Please enter your service name : ")
                trans("Please enter your service name : ")

                print("Please enter your sales Price :")
                trans("Please enter your sales Price :")

                print("Please select the following to proceed :")
                trans("Please select the following to proceed :")
                print("Price with GST :")
                print("Price without GST")

                print("Please enter HSN Code :")
                trans("Please enter HSN Code :")

                print("Please enter GST Rate: :")
                trans("Please enter GST Rate: :")

                print("Thanks, you have successfully added your service :")
                trans("Thanks, you have successfully added your service :")
            elif 'no' in ser2:
                print('You have selected to not add Orders record!')
                trans('You have selected to not add Orders record!')
                break

##########################################

class Managequotation:
    def manage_quotation():
        print('Hi, Welcome! You have selected to manage quotation :')
        trans('Hi, Welcome! You have selected to manage quotation')
        sleep(1)

        Total_quotation = 450000
        pending_quotation= 20000
        Cancelled= 900
        total_orders=100

        print('Your Current total quotation is ' + str (Total_quotation) + ' from which pending quotation is ' + str(pending_quotation) + ' and total order is ' + total_orders )
        trans('Your Current total quotation is ' + str (Total_quotation) + ' from which pending quotation is ' + str(pending_quotation) + ' and total order is ' + total_orders )

        print('Please check the following detail of your generated quotation and other important metrics:')
        trans('Please check the following detail of your generated quotation and other important metrics:')
        while True:
            print("Do you want to add quotation record? :")
            trans("Do you want to add quotation record? :")
            print('1) Yes')
            print('2) No')
            t1= takeCommand().lower()
            if 'yes' in t1:
                print('You have selected to add quotation record!')
                trans('You have selected to add quotation record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    trans("Please select the following option that you want to proceed with:")
                    print('1) Record quotation')
                    print('2) view quotation')
                    r1=takeCommand().lower()
                    if 'record quotation' in r1:
                        print("You have selected to proceed to record quotation : ")
                        trans("You have selected to proceed to record quotation : ")
                        Managequotation.record_Expenses()
                    elif 'view quotation' in r1:
                        print("You have selected to proceed to view quotation : ")
                        trans("You have selected to proceed to view quotation : ")
                        sleep(1)
                        print("You may view your quotation record from below and also share the receipt : ")
                        trans("You may view your quotation record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add quotation record!')
                trans('You have selected to not add quotation record!')
                break
            
    def record_Orders():
        print('You have selected to add quotation record for your client :')
        trans('You have selected to add quotation record for your client :')

        print('You may edit your quotation no and date from below : ')
        trans('You may edit your quotation no and date from below : ')

        print('Please enter your client name :')
        trans('Please enter your client name :')
        Managequotation.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        trans('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new quotation record? :")
            trans("Do you want to add new quotation record? :")
            print('1) Yes')
            print('2) No')
            ser2=takeCommand().lower()
            if 'yes' in ser2:
                print("Please enter your service name : ")
                trans("Please enter your service name : ")

                print("Please enter your rate :")
                trans("Please enter your rate :")

                print("Please select the following to proceed :")
                trans("Please select the following to proceed :")
                print("Price with GST :")
                print("Price without GST")

                print("Please enter HSN Code :")
                trans("Please enter HSN Code :")

                print("Please enter GST Rate: :")
                trans("Please enter GST Rate: :")

                print("Thanks, you have successfully added your service :")
                trans("Thanks, you have successfully added your service :")
            elif 'no' in ser2:
                print('You have selected to not add quotation record!')
                trans('You have selected to not add quotation record!')
                break

###############################

class leadgen:
    def lead():
        print('Hi, Welcome! You have selected to check your Leads generated: ')
        trans('Hi, Welcome! You have selected to check your Leads generated: ')
        sleep(1)

        print('You may check or edit your Leads generated from below and add new leads : ')
        trans('You may check or edit your Leads generated from below and add new leads : ')
        sleep(1)

    def lead_form():
        trans("Please Select your lead name :")
        lead_name = str(input("Please Select your lead name :"))
        sleep(1)

###############################
class Notification:
    def notification():
        print('Hi, Welcome! You have selected to check your notification preference: ')
        trans('Hi, Welcome! You have selected to check your notification preference: ')
        sleep(1)

        print('Please edit your notification preferences from below: ')
        trans('Please edit your notification preferences from below: ')
        sleep(1)

class Business_card:
    def business_card():
        print('Hi, Welcome! You have selected to check your business_card: ')
        trans('Hi, Welcome! You have selected to check your business_card: ')
        sleep(1)

        print('Please find the below business card templates that you may share and download. And also in order to edit your details please complete your profile: ')
        trans('Please find the below business card templates that you may share and download. And also in order to edit your details please complete your profile: ')
        sleep(1)

class Currency:
    def currency():
        print('Hi, Welcome! You have selected to check your currency preference: ')
        trans('Hi, Welcome! You have selected to check your currency preference: ')
        sleep(1)

        print('Please select your currency preferences from below: ')
        trans('Please select your currency preferences from below: ')
        sleep(1)
        curr=takeCommand().lower

class Calander_setting:
    def calander_setting():
        print('Hi, Welcome! You have selected to check your calander setting: ')
        trans('Hi, Welcome! You have selected to check your calander setting: ')
        sleep(1)

        print('Please edit your calander setting preferences from below: ')
        trans('Please edit your calander setting preferences from below: ')
        sleep(1)

class Feedback:
    def feedback():
        print('Hi, Welcome! You have selected to give your valuable feedback & suggestions: ')
        trans('Hi, Welcome! You have selected to give your valuable feedback & suggestions: ')
        sleep(1)

        trans("Please give your feedback for our service: ")
        feedback = str(input("Please give your feedback for our service: '"))
        sleep(1)

        trans("Please give your suggestions for our service: ")
        suggestions = str(input("Please give your suggestions for our service: '"))
        sleep(1)

class Manage_color:
    def manage_color():
        print('Hi, Welcome! You have selected to give edit the color layout of the app : ')
        trans('Hi, Welcome! You have selected to give edit the color layout of the app : ')
        sleep(1)

        print('Please edit your color layout preferences from below: ')
        trans('Please edit your color layout preferences from below: ')
        sleep(1)

class Upgrade:
    def upgrade():
        print('Hi, Welcome! You have selected to upgrade the app : ')
        trans('Hi, Welcome! You have selected to upgrade the app : ')
        sleep(1)

        print('Please select the option that you want to upgrade to : ')
        trans('Please select the option that you want to upgrade to : ')
        sleep(1)

class Recurrence:
    def recurrence():
        print('Hi, Welcome! You have selected to edit your recurrence preference: ')
        trans('Hi, Welcome! You have selected to edit your recurrence preference: ')
        sleep(1)

        print('Please edit your recurrence preferences from below: ')
        trans('Please edit your recurrence preferences from below: ')
        sleep(1)

###############################

if __name__ == "__main__":
    greeting()
    language()
    welcome()
    home()
    pr = SelectProfession()
    pr.employee()
    pr.professionals()
    pr.retailers()
    pr.others()
    while True:
        print("1) Networth")
        print("2) Bank Balance")
        print("3) Wallet")
        print("4) Money Transfer")
        print("5) Bill Payment")
        print("6) Insurance")
        product = takeCommand().lower()
        if 'networth' in product or 'net worth' in product or '1' in product:
            Networth()
        elif 'bank balance' in product:
            bank_balance()
            while True: 
                print('Do you want to TopUp your wallet or do Payment transfer your balance : ')
                trans('Do you want to TopUp your wallet or do Payment transfer your balance : ')
                print('1) Yes')
                print('2) No')
                sleep(1)
                s1= takeCommand().lower()
                if 'yes' in s1:
                    Newrecord()
                    break
                elif 'no' in s1:
                    break
        elif 'wallet' in product:
            Wallet()
        elif 'Money Transfer' in product:
            Money_Transfer()
        elif 'bill payment' in product:
            Bill_payment()
        elif 'insurance' in product:
            Insurance()
        elif "manage budget" in product:
            mr = ManageBudget()
            mr.income()
            mr.expense()
        elif "digital bank services" in product:
            digi = Digitalbankingservices()
            digi.retailerbanking()
            digi.digitalBankingServices()
            digi.open_account()
        elif "score card" in product:
            sc=Scorecard()
            sc.scorecard()
        elif "e invoicing" in product:
            ev = Evoicing()
            ev.einvoicing()
        elif "manage stoks" in product:
            ms = Manage_stoks()
            ms.manage_stocks()
        elif "manage other expenses" in product:
            me = Manageotherexpenses()
            me.manageotherexpenses()
        elif "Manage orders" in product:
            mo = Manageorders()
            mo.manageorders()
        elif "Manage return" in product:
            mr = Managereturn()
            mr.managereturn()
        elif "Manage staff salary" in product:
            ms = Managestaffsalary()
            ms.managestaffsalary()
        elif "rewards" in product:
            rw = Rewards()
            rw.rewards()
        elif "refer and earn" in product:
            rf = Referandearn()
            rf.referandearn()
        elif " document manager" in product:
            dc = Documentmanager()
            dc.documentmanager()
        elif "instant loan" in product:
            il = InstantLoan()
            il.instantloan()
        elif "password manager" in product:
            ps = Passwordmanager()
            ps.passwordmanager()
        elif "tax return" in product:
            tx= TaxReturn()
            tx.incometaxreturn()
            tx.gstReturn()
        elif "mutual fund" in product:
            mf = Mutual_fund()
            mf.highlystablefunds()
            mf.balancedfunds()
            mf.highgrowthfunds()
        elif "online store" in product:
            ol = OnlineStore()
            ol.onlinestore()
        elif "Online Services" in product:
            ols = OnlineServices()
            ols.onlineServices()
        elif 'exit' in product:
            trans("Thanks for giving me your time")
            exit()
        trans("Please select your correct product options..")

##########################################





































