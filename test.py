import time
import psutil


# 'psutil.net_io_counters()' returns values since last system restart.
last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

print(last_received)
print(last_sent)
print(last_total)

CURRENT_TOTAL = 0
CURRENT_RECV = 0
CURRENT_SENT = 0

while True:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    # Bytes --> KB --> MB
    new_received_in_mb = new_received / 1024 / 1024
    new_sent_in_mb = new_sent / 1024 / 1024
    new_total_in_mb = new_total / 1024 / 1024

    # print(
    #     f"{new_received_in_mb:.2f} MB received, {new_sent_in_mb:.2f} MB sent, {new_total_in_mb:.2f} MB total"
    # )

    CURRENT_TOTAL += new_total_in_mb
    CURRENT_RECV += new_received_in_mb
    CURRENT_SENT += new_sent_in_mb

    print(
        f"{CURRENT_TOTAL:.2f} MB Total, {CURRENT_RECV:.2f} MB Recev, {CURRENT_SENT:.2f} MB Sent"
    )

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(1)
