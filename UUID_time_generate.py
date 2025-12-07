import uuid
import datetime

#ID construction process
def uuid_v1_rebuild(dt, clock_seq, node):
    # UUID epoch
    uuid_epoch = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)
    dt = dt.astimezone(datetime.timezone.utc)

    # Convert to 100ns intervals
    intervals = int((dt - uuid_epoch).total_seconds() * 10_000_000)

    # timestamp parts
    time_low = intervals & 0xFFFFFFFF
    time_mid = (intervals >> 32) & 0xFFFF
    time_hi_version = ((intervals >> 48) & 0x0FFF) | (1 << 12)

    # clock sequence
    clock_seq &= 0x3FFF
    cs_low = clock_seq & 0xFF
    cs_hi = (clock_seq >> 8) | 0x80  # RFC 4122 variant

    return uuid.UUID(fields=(
        time_low,
        time_mid,
        time_hi_version,
        cs_hi,
        cs_low,
        node
    ))


clock_seq = 11417
node = 0x026ccdf7d769

#Create possible values between given times
start_hour = 0
start_minute = 0
while True:
	start_minute += 1

	if start_minute == 60:
		start_minute = 0
		start_hour += 1

	if start_hour == 24:
		break

	dt = datetime.datetime(2025, 11, 21, start_hour, start_minute, 0) #YYYY-MM-dd-hh-mn-ss
	u = uuid_v1_rebuild(dt, clock_seq, node)
	print(u)
