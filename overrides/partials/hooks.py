from datetime import datetime
from dateutil import parser
import locale



def time_time(time):
    time=time.replace('-', '/')
    time = parser.parse(time).isoformat()
    try:
        time = datetime.fromisoformat(time)
        return datetime.strftime(time,'%d %B %Y')
    except AttributeError:
        return datetime.strftime(str(time),'%d %B %Y')
    except ValueError:
        print('value error!')
        return time

def time_to_iso(time):
    time=time.replace('-', '/')
    
    try:
        return parser.parse(time).isoformat()
    except AttributeError:
        return time

def on_env(env, config, files, **kwargs):
    print('locale to set:', config['theme']['language'])
    print('get locale', locale.getlocale())
    locale_toset = config['theme']['language']
    if (locale_toset != locale_toset + '_' + locale_toset.upper()):
        locale_toset = locale_toset + '_' + locale_toset.upper()
    print(locale_toset)
    locale.setlocale(locale.LC_TIME, locale_toset)
    env.filters['convert_time'] = time_time
    env.filters['iso_time'] = time_to_iso
    return env