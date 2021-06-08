from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import ResourceForm
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(meetingtitle='May #1 - Weekly Project Night')
        self.date=Meeting(meetingdate=datetime.date(2021,5,1))
        self.location=Meeting(meetinglocation='Virtual')

        
    def test_meetingstring(self):
        self.assertEqual(str(self.title), 'May #1 - Weekly Project Night')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resourcename='Welcome to Python.org')
        self.type=Resource(resourcetype='https://www.python.org/')
        self.dateentered=Resource(resourcedateentered=datetime.date(2021,5,10))

    def test_resourcestring(self):
        self.assertEqual(str(self.name), 'Welcome to Python.org')

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.title=Event(eventtitle='Capitol Hill Python Meetup')
        self.location=Event(eventlocation='Capitol Hill')
        self.date=Event(eventdate=datetime.date(2021,5,10))
        self.userid=User(username='Darya')

    def test_eventstring(self):
        self.assertEqual(str(self.title), 'Capitol Hill Python Meetup')

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'club_event')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.attendance=User(username='Darya')
    
    def test_meetingminutesstring(self):
        self.assertEqual(str(self.attendance), 'Darya')

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

# Ran 8 tests and OK

class NewResourceForm(TestCase):
    #valid form date
    def test_resourceform(self):
        data={
                'resourcename': "Welcome to Python.org", 
                'resourcetype': "Url", 'resourceurl': "https://www.python.org/", 
                'resourcedateentered': "2021-5-10", 
                'userid': "Darya", 
                'resourcedescription': "The official home of the Python Programming Language."
            }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

    def test_resourceform_Invalid(self):
        data={
                'resourcename': "Welcome to Python.org", 
                'resourcetype': "Url", 'resourceurl': "https://www.python.org/", 
                'resourcedateentered': "2021-05-10", 
                'userid': "Darya", 
                'resourcedescription': "The official home of the Python Programming Language."
            }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

class NewMeetingForm(TestCase):
    #valid form date
    def test_meetingform(self):
        data={
                'meetingtitle': "Python Block Party", 
                'meetingdate': "2021-06-03",  
                'meetingtime': "03/06/2021 18:00:00", 
                'meetinglocation': "Capitol Hill", 
                'meetingagenda': "In person meeting"
            }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

    def test_meetingform_Invalid(self):
        data={
                'meetingtitle': "Python Block Party", 
                'meetingdate': "2021-6-03",  
                'meetingtime': "03/06/2021 18:00:00", 
                'meetinglocation': "Capitol Hill", 
                'meetingagenda': "In person meeting"
            }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

#Ran 12 tests and OK

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='Darya', password='zhopka#0316')
        self.name=Resource.objects.create(resourcename='Welcome to Python.org',
        resourcetype='Url', resourceurl='https://www.python.org/',
        resourcedateentered=datetime.date(2021,5,10),
        userid=self.test_user,
        resourcedescription='The official home of the Python Programming Language.')
      
    def test_user_enters_valid_date(self):
        response=self.client.post(reverse('login'),{'username': self.test_user, 'password':'zhopka#0316'}, follow=True)

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='Darya', password='zhopka#0316')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'Darya')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newresource.html')

#Ran 14 tests and OK

          






