import sys
from nose import with_setup

import coderwall
from coderwall import CoderWall

real_get_json_data = coderwall.get_json_data


def get_mock_data(*username):
    return """
    {
        "name": "Cameron Currie",
        "location": "Texas",
        "endorsements": 7,
        "badges": [
            {
                "name": "Test Badge 1",
                "description": "A test badge 1",
                "badge": "http://test.badge1"
            },
            {
                "name": "Test Badge 2",
                "description": "A test badge 2",
                "badge": "http://test.badge2"
            }
        ]
    }
    """


def setUp():
    coderwall.get_json_data = get_mock_data


def tearDown():
    coderwall.get_json_data = real_get_json_data


@with_setup(setUp, tearDown)
def test_parse_json_data():
    result = coderwall.parse_json_data(get_mock_data())

    assert result[0] == 'Cameron Currie'
    assert result[1] == 'Texas'
    assert result[2] == 7

    assert len(result[3]) == 2
    assert result[3][0]['name'] == 'Test Badge 1'
    assert result[3][0]['badge'] == 'http://test.badge1'


@with_setup(setUp, tearDown)
def test_parse_badges():
    raw_badges = coderwall.parse_json_data(get_mock_data())[3]
    badges = coderwall.parse_badges(raw_badges)

    assert len(badges) == 2
    assert badges[0].name == 'Test Badge 1'
    assert badges[0].image_uri == 'http://test.badge1'


@with_setup(setUp, tearDown)
def test_coderwall_parsing():
    cwc = CoderWall('cwc')

    assert cwc.username == 'cwc'
    assert cwc.location == 'Texas'
    assert cwc.endorsements == 7

    assert len(cwc.badges) == 2
    assert cwc.badges[0].name == 'Test Badge 1'
    assert cwc.badges[0].image_uri == 'http://test.badge1'


@with_setup(setUp, tearDown)
def test_coderwall_to_str():
    cwc = CoderWall('cwc')
    expStr2 = """Cameron Currie (cwc), Texas, Endorsed 7 times: [Badge(name=u'Test Badge 1',description=u'A test badge 1',image_uri=u'http://test.badge1'), Badge(name=u'Test Badge 2',description=u'A test badge 2',image_uri=u'http://test.badge2')]"""
    expStr3 = """Cameron Currie (cwc), Texas, Endorsed 7 times: [Badge(name='Test Badge 1',description='A test badge 1',image_uri='http://test.badge1'), Badge(name='Test Badge 2',description='A test badge 2',image_uri='http://test.badge2')]"""

    if sys.version_info[0] >= 3:
        expStr = expStr3
    else:
        expStr = expStr2

    assert str(cwc) == expStr, "str(cwc) was: %s, expected: %s" % (str(cwc), expStr)
