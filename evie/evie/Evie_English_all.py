import pyttsx3
import speech_recognition as sr
import datetime
import os 
import random
import sys
import requests 
import re 
import time
import winsound

import pyttsx3 
import speech_recognition as sr
import datetime
import os
from PIL import Image
from time import sleep
import ecapture as ec
from gtts import gTTS


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('voice',50)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takecommmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5, phrase_time_limit=20)
    try:
        print("Reconigizing.......")
        query = r.recognize_google(audio ,language="en-in")
        print(f"User said:{query}")

    except Exception as e:
        speak("say that again please......")
        return "none"
    return query  

#########################

class SelectProfession:
    speak("please select your profession")
    def employee(self):
        speak("please enter the personal details")
        speak("please enter your Name")
        name =takecommmand().lower()
        name = input("Enter the name : " +name)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please enter the residential address")
        address = takecommmand().lower()
        address = input("enter the residential address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip  code")
        zip_code = takecommmand().lower()
        zip_code = input("enter the zip code" + zip_code)
        speak("please enter pan card number")
        Pancard = takecommmand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)

        speak("please enter adhar card number")
        adharcard = takecommmand().lower()
        if len(adharcard) == 12 :
            adharcard = int(input("Enter the adharcard number : "+adharcard))
        speak("sorry sir adhar card number is invalid please check it")    
        speak("please enter email")
        email = takecommmand().lower()
        email = input("Enter the email : "+email)
        speak("please enter the employer details")
        speak("please enter the employment name")
        employer_name = takecommmand().lower()
        employer_name = input("Enter the Employer Name : "+employer_name)
        speak("please enter the office address")
        address = takecommmand().lower()
        address = input("enter the office address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip code")
        zip_code = takecommmand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        speak("please enter your designation")
        designation = takecommmand().lower()
        designation = input("Enter the designation : "+designation)
        speak("please enter the department")
        department = takecommmand().lower()
        department = input("Enter the Department name : "+department)
        speak("please enter the email id")
        email = takecommmand().lower()
        Email = input("Enter the  email id : "+email)
        speak("please enter the offical contact number : ")
        Official_number = takecommmand().lower()
        Official_number = input("Enter official contact number : " +Official_number)

    def professionals(self):
        speak("please enter the personal details")
        speak("please enter your Name")
        name =takecommmand().lower()
        name = input("Enter the name : " +name)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please enter the residential address")
        address = takecommmand().lower()
        address = input("enter the residential address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip code")
        zip_code = takecommmand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        speak("please enter pan card number")
        Pancard = takecommmand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        speak("please enter adhar card number")
        adharcard = takecommmand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        speak("please enter email")
        email = takecommmand().lower()
        email = input("Enter the email : "+email)
        pr.businessname()
        speak("do you want to list your business on preferred online store yes or no")
        print("do you want to list your business on preferred online store yes / no")

        speak("do you want to add more business yes or no")
        businessname = takecommmand().lower()
        if "yes" in businessname:
            pr.businessname()

        if "no" in businessname:
            speak("thank you selecting business")    

    def retailers(self):
        speak("please enter your Name")
        name =takecommmand().lower()
        name = input("Enter the name : " +name)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please enter the residential address")
        address = takecommmand().lower()
        address = input("enter the residential address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip code")
        zip_code = takecommmand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        speak("please enter pan card number")
        Pancard = takecommmand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        speak("please enter adhar card number")
        adharcard = takecommmand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        if len(adharcard) == 12 :
            adharcard = int(input("Enter the adharcard number : "+adharcard))
        speak("sorry sir adhar card number is invalid please check it")    
        speak("please enter email")
        email = takecommmand().lower()
        email = input("Enter the email : "+email)
        pr.businessname()
        speak("do you want to list your business on preferred online store yes or no")
        print("do you want to list your business on preferred online store yes / no")
        speak("do you want to add more business yes or no")
        businessname = takecommmand().lower()
        if "yes" in businessname:
            pr.businessname()

        if "no" in businessname:
            speak("thank you selecting retailer")  
    
    
    def others(self):
        speak("please enter the personal details")
        speak("please enter your Name")
        name =takecommmand().lower()
        name = input("Enter the name : " +name)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please enter the residential address")
        address = takecommmand().lower()
        address = input("enter the residential address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip code")
        zip_code = takecommmand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        speak("please enter pan card number")
        Pancard = takecommmand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        speak("please enter adhar card number")
        adharcard = takecommmand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        if len(adharcard) == 12 :
            adharcard = int(input("Enter the adharcard number : "+adharcard))
        speak("sorry sir adhar card number is invalid please check it")    
        speak("please enter email")
        email = takecommmand().lower()
        email = input("Enter the email : "+email)
        speak("please enter the employer details")
        speak("please enter the employment name")
        employer_name = takecommmand().lower()
        employer_name = input("Enter the Employer Name : "+employer_name)
        speak("please enter the office address")
        address = takecommmand().lower()
        address = input("enter the office address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip code")
        zip_code = takecommmand().lower()
        zip_code = input("Enter the zip code : "+zip_code)
        speak("please enter your designation")
        designation = takecommmand().lower()
        designation = input("Enter the designation : "+designation)
        speak("please enter the department")
        department = takecommmand().lower()
        department = input("Enter the Department name : "+department)
        speak("please enter the email id")
        email = takecommmand().lower()
        Email = input("Enter the  email id : "+email)
        speak("please enter the offical contact number : ")
        Official_number = takecommmand().lower()
        Official_number = input("Enter official contact number : "+Official_number)
    
    def businessname(self):
        speak("please Enter business name")
        business_name = takecommmand().lower()
        business_name = input("Enter the business name : ")
        speak("Please Select business type")
    
        business_name = ["business advisors","finance adviors","Mutual fund advisors",'Electricals store',"insurance advisors","technical consultants",
        "software developers","mobile app developers","Digital marketing","tax consultants","project consultants","legal consultants","others"]
        print(business_name)
        select_business_name = input(business_name)
        speak("thank you for selecting the business"+business_name)
        
        speak("do you have GST Registration yes or no ")
        print("do you have GST Registration yes / no")
        GST_registration = takecommmand().lower()
        if "yes" in GST_registration:
            speak("Enter the GST Number")
            GST_number = input("Enter the GST number : ")
        elif "no" in GST_registration:
            pass
        speak("please enter the residential address")
        address = takecommmand().lower()
        address = input("enter the residential address : "+address)
        speak("please enter city name")
        city = takecommmand().lower()
        city = input("enter the city name : "+city)
        speak("please enter state name")
        state = takecommmand().lower()
        state = input("Enter the state name : "+state)
        speak("please enter the country name")
        country = takecommmand().lower()
        country = input("Enter the country name : "+country)
        speak("Please enter zip code")
        zip_code = takecommmand().lower()
        zip_code = input("Enter the zip code : "+zip_code)    
        speak("please enter email")
        offcial_email = takecommmand().lower()
        offcial_email = input("Enter the email : "+offcial_email)
        speak("please enter the official contact number")
        offcial_number = takecommmand().lower()
        Official_number = input("Enter official contact number : "+ offcial_number)
        speak("do you want to list your business on preferred online store yes or no")
        print("do you want to list your business on preferred online store yes / no")

class ManageBudget:

    def income(self):
        speak("please select the options for income")
        income = ["salary","interest","rental","dividend","gift","gain on sale of shares","gain on sale mutual fund","others"]
        print(income)
        income = takecommmand().lower()
        if re.search("salary|interest|rental|dividend|gift|gain on sale of shares|gain on sale mutual fund|others",income):
            select_income = input(income)
            speak("selected option has" +    select_income)
            speak("please enter the name ")
            name = takecommmand().lower()
            name = input("Enter the name : "+name)
            speak("thank you for choosing income"   +        select_income)    
        speak("please select correct option in income")
        mr.income()
    def expense(self):
        speak("please select the options for expense")
        expense = ["Rent & Electricity","holidays & outgoing",
                    "loan obligations","insurance","fees & bills","car",
                    "education","Entertainment","family & personal",
                    "contigencies","mobile & internet","saving & investment","home",
                    "groceries","beauty","food & drinks","gifts","healthcare","shopping",
                    "sports & hobbies","transport","work","charities"]
        print(expense)
        expence = takecommmand().lower()
        if re.search("Rent & Electricity|holidays & outgoing|loan obligations|insurance|fees & bills|car|education|Entertainment|family & personal|contigencies|mobile & internet|saving & investment|home|groceries|beauty|food & drinks|gifts|healthcare|shopping|sports & hobbies|transport|work|charities",expence):
            select_expense = input(expense)
            speak("selected option has" +     select_expense)
            speak("please enter the name ")
            name = takecommmand().lower()
            name = input("Enter the name : "+name)
            speak("thank you for choosing expense"+      select_expense)
        speak("please select correct option in expense")
        mr.expense()

class Digitalbankingservices:
    def retailerbanking(self):
        speak("cash disbursal")
        speak("cash collection")
        speak("cheque collection")
        speak("E M I collection")

        retailers = ["cash disbursal","cash collecion","cheque collection","emi collection"]
        print(retailers)
        retailers = takecommmand().lower()
        if re.search("cash disbursal|cash collecion|cheque collection|emi collection",retailers):
            if "cash disbursal" or "cash collection" or "cheque collection" in retailers:
                speak("Verifying the all details and to proceed to action")
                speak("Enter the OTP ")
                otp = int(input("Enter the otp : "))
            elif "emi collection" in retailers:
                speak("please select financial institution")
                speak("please enter the loan account number")
                loan_number = takecommmand().lower()
                loan_number = input("Enter the loan account number : "+loan_number)
        speak("please select correct option")
        digi.retailerbanking()

        retailers = input(retailers)
        retailers = retailers.lower()
        if "cash disbursal" in retailers :
            speak("Verifying the all details and to proceed to action")
            speak("Enter the OTP ")
            otp = int(input("Enter the otp : "))
            speak("your cash has been dibursed")
        elif "cash collecion" in retailers:
            speak("Verifying the all details and to proceed to action")
            speak("Enter the OTP ")
            otp = int(input("Enter the otp : "))
            speak("your cash has been dibursed")
        elif "cheque collection" in retailers:
            speak("Verifying the all details and to proceed to action")
            speak("Enter the OTP ")
            otp = int(input("Enter the otp : "))
            speak("your cash has been dibursed")
        elif "emi collection" in retailers:
            speak("please select financial institution")
            speak("please enter the loan account number")
            loan_number = takecommmand().lower()
            loan_number = input("Enter the loan account number : "+loan_number)

    def digitalBankingServices(self):
        speak("active accounts")
        speak("money transfer")
        speak("cash withdrawal")
        speak("cash desposite")
        speak("cheque clearing")
        speak("virtual multipurpose")
        speak("loan e m i payments")

    def open_account(self):
        speak("you want to new account then click on new account form")
        speak("please enter the first name")
        first_name = takecommmand().lower()
        first_name = input("Enter the first name : "+first_name)
        speak("please enter the last name")
        last_name = takecommmand().lower()
        last_name = input("Enter the last name : "+last_name)
        speak("please enter the Email")
        email = takecommmand().lower()
        email = input("enter the Email : "+email)
        speak("please enter the mobile number")
        mobile = takecommmand().lower()
        mobile = input("Enter the mobile number : "+mobile)
        speak("please enter date of birth")
        DOB = input("Enter the DOB : ")
        speak("please enter father name")
        father = takecommmand().lower()
        father = input("Enter the father name : "+father)
        speak("please enter the mother name")
        mother = takecommmand().lower()
        mother = input("Enter the mother name : "+mother)
        speak("please enter the nationality")
        nationality = takecommmand().lower()
        nationality = input("Enter the Nationality : "+nationality)
        speak("please attached the scan adharcard file")
        adharcard = input("attached adhar card : ")
        speak("please attached the pancard file")
        pancard = input("attached pan card : ")
        speak("please select scan photograph")
        photograph = input("attached photograph : ")

class Evoicing:
    def einvoicing(self):
        speak("welcome to e invoicing")
        speak("Do you want to  record new sale yes or no")
        evoice = takecommmand().lower()
        if "yes" in evoice: 
            speak("please enter client name")
            client_name = takecommmand().lower()
            client_name = input("Enter the client name : "+client_name)

            speak("do you want to create new item yes or no")
            new_item = takecommmand().lower()
            if "yes" in new_item:
                speak("please the add category name")
                add_category = takecommmand().lower()
                add_category = input("enter the category name : "+add_category)
                speak("please enter the name")
                name = takecommmand().lower()
                name = input("Ente the name : "+name)
                speak("please select the packing type")
                packing_type = input("please select packing type : ")
                speak("Please enter the packing size")
                packing_size = takecommmand().lower()
                packing_size = input("Enter the packing size : "+packing_size)
                speak("Please enter purchase cost")
                purhase_cost = takecommmand().lower()
                purhase_cost = input("Enter the purhase cost : "+purhase_cost)
                speak("Please enter the maximum retail price")
                max_retailer = takecommmand().lower()
                max_retailer = input("Enter the maximum retailer price : "+max_retailer)
                speak("Please enter the offer price")
                offer_price = takecommmand().lower()
                offer_price = input("Enter the offer price : "+offer_price)
                speak("Please enter the stock Quantity")
                stock_QTY = takecommmand().lower()
                stock_QTY = input("Enter the stock quanlity : "+stock_QTY)
                speak("Please select the stocks")
                speak("Please enter minimum level")
                minimum_level = takecommmand().lower()
                minimum_level = input("Enter the minimum level : "+minimum_level)
                speak("Please stock update on date")
                speak("Please upload product image")
                speak("Please select tax")
                speak("Please enter the HSN code")
                hsn_code = takecommmand().lower()
                hsn_code = input("Enter the hsn code : "+hsn_code)
                speak("Please select gst") 
            if "no" in new_item:
                speak("previous item list please check it below")  
        if "no" in evoice:
            speak("thank you for choosing e invoice") 

class Manage_stoks:
    def manage_stocks(self):
        speak("welcome to e manage stock")
        speak("Do you want to  add stocks yes or no")  
        manage_stocks = takecommmand().lower()
        if "Yes" in manage_stocks: 
            speak("please the add category name")
            speak("please the add category name")
            add_category = takecommmand().lower()
            add_category = input("enter the category name : "+add_category)
            speak("please enter the name")
            name = takecommmand().lower()
            name = input("Ente the name : "+name)
            speak("please select the packing type")
            packing_type = input("please select packing type : ")
            speak("Please enter the packing size")
            packing_size = takecommmand().lower()
            packing_size = input("Enter the packibg size : "+packing_size)
            speak("Please enter purchase cost")
            purhase_cost = takecommmand().lower()
            purhase_cost = input("Enter the purhase cost : "+purhase_cost)
            speak("Please enter the maximum retail price")
            max_retailer = takecommmand().lower()
            max_retailer = input("Enter the maximum retailer price : "+max_retailer)
            speak("Please enter the offer price")
            offer_price = takecommmand().lower()
            offer_price = input("Enter the offer price : "+offer_price)
            speak("Please enter the stock Quantity")
            stock_QTY = takecommmand().lower()
            stock_QTY = input("Enter the stock quanlity : "+stock_QTY)
            speak("Please select the stocks")
            speak("Please enter minimum level")
            minimum_level = takecommmand().lower()
            minimum_level = input("Enter the minimum level : "+minimum_level)
            speak("Please stock update on date")
            speak("Please upload product image")
            speak("Please select tax")
            speak("Please enter the HSN code")
            hsn_code = takecommmand().lower()
            hsn_code = input("Enter the hsn code : "+hsn_code)
            speak("Please select gst")     

        if "no" in manage_stocks:
            speak("thank you for selecting manage stocks check privious stocks")

class Manageotherexpenses :
    def manageotherexpenses(self):
        speak("welcome to e manage  other expenses")
        speak("Do you want to record new expenses yes or no ")
        Manage_expenses = takecommmand().lower()
        if "yes" in Manage_expenses: 
            speak("please enter client name")
            client_name = takecommmand().lower()
            client_name = input("Enter the client name : "+client_name)
            speak("do you want to create new services yes or no")
            new_service = takecommmand().lower()
            if "yes" in new_service:  
                speak("Please enter the expenses name")
                expense_name = takecommmand().lower()
                expense_name = input("Enter the expenses name : "+expense_name)
                speak("Please enter the amount")
                amount = takecommmand().lower()
                amount = input("Enter the amount : "+amount)
                speak("Please select the option")

            if "no" in new_service:
                speak("please check all previous services")
        if "no" in Manage_expenses:
            speak("thank you for choosing manage expenses") 

class Manageorders:
    def manageorders(Self):
        speak("welcome to manage  orders")
    def salesorder(self):
        speak("Do you want to add orders yes or no")
        sales = takecommmand().lower()
        if "yes" in sales:
            speak("please enter client name")
            client_name = takecommmand().lower()
            client_name = input("Enter the client name : "+client_name)
            speak("do you want to add items yes or no")
            new_items = takecommmand().lower()
            if "yes" in new_items:
                speak("Please enter the name")
                name = takecommmand().lower()
                name = input("Enter the name : "+name)
                speak("Please enter the quantity")
                QTY = takecommmand().lower()
                QTY = input("Enter the QTY : "+QTY)
                speak("Please enter the unit")
                unit = takecommmand().lower()
                unit = input("Enter the unit : "+unit )
                speak("Please add packing type")
            if "no" in new_items:
                speak("thank you for selecting sales")    
        if "no" in sales:
            speak("please check all previous records")

    def purchaseorder(self):
        speak("Do you want to add orders yes or no")
        purhase = takecommmand().lower()
        if "yes" in purhase:
            speak("Enter the client name ")
            client_name = takecommmand().lower()
            client_name = input("Enter the client name : "+client_name)
        if "no" in purhase:
            speak("check all purhase record below")

class Managereturn:
    def managereturn(self):
        speak("welcome to manage  return")
        sales = takecommmand().lower()
        if "yes" in sales:
            speak("please enter client name")
            client_name = takecommmand().lower()
            client_name = input("Enter the client name : "+client_name)
	
        if "no" in sales:
            speak("please check all previous recors\d")

    def purchaseorder(self):
        speak("Do you want to add orders yes or no")
        purhase = takecommmand().lower()
        if "yes" in purhase:
            speak("Enter the client name ")
            client_name = takecommmand().lower()
            client_name = input("Enter the client name : "+client_name)
        if "no" in purhase:
            speak("check all purhase record below")

class Managestaffsalary:
    def managestaffsalary(self):
        speak("welcome to manage staff salary")
        speak("do you want to add staff")
        staff = takecommmand().lower()
        if "yes" in staff:
            speak("Please enter the staff full name")
            fullname = takecommmand().lower()
            fullname = input("Enter the full name : "+fullname)
            speak("Please enter the mobile number")
            mobile = takecommmand().lower()
            mobile = input("Enter the mobile number : "+mobile)
            speak("Select the type of salary payment")

            speak("Please add salary details") 
            speak("Please enter the monthly salary ")
            month_salary = takecommmand().lower()
            month_salary = input("Enter the month salary : "+month_salary)
            speak("Please add  overtime rate")
            overtime = takecommmand().lower()
            overtime = input("Enter the overtime details : "+overtime)

            speak("Please add late fine rate")
            fine_late = takecommmand().lower()
            fine_late = input("Enter the fine late amount : ")

            speak("Please select payment cycle ")

            speak("Please enter the pending salary ")
            pending = takecommmand().lower()
            pending = input("Enter the pending salary : "+pending)
            speak("Please select month of salary")
            speak("Please enter the pending overtime")
            pending_ov = takecommmand().lower()
            pending_ov = input("Enter the pending overtime : "+pending_ov)
            speak("Please select month of overtime salary")
            speak("Please add the advances")
            advance = takecommmand().lower()
            advance = input("enter the advance : "+advance) 
        if "no" in staff:
            speak("thank you for selecting manage staff salary")

class Scorecard:
    def scorecard():
        speak("please update the credit score")
        speak("please enter your Name")
        name = takecommmand().lower()
        name = input("Enter the name : "+name)
        speak("please enter the mobile number")
        mobile = takecommmand().lower()
        mobile = input("Enter the Mobile number : "+mobile)
        speak("please enter email")
        email = takecommmand().lower()
        email = input("Enter the email : "+email)
        speak("please enter pancard number")
        Pancard = takecommmand().lower()
        Pancard = input("Enter the pancard number : "+Pancard)
        speak("please enter adharcard number")
        adharcard = takecommmand().lower()
        adharcard = input("Enter the adharcard number : "+adharcard)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please enter the address")
        address = takecommmand().lower()
        address = input("enter the address : "+address)
    
    def investmentRiskScore(self):
        speak("please update the investment risk score")
    def personaldetails(self):
        speak("please Fill the personal details")
        speak("please Enter the name")
        name = takecommmand().lower()
        name = input("Enter the name : "+name)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please choose the professional ")
        speak("profession 1")
        speak("profession 2")
        speak("professional 3") 
        profession = input("please choose the profession")
        speak("please enter the monthly income")
        monthly_income = takecommmand().lower()
        monthly_income = input("Enter the monthly income : "+monthly_income)
        speak("please enter monthly expense")
        monthly_expense = takecommmand().lower()
        monthly_expense = input("Enter the monthly expense : "+monthly_expense)
        speak("please enter the monthly loan obligation")
        loan_obligation = takecommmand().lower()
        loan_obligation = input("Enter the monthly loan obligation : "+loan_obligation)

    def familydetails(self):
        speak("please fill the family details")
        speak("please enter the name")
        name = takecommmand().lower()
        name = input("enter the name : "+ name)
        speak("please enter the date of birth")
        DOB = input("Enter the Date of birth : ")
        speak("please choose the qualification")
        speak("qualification 1 ")
        speak("qualification 2 ")
        speak("qualification 3 ")
        qualification = input("please choose the qualification : ")
        speak("please choose the professional ")
        speak("profession 1")
        speak("profession 2")
        speak("professional 3") 
        profession = input("please choose the profession")
        speak("please enter the monthly income")
        monthly_income = takecommmand().lower()
        monthly_income = input("Enter the monthly income : "+monthly_income)
        speak("please choose the relation")
        speak("relation 1 ")
        speak("relation 2 ")
        speak("relation 3 ")
        relation = input("please choose the relation : ")

    def educationdetails(self):
        speak("please fill the education Details")
        speak("please enter the name")
        name = takecommmand().lower()
        name = input("Enter the name : "+name)
        speak("please enter the relationship")
        relationship = takecommmand().lower()
        relationship = input("Enter the relationship : "+relationship)
        speak("please enter the nature of obligation")
        nature_obligation = takecommmand().lower()
        nature_obligation = input("Enter the nature of obligation : "+nature_obligation)
        speak("please enter the expected expense")
        expected_expense = takecommmand().lower()
        expected_expense = input("Enter the expected expense : "+expected_expense)
        speak("please enter the expected date year")
        expected_date_year = input("Enter the expected date/year : ")

    def socialobligationdetails(self):    
        speak("please enter the name")
        name = takecommmand().lower()
        name = input("Enter the name : "+name)
        speak("please enter the relationship")
        relationship = takecommmand().lower()
        relationship = input("Enter the relationship : "+relationship)
        speak("please enter the nature of obligation")
        nature_obligation = takecommmand().lower()
        nature_obligation = input("Enter the nature of obligation : "+nature_obligation)
        speak("please enter the expected expense")
        expected_expense = takecommmand().lower()
        expected_expense = input("Enter the expected expense : "+expected_expense)
        speak("please enter the expected date year")
        expected_date_year = input("Enter the expected date/year : ")

    def retirementdetails(self):
        speak("please enter retirement details")
        speak("please enter the retirement age")
        retirement_age = takecommmand().lower()
        retirement_age = input("Enter the  retirement age : "+retirement_age)
        speak("please choose the fund type")
        speak("fund 1 ")
        speak("fund 2 ")
        speak("fund 3 ")
        relation = input("please choose the funds : ")

    def contigencydetails():
        speak("please enter the contigency plan details")
        speak("Please enter the amount")
        amount = takecommmand().lower()
        amount = input("Enter the amount : "+amount)
        speak("please enter the frequency")
        frequency = takecommmand().lower()
        frequency  = input("Enter the frequency : "+frequency)

    def behaviorscore():
        pass
    def overallscore():
        pass
    
    def scorecard(self):
        speak("welcome in scorecard")
        speak("credit score")
        speak("investment risk score")
        speak("behavior score")
        speak("overall score")
        scorecard = takecommmand().lower()
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

        speak("please select the correct option")
        sc.scorecard()
class Rewards:
    def rewards(self):
        speak("welcome to reward")
        speak("rewards here tap to scratch")
        speak("please used this code to claim now")

class Referandearn:
    def referandearn(self):
        speak("welcome to refer and earn")
        speak("Earn 100 rupees every time a referred friends makes their 1st payment on payment from bank A/C")

class Documentmanager:
    def documentmanager(self):
        speak("welcome to documents manager")
        speak("do you want to add documents yes or no")
        Documentmanager = takecommmand().lower()
        if "yes" in Documentmanager: 
            speak("please upload the documents")
            speak("please add notes")
            speak("please voice data")
        elif "No" in Documentmanager:
            speak("thank you")
        speak("do you want add folder yes or no ")
        folder = takecommmand().lower()
        if "yes" in folder:
            speak("please add the documents folder")
        elif "No" in folder:
            speak("thank you")

class Passwordmanager:
    def passwordmanager(self):
        speak("welcome to password manager")
        speak("please enter the security password")

class TaxReturn:
    def incometaxreturn(self):
        speak("please add new data")
        speak("please enter the assesment year")
        assessment_year = input("enter the assessment_year : ")
        speak("please select type of return")
        speak("original")
        print("original")
        speak("modified")
        print("modified")
        type_of_return = input("please choose the type of return : ")
        speak("please enter the due date")
        due_date = input("enter the due date : ")
        speak("please enter the submitted date on")
        submitted_date = input("Enter the submitted date on : ")
        speak("please enter the taxable income")
        texable_income = takecommmand().lower()
        taxable_income = input("Enter the taxable income : "+texable_income)

        speak("please enter liability(refund)")
        refund = takecommmand().lower()
        refund = input("Enter the liability(refund) : "+refund)
        speak("please enter the status")
        status = takecommmand().lower()
        status = input("Enter the Status : "+status)
    
    def gstReturn(self):
        speak("please add new data")
        speak("please choose return type")
        gst_type = ["GSTR-1","GSTR-2","GSTR-3","GSTR_3B","GSTR-4","GSTR-5","GSTR-6","GSTR-7","GSTR-8","GSTR-9","GSTR-9A","GSTR-9C","GSTR-10","GSTR-11"]
        print(gst_type)
        select_gst = input(gst_type)
        speak("thank you for select "   +      select_gst)
        speak("please select recurrence")
        print("Anually")
        speak("anullay")
        print("quartely")
        speak("quartely")
        print("monthly")
        speak("monthly")
        speak("please enter the assesment year")
        assessment_year = input("enter the assessment_year : ")
        speak("please enter the due date")
        due_date = input("enter the due date : ")
        speak("please enter the submitted date on")
        submitted_date = input("Enter the submitted date on : ")
        speak("please enter the sales value")
        sales_value = takecommmand().lower()
        sales_value = input("Enter the sales value : "+sales_value)
        speak("please enter liability(refund)")
        refund = takecommmand().lower()
        refund = input("Enter the liability(refund) : "+refund)
        speak("please enter the status")
        status = takecommmand().lower()
        status = input("Enter the Status : "+status)

class Mutual_fund:
    def highlystablefunds(self):
        funds = ["liquid funds","debt funds","gold funds"]
        print(funds)
        funds = takecommmand().lower()
        if re.search("liquid funds|debt funds|gold funds",funds):
            speak("thank you for selected funds is "  +    funds)
            speak("check all details above and continue it")
        
            speak("please select the investment type")
            speak("money sip")
            speak("one time")
            a = ["money sip" , "one time"]
            a = input(a)
            speak("so you have selected"   +     a)

            speak("please enter the investment amount")
            investment_amount = int(input("Enter the amount : "))

            speak("please enter scedule investment on every")
            ddmmyy = input("Enter the date month year : ")
            
            speak("please setup your investment account")
            speak("please enter the pancard number")
            pancard = input("Enter PAN to create account : ")

            speak("please select the ADF pay terms and condition")
        speak("please select correct option")
        mf.highlystablefunds()

    def balancedfunds(self):
        funds = ["super funds","aggressive hybrid","dynamic asset allocation"]
        print(funds)
        if re.search("super funds|aggressive hybrid|dynamic asset allocation",funds):
            speak("thank you for selected fund is " +   funds)
            speak("check all details above and continue it")

            speak("please select the investment type")
            speak("money sip")
            speak("one time")
            a = ["money sip" , "one time"]
            a = input(a)
            speak("so you have selected"   +      a)

            speak("please enter the investment amount")
            investment_amount = int(input("Enter the amount : "))

            speak("please enter scedule investment on every")
            ddmmyy = input("Enter the date month year : ")

            speak("please setup your investment account")
            speak("please enter the pancard number")
            pancard = input("Enter PAN to create account : ")

            speak("please select the ADF pay terms and condition")

        speak("please select correct option")
        mf.balancedfunds()

    def highgrowthfunds(self):
        funds = ["tax saving funds","large cap funds","diversified funds","mid & small cap","index funds"]
        funds = takecommmand().lower()
        if re.search("tax saving funds|large cap funds|diversified funds|mid & small cap|index funds",funds):
            speak("thank you for selected fund is "+      funds)
            speak("check all details above and continue it")
        
            speak("please select the investment type")
            speak("money sip")
            speak("one time")
            a = ["money sip" , "one time"]
            a = input(a)
            speak("so you have selected" + a)

            speak("please enter the investment amount")
            investment_amount = int(input("Enter the amount : "))

            speak("please enter scedule investment on every")
            ddmmyy = input("Enter the date month year : ")

            speak("please setup your investment account")
            speak("please enter the pancard number")
            pancard = input("Enter PAN to create account : ")

            speak("please select the ADF pay terms and condition")
        speak("please select correct option")
        mf.highgrowthfunds()
class StockMarket:
    pass

class FixedDeposite:
    pass

class InstantLoan:
    def instantloan(self):
        speak("welcome to instant loan services")

class BusinessLoan:
    pass

class OnlineStore:
    def onlinestore(self):
        speak("Welcome to online Stores")

        online_store = ["provisional store","fruit & vegetable store","sweet & confectionery","electrical store","mechanics & repair","fintness & health supplement","electronics appliance","fashion store","gold & jeweleries","mobile & accessories","book & stationary","computer accessories","games & gift","kitchen appliances","medical store","health clinic","personal & baby care","home furnishing","home appliances","makeup artist","beauty parlour & saloon","travel agent","restaurants","others"]
        print(online_store)

        online_store = takecommmand().lower()
        if re.search("provisional store|fruit & vegetable store|sweet & confectionery|electrical store|mechanics & repair|fintness & health supplement|electronics appliance|fashion store|gold & jeweleries|mobile & accessories|book & stationary|computer accessories|games & gift|kitchen appliances|medical store|health clinic|personal & baby care|home furnishing|home appliances|makeup artist|beauty parlour & saloon|travel agent|restaurants|others",online_store):
            speak("thank you for selected"  +     online_store)

        speak("please select corrct option")    
class OnlineServices:
    
    def onlineServices(self):
        speak("welcome to online services")
        online_services = ["saloon for woment","saloon for Men","makeup artists","ac service & repair","appliance repair","painter","cleaning & disinfection","electrician","plumber","carpenters","pest control","car mechanics","fitness centres","web developer","mobile app developer","IT services","computer repair","networking services","financial consultants","legal consultants","financial advisor","tax advisors","baby care","house keeping","others"]
        print(online_services)
        if re.search("saloon for woment|saloon for Men|makeup artists|ac service & repair|appliance repair|painter|cleaning & disinfection|electrician|plumber|carpenters|pest control|car mechanics|fitness centres|web developer|mobile app developer|IT services|computer repair|networking services|financial consultants|legal consultants|financial advisor|tax advisors|baby care|house keeping|others",online_services):
            speak("thank you for selected" +        online_services)
        speak("please select correct option")

########################################

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")
    speak("Welcome to ADF PAY!")
    print("Welcome to ADF PAY!")
    sleep(3)

def language():
    print('Please Select your Language:')
    print('1) English')
    print('2) Hindi')
    print('3) Marathi')
    speak('Please Select your Language:')
    lang = takecommmand().lower()
    if 'english' in lang:
        print("You have selected to proceed in English language")
        speak("You have selected to proceed in English language")
    elif 'hindi' in lang:
        print("You have selected to proceed in Hindi language")
        speak("You have selected to proceed in Hindi language")
    elif 'marathi' in lang:
        print("You have selected to proceed in Hindi language")
        speak("You have selected to proceed in Hindi language")
    sleep(1)
    print(" \n ")

def welcome():
    print('Sign Up to register yourself!')
    speak('Sign Up to register yourself!')
    sleep(1)

    print('Please Enter your Mobile Number')
    speak('Please Enter your Mobile Number')
    mobile=takecommmand().lower()


    print('Please enter 6 digit Otp sent to your mobile no')
    speak('Please enter 6 digit Otp sent to your mobile no')
    otp= takecommmand().lower()
    sleep(1)

    print('Thanks for signing up!')
    speak('Thanks for signing up.. ')
    sleep(3)

def home():
    print("Welcome to ADFPAY. We have varirty of products to explore!!")
    speak("Welcome to ADFPAY. We have varirty of products to explore!!")
    sleep(1)

    print("You may update your profile by visiting the side menu and also update the settings !")
    speak("You may update your profile by visiting the side menu and also update the settings !")
    sleep(1)

    print("Please select the products from below : ")
    speak("Please select the products from below")
#####################

class Networth:
    def Networth(self):
        print('Hi, Welcome to check your Networth!')
        speak('Hi, Welcome to check your Networth!')
        sleep(1)

        Networth= "450000"

        print('Your Current Networth is '+ Networth)
        speak('Your Current Networth is '+ Networth)
        sleep(1)

        print('Please select the following that you want to proceed with : ')
        speak('Please select the following that you want to proceed with : ')
        print('1) Assets')
        print('2) Liabilities')
        opt= takecommmand().lower()
        if 'assets' in opt:
            print("You have selected to assets")
            speak("You have selected to assets")
            Networth.assets()
        elif 'Liabilities' in opt:
            print("You have selected to Liabilities")
            speak("You have selected to Liabilities")
            Networth.Liabilities()
        sleep(1)

    def assets():
        investment= 10000
        current_value= 11000
        Gain= (current_value-investment)/investment
        print('Your Current value of your investment is '+ str(current_value) + ' with a gain of ' + str(Gain))
        speak('Your Current value of your investment is '+ str(current_value) + ' with a gain of ' + str(Gain))
        speak("You may also check your assests as segmented below:")
        sleep(3)

        print("Do you want to add new records to your assets?")
        speak("Do you want to add new records to your assets?")
        print("1) Yes")
        print("2) No")
        New_record_ass= takecommmand().lower()
        if 'yes' in New_record_ass:
            Networth.asset_add_record()
        elif 'no' in New_record_ass:
            exit()

    def Liabilities():
        total_Liabilities= 3000
        current_balance= 5000
        Gain= (current_balance-total_Liabilities)/total_Liabilities
        print('Your Current value of your investment is '+ str(current_balance) + ' with a gain of ' + str(Gain))
        speak('Your Current value of your investment is '+ str(current_balance) + ' with a gain of ' + str(Gain))
        speak("You may also check your Liabilities as segmented below:")
        sleep(3)

        print("Do you want to add new records to your liabilities?")
        speak("Do you want to add new records to your liabilities?")
        print("1) Yes")
        print("2) No")
        New_record_lia= takecommmand().lower()
        if 'yes' in New_record_lia:
            Networth.liabilities_add_record()
        elif 'no' in New_record_lia:
            exit()

    def asset_add_record():
        print("You have selected to add new asset record ")
        speak("You have selected to add new asset record ")
        sleep(1)

        print("Please select the below assets that you want to add to your networth : ")
        speak("Please select the below assets that you want to add to your networth : ")
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

        assets= takecommmand().lower()
        sleep(1)
        if 'fixed deposit' in assets:
            print("You have selected Fixed Deposit")
            speak("You have selected Fixed Deposit")
            sleep(1)
            print("You may proceed to edit fixed deposit from below or add new Fixed Deposit details : ")
            speak("You may proceed to edit fixed deposit from below or add new Fixed Deposit details : ")
            sleep(1)

            print("Do you want to add new records to FD?")
            speak("Do you want to add new records to FD?")
            print("1) Yes")
            print("2) No")
            New_record_FD= takecommmand().lower()
            if 'yes' in New_record_FD:
                Networth.Fixed_Deposit()
            elif 'no' in New_record_FD:
                exit()
            
        elif 'insurance policy' in assets:
            print("You have selected Insurance Policy")
            speak("You have selected Insurance Policy")
            sleep(1)
            print("You may proceed to edit Insurance Policy from below or add new Insurance Policy details : ")
            speak("You may proceed to edit Insurance Policy from below or add new Insurance Policy details : ")
            sleep(1)

            print("Do you want to add new records to Insurance Policy?")
            speak("Do you want to add new records to Insurance Policy?")
            print("1) Yes")
            print("2) No")
            New_record_pol= takecommmand().lower()
            if 'yes' in New_record_pol:
                Networth.insurance_policies()
            elif 'no' in New_record_pol:
                exit()

        elif 'mutual fund' in assets:
            print("You have selected Mutual Fund")
            speak("You have selected Mutual Fund")
            sleep(1)
            print("You may proceed to edit Mutual Fund from below or add new Mutual Fund details : ")
            speak("You may proceed to edit Mutual Fund from below or add new Mutual Fund details : ")
            sleep(1)

            print("Do you want to add new records to Mutual Fund?")
            speak("Do you want to add new records to Mutual Fund?")
            print("1) Yes")
            print("2) No")
            New_record_fund= takecommmand().lower()
            if 'yes' in New_record_fund:
                Networth.Mutual_Fund()
            elif 'no' in New_record_fund:
                exit()

        elif 'shares and debentures' in assets:
            print("You have selected Shares and Debentures")
            speak("You have selected Shares and Debentures")
            sleep(1)
            print("You may proceed to edit Shares and Debentures from below or add new Shares and Debentures details : ")
            speak("You may proceed to edit Shares and Debentures from below or add new Shares and Debentures details : ")
            sleep(1)

            print("Do you want to add new records to Shares and Debentures?")
            speak("Do you want to add new records to Shares and Debentures?")
            print("1) Yes")
            print("2) No")
            New_record_shares= takecommmand().lower()
            if 'yes' in New_record_shares:
                Networth.Shares()
            elif 'no' in New_record_shares:
                exit()

        elif 'security and bonds' in assets:
            print("You have selected Security & Bonds")
            speak("You have selected Security & Bonds")
            sleep(1)
            print("You may proceed to edit Security & Bonds from below or add new Security & Bonds details : ")
            speak("You may proceed to edit Security & Bonds from below or add new Security & Bonds details : ")
            sleep(1)

            print("Do you want to add new records to Security & Bonds?")
            speak("Do you want to add new records to Security & Bonds?")
            print("1) Yes")
            print("2) No")
            New_record_bonds= takecommmand().lower()
            if 'yes' in New_record_bonds:
                Networth.security()
            elif 'no' in New_record_bonds:
                exit()

        elif 'crypto' in assets:
            print("You have selected Crypto")
            speak("You have selected Crypto")
            sleep(1)
            print("You may proceed to edit Crypto from below or add new Crypto details : ")
            speak("You may proceed to edit Crypto from below or add new Crypto details : ")
            sleep(1)

            print("Do you want to add new records to Crypto?")
            speak("Do you want to add new records to Crypto?")
            print("1) Yes")
            print("2) No")
            New_record_Crypto= takecommmand().lower()
            if 'yes' in New_record_Crypto:
                Networth.Crypto()
            elif 'no' in New_record_Crypto:
                exit()

        elif 'property details' in assets:
            print("You have selected Property Details")
            speak("You have selected Property Details")
            sleep(1)
            print("You may proceed to edit Property Details from below or add new Property Details : ")
            speak("You may proceed to edit Property Details from below or add new Property Details : ")
            sleep(1)

            print("Do you want to add new records to Property Details?")
            speak("Do you want to add new records to Property Details?")
            print("1) Yes")
            print("2) No")
            New_record_property= takecommmand().lower()
            if 'yes' in New_record_property:
                Networth.Property_Details()
            elif 'no' in New_record_property:
                exit()

        elif 'gold & jewellery' in assets:
            print("You have selected Gold & Jewellery")
            speak("You have selected Gold & Jewellery")
            sleep(1)
            print("You may proceed to edit Gold & Jewellery from below or add new Gold & Jewellery details : ")
            speak("You may proceed to edit Gold & Jewellery from below or add new Gold & Jewellery details : ")
            sleep(1)

            print("Do you want to add new records to Gold & Jewellery?")
            speak("Do you want to add new records to Gold & Jewellery?")
            print("1) Yes")
            print("2) No")
            New_record_gold= takecommmand().lower()
            if 'yes' in New_record_gold:
                Networth.Gold()
            elif 'no' in New_record_gold:
                exit()
            
        elif 'vehicles' in assets:
            print("You have selected Vehicles")
            speak("You have selected Vehicles")
            sleep(1)
            print("You may proceed to edit Vehicles from below or add new Vehicles details : ")
            speak("You may proceed to edit Vehicles from below or add new Vehicles details : ")
            sleep(1)

            print("Do you want to add new records to vehicles?")
            speak("Do you want to add new records to vehicles?")
            print("1) Yes")
            print("2) No")
            New_record_veh= takecommmand().lower()
            if 'yes' in New_record_veh:
                Networth.Vehicles()
            elif 'no' in New_record_veh:
                exit()
            
        elif 'saving certificates' in assets:
            print("You have selected Saving Certificates")
            speak("You have selected Saving Certificates")
            sleep(1)
            print("You may proceed to edit Saving Certificates from below or add new Saving Certificates details : ")
            speak("You may proceed to edit Saving Certificates from below or add new Saving Certificates details : ")
            sleep(1)

            print("Do you want to add new records to saving certificates?")
            speak("Do you want to add new records to saving certificates?")
            print("1) Yes")
            print("2) No")
            New_record_cer= takecommmand().lower()
            if 'yes' in New_record_cer:
                Networth.Saving_Certificates()
            elif 'no' in New_record_cer:
                exit()

        elif 'other Assets' in assets:
            print("You have selected Other Assets")
            speak("You have selected Other Assets")
            sleep(1)
            print("You may proceed to edit Other Assets from below or add new Other Assets details : ")
            speak("You may proceed to edit Other Assets from below or add new Other Assets details : ")
            sleep(1)

            print("Do you want to add new records to other Assets?")
            speak("Do you want to add new records to other Assets?")
            print("1) Yes")
            print("2) No")
            New_record_other= takecommmand().lower()
            if 'yes' in New_record_other:
                Networth.Other_Assets()
            elif 'no' in New_record_other:
                exit()
            sleep(1)

    def liabilities_add_record():
        print("You have selected to add new Liabilities record ")
        speak("You have selected to add new Liabilities record ")
        sleep(1)

        print("Please select the below Liabilities that you want to add to your networth : ")
        speak("Please select the below Liabilities that you want to add to your networth : ")
        print('1) Credit Cards')
        print('2) Loans ')
        print('3) Monthly Obligations')
        print('4) Others')

        Liabilities= takecommmand().lower()
        sleep(1)
        if 'credit cards' in Liabilities:
            print("You have selected Credit Cards")
            speak("You have selected Credit Cards")
            sleep(1)
            print("You may proceed to edit Credit Cards from below or add new Credit Cards details : ")
            speak("You may proceed to edit Credit Cards from below or add new Credit Cards details : ")
            sleep(1)

            print("Do you want to add new records to credit cards?")
            speak("Do you want to add new records to credit cards?")
            print("1) Yes")
            print("2) No")
            New_record_credit= takecommmand().lower()
            if 'yes' in New_record_credit:
                Networth.Credit_Cards()
            elif 'no' in New_record_credit:
                exit()
            
        elif 'loans' in Liabilities:
            print("You have selected Loans")
            speak("You have selected Loans")
            sleep(1)

            print("Please select the below loans that you want to add to your networth : ")
            speak("Please select the below loans that you want to add to your networth : ")
            print('1) Financial Institutions')
            print('2) Private Lenders ')
            print('3) Friends & Relatives')
            l1= takecommmand().lower()
            if 'financial institutions' in l1:
                print("You have selected to Financial Institutions")
                speak("You have selected to Financial Institutions")
                
                print("You may proceed to edit Financial Institutions loans from below or add new details : ")
                speak("You may proceed to edit Financial Institutions loans from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to credit cards?")
                speak("Do you want to add new records to credit cards?")
                print("1) Yes")
                print("2) No")
                New_record_credit= takecommmand().lower()
                if 'yes' in New_record_credit:
                    Networth.Financial_Institutions()
                elif 'no' in New_record_credit:
                    exit()

            elif 'private lenders' in l1:
                print("You have selected to Private Lenders")
                speak("You have selected to Private Lenders")
                
                print("You may proceed to edit Private Lenders Loans from below or add new details : ")
                speak("You may proceed to edit Private Lenders Loans from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to private lenders?")
                speak("Do you want to add new records to private lenders?")
                print("1) Yes")
                print("2) No")
                New_record_lend= takecommmand().lower()
                if 'yes' in New_record_lend:
                    Networth.Private_Lenders()
                elif 'no' in New_record_lend:
                    exit()
                
            elif 'friends & relatives' in l1:
                print("You have selected to Friends & Relatives")
                speak("You have selected to Friends & Relatives")
                Liabilities()
                print("You may proceed to edit Friends & Relatives Loans from below or add new details : ")
                speak("You may proceed to edit Friends & Relatives Loans from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to friends & relatives?")
                speak("Do you want to add new records to friends & relatives?")
                print("1) Yes")
                print("2) No")
                New_record_fri= takecommmand().lower()
                if 'yes' in New_record_fri:
                    Networth.Friends()
                elif 'no' in New_record_fri:
                    exit()

        elif 'monthly Obligations' in Liabilities:
            print("You have selected Monthly Obligations")
            speak("You have selected Monthly Obligations")
            sleep(1)
            print("Please select the below Monthly Obligations loans that you want to add to your networth : ")
            speak("Please select the below Monthly Obligations loans that you want to add to your networth : ")
            print('1) Insurance Premium')
            print('2) SIP Instalments')
            print('3) Recurring deposits')
            m1= takecommmand().lower()
            if 'insurance premium' in m1:
                print("You have selected to Insurance Premium")
                speak("You have selected to Insurance Premium")
                
                print("You may proceed to edit Insurance Premium from below or add new details : ")
                speak("You may proceed to edit Insurance Premium from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to insurance premium?")
                speak("Do you want to add new records to insurance premium?")
                print("1) Yes")
                print("2) No")
                New_record_pre= takecommmand().lower()
                if 'yes' in New_record_pre:
                    Networth.insurance_policies()
                elif 'no' in New_record_pre:
                    exit()

            elif 'sip instalments' in m1:
                print("You have selected to SIP Instalments")
                speak("You have selected to SIP Instalments")
                
                print("You may proceed to edit SIP Instalments from below or add new details : ")
                speak("You may proceed to edit SIP Instalments from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to SIP Instalments?")
                speak("Do you want to add new records to SIP Instalments?")
                print("1) Yes")
                print("2) No")
                New_record_sip= takecommmand().lower()
                if 'yes' in New_record_sip:
                    Networth.SIP_Instalments()
                elif 'no' in New_record_sip:
                    exit()

            elif 'recurring deposits' in m1:
                print("You have selected to Recurring deposits")
                speak("You have selected to Recurring deposits")
                
                print("You may proceed to edit Recurring deposits from below or add new details : ")
                speak("You may proceed to edit Recurring deposits from below or add new details : ")
                sleep(1)

                print("Do you want to add new records to recurring deposits?")
                speak("Do you want to add new records to recurring deposits?")
                print("1) Yes")
                print("2) No")
                New_record_recc= takecommmand().lower()
                if 'yes' in New_record_recc:
                    Networth.Recurring()
                elif 'no' in New_record_recc:
                    exit()
            
        elif 'Others' in Liabilities:
            print("You have selected Others")
            speak("You have selected Others")
            sleep(1)
            print("You may proceed to edit Others from below or add new Others details : ")
            speak("You may proceed to edit Others from below or add new Others details : ")
            sleep(1)

            print("Do you want to add new records to Others?")
            speak("Do you want to add new records to Others?")
            print("1) Yes")
            print("2) No")
            New_record_otherr= takecommmand().lower()
            if 'yes' in New_record_otherr:
                Networth.Other()
            elif 'no' in New_record_otherr:
                exit()

    def Fixed_Deposit():
        print("You have selected to enter new Fixed Deposit")
        speak("You have selected to enter new Fixed Deposit")
        sleep(1)

        speak("Please Select your institution Type :")
        inst_type = str(input("Please Select your institution Type :"))
        sleep(1)
        
        speak("Please enter your FD Type :")
        FD_type = str(input("Please enter your FD Type :"))
        sleep(1)

        speak("Please enter your Invested Value :")
        Invested = str(input("Please enter your Invested Value :"))
        sleep(1)

        speak("Please enter your Annual Rate of Insterest :")
        Ann_rate = str(input("Please enter your Annual Rate of Insterest :"))
        sleep(1)

        speak("Please enter your Interest compounding Frequency :")
        Com_fre= str(input("Please enter your Interest compounding Frequency :"))
        sleep(1)

        speak("Please enter your Investing period :")
        period = str(input("Please enter your Investing period :"))
        sleep(1)

        speak("Please enter your Current Value :")
        curr_val = str(input("Please enter your Current Value :"))
        sleep(1)

        speak("Please enter your start Date :")
        start_date = str(input("Please enter your start Date :"))
        sleep(1)

        speak("Please enter your Note :")
        Note = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def insurance_policies():
        print("You have selected to enter new Insurance Policies")
        speak("You have selected to enter new Insurance Policies")
        sleep(1)

        speak("Please Select your insurance Policies :")
        ins_pol = str(input("Please Select your insurance Policies :"))
        sleep(1)
        
        speak("Please enter your Company Name :")
        com_name = str(input("Please enter your Company Name :"))
        sleep(1)

        speak("Please enter your Policy Name :")
        Pol_name = str(input("Please enter your Policy Name :"))
        sleep(1)

        speak("Please enter your Policy Number :")
        pol_no = str(input("Please enter your Policy Number :"))
        sleep(1)

        speak("Please enter your Start Date :")
        srt_date= str(input("Please enter your Start Date :"))
        sleep(1)

        speak("Please enter your Premium Amount :")
        amount = str(input("Please enter your Premium Amount :"))
        sleep(1)

        speak("Please enter your Recurrence :")
        rec = str(input("Please enter your Recurrence :"))
        sleep(1)

        speak("Please enter your premium due :")
        due = str(input("Please enter your premium due :"))
        sleep(1)

        speak("Please enter your Sum Assured :")
        sum_assured = str(input("Please enter your Sum Assured :"))
        sleep(1)

        speak("Please enter your Maturity Date :")
        mat_date = str(input("Please enter your Maturity Date :"))
        sleep(1)

        speak("Please enter your Maturity Value :")
        mat_val = str(input("Please enter your Maturity Value :"))
        sleep(1)

        speak("Please enter your Note :")
        Note1 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Mutual_Fund():
        print("You have selected enter to new Mutual Fund")
        speak("You have selected enter to new Mutual Fund")
        sleep(1)

        speak("Please enter the Company Name :")
        com = str(input("Please enter the Company Name :"))
        sleep(1)
        
        speak("Please enter your Scheme Name :")
        scheme = str(input("Please enter your scheme Name :"))
        sleep(1)

        speak("Please enter your scheme type :")
        sch_type = str(input("Please enter your scheme type :"))
        sleep(1)

        speak("Please enter your fund class :")
        fund_class = str(input("Please enter your fund class :"))
        sleep(1)

        speak("Please enter your Portfolio Number :")
        port_no = str(input("Please enter your Portfolio Number :"))
        sleep(1)

        speak("Please enter your purchase Date :")
        pur_date= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter units :")
        units = str(input("Please enter units :"))
        sleep(1)

        speak("Please enter Rate :")
        rate = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter your Invested Value :")
        invest_value = str(input("Please enter your invested Value :"))
        sleep(1)

        speak("Please enter current value :")
        curr_vall = str(input("Please enter your current value :"))
        sleep(1)

        speak("Please enter Gain/Loss :")
        mat_val = str(input("Please enter Gain/Loss :"))
        sleep(1)

        speak("Please enter your Note :")
        Note2 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Shares():
        print("You have selected to enter new Shares")
        speak("You have selected to enter new Shares")
        sleep(1)

        speak("Please enter the Script type :")
        Script = str(input("Please enter the Script type :"))
        sleep(1)
        
        speak("Please enter your Company Name :")
        c1 = str(input("Please enter your Company Name :"))
        sleep(1)

        speak("Please enter your Demat account Number :")
        Demat_no = str(input("Please enter your Demat account Number :"))
        sleep(1)

        speak("Please enter your Demat Holding Company :")
        fund_class = str(input("Please enter your Demat Holding Company :"))
        sleep(1)

        speak("Please enter your purchase Date :")
        pur_date1= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter your Number of shared/Debentures :")
        no_shares = str(input("Please enter your Number of shared/Debentures :"))
        sleep(1)

        speak("Please enter Rate :")
        rate1 = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter your Invested Value :")
        invest_value1 = str(input("Please enter your invested Value :"))
        sleep(1)

        speak("Please enter current market value :")
        curr_vall1 = str(input("Please enter your current market value :"))
        sleep(1)

        speak("Please enter Gain/Loss :")
        Gain1 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        speak("Please enter your Note :")
        Note3 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def security():
        print("You have selected to enter Security & Bonds")
        speak("You have selected to enter Security & Bonds")
        sleep(1)

        speak("Please enter the Script type :")
        Script1 = str(input("Please enter the Script type :"))
        sleep(1)
        
        speak("Please enter institution Name :")
        i1 = str(input("Please enter your institution Name :"))
        sleep(1)

        speak("Please enter Instrument Number :")
        Demat_no = str(input("Please enter Instrument Number :"))
        sleep(1)

        speak("Please enter your purchase Date :")
        pur_date2= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter your Number of units :")
        units1 = str(input("Please enter your Number of units :"))
        sleep(1)

        speak("Please enter Rate :")
        rate2 = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter your Invested Value :")
        invest_value2 = str(input("Please enter your invested Value :"))
        sleep(1)

        speak("Please enter current value :")
        curr_vall2 = str(input("Please enter your current  value :"))
        sleep(1)

        speak("Please enter Gain/Loss :")
        Gain2 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        speak("Please enter your Note :")
        Note4 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Crypto():
        print("You have selected to enter Cryptocurrency")
        speak("You have selected to enter Cryptocurrency")
        sleep(1)

        speak("Please enter the Currency Name :")
        Script2 = str(input("Please enter the Currency Name :"))
        sleep(1)
        
        speak("Please enter Wallet Name :")
        i2 = str(input("Please enter your Wallet Name :"))
        sleep(1)

        speak("Please enter purchase Date :")
        pur_date3= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter Number of units :")
        units2 = str(input("Please enter your Number of units :"))
        sleep(1)

        speak("Please enter Rate :")
        rate3 = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter your Invested Value :")
        invest_value3 = str(input("Please enter your invested Value :"))
        sleep(1)

        speak("Please enter current market value :")
        curr_vall3 = str(input("Please enter your current market value :"))
        sleep(1)

        speak("Please enter Gain/Loss :")
        Gain3 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        speak("Please enter your Note :")
        Note5 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Property_Details():
        print("You have selected to enter Property Details")
        speak("You have selected to enter Property Details")
        sleep(1)

        speak("Please enter the Property Type:")
        Script2 = str(input("Please enter the Property Type :"))
        sleep(1)
        
        print("Please fill property details :")
        speak("Please fill property details :")
        sleep(1)
        speak("Please enter your property :")
        property = str(input("Please enter your property :"))
        sleep(1)

        speak("Please enter your property Name :")
        Pro_name = str(input("Please enter your property Name :"))
        sleep(1)

        speak("Please enter your property Status :")
        Pro_status = str(input("Please enter your property status :"))
        sleep(1)

        speak("Please enter BHK No :")
        BHK = str(input("Please enter your BHK No :"))
        sleep(1)

        speak("Please enter your Size :")
        size = str(input("Please enter your Size :"))
        sleep(1)

        speak("Please enter Property Location country :")
        country = str(input("Please enter Property Location country :"))
        sleep(1)

        speak("Please enter state :")
        state= str(input("Please enter state :"))
        sleep(1)

        speak("Please enter city :")
        city= str(input("Please enter city :"))
        sleep(1)

        speak("Please enter sector :")
        sector= str(input("Please enter sector :"))
        sleep(1)

        speak("Please enter Gain/Loss :")
        Gain4 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        speak("Please enter your Note :")
        Note5 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Gold():
        print("You have selected to enter Gold & Jewellery")
        speak("You have selected to enter Gold & Jewellery")
        sleep(1)

        speak("Please enter the Jewellery type :")
        jewel = str(input("Please enter the Jewellery type :"))
        sleep(1)
        
        speak("Please enter Name :")
        namee = str(input("Please enter Name :"))
        sleep(1)

        speak("Please enter purchase Date :")
        pur_date5= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter purity in the scale of 1 karat to 24 karat:")
        purity = str(input("Please enter purity :"))
        sleep(1) 

        speak("Please enter weight :")
        weight = str(input("Please enter your weight :"))
        sleep(1)

        speak("Please enter Rate :")
        rate5 = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter your Invested Value :")
        invest_value5 = str(input("Please enter your invested Value :"))
        sleep(1)

        speak("Please enter current market value :")
        curr_vall5 = str(input("Please enter your current market value :"))
        sleep(1)

        speak("Please enter Gain/Loss :")
        Gain5 = str(input("Please enter Gain/Loss :"))
        sleep(1)

        speak("Please enter your Note :")
        Note7 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Vehicles():
        print("You have selected to enter Vehicles")
        speak("You have selected to enter Vehicles")
        sleep(1)

        speak("Please enter the Vehicles Name :")
        vel_name = str(input("Please enter the Vehicles Name :"))
        sleep(1)
        
        speak("Please enter model :")
        model = str(input("Please enter Model :"))
        sleep(1)

        speak("Please enter Year :")
        year = str(input("Please enter Year :"))
        sleep(1)

        speak("Please enter purchase Date :")
        pur_date6= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter insurance till :")
        insure_till = str(input("Please enter insurance till :"))
        sleep(1) 

        speak("Please enter Registration till :")
        reg_till = str(input("Please enter Registration till :"))
        sleep(1)

        speak("Please enter Purchase Cost :")
        cost = str(input("Please Purchase Cost :"))
        sleep(1)

        speak("Please enter current Price :")
        curr_vall6 = str(input("Please enter your current Price :"))
        sleep(1)

        speak("Please enter your Note :")
        Note8 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Saving_Certificates():
        print("You have selected to enter Saving Certificates")
        speak("You have selected to enter Saving Certificates")
        sleep(1)

        speak("Please enter the Certificate type :")
        cer_type = str(input("Please enter the Certificate type :"))
        sleep(1)
        
        speak("Please enter Institution Name :")
        ist_name = str(input("Please enter Institution Name :"))
        sleep(1)

        speak("Please enter purchase Date :")
        pur_date7= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter No of Units :")
        units2 = str(input("Please enter No of Units :"))
        sleep(1)

        speak("Please enter Rate :")
        ratee = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter Invested Value :")
        cost1 = str(input("Please enter Invested Value :"))
        sleep(1)

        speak("Please enter current Value :")
        curr_vall7 = str(input("Please enter your current Value :"))
        sleep(1)

        speak("Please enter Gain :")
        Gainn = str(input("Please enter Gain :"))
        sleep(1)

        speak("Please enter your Note :")
        Note9 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Other_Assets():
        print("You have selected to enter Other Assets")
        speak("You have selected to enter Other Assets")
        sleep(1)

        speak("Please enter the Asset Type :")
        ast_type = str(input("Please enter the Asset Type :"))
        sleep(1)
        
        speak("Please enter Asset Name :")
        ast_name = str(input("Please enter Asset Name :"))
        sleep(1)

        speak("Please enter purchase Date :")
        pur_date8= str(input("Please enter your purchase Date :"))
        sleep(1)

        speak("Please enter No of Units :")
        units3 = str(input("Please enter No of Units :"))
        sleep(1)

        speak("Please enter Rate :")
        ratee1 = str(input("Please enter Rate :"))
        sleep(1)

        speak("Please enter Invested Value :")
        inv_value = str(input("Please enter Invested Value :"))
        sleep(1)

        speak("Please enter current Value :")
        curr_vall8 = str(input("Please enter your current Value :"))
        sleep(1)

        speak("Please enter Gain :")
        Gain1 = str(input("Please enter Gain :"))
        sleep(1)

        speak("Please enter your Note :")
        Note10 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Credit_Cards():
        print("You have selected to enter Credit Cards")
        speak("You have selected to enter Credit Cards")
        sleep(1)

        speak("Please enter the Bank :")
        Bank1 = str(input("Please enter the Bank :"))
        sleep(1)
        
        speak("Please enter Card Number :")
        card_no = str(input("Please enter Card Number :"))
        sleep(1)

        speak("Please enter Card Limit :")
        card_limit= str(input("Please enter your Card Limit :"))
        sleep(1)

        speak("Please enter Outstanding :")
        outstanding = str(input("Please enter Outstanding :"))
        sleep(1)

        speak("Please enter minimum value :")
        min_value = str(input("Please enter minimum value :"))
        sleep(1)

        speak("Please enter billing Cycle :")
        bii_cycle = str(input("Please enter your billing Cycle :"))
        sleep(1)

        speak("Please enter billing Date :")
        bill_date = str(input("Please enter billing Date :"))
        sleep(1)

        speak("Please enter your Due Date :")
        Due_date = str(input("Please enter your Due Date :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Financial_Institutions():
        print("You have selected to enter Financial Institutions")
        speak("You have selected to enter Financial Institutions")
        sleep(1)

        speak("Please enter the Financial Institutions Name :")
        Bank1 = str(input("Please enter the Financial Institutions Name :"))
        sleep(1)
        
        speak("Please enter Loan Facility :")
        loan_fac = str(input("Please enter Loan Facility :"))
        sleep(1)

        speak("Please enter Loan account Number :")
        loan_no= str(input("Please enter Loan account Number :"))
        sleep(1)

        speak("Please enter Start Date :")
        start_date = str(input("Please enter Start Date :"))
        sleep(1)

        speak("Please enter minimum value :")
        min_value1 = str(input("Please enter minimum value :"))
        sleep(1)

        speak("Please enter Loan Amount :")
        Loan_amt = str(input("Please enter your Loan Amount :"))
        sleep(1)

        speak("Please enter No of EMI :")
        No_emi = str(input("Please enter No of EMI :"))
        sleep(1)

        speak("Please enter your EMI Cycle :")
        emi_cyc = str(input("Please enter your EMI Cycle :"))
        sleep(1)

        speak("Please enter your EMI Amount :")
        emi_amount = str(input("Please enter your EMI Amount :"))
        sleep(1)

        speak("Please enter your EMI Due On :")
        Due_date1 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)    

    def Private_Lenders():
        print("You have selected to enter Private Lenders")
        speak("You have selected to enter Private Lenders")
        sleep(1)

        speak("Please enter the Private Lender Name :")
        lender = str(input("Please enter the Private Lender Name :"))
        sleep(1)
        
        speak("Please enter Loan Facility :")
        loan_fac1= str(input("Please enter Loan Facility :"))
        sleep(1)

        speak("Please enter Start Date :")
        start_date1 = str(input("Please enter Start Date :"))
        sleep(1)

        speak("Please enter Loan Amount :")
        Loan_amt1 = str(input("Please enter your Loan Amount :"))
        sleep(1)

        speak("Please enter No of EMI :")
        No_emi1 = str(input("Please enter No of EMI :"))
        sleep(1)

        speak("Please enter your EMI Cycle :")
        emi_cyc1 = str(input("Please enter your EMI Cycle :"))
        sleep(1)

        speak("Please enter your EMI Amount :")
        emi_amount1 = str(input("Please enter your EMI Amount :"))
        sleep(1)

        speak("Please enter your EMI Due On :")
        Due_date2 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Friends():
        print("You have selected to enter Friends & Relatives")
        speak("You have selected to enter Friends & Relatives")
        sleep(1)

        speak("Please enter the Name :")
        lender1 = str(input("Please enter the Private Lender Name :"))
        sleep(1)

        speak("Please enter the relationship with the lender :")
        relationship = str(input("Please enter the relationship :"))
        sleep(1)
        
        speak("Please enter Loan Facility :")
        loan_fac2= str(input("Please enter Loan Facility :"))
        sleep(1)

        speak("Please enter Start Date :")
        start_date2 = str(input("Please enter Start Date :"))
        sleep(1)

        speak("Please enter Loan Amount :")
        Loan_amt2 = str(input("Please enter your Loan Amount :"))
        sleep(1)

        speak("Please enter No of EMI :")
        No_emi2 = str(input("Please enter No of EMI :"))
        sleep(1)

        speak("Please enter your EMI Cycle :")
        emi_cyc2 = str(input("Please enter your EMI Cycle :"))
        sleep(1)

        speak("Please enter your EMI Amount :")
        emi_amount2 = str(input("Please enter your EMI Amount :"))
        sleep(1)

        speak("Please enter your EMI Due On :")
        Due_date3 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def insurance_policies():
        print("You have selected to enter new Insurance Policies")
        speak("You have selected to enter new Insurance Policies")
        sleep(1)

        speak("Please Select your insurance Policies :")
        ins_pol1 = str(input("Please Select your insurance Policies :"))
        sleep(1)
        
        speak("Please enter your Company Name :")
        com_namee1 = str(input("Please enter your Company Name :"))
        sleep(1)

        speak("Please enter your Policy Name :")
        Pol_name1 = str(input("Please enter your Policy Name :"))
        sleep(1)

        speak("Please enter your Policy Number :")
        pol_no1 = str(input("Please enter your Policy Number :"))
        sleep(1)

        speak("Please enter your Start Date :")
        srt_datee1= str(input("Please enter your Start Date :"))
        sleep(1)

        speak("Please enter your Premium Amount :")
        amountt1 = str(input("Please enter your Premium Amount :"))
        sleep(1)

        speak("Please enter your Recurrence :")
        rec1 = str(input("Please enter your Recurrence :"))
        sleep(1)

        speak("Please enter your premium due :")
        due1 = str(input("Please enter your premium due :"))
        sleep(1)

        speak("Please enter your Sum Assured :")
        sum_assured1 = str(input("Please enter your Sum Assured :"))
        sleep(1)

        speak("Please enter your Maturity Date :")
        mat_date1 = str(input("Please enter your Maturity Date :"))
        sleep(1)

        speak("Please enter your Maturity Value :")
        mat_val1 = str(input("Please enter your Maturity Value :"))
        sleep(1)

        speak("Please enter your Note :")
        Note11 = str(input("Please enter your Note :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def SIP_Instalments():
        print("You have selected to enter SIP Instalments")
        speak("You have selected to enter SIP Instalments")
        sleep(1)

        speak("Please enter the company Name :")
        n2 = str(input("Please enter the company Name :"))
        sleep(1)

        speak("Please enter the scheme name :")
        Scheme1 = str(input("Please enter the scheme name :"))
        sleep(1)

        speak("Please enter Start Date :")
        start_date4 = str(input("Please enter Start Date :"))
        sleep(1)

        speak("Please enter End Date :")
        End_date1 = str(input("Please enter End Date :"))
        sleep(1)

        speak("Please enter SIP Amount :")
        SIP_amt2 = str(input("Please enter your SIP Amount :"))
        sleep(1)

        speak("Please enter your EMI Due On :")
        Due_date5 = str(input("Please enter your EMI Due On :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Recurring():
        print("You have selected to enter Recurring Deposits")
        speak("You have selected to enter Recurring Deposits")
        sleep(1)

        speak("Please enter the bank Name :")
        b2 = str(input("Please enter the bank Name :"))
        sleep(1)

        speak("Please enter the scheme name :")
        Scheme2 = str(input("Please enter the scheme name :"))
        sleep(1)

        speak("Please enter Start Date :")
        start_date5 = str(input("Please enter Start Date :"))
        sleep(1)

        speak("Please enter Maturity Date :")
        Maturity_date1 = str(input("Please enter Maturity Date :"))
        sleep(1)

        speak("Please enter Deposit Amount :")
        dep_amt2 = str(input("Please enter your Deposit Amount :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

    def Other():
        print("You have selected to enter Other Details ")
        speak("You have selected to enter Other Details")
        sleep(1)

        speak("Please enter the Type :")
        Type1 = str(input("Please enter the Type :"))
        sleep(1)

        speak("Please enter the name :")
        n3 = str(input("Please enter the name :"))
        sleep(1)

        speak("Please enter Amount Payable :")
        payable = str(input("Please enter Amount Payable :"))
        sleep(1)

        speak("Please enter Recurrence :")
        rec2 = str(input("Please enter Recurrence :"))
        sleep(1)

        speak("Please enter Due Date :")
        due_date2 = str(input("Please enter Due Date :"))
        sleep(1)

        speak("You have successfully uploaded your details :")
        print("You have successfully uploaded your details !")
        sleep(1)

#######################################
class Bank_balance:
    def bank_balance():
        print('Hi, Welcome! You have selected to check your Bank Balance!')
        speak('Hi, Welcome! You have selected to check your Bank Balance!')
        sleep(1)

        Bank_Balance= 450000
        cash_balance= 400000

        Total_bal= Bank_Balance + cash_balance

        print('Your Current Bank Balance is ' + str(Bank_Balance) + " & your cash balance is " + str(cash_balance))
        speak('Your Current Bank Balance is ' + str(Bank_Balance) + " & your cash balance is " + str(cash_balance))
        sleep(1)

    def Newrecord():
        print('Hi, Welcome! You have selected to add new record to your bank balance!')
        speak('Hi, Welcome! You have selected to add new record to your bank balance!')
        sleep(1)

        print('Please select the following that you want to proceed with : ')
        speak('Please select the following that you want to proceed with : ')
        print('1) Bank Balance')
        print('2) Cash Balance')
        bal= takecommmand().lower()

        if 'bank balance' in bal:
            print('Hi, Welcome! You have selected to add new record to your bank balance!')
            speak('Hi, Welcome! You have selected to add new record to your bank balance!')
            sleep(1)

            print("You may proceed to edit bank balance from below or add new bank balance details : ")
            speak("You may proceed to edit bank balance from below or add new bank balance details : ")
            sleep(1)
            Bank_balance.bank_bal_record()
        elif 'cash balance' in bal:
            print('Hi, Welcome! You have selected to add new record to your cash balance!')
            speak('Hi, Welcome! You have selected to add new record to your cash balance!')
            sleep(1)

            print("You may proceed to edit cash balance from below or add new cash balance details : ")
            speak("You may proceed to edit cash balance from below or add new cash balance details : ")
            sleep(1)
            Bank_balance.cash_bal_record()
        sleep(1)

    def bank_bal_record():
        speak("Please enter the Bank :")
        Bank1 = str(input("Please enter the Bank :"))
        sleep(1)

        speak("Please enter the Account Type :")
        acc_type = str(input("Please enter the Account Type :"))
        sleep(1)

        speak("Please enter the Account Number :")
        acc_no = str(input("Please enter the Account Number :"))
        sleep(1)

        speak("Please enter the Balance :")
        bal1 = str(input("Please enter the Balance :"))
        sleep(1)

        speak("Please enter the Date Updated :")
        date_upt = str(input("Please enter the Date Updated :"))
        sleep(1)

        print('Thanks you have successfully updated your bank balance!')
        speak('Thanks you have successfully updated your bank balance!')
        sleep(1)

    def cash_bal_record():
        speak("Please enter the Balance Amount :")
        bal1 = str(input("Please enter the Balance Amount :"))
        sleep(1)

        speak("Please enter the Date Updated :")
        date_upt = str(input("Please enter the Date Updated :"))
        sleep(1)

        print('Thanks you have successfully updated your cash balance!')
        speak('Thanks you have successfully updated your cash balance!')
        sleep(1)

#######################################
class Wallet:
    def Wallet():
        print('Hi, Welcome! You have selected to check your Wallet!')
        speak('Hi, Welcome! You have selected to check your Wallet!')
        sleep(1)

        Wallet_bal= 450000

        print('Your Current Wallet Balance is ' + str(Wallet_bal))
        speak('Your Current Wallet Balance is ' + str(Wallet_bal))
        sleep(1)
        while True:
            print('Do you want to TopUp your wallet or do Payment transfer your balance : ')
            speak('Do you want to TopUp your wallet or do Payment transfer your balance : ')
            print('1) Yes')
            print('2) No')
            sleep(1)
            in1= takecommmand().lower()
            if 'yes' in in1:
                print('Hi, You have selected to do transaction in your Wallet!')
                speak('Hi, You have selected to do transaction in your Wallet!')
                sleep(1)
                while True:
                    print('Please select the following that you want to proceed with : ')
                    speak('Please select the following that you want to proceed with : ')
                    print('1) Top-Up Wallet')
                    print('2) Wallet to Wallet Transfer')
                    print('3) Own Bank Transfer')
                    trans= takecommmand().lower()
                    if 'topup wallet' in trans or 'top up wallet' in trans or '1' in trans:
                        print("You have selected to topup your wallet!")
                        speak("You have selected to topup your wallet!")
                        sleep(1)

                        speak("Please enter the amount that you want to topup with : ")
                        topup_amt = str(input("Please enter the amount that you want to topup with : "))
                        sleep(1)
                        Wallet.Payment()
                        break
                    elif 'wallet to wallet transfer' in trans or 'wallet to wallet transfer' in trans:
                        print("You have selected to topup your wallet!")
                        speak("You have selected to topup your wallet!")
                        sleep(1)

                        speak("Please enter the contact number linked to other wallet that you want to transfer to : ")
                        contact_no = str(input("Please enter the the contact number linked to other wallet : "))
                        sleep(1)

                        speak("Please enter the name of the person that you want to transfer to : ")
                        topup_amt = str(input("Please enter the the name of the person to : "))
                        sleep(1)

                        speak("Please enter the amount that you want to transfer to other wallet : ")
                        topup_amt = str(input("Please enter the amount that you want to transfer : "))
                        sleep(1)

                        print('Thanks you have successfully transfered your payment to other wallet')
                        speak('Thanks you have successfully transfered your payment to other wallet')
                        sleep(1)
                        break
                    elif 'Own Bank Transfer' in trans:
                        print("You have selected to Transfer to your Own Bank!")
                        speak("You have selected to Transfer to your Own Bank!")
                        sleep(1)

                        speak("Please enter the account number : ")
                        acc_no1 = str(input("Please enter the account number : "))
                        sleep(1)

                        speak("Please enter the account type : ")
                        acc_type = str(input("Please enter the account type : "))
                        sleep(1)

                        speak("Please enter the IFSC Code : ")
                        IFSC = str(input("Please enter the IFSC Code : "))
                        sleep(1)

                        speak("Please enter the MICR Code : ")
                        MICR = str(input("Please enter the IFSC Code : "))
                        sleep(1)

                        speak("Please enter the amount that you want to transfer : ")
                        trans_amt = str(input("Please enter the amount that you want to transfer : "))
                        sleep(1)

                        print('Thanks you have successfully transfered your payment to your bank')
                        speak('Thanks you have successfully transfered your payment to your bank')
                        sleep(4)
                        break
                break
            elif 'no' in in1:
                break
                sleep(4)

    def Payment():
        print("Please select the following options to proceed with payment :")
        speak("Please select the following options to proceed with payment :")
        sleep(1)
        while True:
            print('1) UPI')
            print('2) Debit Card')
            print('3) Credit Card')
            payment= takecommmand().lower()
            if 'u p i' in payment:
                print("You have selected to proceed with UPI")
                speak("You have selected to proceed with UPI")
                sleep(1)

                speak("Please enter the phone number :")
                phone_no = str(input("Please enter the phone number :"))
                sleep(1)

                speak("Please enter the beneficiary name :")
                bene_name = str(input("Please enter the beneficiary name :"))
                sleep(1)

                print('Thanks you have successfully done payment with UPI')
                speak('Thanks you have successfully done payment with UPI')
                sleep(1)
                break
            elif 'debit card' in payment:
                print("You have selected to proceed with debit card")
                speak("You have selected to proceed with debit card")
                sleep(1)

                speak("Please enter the card number :")
                card_no = str(input("Please enter the card number :"))
                sleep(1)

                speak("Please enter the beneficiary name :")
                bene_name1 = str(input("Please enter the beneficiary name :"))
                sleep(1)

                speak("Please enter the expiry date :")
                exp_date = str(input("Please enter the expiry date :"))
                sleep(1)

                speak("Please enter the CVV Code :")
                cvv_code = str(input("Please enter the CVV Code :"))
                sleep(1)

                print('Thanks you have successfully done payment with your debit card! ')
                speak('Thanks you have successfully done payment with your debit card!')
                sleep(1)
                break
            elif 'credit card' in payment:
                print("You have selected to proceed with Credit Card")
                speak("You have selected to proceed with Credit Card")
                sleep(1)

                speak("Please enter the Credit card number :")
                card_no1 = str(input("Please enter the Credit card number :"))
                sleep(1)

                speak("Please enter the beneficiary name :")
                bene_name2 = str(input("Please enter the beneficiary name :"))
                sleep(1)

                speak("Please enter the expiry date :")
                exp_date1 = str(input("Please enter the expiry date :"))
                sleep(1)

                speak("Please enter the CVV Code :")
                cvv_code1 = str(input("Please enter the CVV Code :"))
                sleep(1)

                print('Thanks you have successfully done payment with your Credit card! ')
                speak('Thanks you have successfully done payment with your Credit card!')
                sleep(1)
                break

#######################################
class Money_Transfer:
    def Money_Transfer():
        print('Hi, Welcome! You have selected to money transfer section')
        speak('Hi, Welcome! You have selected to money transfer section')
        sleep(1)

        print('Please select the following that you want to proceed with : ')
        speak('Please select the following that you want to proceed with : ')
        print('1) Send Money')
        print('2) Receive Money')
        money_trans= takecommmand().lower()
        if 'send money' in money_trans:
            payables=2000
            money_sent=500
            print('Your payables are ' + payables + "& your total money sent is " + money_sent)
            speak('Your payables are ' + payables + "& your total money sent is " + money_sent)
            sleep(1)

            print('Do you want to send money : ')
            speak('Do you want to send money : ')
            print('1) Yes')
            print('2) No')
            sleep(1)
            send_money= takecommmand().lower()
            if 'yes' in send_money:
                print('You have selected to send money : ')
                speak('You have selected to send money : ')
                sleep(1)
                speak("Please enter the amount that you want to send : ")
                amount_send = str(input("Please enter the amount that you want to send : "))
                sleep(1)
                print('Thanks you have successfully sent money')
                speak('Thanks you have successfully sent money')
                sleep(1)
            elif 'no' in send_money:
                print('You do want to send money!')
                speak('You do want to send money!')
        elif 'receive money' in money_trans:
            print('Hi, Welcome! You have selected to receive money')
            speak('Hi, Welcome! You have selected to receive money')
            sleep(1)
            
################################
class Bill_payment:
    def Bill_payment():
        print('Hi, Welcome! You have selected to Bill Payments')
        speak('Hi, Welcome! You have selected to Bill Payments')
        sleep(1)

        while True:
            print('Please select the following that you want to proceed with : ')
            speak('Please select the following that you want to proceed with : ')
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
            bill_pay= takecommmand().lower()
            if "recharge mobile" in bill_pay:
                print('Hi, Welcome! You have selected to Recharge Mobile')
                speak('Hi, Welcome! You have selected to Recharge Mobile')
                sleep(1)

                speak("Please enter the mobile no that you want to recharge : ")
                rech_mob = str(input("Please enter the mobile no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your mobile!')
                speak('Thanks you have successfully recharged your mobile!')
                sleep(1)
                break
            elif 'postpaid  mobile bill' in bill_pay:
                print('Hi, Welcome! You have selected to Postpaid Mobile Bill')
                speak('Hi, Welcome! You have selected to Postpaid Mobile Bill')
                sleep(1)

                speak("Please enter the mobile no that you want to recharge : ")
                postpaid_mob = str(input("Please enter the mobile no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your postpaid mobile!')
                speak('Thanks you have successfully recharged your postpaid mobile!')
                sleep(1)
                break
            elif 'dth' in bill_pay:
                print('Hi, Welcome! You have selected to DTH Recharge')
                speak('Hi, Welcome! You have selected to DTH Recharge')
                sleep(1)

                speak("Please enter the DTH Operator that you use : ")
                dth_op = str(input("Please enter the DTH Operator that you use: "))
                sleep(1)

                speak("Please enter your DTH subscriber no that you want to recharge : ")
                dth_sub = str(input("Please enter your DTH subscriber no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your DTH!')
                speak('Thanks you have successfully recharged your DTH!')
                sleep(1)
                break
            elif 'broadband bill' in bill_pay:
                print('Hi, Welcome! You have selected to Broadband/ landline bill')
                speak('Hi, Welcome! You have selected to Broadband/ landline bill')
                sleep(1)

                speak("Please enter the broadband no that you want to recharge : ")
                brodband_no = str(input("Please enter the broadband or landline no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your postpaid mobile!')
                speak('Thanks you have successfully recharged your postpaid mobile!')
                sleep(1)
                break
            elif 'cable tv' in bill_pay:
                print('Hi, Welcome! You have selected to Cable TV')
                speak('Hi, Welcome! You have selected to Cable TV')
                sleep(1)

                speak("Please enter the cable tv Operator that you use : ")
                cable_op = str(input("Please enter the cable tv Operator that you use: "))
                sleep(1)

                speak("Please enter your cable tv subscriber no that you want to recharge : ")
                cable_sub = str(input("Please enter your Dcable tvTH subscriber no that you want to recharge : "))
                sleep(1)

                print('Thanks you have successfully recharged your cable tv!')
                speak('Thanks you have successfully recharged your cable tv!')
                sleep(1)
                break        
            elif 'electricity bills' in bill_pay:
                print('Hi, Welcome! You have selected to Electricity Bills')
                speak('Hi, Welcome! You have selected to Electricity Bills')
                sleep(1)

                speak("Please enter your State : ")
                ele_state = str(input("Please enter your State "))
                sleep(1)

                speak("Please enter your City : ")
                ele_city = str(input("Please enter your city "))
                sleep(1)

                speak("Please enter your electricity distributer : ")
                ele_dis = str(input("Please enter your electricity distributer  "))
                sleep(1)

                speak("Please enter your connection type : ")
                ele_conn = str(input("Please enter your connection type  "))
                sleep(1)

                speak("Please enter your CA Number : ")
                ele_CA = str(input("Please enter your CA Number : "))
                sleep(1)

                print('Thanks you have successfully paid your electricity bills!')
                speak('Thanks you have successfully paid your electricity bills!')
                sleep(1)
                break
            elif 'gas bills' in bill_pay:
                print('Hi, Welcome! You have selected to Gas Bills')
                speak('Hi, Welcome! You have selected to Gas Bills')
                sleep(1)

                speak("Please enter your State : ")
                gas_state = str(input("Please enter your State "))
                sleep(1)

                speak("Please enter your City : ")
                gas_city = str(input("Please enter your city "))
                sleep(1)

                speak("Please enter your Gas Supplier : ")
                gas_sup = str(input("Please enter your Gas Supplier  "))
                sleep(1)

                speak("Please enter your customer ID : ")
                gas_ID = str(input("Please enter your customer ID :  "))
                sleep(1)

                print('Thanks you have successfully paid your Gas bills!')
                speak('Thanks you have successfully paid your Gas bills!')
                sleep(1)
                break
            elif 'water bill' in bill_pay:
                print('Hi, Welcome! You have selected to proceed with water Bill')
                speak('Hi, Welcome! You have selected to proceed with water Bill')
                sleep(1)

                speak("Please enter your State : ")
                water_state = str(input("Please enter your State : "))
                sleep(1)

                speak("Please enter your City : ")
                water_city = str(input("Please enter your city : "))
                sleep(1)

                speak("Please enter your Board : ")
                water_sup = str(input("Please enter your Board : "))
                sleep(1)

                speak("Please enter your customer ID : ")
                water_ID = str(input("Please enter your customer ID :  "))
                sleep(1)

                print('Thanks you have successfully paid your water bills!')
                speak('Thanks you have successfully paid your water bills!')
                sleep(1)
                break
            elif 'emi payments' in bill_pay:
                print('Hi, Welcome! You have selected to EMI Payments')
                speak('Hi, Welcome! You have selected to EMI Payments')
                sleep(1)

                speak("Please enter your Financial Institution : ")
                Fin_Ins = str(input("Please enter your Financial Institution : "))
                sleep(1)

                speak("Please enter your loan Account No : ")
                loan_acc_no = str(input("Please enter your loan Account No :  "))
                sleep(1)

                print('Thanks you have successfully paid your EMI Payments!')
                speak('Thanks you have successfully paid your EMI Payments!')
                sleep(1)
                break
            elif 'card payments' in bill_pay:
                print('Hi, Welcome! You have selected to card payments')
                speak('Hi, Welcome! You have selected to Card Payments')
                sleep(1)
            speak('Please select the correct product options')
    ################################

class Insurance:
    def Insurance():
        print('Hi, Welcome! You have selected to Insurance section')
        speak('Hi, Welcome! You have selected to Insurance section')
        sleep(1)
        print("Please select the insurance that you want to proceed with : ")
        speak("Please select the insurance that you want to proceed with : ")
        print('1) Life Insurance')
        print('2) Health Insurance')
        print("3) Vehicle insurance")
        print('2) Other Insurance')
        print("3) Investment Plans")
        insurance = takecommmand().lower()
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
        speak('Hi, Welcome! You have selected to manage revenue')
        sleep(1)

        Total_Revenue = 450000
        Total_receivables= 20000
        Overdue= 900
        Projects=1

        print('Your Current total revenue balance is ' + str (Total_Revenue) + ' from which total receivables is ' + str(Total_receivables) + ' and Overdue is ' + Overdue )
        speak('Your Current total revenue balance is ' + str (Total_Revenue) + ' from which total receivables is ' + str(Total_receivables) + ' and Overdue is ' + Overdue )

        print('Please check the following detail of your generated revenue and other important metrics:')
        speak('Please check the following detail of your generated revenue and other important metrics:')
        while True:
            print("Do you want to add revenue record? :")
            speak("Do you want to add revenue record? :")
            print('1) Yes')
            print('2) No')
            t1= takecommmand().lower()
            if 'yes' in t1:
                print('You have selected to add revenue record!')
                speak('You have selected to add revenue record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    speak("Please select the following option that you want to proceed with:")
                    print('1) Record Revenue')
                    print('2) view revenue')
                    r1=takecommmand().lower()
                    if 'record revenue' in r1:
                        print("You have selected to proceed to record revenue : ")
                        speak("You have selected to proceed to record revenue : ")
                        Managerevenue.record_revenue()
                    elif 'view revenue' in r1:
                        print("You have selected to proceed to view revenue : ")
                        speak("You have selected to proceed to view revenue : ")
                        sleep(1)
                        print("You may view your revenue record from below and also share the receipt : ")
                        speak("You may view your revenue record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add revenue record!')
                speak('You have selected to not add revenue record!')
                break
            
    def record_revenue():
        print('You have selected to add revenue record for your client :')
        speak('You have selected to add revenue record for your client :')

        print('You may edit your invoice no and date from below : ')
        speak('You may edit your invoice no and date from below : ')

        print('Please enter your client name :')
        speak('Please enter your client name :')
        Managerevenue.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        speak('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new service record? :")
            speak("Do you want to add new service record? :")
            print('1) Yes')
            print('2) No')
            ser1=takecommmand().lower()
            if 'yes' in ser1:
                print("Please enter your item category : ")
                speak("Please enter your item category : ")

                print("Please enter your item Name :")
                speak("Please enter your item Name :")

                print("Please enter the listed rate: :")
                speak("Please enter the listed rate: :")

                print("Please enter the offer rate: :")
                speak("Please enter the offer rate: :")

                print("Please select the following to proceed :")
                speak("Please select the following to proceed :")
                print("Include Tax :")
                print("Exclude Tax :")

                print("Please enter HSN Code :")
                speak("Please enter HSN Code :")

                print("Please enter GST Rate: :")
                speak("Please enter GST Rate: :")

                print("Thanks, you have successfully added your service :")
                speak("Thanks, you have successfully added your service :")
            elif 'no' in ser1:
                print('You have selected to not add revenue record!')
                speak('You have selected to not add revenue record!')
                break
###############################

class Manageexpenses:
    def manage_Expenses():
        print('Hi, Welcome! You have selected to manage Expenses')
        speak('Hi, Welcome! You have selected to manage Expenses')
        sleep(1)

        Total_Expenses = 450000
        Total_payables= 20000
        Overdue= 900
        Projects=1

        print('Your Current total Expenses balance is ' + str (Total_Expenses) + ' from which total receivables is ' + str(Total_payables) + ' and Overdue is ' + Overdue )
        speak('Your Current total Expenses balance is ' + str (Total_Expenses) + ' from which total receivables is ' + str(Total_payables) + ' and Overdue is ' + Overdue )

        print('Please check the following detail of your generated Expenses and other important metrics:')
        speak('Please check the following detail of your generated Expenses and other important metrics:')
        while True:
            print("Do you want to add Expenses record? :")
            speak("Do you want to add Expenses record? :")
            print('1) Yes')
            print('2) No')
            t1= takecommmand().lower()
            if 'yes' in t1:
                print('You have selected to add Expenses record!')
                speak('You have selected to add Expenses record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    speak("Please select the following option that you want to proceed with:")
                    print('1) Record Expenses')
                    print('2) view Expenses')
                    r1=takecommmand().lower()
                    if 'record Expenses' in r1:
                        print("You have selected to proceed to record Expenses : ")
                        speak("You have selected to proceed to record Expenses : ")
                        Manageexpenses.record_Expenses()
                    elif 'view Expenses' in r1:
                        print("You have selected to proceed to view Expenses : ")
                        speak("You have selected to proceed to view Expenses : ")
                        sleep(1)
                        print("You may view your Expenses record from below and also share the receipt : ")
                        speak("You may view your Expenses record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add Expenses record!')
                speak('You have selected to not add Expenses record!')
                break
            
    def record_Expenses():
        print('You have selected to add Expenses record for your client :')
        speak('You have selected to add Expenses record for your client :')

        print('You may edit your invoice no and date from below : ')
        speak('You may edit your invoice no and date from below : ')

        print('Please enter your client name :')
        speak('Please enter your client name :')
        Manageexpenses.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        speak('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new Expenses record? :")
            speak("Do you want to add new Expenses record? :")
            print('1) Yes')
            print('2) No')
            ser2=takecommmand().lower()
            if 'yes' in ser2:
                print("Please enter your Expenses Name :")
                speak("Please enter your Expenses Name :")

                print("Please enter the Expenses amount: :")
                speak("Please enter the Expenses amount: :")

                print("Please enter the offer rate: :")
                speak("Please enter the offer rate: :")

                print("Please select the following to proceed :")
                speak("Please select the following to proceed :")
                print("Price with GST :")
                print("Price without GST")

                print("Thanks, you have successfully added your service :")
                speak("Thanks, you have successfully added your service :")
            elif 'no' in ser2:
                print('You have selected to not add Expenses record!')
                speak('You have selected to not add Expenses record!')
                break

###############################
class Manageorder:
    def manage_orders():
        print('Hi, Welcome! You have selected to manage Orders')
        speak('Hi, Welcome! You have selected to manage Orders')
        sleep(1)

        Total_Orders = 450000
        pending_Orders= 20000
        Cancelled= 900
        closed_orders=100

        print('Your Current total Orders is ' + str (Total_Orders) + ' from which pending orders is ' + str(pending_Orders) + ' and closed order is ' + closed_orders )
        speak('Your Current total Orders is ' + str (Total_Orders) + ' from which total receivables is ' + str(pending_Orders) + ' and Overdue is ' + closed_orders )

        print('Please check the following detail of your generated Orders and other important metrics:')
        speak('Please check the following detail of your generated Orders and other important metrics:')
        while True:
            print("Do you want to add Orders record? :")
            speak("Do you want to add Orders record? :")
            print('1) Yes')
            print('2) No')
            t1= takecommmand().lower()
            if 'yes' in t1:
                print('You have selected to add Orders record!')
                speak('You have selected to add Orders record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    speak("Please select the following option that you want to proceed with:")
                    print('1) Record Orders')
                    print('2) view Orders')
                    r1=takecommmand().lower()
                    if 'record orders' in r1:
                        print("You have selected to proceed to record Orders : ")
                        speak("You have selected to proceed to record Orders : ")
                        Manageorder.record_Expenses()
                    elif 'view orders' in r1:
                        print("You have selected to proceed to view Orders : ")
                        speak("You have selected to proceed to view Orders : ")
                        sleep(1)
                        print("You may view your Orders record from below and also share the receipt : ")
                        speak("You may view your Orders record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add Orders record!')
                speak('You have selected to not add Orders record!')
                break
            
    def record_Orders():
        print('You have selected to add Orders record for your client :')
        speak('You have selected to add Orders record for your client :')

        print('You may edit your Orders no and date from below : ')
        speak('You may edit your Orders no and date from below : ')

        print('Please enter your client name :')
        speak('Please enter your client name :')
        Manageorder.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        speak('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new Orders record? :")
            speak("Do you want to add new Orders record? :")
            print('1) Yes')
            print('2) No')
            ser2=takecommmand().lower()
            if 'yes' in ser2:
                print("Please enter your service name : ")
                speak("Please enter your service name : ")

                print("Please enter your sales Price :")
                speak("Please enter your sales Price :")

                print("Please select the following to proceed :")
                speak("Please select the following to proceed :")
                print("Price with GST :")
                print("Price without GST")

                print("Please enter HSN Code :")
                speak("Please enter HSN Code :")

                print("Please enter GST Rate: :")
                speak("Please enter GST Rate: :")

                print("Thanks, you have successfully added your service :")
                speak("Thanks, you have successfully added your service :")
            elif 'no' in ser2:
                print('You have selected to not add Orders record!')
                speak('You have selected to not add Orders record!')
                break

##########################################

class Managequotation:
    def manage_quotation():
        print('Hi, Welcome! You have selected to manage quotation :')
        speak('Hi, Welcome! You have selected to manage quotation')
        sleep(1)

        Total_quotation = 450000
        pending_quotation= 20000
        Cancelled= 900
        total_orders=100

        print('Your Current total quotation is ' + str (Total_quotation) + ' from which pending quotation is ' + str(pending_quotation) + ' and total order is ' + total_orders )
        speak('Your Current total quotation is ' + str (Total_quotation) + ' from which pending quotation is ' + str(pending_quotation) + ' and total order is ' + total_orders )

        print('Please check the following detail of your generated quotation and other important metrics:')
        speak('Please check the following detail of your generated quotation and other important metrics:')
        while True:
            print("Do you want to add quotation record? :")
            speak("Do you want to add quotation record? :")
            print('1) Yes')
            print('2) No')
            t1= takecommmand().lower()
            if 'yes' in t1:
                print('You have selected to add quotation record!')
                speak('You have selected to add quotation record!')
                sleep(1)
                while True:
                    print("Please select the following option that you want to proceed with:")
                    speak("Please select the following option that you want to proceed with:")
                    print('1) Record quotation')
                    print('2) view quotation')
                    r1=takecommmand().lower()
                    if 'record quotation' in r1:
                        print("You have selected to proceed to record quotation : ")
                        speak("You have selected to proceed to record quotation : ")
                        Managequotation.record_Expenses()
                    elif 'view quotation' in r1:
                        print("You have selected to proceed to view quotation : ")
                        speak("You have selected to proceed to view quotation : ")
                        sleep(1)
                        print("You may view your quotation record from below and also share the receipt : ")
                        speak("You may view your quotation record from below and also share the receipt : ")
                        sleep(1)
            elif 'no' in t1:
                print('You have selected to not add quotation record!')
                speak('You have selected to not add quotation record!')
                break
            
    def record_Orders():
        print('You have selected to add quotation record for your client :')
        speak('You have selected to add quotation record for your client :')

        print('You may edit your quotation no and date from below : ')
        speak('You may edit your quotation no and date from below : ')

        print('Please enter your client name :')
        speak('Please enter your client name :')
        Managequotation.add_service()

    def add_service():
        print('Please select the options from below to proceed or you may proceed to add new record :')
        speak('Please select the options from below to proceed or you may proceed to add new record :')
        while True:
            print("Do you want to add new quotation record? :")
            speak("Do you want to add new quotation record? :")
            print('1) Yes')
            print('2) No')
            ser2=takecommmand().lower()
            if 'yes' in ser2:
                print("Please enter your service name : ")
                speak("Please enter your service name : ")

                print("Please enter your rate :")
                speak("Please enter your rate :")

                print("Please select the following to proceed :")
                speak("Please select the following to proceed :")
                print("Price with GST :")
                print("Price without GST")

                print("Please enter HSN Code :")
                speak("Please enter HSN Code :")

                print("Please enter GST Rate: :")
                speak("Please enter GST Rate: :")

                print("Thanks, you have successfully added your service :")
                speak("Thanks, you have successfully added your service :")
            elif 'no' in ser2:
                print('You have selected to not add quotation record!')
                speak('You have selected to not add quotation record!')
                break

###############################

class leadgen:
    def lead():
        print('Hi, Welcome! You have selected to check your Leads generated: ')
        speak('Hi, Welcome! You have selected to check your Leads generated: ')
        sleep(1)

        print('You may check or edit your Leads generated from below and add new leads : ')
        speak('You may check or edit your Leads generated from below and add new leads : ')
        sleep(1)

    def lead_form():
        speak("Please Select your lead name :")
        lead_name = str(input("Please Select your lead name :"))
        sleep(1)

###############################
class Notification:
    def notification():
        print('Hi, Welcome! You have selected to check your notification preference: ')
        speak('Hi, Welcome! You have selected to check your notification preference: ')
        sleep(1)

        print('Please edit your notification preferences from below: ')
        speak('Please edit your notification preferences from below: ')
        sleep(1)

class Business_card:
    def business_card():
        print('Hi, Welcome! You have selected to check your business_card: ')
        speak('Hi, Welcome! You have selected to check your business_card: ')
        sleep(1)

        print('Please find the below business card templates that you may share and download. And also in order to edit your details please complete your profile: ')
        speak('Please find the below business card templates that you may share and download. And also in order to edit your details please complete your profile: ')
        sleep(1)

class Currency:
    def currency():
        print('Hi, Welcome! You have selected to check your currency preference: ')
        speak('Hi, Welcome! You have selected to check your currency preference: ')
        sleep(1)

        print('Please select your currency preferences from below: ')
        speak('Please select your currency preferences from below: ')
        sleep(1)
        curr=takecommmand().lower

class Calander_setting:
    def calander_setting():
        print('Hi, Welcome! You have selected to check your calander setting: ')
        speak('Hi, Welcome! You have selected to check your calander setting: ')
        sleep(1)

        print('Please edit your calander setting preferences from below: ')
        speak('Please edit your calander setting preferences from below: ')
        sleep(1)

class Feedback:
    def feedback():
        print('Hi, Welcome! You have selected to give your valuable feedback & suggestions: ')
        speak('Hi, Welcome! You have selected to give your valuable feedback & suggestions: ')
        sleep(1)

        speak("Please give your feedback for our service: ")
        feedback = str(input("Please give your feedback for our service: '"))
        sleep(1)

        speak("Please give your suggestions for our service: ")
        suggestions = str(input("Please give your suggestions for our service: '"))
        sleep(1)

class Manage_color:
    def manage_color():
        print('Hi, Welcome! You have selected to give edit the color layout of the app : ')
        speak('Hi, Welcome! You have selected to give edit the color layout of the app : ')
        sleep(1)

        print('Please edit your color layout preferences from below: ')
        speak('Please edit your color layout preferences from below: ')
        sleep(1)

class Upgrade:
    def upgrade():
        print('Hi, Welcome! You have selected to upgrade the app : ')
        speak('Hi, Welcome! You have selected to upgrade the app : ')
        sleep(1)

        print('Please select the option that you want to upgrade to : ')
        speak('Please select the option that you want to upgrade to : ')
        sleep(1)

class Recurrence:
    def recurrence():
        print('Hi, Welcome! You have selected to edit your recurrence preference: ')
        speak('Hi, Welcome! You have selected to edit your recurrence preference: ')
        sleep(1)

        print('Please edit your recurrence preferences from below: ')
        speak('Please edit your recurrence preferences from below: ')
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
        product = takecommmand().lower()
        if 'networth' in product or 'net worth' in product or '1' in product:
            Networth()
        elif 'bank balance' in product:
            bank_balance()
            while True: 
                print('Do you want to TopUp your wallet or do Payment transfer your balance : ')
                speak('Do you want to TopUp your wallet or do Payment transfer your balance : ')
                print('1) Yes')
                print('2) No')
                sleep(1)
                s1= takecommmand().lower()
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
            speak("Thanks for giving me your time")
            exit()
        speak("Please select your correct product options..")

##########################################





































