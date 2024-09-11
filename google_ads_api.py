import google.ads.google_ads.client

def initialize_ads_client(config_file):
    client = google.ads.google_ads.client.GoogleAdsClient.load_from_storage(config_file)
    return client
