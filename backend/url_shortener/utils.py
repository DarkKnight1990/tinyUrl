import calendar
import time

MACHINE_ID = "1"
DATACENTER_ID = "1"
BASE_57 = "123456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"


def get_machine_id() -> int:
    return MACHINE_ID


def get_datacenter_id() -> int:
    return DATACENTER_ID


def get_unique_id() -> int:
    """
    A unique ID generator, that returns unique ID if the fowllowing format

    unique_id = sign_value + timestamp + machineID + DataCenterID + sequence(12bit)

    return: int(unique_id)
    """
    sign_value = "0"
    timestamp = str(calendar.timegm(time.gmtime()))
    machine_id = get_machine_id()
    datacenter_id = get_datacenter_id()
    sequence = "0000"

    unique_id = sign_value + timestamp + machine_id + datacenter_id + sequence

    return int(unique_id)


def encode_base62(num, alphabet=BASE_57) -> str:
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return "".join(arr)


def decode_base62(string, alphabet=BASE_57):
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = strlen - (idx + 1)
        num += alphabet.index(char) * (base ** power)
        idx += 1
    return num
