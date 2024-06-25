import json
from core.models import BrokerScrappingData
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            queryset = BrokerScrappingData.objects.select_related(
                "broker_linkedin_profile"
            ).all()
            total_count = queryset.count()
            # Determine the size of each chunk
            chunk_size = total_count // 4

            # Divide the queryset into four parts
            chunks = [queryset[i * chunk_size : (i + 1) * chunk_size] for i in range(4)]

            # Handle the remainder if total_count is not perfectly divisible by 4
            if total_count % 4 != 0:
                chunks[-1] |= queryset[4 * chunk_size :]

            # Iterate over the chunks and serialize each to JSON
            for idx, chunk in enumerate(chunks):
                data = []
                for obj in chunk:
                    obj_dict = {
                        "crd": obj.broker_linkedin_profile.broker.crd,
                        "brokerData": {
                            "id": obj.broker_linkedin_profile.broker.id,
                            "npm": obj.broker_linkedin_profile.broker.npm,
                            "firstName": obj.broker_linkedin_profile.broker.firstName,
                            "middleName": obj.broker_linkedin_profile.broker.middleName,
                            "lastName": obj.broker_linkedin_profile.broker.lastName,
                            "otherNames": obj.broker_linkedin_profile.broker.otherNames,
                            "team": obj.broker_linkedin_profile.broker.team,
                            "brokerDealer": obj.broker_linkedin_profile.broker.brokerDealer,
                            "brokerDealerCRD": obj.broker_linkedin_profile.broker.brokerDealerCRD,
                            "yearsWithCurrentBD": obj.broker_linkedin_profile.broker.yearsWithCurrentBD,
                            "currentBDStartDate": str(
                                obj.broker_linkedin_profile.broker.currentBDStartDate
                            ),
                            "ria": obj.broker_linkedin_profile.broker.ria,
                            "riaCRD": obj.broker_linkedin_profile.broker.riaCRD,
                            "yearsWithCurrentRIA": obj.broker_linkedin_profile.broker.yearsWithCurrentRIA,
                            "currentRIAStateDate": str(
                                obj.broker_linkedin_profile.broker.currentRIAStateDate
                            ),
                            "address": obj.broker_linkedin_profile.broker.address,
                            "city": obj.broker_linkedin_profile.broker.city,
                            "state": obj.broker_linkedin_profile.broker.state,
                            "zip": obj.broker_linkedin_profile.broker.zip,
                            "metroArea": obj.broker_linkedin_profile.broker.metroArea,
                            "licensesAndExams": obj.broker_linkedin_profile.broker.licensesAndExams,
                            "title": obj.broker_linkedin_profile.broker.title,
                            "designations": obj.broker_linkedin_profile.broker.designations,
                            "phone": obj.broker_linkedin_profile.broker.phone,
                            "phone_type": obj.broker_linkedin_profile.broker.phone_type,
                            "linkedIn": obj.broker_linkedin_profile.broker.linkedIn,
                            "email1": obj.broker_linkedin_profile.broker.email1,
                            "email2": obj.broker_linkedin_profile.broker.email2,
                            "email3": obj.broker_linkedin_profile.broker.email3,
                            "personalEmail": obj.broker_linkedin_profile.broker.personalEmail,
                            "bio": obj.broker_linkedin_profile.broker.bio,
                            "yearsOfExperience": obj.broker_linkedin_profile.broker.yearsOfExperience,
                            "estAge": obj.broker_linkedin_profile.broker.estAge,
                            "previousBrokerDealer": obj.broker_linkedin_profile.broker.previousBrokerDealer,
                            "previousRIA": obj.broker_linkedin_profile.broker.previousRIA,
                            "gender": obj.broker_linkedin_profile.broker.gender,
                            "teamId": obj.broker_linkedin_profile.broker.teamId,
                            "personTagRole": obj.broker_linkedin_profile.broker.personTagRole,
                            "personTagFamily": obj.broker_linkedin_profile.broker.personTagFamily,
                            "personTagHobbies": obj.broker_linkedin_profile.broker.personTagHobbies,
                            "personTagExpertise": obj.broker_linkedin_profile.broker.personTagExpertise,
                            "personTagServices": obj.broker_linkedin_profile.broker.personTagServices,
                            "personTagInvestments": obj.broker_linkedin_profile.broker.personTagInvestments,
                            "personTagSportsTeams": obj.broker_linkedin_profile.broker.personTagSportsTeams,
                            "personTagSchool": obj.broker_linkedin_profile.broker.personTagSchool,
                            "personTagGreekLife": obj.broker_linkedin_profile.broker.personTagGreekLife,
                            "personTagMilitaryStatus": obj.broker_linkedin_profile.broker.personTagMilitaryStatus,
                            "personTagFaithBasedInvesting": obj.broker_linkedin_profile.broker.personTagFaithBasedInvesting,
                            "firmTagPlatform": obj.broker_linkedin_profile.broker.firmTagPlatform,
                            "firmTagTechnology": obj.broker_linkedin_profile.broker.firmTagTechnology,
                            "firmTagServices": obj.broker_linkedin_profile.broker.firmTagServices,
                            "firmTagInvestments": obj.broker_linkedin_profile.broker.firmTagInvestments,
                            "firmTagCustodian": obj.broker_linkedin_profile.broker.firmTagCustodian,
                            "firmTagClients": obj.broker_linkedin_profile.broker.firmTagClients,
                            "firmTagCRM": obj.broker_linkedin_profile.broker.firmTagCRM,
                            "notes": obj.broker_linkedin_profile.broker.notes,
                            "profile": obj.broker_linkedin_profile.broker.profile,
                            "secLink": obj.broker_linkedin_profile.broker.secLink,
                            "finraLink": obj.broker_linkedin_profile.broker.finraLink,
                            "firmCompanyName": obj.broker_linkedin_profile.broker.firmCompanyName,
                            "firmType": obj.broker_linkedin_profile.broker.firmType,
                            "firmAddress": obj.broker_linkedin_profile.broker.firmAddress,
                            "firmCity": obj.broker_linkedin_profile.broker.firmCity,
                            "firmState": obj.broker_linkedin_profile.broker.firmState,
                            "firmZip": obj.broker_linkedin_profile.broker.firmZip,
                            "firmPhone": obj.broker_linkedin_profile.broker.firmPhone,
                            "firmAUM": obj.broker_linkedin_profile.broker.firmAUM,
                            "firmTotalAccounts": obj.broker_linkedin_profile.broker.firmTotalAccounts,
                            "firmCustodians": obj.broker_linkedin_profile.broker.firmCustodians,
                            "firmTotalEmployees": obj.broker_linkedin_profile.broker.firmTotalEmployees,
                            "firmRIAReps": obj.broker_linkedin_profile.broker.firmRIAReps,
                            "firmBDReps": obj.broker_linkedin_profile.broker.firmBDReps,
                            "firmForm13f": obj.broker_linkedin_profile.broker.firmForm13f,
                            "lines": obj.broker_linkedin_profile.broker.lines,
                            "carrier": obj.broker_linkedin_profile.broker.carrier,
                            "company": obj.broker_linkedin_profile.broker.company,
                            "initialAppointmentDate": str(
                                obj.broker_linkedin_profile.broker.initialAppointmentDate
                            ),
                            "captive": obj.broker_linkedin_profile.broker.captive,
                            "numOfCarriers": obj.broker_linkedin_profile.broker.numOfCarriers,
                            "numOfLines": obj.broker_linkedin_profile.broker.numOfLines,
                            "nonProducing": obj.broker_linkedin_profile.broker.nonProducing,
                            "insuranceYearsOfExperience": obj.broker_linkedin_profile.broker.insuranceYearsOfExperience,
                        },
                        "linkedInData": {
                            "urn": obj.broker_linkedin_profile.urn,
                            "username": obj.broker_linkedin_profile.username,
                            "firstName": obj.broker_linkedin_profile.firstName,
                            "lastName": obj.broker_linkedin_profile.lastName,
                            "isOpenToWork": obj.broker_linkedin_profile.isOpenToWork,
                            "isHiring": obj.broker_linkedin_profile.isHiring,
                            "profilePicture": obj.broker_linkedin_profile.profilePicture,
                            "summary": obj.broker_linkedin_profile.summary,
                            "headline": obj.broker_linkedin_profile.headline,
                            "geo": obj.broker_linkedin_profile.geo,
                            "languages": obj.broker_linkedin_profile.languages,
                            "educations": obj.broker_linkedin_profile.educations,
                            "position": obj.broker_linkedin_profile.position,
                            "fullPositions": obj.broker_linkedin_profile.fullPositions,
                            "skills": obj.broker_linkedin_profile.skills,
                            "givenRecommendation": obj.broker_linkedin_profile.givenRecommendation,
                            "givenRecommendationCount": obj.broker_linkedin_profile.givenRecommendationCount,
                            "receivedRecommendation": obj.broker_linkedin_profile.receivedRecommendation,
                            "receivedRecommendationCount": obj.broker_linkedin_profile.receivedRecommendationCount,
                            "courses": obj.broker_linkedin_profile.courses,
                            "certifications": obj.broker_linkedin_profile.certifications,
                            "honors": obj.broker_linkedin_profile.honors,
                            "projects": obj.broker_linkedin_profile.projects,
                            "volunteering": obj.broker_linkedin_profile.volunteering,
                            "supportedLocales": obj.broker_linkedin_profile.supportedLocales,
                            "multiLocaleFirstName": obj.broker_linkedin_profile.multiLocaleFirstName,
                            "multiLocaleLastName": obj.broker_linkedin_profile.multiLocaleLastName,
                            "multiLocaleHeadline": obj.broker_linkedin_profile.multiLocaleHeadline,
                        },
                        "scrappedData": json.loads(obj.content),
                    }
                    data.append(obj_dict)

                # Define the file path for each JSON file
                file_path = f"data_{idx + 1}.json"

                # Write JSON data to file
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

            self.stdout.write(self.style.SUCCESS("Successfully created 4 JSON files"))
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error: {e.__traceback__.tb_lineno}, {e}")
            )
