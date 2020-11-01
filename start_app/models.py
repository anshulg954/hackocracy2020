from django.db import models


#  companies tryping to get funding.
# find sucess ratio such product.
class Company_CEO(models.Model):
    fullname = models.CharField(max_length=100) # name of CEO of company.  
    emailAddress = models.EmailField() # email address of user. 
    state = models.CharField(max_length=100)  # state
    #productType = models.CharField(max_length=100)  # which type of product company will be selling
    budgetRange = models.IntegerField()  # budget is in Millions.
    phoneNumber = models.CharField(max_length=20) # phone number of company.     
    isConfirmed = models.BooleanField()  # whether user is confirmed.
    
    def __str__(self):
        return self.fullname  # get the fullname.

    def get_absolute_url(self):
        return f"companyView/{self.emailAddress}-{self.productType}"
    

# Funder want to fund Companies.
# match Funders with Startup. 
class Funder(models.Model):
    ventureName = models.CharField(max_length=100)  # name of venture want to fund.
    maximum_funding_capacity = models.IntegerField(default=0)  # maximum funding capacities in Million.
    emailAddress = models.EmailField()  # email address of venture
    # space seprated names of product companies what to fund. 
    productType = models.CharField(max_length=300)
    # List of states where peoples want to fund.
    state_list = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=300)  # phone number of company.
    isConfirmed = models.BooleanField() # is user is confirmed.
    minimum_accepted_score = models.FloatField(default=0.0)

    def __str__(self): 
        return self.emailAddress  # get fullname.
        
    def get_absolute_url(self):
        return f"FunderView/{self.emailAddress}_{self.ventureName}" # url to view the Funder



class StartUpProduct(models.Model):
    productID = models.AutoField(primary_key=True)  # auto increment id.
    productName = models.CharField(max_length = 200)
    productType = models.CharField(max_length=100)  # type of product.
    shortDescription = models.TextField()  # short description of prouduct.
    # binary relation between product and comapnies CEO. 
    company_ceo = models.ForeignKey(Company_CEO, on_delete=models.PROTECT, related_name='product_company')
    patent = models.BooleanField(default=False)
    predicted_score = models.FloatField(default=0)
    # do company have copyright of application.

    def __str__(self):
        return str(self.productID) + self.productType

    def predictScore(self):
        list_of_words = self.shortDescription.split(' ')
        score = (5*list_of_words.count('AI')+2*list_of_words.count('Efficient')-3*list_of_words.count('C')+
               5*list_of_words.count('Python')+2*list_of_words('Android')+3*list_of_words.count('DataBase'))
        self.predicted_score=score

    def get_absolute_url(self):
        return f"Product/{self.productID}-{self.productType}" # seprate url for this.

# mapping done by Machine based on simple algorithm. 
class Company_Funder_Mapping(models.Model):
    company_emailAddress = models.EmailField() # company email address. 
    funder_emailAddress = models.EmailField()  # funder email addresss.
    

# Filtered Maping Done by AI based on rigrous training
class AI_filtered_Company_Funder_Mapping(models.Model):
    company_emailAddress = models.EmailField()  # company email address.
    funder_emailAddress = models.EmailField() # funder email address  


# OTP generator
class usrOTP(models.Model):
    emailAddress = models.EmailField()  # email address of usr
    otp = models.IntegerField()  # otp generator.
    generated_time_date = models.DateTimeField(auto_now_add=True)  # time and add of otp generated.
    
    def __str__(self):
        return self.emailAddress # email address as label. 