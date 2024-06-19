import requests
from django.core.management.base import BaseCommand
from core.models import Brokers, BrokersLinkedInProfileData


class Command(BaseCommand):
    help = "Fetch LinkedIn profile data for brokers and save to database"

    def handle(self, *args, **kwargs):
        # Fetch all brokers
        brokers = Brokers.objects.all()
        BrokersLinkedInProfileData.objects.all().delete()

        # List to store profile data instances
        profile_data_list = []

        for broker in brokers:
            if broker.linkedIn:
                linkedin_url = broker.linkedIn
            else:
                linkedin_url = f"https://www.linkedin.com/in/{broker.first_name.lower()}{broker.last_name.lower()}"

            # Fetch the data from the API
            url = "https://linkedin-data-api.p.rapidapi.com/get-profile-data-by-url"
            querystring = {"url": linkedin_url}

            headers = {
                "x-rapidapi-key": "2434c2db2cmsh8806e8f7d25ff91p11364djsn187b68b0660c",
                "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
            }

            response = requests.get(url, headers=headers, params=querystring)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()

                # Prepare the profile data instance
                profile_data = BrokersLinkedInProfileData(
                    broker=broker,
                    urn=data.get("urn"),
                    username=data.get("username"),
                    firstName=data.get("firstName"),
                    lastName=data.get("lastName"),
                    isOpenToWork=data.get("isOpenToWork"),
                    isHiring=data.get("isHiring"),
                    profilePicture=data.get("profilePicture"),
                    summary=data.get("summary"),
                    headline=data.get("headline"),
                    geo=data.get("geo"),
                    languages=data.get("languages"),
                    educations=data.get("educations"),
                    position=data.get("position"),
                    fullPositions=data.get("fullPositions"),
                    skills=data.get("skills"),
                    givenRecommendation=data.get("givenRecommendation"),
                    givenRecommendationCount=data.get("givenRecommendationCount"),
                    receivedRecommendation=data.get("receivedRecommendation"),
                    receivedRecommendationCount=data.get("receivedRecommendationCount"),
                    courses=data.get("courses"),
                    certifications=data.get("certifications"),
                    honors=data.get("honors"),
                    projects=data.get("projects"),
                    volunteering=data.get("volunteering"),
                    supportedLocales=data.get("supportedLocales"),
                    multiLocaleFirstName=data.get("multiLocaleFirstName"),
                    multiLocaleLastName=data.get("multiLocaleLastName"),
                    multiLocaleHeadline=data.get("multiLocaleHeadline"),
                )

                # Append to the list
                profile_data_list.append(profile_data)
                print(
                    f"Data fetched for {broker.crd} - {broker.firstName} {broker.middleName} {broker.lastName}"
                )
            else:
                print(response.json())
                print(
                    f"Failed to fetch data for broker {broker.crd}: {response.status_code}"
                )

        # Bulk create the list of profile data instances
        BrokersLinkedInProfileData.objects.bulk_create(profile_data_list)
        print(f"Successfully saved {len(profile_data_list)} LinkedIn profiles.")
