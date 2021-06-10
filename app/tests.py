from django.test import TestCase
from .models import *
from pprint import pprint 
# from model_bakery import baker

# class TestContact(TestCase):
#     def setUp(self):
#         self.contact = baker.make('app.Contact')
#         pprint(self.contact.__dict__)

#     def test_contact_user(self):
#         user = User.objects.create_user(username='Testing', password='Test@123')
#         product_user = Contact.objects.create(manager=user)
#         self.assertEqual(user, product_user.manager)


# Create your tests here.
class TitleTesting(TestCase):  # Test 1
    def test_category_title(self):
        title = Contact.objects.create(name="Name Surname")
        self.assertEqual(str(title), "Name Surname")
    def test_category_title(self):
        title = Contact.objects.create(name="Hello World")
        self.assertEqual(str(title), "Hello World")
    def test_category_title(self):
        title = Contact.objects.create(name="John Wood")
        self.assertEqual(str(title), "John Wood") 

class EmailTesting(TestCase):  # Test 2
    def test_category_email(self):
        Email = Contact.objects.create(email = str("test1@gmail.com"))
        # Email = self.stringconv(Email)
        self.assertEqual(str(Email), "test1@gmail.com") 
    def test_category_email(self):
        Email = Contact.objects.create(email = str("test123232323@gmail.com"))
        # Email = self.stringconv(Email)
        self.assertEqual(str(Email), "test123232323@gmail.com") 
    def test_category_email(self):
        Email = Contact.objects.create(email = str("just_for_testing@gg.com"))
        # Email = self.stringconv(Email)
        self.assertEqual(str(Email), "just_for_testing@gg.com")    

class GenderTesting(TestCase):  # Test 3
    def test_category_gender(self):
        Gender = Contact.objects.create(gender = str("Male"))
        self.assertEqual(str(Gender), "Male") 
    def test_category_gender(self):
        Gender = Contact.objects.create(gender = str("Female"))
        self.assertEqual(str(Gender), "Female") 

class PhoneNumberTesting(TestCase):  # Test 4
    def test_category_phone(self):
        Ph = Contact.objects.create(phone = str("8989898989"))
        self.assertEqual(str(Ph), "8989898989") 
    def test_category_phone(self):
        Ph = Contact.objects.create(phone = str("1222"))
        self.assertEqual(str(Ph), "1222") 

class INFO_Testing(TestCase):  # Test 5
    def test_category_info(self):
        Info = Contact.objects.create(info = str("Singer"))
        self.assertEqual(str(Info), "Singer") 
    def test_category_info(self):
        Info = Contact.objects.create(info = str("Software Engineer"))
        self.assertEqual(str(Info), "Software Engineer") 
    def test_category_info(self):
        Info = Contact.objects.create(info = str("Dancer"))
        self.assertEqual(str(Info), "Dancer") 
    def test_category_info(self):
        Info = Contact.objects.create(info = str("Data Scientist"))
        self.assertEqual(str(Info), "Data Scientist") 

class Detail_Testing(TestCase):  # Test Case 6
    def test_category_title(self):
        title = Contact.objects.create(name="Name Surname")
        self.assertEqual(str(title), "Name Surname")
    def test_category_email(self):
        Email = Contact.objects.create(email = str("test123232323@gmail.com"))
        # Email = self.stringconv(Email)
        self.assertEqual(str(Email), "test123232323@gmail.com") 
    def test_category_gender(self):
        Gender = Contact.objects.create(gender = str("Male"))
        self.assertEqual(str(Gender), "Male") 
    def test_category_gender(self):
        Gender = Contact.objects.create(gender = str("Female"))
        self.assertEqual(str(Gender), "Female") 
    def test_category_phone(self):
        Ph = Contact.objects.create(phone = str("8989898989"))
        self.assertEqual(str(Ph), "8989898989") 
    def test_category_info(self):
        Info = Contact.objects.create(info = str("Data Scientist"))
        self.assertEqual(str(Info), "Data Scientist") 