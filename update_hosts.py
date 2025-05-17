import requests

# URLs of upstream hosts files to merge
UPSTREAM_URLS = [
    "https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt"
]

# Your custom hosts entries (to always include)
CUSTOM_HOSTS = [
    "127.0.0.1 ads.facebook.com",
    "127.0.0.1 ads.ak.facebook.com",
    "127.0.0.1 ad.doubleclick.net",
    "127.0.0.1 connect.facebook.net",
    "127.0.0.1 graph.facebook.com",
    "127.0.0.1 creative.ak.fbcdn.net",
    "127.0.0.1 external.ak.fbcdn.net",
    "127.0.0.1 pixel.facebook.com",
    "127.0.0.1 edge-mqtt.facebook.com",
    "127.0.0.1 edge-chat.facebook.com",
    "127.0.0.1 scontent.xx.fbcdn.net",
    "127.0.0.1 static.xx.fbcdn.net",
    "127.0.0.1 star.c10r.facebook.com",
    "127.0.0.1 video.c10r.facebook.com",
    "127.0.0.1 z-m-scontent.xx.fbcdn.net",
    "127.0.0.1 secure.facebook.com",
    "127.0.0.1 instagramads.com",
    "127.0.0.1 ads.instagram.com",
    "127.0.0.1 i.instagram.com",
    "127.0.0.1 b.instagram.com",
    "127.0.0.1 cdninstagram.com",
    "127.0.0.1 scontent.cdninstagram.com",
]

def fetch_hosts(url):
    resp = requests.get(url)
    resp.raise_for_status()
    lines = resp.text.splitlines()
    # Filter out comments and empty lines
    hosts = [line.strip() for line in lines if line.strip() and not line.startswith("#")]
    return hosts

def main():
    all_hosts = set()
    for url in UPSTREAM_URLS:
        hosts = fetch_hosts(url)
        all_hosts.update(hosts)
    all_hosts.update(CUSTOM_HOSTS)
    # Sort for neatness
    all_hosts = sorted(all_hosts)
    with open("hosts.txt", "w") as f:
        f.write("\n".join(all_hosts))
    print("hosts.txt updated with merged hosts.")

if __name__ == "__main__":
    main()
