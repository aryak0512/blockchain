import hashlib
import json

def crypto_hash(*args):
    """
    Take varargs and individually stringifies them using json dumps and concatanates them into a single string
    Sorted is used since sequence change should always produce same hash value
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = "".join(stringified_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def crypto_hash2(data):
    # converts data structure passed into a string as encode needs only string
    stringified_data = json.dumps(data)
    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

def main():
    print(crypto_hash('one', 2, [3]))
    print(crypto_hash( 2, [3],'one'))

if __name__ == '__main__':
    main()