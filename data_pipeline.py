from google_ads_api import initialize_ads_client

def get_campaign_data(client, customer_id):
    ga_service = client.get_service("GoogleAdsService")
    query = """
        SELECT campaign.id, campaign.name, campaign.status
        FROM campaign
        WHERE campaign.status = 'ENABLED'
        """
    response = ga_service.search_stream(customer_id=customer_id, query=query)
    
    campaign_data = []
    for batch in response:
        for row in batch.results:
            campaign_data.append({
                "id": row.campaign.id,
                "name": row.campaign.name,
                "status": row.campaign.status.name
            })
    
    return campaign_data
