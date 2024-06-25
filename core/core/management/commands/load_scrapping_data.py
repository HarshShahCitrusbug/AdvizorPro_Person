import requests
from core.models import BrokersLinkedInProfileData, BrokerScrappingData
from django.core.management.base import BaseCommand


def scrap_broker_data_using_crd(crd: str):
    url = "https://api.brokercheck.finra.org/search/individual/1200160"

    # Fetch the data from the API
    response = requests.get(url)

    # Ensure the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            linkedIn_brokers_list = list(
                BrokersLinkedInProfileData.objects.select_related("broker").all()
            )

            for linkedIn_broker in linkedIn_brokers_list:
                response = scrap_broker_data_using_crd(linkedIn_broker.broker.crd)

                broker_scrapping_data = BrokerScrappingData(
                    broker=linkedIn_broker.broker,
                    content=response.get("hits", {})
                    .get("hits", [])[0]
                    .get("_source", {})
                    .get("content", {}),
                )
                broker_scrapping_data.save()

            self.stdout.write(self.style.SUCCESS("Successfully data populated"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
