import requests


def send_msg(msg):
    headers = {"Authorization": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjY2NjU0NSwidXVpZCI6ImY0YWU4YmRmZDg4NTlkYzQiLCJpc19hZG1pbiI6ZmFsc2UsImJhY2tzdGFnZV9yb2xlIjoiIiwiaXNfc3VwZXJfYWRtaW4iOmZhbHNlLCJzdWJfbmFtZSI6IiIsInRlbmFudCI6ImF1dG9kbCIsInVwayI6IiJ9.aj4iM794XW5RZe4h2xTXuv2d8vb-_WvFPhhxL5nFkLNHGbN600FsMi2u6XG2iNqjhHPzGPb09S65apiY9GBkSg"}
    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/send",
                     json={
                         "title": "From Instance",
                         "name": "MT train",
                         "content": "{}".format(msg),
                     }, headers = headers)
    return resp    
if __name__ == "__main__":
    resp = send_msg("test")
    print(resp.content.decode())