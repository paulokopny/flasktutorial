
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
    }
}


def get_user(username):
    return _users.get(username)
