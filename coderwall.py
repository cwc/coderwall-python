"""
This module provides a simple interface to the API at http://coderwall.com.

Uses the json module introduced in Python 2.6.

See the CoderWall class for a usage example. The module can also be used as a
standalone script (i.e. 'python -m coderwall').
"""

import json
import urllib2

class CoderWall:

    """
    Represents a CoderWall user and provides access to all of the user's data.

    Fields:

    name
    location
    endorsements
    badges

    Usage:

    >>> cwc = CoderWall('cwc')
    >>> cwc.name
    u'Cameron Currie'
    >>> cwc.location
    u'Austin, TX'
    >>> cwc.endorsements
    0
    >>> cwc.badges
    [Charity: Fork and commit to someone's open source project in need, 
    Python: Would you expect anything less? Have at least one original repo 
    where Python is the dominant language, T-Rex: Have at least one original 
    repo where C is the dominant language]
    >>> cwc.badges[0].image_uri
    http://cdn.coderwall.com/assets/badges/charity-bf61e713137d910534ff805f389bcffb.png
    >>> print cwc
    Cameron Currie (cwc), Austin, TX, Endorsed 0 times: [Charity: Fork and 
    commit to someone's open source project in need, Python: Would you expect 
    anything less? Have at least one original repo where Python is the dominant 
    language, T-Rex: Have at least one original repo where C is the dominant 
    language]
    """

    def __init__(self, username):
        self.username = username

        data = parse_json_data(get_json_data(self.username))

        if data is not None:
            self.name = data[0]
            self.location = data[1]
            self.endorsements = data[2]
            self.badges = parse_badges(data[3])
        else:
            raise NameError(self.username + ' does not appear to be a CoderWall user')

    def __repr__(self):
        return "CoderWall(username=%r)" % (self.username)

    def __str__(self): 
        return self.name + ' (' + self.username + '), ' + self.location + ', Endorsed ' + str(self.endorsements) + ' times: ' + str(self.badges)

class Badge:

    """
    Represents a CoderWall badge and provides access to its attributes, such as
    the image URL.

    Fields:

    name
    description
    image_uri
    """ 
    
    def __init__(self, name, description, image_uri):
        self.name = name
        self.description = description
        self.image_uri = image_uri

    def __repr__(self):
        return "Badge(name=%r,description=%r,image_uri=%r)" % (self.name, self.description, self.image_uri)

    def __str__(self):
        return self.name + ': ' + self.description

def get_json_data(username):
    """
    Connect to CoderWall and return the raw JSON data for the given 
    username. 
    """

    api_url = 'http://coderwall.com/' + username + '.json'

    try:
        response = urllib2.urlopen(api_url, None, 5)
    except urllib2.URLError:
        return '' # TODO Better error handling

    return response.read()

def parse_json_data(json_data):
    """ Parse the given JSON data and return data about the user. """

    try:
        data = json.loads(json_data)
    except ValueError:
        return None # TODO Better error handling

    name = data['name']
    location = data['location']
    endorsements = data['endorsements'] 
    badges = data['badges']

    return (name, location, endorsements, badges)

def parse_badges(raw_badges):
    """
    Parse the given list of dictionaries, interpret each as a 
    CoderWall badge, and return a list of Badge objects.
    """

    badges = []
    for raw_badge in raw_badges:
       badges.append(Badge(raw_badge['name'], 
            raw_badge['description'], raw_badge['badge']))

    return badges

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print 'Usage: ' + sys.argv[0] + ' USERNAME...'
    else:
        for username in sys.argv[1:]:
            print CoderWall(username)
