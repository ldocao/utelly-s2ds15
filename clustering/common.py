import uuid
from utils import becomes_list, add_to_list
import metric.numerical_distance as numdist



##duration should be expressed as datetime.timedelta object
UNKNOWN = None #define what should be put if unknown or not available


class Group():
    """Group found from clustering"""

    def __init__(self, keywords, members):
        self._id = uuid.uuid4() ##need to change uuid to pymongo objectid
        self.keywords = becomes_list(keywords)
        self.members = becomes_list(members)

    def add_member(self, new_member):
        self.members = add_to_list(self.members,new_member)


    def __repr__(self):
        return str(self.__class__.__name__)+"("+str(len(self.members))+")"




class Event():
    """Event

    Parameters:
    ----------
    **kwargs: key (string) = value (float)
        set of attributes
    """

    def __init__(self, **kwargs):
        self._id = uuid.uuid4()

        ##recursively define class attributes
        for key, value in kwargs.items():
            setattr(self, key, value)





        
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
