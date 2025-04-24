import requests


def send_msg(msg):
    print("send_msg() is deleted on purpose")
    return resp    
if __name__ == "__main__":
    resp = send_msg("test")
    print(resp.content.decode())