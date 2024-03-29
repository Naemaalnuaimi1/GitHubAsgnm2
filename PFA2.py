from enum import Enum

class VisitorCategory(Enum):
    ADULT = "Adult"
    CHILD = "Child"
    STUDENT = "Student"
    SENIOR = "Senior"
    GROUP = "Group"

class Visitor:
    def __init__(self,name,age,visitor_category):
        self.name = name
        self.age = age
        self.visitor_category = visitor_category

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_visitor_category(self):
        return self.visitor_category

    def set_visitor_category(self, visitor_category):
        self.visitor_category = visitor_category


class Item:
    def __init__(self, title, artist, date_of_creation,historical_significance ):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance

    def get_title(self):
        return self.title

    def set_title(self,title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self,artist):
        self.artist = artist

    def get_date_of_creation(self):
        return self.date_of_creation

    def set_date_of_creation(self,date_of_creation):
        self.date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self.historical_significance

    def set_historical_significance(self,historical_significance):
        self.historical_significance = historical_significance

#Artwork inherits from Item

class Artwork(Item):
    def __init__(self, name, color, title,artist,date_of_creation,historical_significance ):
        super().__init__(title,artist,date_of_creation,historical_significance)
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

#Exhibition has an aggragation relationship with Item

class Exhibition:
    def __init__(self, name,duration,location ):
        self.name = name
        self.duration = duration
        self.location = location
        self.items = []

    def add_item(self , item):
        self.items.append(item)

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_duration(self):
        return self.duration

    def set_duration(self,duration):
        self.duration = duration

    def get_location(self):
        return self.location

    def set_location(self,location):
        self.location = location

#Visitor has an association relationship with Ticket

class Ticket:
    def __init__(self, exhibition_name,ticket_date,visitor_type,duration, location, visitor_category, ticket_price ):
        self.exhibition_name = exhibition_name
        self.ticket_date = ticket_date
        self.visitor_type = visitor_type
        self.duration = duration
        self.location = location
        self.visitor_category = visitor_category
        self.ticket_price = ticket_price

    def get_exhibition_name(self):
        return self.exhibition_name

    def set_exhibition_name(self,exhibition_name):
        self.exhibition_name = exhibition_name

    def get_ticket_date(self):
        return self.ticket_date

    def set_ticket_date(self,ticket_date):
        self.ticket_date = ticket_date

    def get_visitor_type(self):
        return self.visitor_type

    def set_visitor_type(self,visitor_type):
        self.visitor_type = visitor_type

    def get_duration(self):
        return self.duration

    def set_duration(self,duration):
        self.duration = duration

    def get_location(self):
        return self.location

    def set_location(self,location):
        self.location = location

    def get_visitor_category(self):
        return self.visitor_category

    def set_visitor_category(self,visitor_category):
        self.visitor_category = visitor_category

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self,ticket_price):
        self.ticket_price = ticket_price

# SpecialEvent has a composition relationship with Exhibition

class SpecialEvent:
    def __init__(self, name,location,duration,ticket_price,exhibition ):
        self.name = name
        self.exhibition_name = exhibition_name
        self.location = location
        self.duration = duration
        self.ticket_price = ticket_price
        self.exhibition = exhibition

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self,location):
        self.location = location

    def get_duration(self):
        return self.duration

    def set_duration(self,duration):
        self.duration = duration

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self,ticket_price):
        self.ticket_price = ticket_price

    def get_exhibition(self):
        return self.exhibition

    def set_exhibition(self,exhibition):
        self.exhibition = exhibition





