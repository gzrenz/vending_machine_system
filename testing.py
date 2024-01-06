import json

sample = {'ObjectInterpolator': 1629,  'PointInterpolator': 1675, 'RectangleInterpolator': 2042}

with open('result.json', 'w') as fp:
    json.dump(sample, fp)

from accounts import Accounts

accs = Accounts("accounts.json")
accs.set_logged_account("genczar")
accs.set_account_password("Genczar1435")