from urllib.parse import urlparse
import random,string,time
from typing import List, Union

class HumanBytes:
    METRIC_LABELS: List[str] = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB","RB","QB"]
    BINARY_LABELS: List[str] = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
    PRECISION_OFFSETS: List[float] = [0.5, 0.05, 0.005, 0.0005, 0.00005]
    PRECISION_FORMATS: List[str] = ["{}{:.0f} {}", "{}{:.1f} {}", "{}{:.2f} {}", "{}{:.3f} {}", "{}{:.4f} {}", "{}{:.5f} {}"]
    @staticmethod
    def format(num: Union[int, float], metric: bool=False, precision: int=1) -> str:
        assert isinstance(num, (int, float))
        assert isinstance(metric, bool)
        assert isinstance(precision, int) and precision >= 0 and precision <= 3
        unit_labels = HumanBytes.METRIC_LABELS if metric else HumanBytes.BINARY_LABELS
        last_label = unit_labels[-1]
        unit_step = 1000 if metric else 1024
        unit_step_thresh = unit_step - HumanBytes.PRECISION_OFFSETS[precision]
        is_negative = num < 0
        if is_negative:
            num = abs(num)
        for unit in unit_labels:
            if num < unit_step_thresh:
                break
            if unit != last_label:
                num /= unit_step
        return HumanBytes.PRECISION_FORMATS[precision].format("-" if is_negative else "", num, unit)

def gen_ips():
    return f'{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}'

def get_target(url2):
    url = url2.rstrip()
    target = {}
    parsed_url = urlparse(url)
    target['uri'] = parsed_url.path or '/'
    target['host'] = parsed_url.netloc
    target['scheme'] = parsed_url.scheme
    target['port'] = parsed_url.port or ("443" if target['scheme'] == "https" else "80")
    target['normal'] = url2
    return target

def gen_ips():
    return f'{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}'

def gen_id():
    letter = 'abcdefghijklmnopqrstuvwxyz0123456789'
    id_8 = ''
    for _ in range(8):
     id_8 += random.choice((letter))
    id_4v1 = ''
    for _ in range(4):
     id_4v1 += random.choice((letter))
    id_4v2 = ''
    for _ in range(4):
     id_4v2 += random.choice((letter))
    id_4v3 = ''
    for _ in range(4):
     id_4v3 += random.choice((letter))
    id_12 = ''
    for _ in range(12):
     id_12 += random.choice((letter))
    return f'{id_8}-{id_4v1}-{id_4v2}-{id_4v3}-{id_12}'

def generate_url_path(num):
    data = "".join(random.sample(string.printable, int(num)))
    return data