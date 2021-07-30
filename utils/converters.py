from datetime import datetime, timedelta

def getest():
    delta = timedelta(hours=4)
    Time = datetime.utcnow() - delta
    return Time.strftime("%a, %d %b %Y @ %I:%M:%S %p EST")
