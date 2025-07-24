alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    retVal = 0
    # Return 200 for ok
    # Return 500 for not-ok
    if celcius > 200:
        retVal = 500
    else:
        retVal = 200
    return retVal

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
    return celcius


assert(int(alert_in_celcius(400.5))==int(204.72))
assert(alert_failure_count == 1)
assert(int(alert_in_celcius(303.6))==int(150.8))
assert(alert_failure_count == 1)
assert((alert_in_celcius(32))==0)
assert(alert_failure_count == 1)
print(f'{alert_failure_count} alerts failed.')
print('All is well')
