
_users = {
    'paul': {
        'name': 'Pavel Okopnyi',
        'job_title': 'PhD Candidate',
        'workplace': 'UiB'
    },

    'igor': {
        'name': 'Igor Novikov',
        'job_title': 'Designer',
        'workplace': 'ArtLebedev'
    },
    'boris': {
        'name': 'Boris Ivanov',
        'job_title': 'Cat',
        'workplace': 'HSE Sedova'
    },

    'alena': {
        'name': 'Alena Popova',
        'job_title': 'Data Scientist',
        'workplace': 'ITMO'
    }
}


_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)


# Get users filtered by name
def get_users_by_name(q):
    results = []
    # SEARCH
    return results


def get_user(username):
    return _users.get(username)
