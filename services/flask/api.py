import datetime as dt
from flask import Flask, jsonify, request
from exceptions import InvalidUserType


class UserStatusSearch:
    P = 'paying'
    C = 'cancelled'
    NP = 'non-paying'

    RECORDS = [
        {'user_id': 1, 'created_at': '2017-01-01T10:00:00', 'status': P},
        {'user_id': 1, 'created_at': '2017-03-01T19:00:00', 'status': P},
        {'user_id': 1, 'created_at': '2017-02-01T12:00:00', 'status': C},
        {'user_id': 2, 'created_at': '2017-09-01T17:00:00', 'status': P},
        {'user_id': 3, 'created_at': '2017-10-01T10:00:00', 'status': P},
        {'user_id': 3, 'created_at': '2016-02-01T05:00:00', 'status': C},
    ]

    def __init__(self):
        super(UserStatusSearch, self).__init__()

    def get_status(self, user_id, date):
        """
        :param user_id:  int represents the id of user
        :param date: datetime type with pattern = year-month-dayThour:minute:second <=> '2016-02-01T05:00:00'
        :return: string, the correct `user_status` at the given time. :args 'user_id, date' are not type specified! we have
        to ensure that user_id is an Integer and date is a valid Date """

        if not isinstance(date, dt.datetime) or not isinstance(user_id, int):
            return self.NP
            # in other use cases, we could raise an Exception for each type check! one by one verification
            # raise Exception('Not valid user ID!')
            # raise Exception('Not valid Date!')

        for record in self.RECORDS:
            if record['user_id'] == user_id and dt.datetime.strptime(record['created_at'], "%Y-%m-%dT%H:%M:%S") == date:
                return record['status']

        return self.NP


class IpRangeSearch:
    RANGES = {
        'london': [
            {'start': '10.10.0.0', 'end': '10.10.255.255'},
            {'start': '192.168.1.0', 'end': '192.168.1.255'},
        ],
        'munich': [
            {'start': '10.12.0.0', 'end': '10.12.255.255'},
            {'start': '172.16.10.0', 'end': '172.16.11.255'},
            {'start': '192.168.2.0', 'end': '192.168.2.255'},
        ]
    }

    def __init__(self):
        super(IpRangeSearch, self).__init__()

    def __ip_to_intarray__(self, ip):
        """ split a string IP address into 4 integers.
        :param ip: is a string represent an IP @ 32bits
        :return: an array containing 4 integers
        (we are not verifying that each integer should in range [0-255] to be a valid IP @) """
        return [int(x) for x in ip.split('.')]

    def get_city(self, ip):
        """
        search for city name from different ip adresses range
        :param ip: is a string represent an IP @ 32bits
        :return: the city of an IP@ or '**unknown**'
        """
        if not isinstance(ip, str):
            return '**unknown**'
        try:
            # if it is a valid ip address that could be splitted in 4 integers or it will throw an error
            ip4 = self.__ip_to_intarray__(ip)
        except:
            # this is not a valid IP4@, it throws an Exception..
            return '**unknown**'

        for k, v in self.RANGES.items():
            for netip in v:
                start = self.__ip_to_intarray__(netip['start'])
                end = self.__ip_to_intarray__(netip['end'])

                if (ip4[0] >= start[0] and ip4[0] <= end[0]) and (ip4[1] >= start[1] and ip4[1] <= end[1]) and (
                        ip4[2] >= start[2] and ip4[2] <= end[2]) and (ip4[3] >= start[3] and ip4[3] <= end[3]):
                    return k

        return '**unknown**'


app = Flask(__name__)
user_status_search = UserStatusSearch()
ip_range_search = IpRangeSearch()



@app.errorhandler(InvalidUserType)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# this endpoint = /user_status/<user_id>?date=2017-10-10T10:00:00
# accepts user_id as a resource in the url_pattern and date as a parameter in HTTP request in the methode GET
@app.route('/user_status/<user_id>')  ##  oblige to only accepts <int:user_id>
def user_status(user_id):
    """Return user status for a given date."""
    try:
        user_id = int(user_id)
    except:
        raise InvalidUserType('User ID not valid', status_code=410)

    if not request.args.get('date'):
        raise InvalidUserType('date parameter not found in the http query!', status_code=411)
    date = dt.datetime.strptime(str(request.args.get('date')), '%Y-%m-%dT%H:%M:%S')
    return jsonify({
        'user_status': user_status_search.get_status(user_id, date)
    })

# this endpoint = /ip_city/10.0.0.0
# accepts ip as a resource in the url_pattern
@app.route('/ip_city/<ip>')
def ip_city(ip):
    """Return city for a given ip."""
    #  ip = str(request.args.get('ip'))
    # in other workflow! we must verify that the ip address passed in endpoint is valid value!
    arr = ip.split('.')
    if len(arr)!=4:
        raise InvalidUserType('IP not valid', status_code=412)
    try:
        for x in [int(x) for x in arr]:
            if x<0 or x>255:
                raise InvalidUserType('IP not valid', status_code=412)
    except:
        raise InvalidUserType('IP not valid', status_code=412)
    return jsonify({'city': ip_range_search.get_city(ip)})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
