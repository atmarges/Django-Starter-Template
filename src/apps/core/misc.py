from datetime import date


def get_date_dir(pre=None, post=None):
    today = date.today().strftime('%Y/%m/%d/')
    dirs = [pre, today, post]
    dirs = [i for i in dirs if i]
    return ''.join(dirs)
