from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from .models import Funder, Company_CEO, usrOTP, StartUpProduct
from .utils import sendMail_otp_version
import random 

def homepageRender(request):
    context = {}
    return render(request, 'start_app/start_app.home.html', context)  # responce.
    

#### funder side registration process. 

def funderRegisterView(request):
    context = {}
    if request.method == "post":
        signin_userName = request.POST.get('usernameSigin') # sigin username, 
        signin_password = request.POST.get('passwordSignin') # sigin password. 
    else:
        return render(request, 'Funder/registerPage.html', context)  # responce.
    
def startupRegisterView(request):
    context = {}
    return render(request, 'Company/registerPage.html', context)

def roleSelectViewSingup(request):
    context = {}
    return render(request, 'start_app/signup.role.html', context)  # responce.
    
def roleSelectViewSignin(request):
    context = {}
    return render(request, 'start_app/signin.role.html', context)  # responce.
    

def funderSignup(request):
    context = {}
    context['emailAlreadyRegistered'] = False 
    if request.method == "POST":
        emailAddress = request.POST.get('userEmail') # user email address 
        password = request.POST.get('userPassword') # user password 
        maxFunding = request.POST.get('maxFunding') # user funding.  
        telNumber = request.POST.get('userTelnumber')  # user telNumber
        domain = request.POST.get('userDomain')  # user Domain.
        ventureName = request.POST.get('ventureName')
        score = request.POST.get('score')
        # name of venture
        print(emailAddress)
        print(password)
        print(maxFunding)
        print(telNumber)
        print(domain)
        print(ventureName)
        try:
            user = User.objects.create_user(emailAddress, email=emailAddress, password=password)
            funder = Funder()
            funder.emailAddress = emailAddress
            funder.isConfirmed = False
            funder.phoneNumber = telNumber
            funder.maximum_funding_capacity = maxFunding
            funder.productType = domain
            funder.ventureName = ventureName
            funder.minimum_accepted_score = float(score)
            funder.save()  # save the funder
            otp = random.randint(1234, 9999)
            sendMail_otp_version(emailAddress, ventureName, "Investor", otp)  # Send mail.
            otp_sent = usrOTP()
            otp_sent.emailAddress = emailAddress
            otp_sent.otp = otp
            otp_sent.save()  # save it for further use.
            request.session['username'] = emailAddress
            user = authenticate(username=emailAddress, password=password)
            login(request,user) 
            context['userData'] = Funder.objects.get(emailAddress=emailAddress) 
            return render(request, 'Funder/funderNotConfirmed.html', context)
        except:
            context['emailAlreadyRegistered'] = True
            context['emailTarget'] = emailAddress
        return render(request, 'Funder/funderSignup.html', context) # responce. 
    return render(request, 'Funder/funderSignup.html', context)
    

def confirmOTPFunder(request):
    context = {}
    context['wrongotp'] = False 
    if request.method == "POST": 
        emailAddress = request.user.username
        print(emailAddress)
        otp = request.POST.get('otp')
        data = usrOTP.objects.get(emailAddress=emailAddress)
        otp = int(otp)
        if data.otp == otp:
            userdata = Funder.objects.get(emailAddress=emailAddress)
            userdata.isConfirmed = True
            userdata.save()
            return render(request, 'Funder/funderDashBoard.html', context)  # responce.
        else:
            context['wrongotp'] = True
            context['userData'] = Funder.objects.get(emailAddress=emailAddress) # get the Funder Data. 
            return render(request, 'Funder/funderNotConfirmed.html', context) # responce.   
    else:
        return render(request, 'start_app/start_app.home.html', context) 
    

def funderDashBoard(request):
    context = {}



def funderLogin(request):
    context = {}
    context['wrongCredentail'] = False 
    if request.method == "POST":
        username = request.POST.get('username') # user's username 
        password = request.POST.get('password')  # user's password
        user = authenticate(username=username, password=password)
        if user is not None:
            funder = Funder.objects.get(emailAddress=username)
            if funder.isConfirmed:
                context['userData'] = funder
                request.session['username'] = username 
                login(request, user)

                try:
                    productList = StartUpProduct.objects.filter(productType=funder.productType)  # type of products funder want's to fund.
                    context['haveProduct'] = True 
                    print(productList) # get the product List. 
                except:
                    productList = []  # empty List.
                    context['haveProduct'] = False
                print(productList)
                context['productList'] = [i for i in productList if i.company_ceo.budgetRange < funder.maximum_funding_capacity
                                          and i.predicted_score >= funder.minimum_accepted_score]  # add data in productList.
                return render(request, 'Funder/funderDashBoard.html', context) # responce 
            else:
                context['userData'] = funder
                return render(request, 'Funder/funderNotConfirmed.html', context) # responce. 
        else:
            context['wrongCredentail'] = True
            return render(request, 'Funder/funderLogin.html', context)  # responce. 
    return render(request, 'Funder/funderLogin.html', context) # responce. 




### company ceo registration process. 

def companySigup(request):
    context = {}
    if request.method == "POST":
        emailAddress = request.POST.get('userEmail') # user email address 
        password = request.POST.get('userPassword') # user password 
        maxFunding = request.POST.get('maxFunding') # user funding.  
        telNumber = request.POST.get('userTelnumber')  # user telNumber
        #domain = request.POST.get('userDomain')  # user Domain.
        fullName = request.POST.get('fullName') # name of venture
        print(emailAddress)
        print(password)
        print(maxFunding)
        print(telNumber)
        #print(domain)
        print(fullName)
        try:
            user = User.objects.create_user(emailAddress, email=emailAddress, password=password)
            company = Company_CEO()
            company.fullname = fullName 
            company.emailAddress = emailAddress 
            #company.productType = domain
            company.budgetRange = maxFunding
            company.phoneNumber = telNumber
            company.isConfirmed = False
            company.save()
            otp = random.randint(1234, 9999)
            sendMail_otp_version(emailAddress, fullName, "Comapny", otp)  # Send mail.
            otp_sent = usrOTP()
            otp_sent.emailAddress = emailAddress
            otp_sent.otp = otp
            otp_sent.save()  # save it for further use.
            user = authenticate(username=emailAddress, password=password)
            login(request,user) 
            context['userData'] = Company_CEO.objects.get(emailAddress=emailAddress) 
            return render(request, 'Company/companyNotConfirmed.html', context)
        except:
            context['emailAlreadyRegistered'] = True
            context['emailTarget'] = emailAddress
        return render(request, 'Company/companySignup.html', context) # responce. 
    else:
        return render(request, 'Company/companySignup.html', context)  # responce.



def companyDashBoard(request): 
    context = {}
    context['productAdd'] = False 
    
    userName = request.user.username
    if request.method == "POST":
        productName = request.POST.get('productName')
        productType = request.POST.get('productDomain')
        description = request.POST.get('shortDescription')
        ispatent = request.POST.get('havePatent')
        print(productType)
        print(description)
        print(ispatent)
        product = StartUpProduct()
        product.productType = productType
        if ispatent is not None:
            ispatent = True
        else:
            ispatent = False
        product.productName = productName
        product.patent = ispatent
        product.shortDescription = description
        product.company_ceo = Company_CEO.objects.get(emailAddress = userName)
        product.save() # save the product in database. 
        context['productAdd'] = True # set modify flag. 

    if userName is not None:
        print(userName)
        company = Company_CEO.objects.get(emailAddress=userName)


        context['userData'] = Company_CEO.objects.get(emailAddress=userName)

        try:
            dataList = StartUpProduct.objects.filter(company_ceo=company)
            print(dataList)
            context['haveProduct'] = True 
            context['productList'] = dataList 
        except: 
            context['haveProduct'] = False
            context['productList'] = []

        return render(request, 'Company/companyDashBoard.html', context) # responce. 
    else:
        return render(request, 'Company/companyLogin.html', context) #  responce. 

def productView(request,productId):
    context={}
    product=StartUpProduct.objects.filter(productName=productId).first()
    FunderDetails = Funder.objects.filter(productType=product.productType)
    company = product.company_ceo
    context['userData'] = {'name': company.fullname}
    context['name'] = product.productName
    context['score'] = product.predicted_score
    context['funders'] = [i for i in FunderDetails if i.maximum_funding_capacity > company.budgetRange
                        and i.minimum_accepted_score <= product.predicted_score]
    return render(request, 'Company/producthome.html', context=context)

def confirmOTPCompnay(request):
    context = {}
    context['wrongotp'] = False 
    if request.method == "POST": 
        emailAddress = request.user.username
        print(emailAddress)
        otp = request.POST.get('otp')
        data = usrOTP.objects.get(emailAddress=emailAddress)
        otp = int(otp)
        if data.otp == otp:
            userdata = Company_CEO.objects.get(emailAddress=emailAddress)
            userdata.isConfirmed = True
            userdata.save()
            return render(request, 'Company/companyDashBoard.html', context)  # responce.
        else:
            context['wrongotp'] = True
            context['userData'] = Company_CEO.objects.get(emailAddress=emailAddress) # get the Funder Data. 
            return render(request, 'company/compnayNotConfirmed.html', context) # responce.   
    else:
        return render(request, 'start_app/start_app.home.html', context) 


def companyLogin(request): 
    context = {}
    context['wrongCredentail'] = False 
    if request.method == "POST":
        username = request.POST.get('username') # user's username 
        password = request.POST.get('password')  # user's password
        user = authenticate(username=username, password=password)
        if user is not None:
            company = Company_CEO.objects.get(emailAddress=username)
            if company.isConfirmed:
                context['userData'] = company
                request.session['username'] = username 
                #FunderDetails = Funder.objects.filter(productType=company.productType)


                # List of proudct registered 
                try:
                    dataList = StartUpProduct.objects.filter(company_ceo=company)  # get the list of product.
                    context['haveProduct'] = True 
                except:
                    dataList = []  # get the list of product.
                    context['haveProduct'] = False  
                #print(FunderDetails)
                login(request, user)
                context['productList'] = dataList 
                return render(request, 'Company/companyDashBoard.html', context) # responce 
            else:
                context['userData'] = company
                return render(request, 'Company/companyNotConfirmed.html', context) # responce. 
        else:
            context['wrongCredentail'] = True
            return render(request, 'Company/CompanyLogin.html', context)  # responce. 
    return render(request, 'Company/companyLogin.html', context) # responce.         


# logout users. 
def logoutuser(request): 
    context = {}
    logout(request) # logout user 
    return render(request, 'start_app/start_app.home.html', context)  # responce.


# add a product by ceo of company.
def addProduct(request):
    context = {}
    