import yaml
from google_ads_api import initialize_ads_client
from data_pipeline import get_campaign_data

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = load_config("config/google_ads.yaml")
    
    client = initialize_ads_client("config/google_ads.yaml")
    customer_id = config["login_customer_id"]
    
    campaign_data = get_campaign_data(client, customer_id)
    
    # Save to CSV or process further
    print(campaign_data)

