from datetime import timedelta

def add(moment):
    delta = timedelta(seconds=pow(10, 9))
    return moment + delta
