from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

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




