import uuid
from utils import becomes_list
import metrics.numerical_distance as numdist



##duration should be expressed as datetime.timedelta object
UNKNOWN = None #define what should be put if unknown or not available





class Event():
    """Event

    Parameters:
    ----------
    **kwargs: key (string) = value (float)
        set of attributes
    """

    def __init__(self, **kwargs):
        self._event_id = uuid.uuid4()
        for key, value in kwargs.items():
            setattr(self, key, value)
            
        #self.attributes = dict(kwargs) #dynamic variable names

    def __repr__(self):
        return str(self.__class__.__name__)+"("+str(self._event_id)+")"



            

class Cluster():
    """Group found from clustering"""

    def __init__(self, members=[], keywords=[]):
        self._cluster_id = uuid.uuid4() ##need to change uuid to pymongo objectid
        self.members = becomes_list(members)
        self.keywords = becomes_list(keywords)

    def add(self,new):
        try:
            self.members.extend(new)
        except TypeError:
            self.members.append(new)


    def __repr__(self):
        return str(self.__class__.__name__)+"("+str(len(self.members))+")"


    def __getattr__(self, name_of_attribute):
        return [m.__dict__.get(name_of_attribute, UNKNOWN) for m in self.members]





    
class Collection(list):
    """Collection of objects, mongo db alike

    Parameters:
    name: string
        name of collection

    objects: list of objects
        All events belonging to the collection. Must have the same structure.
    """


    ##need to define a collection efficiently. see this ? http://stackoverflow.com/questions/683/using-in-to-match-an-attribute-of-python-objects-in-an-array
    
    def __init__(self, members=[]):
        self._collection_id = uuid.uuid4()
        self.members = becomes_list(members)
        
    def add(self,new):
        try:
            self.members.extend(new)
        except TypeError:
            self.members.append(new)

    def __repr__(self):
        return self.members

    def __getattr__(self, name_of_attribute):
        return [m.__dict__.get(name_of_attribute, UNKNOWN) for m in self.members]




           
class Actor():
    """Actor(ress)"""

    def __init__(self):
        self._id = uuid.uuid4()
        self.first_name = UNKNOWN
        self.second_name = UNKNOWN
        self.last_name = UNKNOWN
        self.date_of_birth = UNKNOWN




class Metric():

    def __init__(self, name, function):
        self.name = name
        self.function = function

    def __repr__(self):
        return self.name






class Distance():

    def __init__(self, event_a, event_b, metric):
        self.metric = metric
        self.value = metric.function(event_a, event_b)


    def __repr__(self):
        return str(self.__class__.__name__)+"("+str(self.value)+","+str(self.metric)+")"
