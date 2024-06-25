import json
from core.models import BrokersLinkedInProfileData
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            queryset = BrokersLinkedInProfileData.objects.select_related("broker").all()
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
                        "id": obj.id,
                        "broker": {
                            "id": obj.broker.id,
                            "crd": obj.broker.crd,
                            "npm": obj.broker.npm,
                            "firstName": obj.broker.firstName,
                            "middleName": obj.broker.middleName,
                            "lastName": obj.broker.lastName,
                            "otherNames": obj.broker.otherNames,
                            "team": obj.broker.team,
                            "brokerDealer": obj.broker.brokerDealer,
                            "brokerDealerCRD": obj.broker.brokerDealerCRD,
                            "yearsWithCurrentBD": obj.broker.yearsWithCurrentBD,
                            "currentBDStartDate": str(obj.broker.currentBDStartDate),
                            "ria": obj.broker.ria,
                            "riaCRD": obj.broker.riaCRD,
                            "yearsWithCurrentRIA": obj.broker.yearsWithCurrentRIA,
                            "currentRIAStateDate": str(obj.broker.currentRIAStateDate),
                            "address": obj.broker.address,
                            "city": obj.broker.city,
                            "state": obj.broker.state,
                            "zip": obj.broker.zip,
                            "metroArea": obj.broker.metroArea,
                            "licensesAndExams": obj.broker.licensesAndExams,
                            "title": obj.broker.title,
                            "designations": obj.broker.designations,
                            "phone": obj.broker.phone,
                            "phone_type": obj.broker.phone_type,
                            "linkedIn": obj.broker.linkedIn,
                            "email1": obj.broker.email1,
                            "email2": obj.broker.email2,
                            "email3": obj.broker.email3,
                            "personalEmail": obj.broker.personalEmail,
                            "bio": obj.broker.bio,
                            "yearsOfExperience": obj.broker.yearsOfExperience,
                            "estAge": obj.broker.estAge,
                            "previousBrokerDealer": obj.broker.previousBrokerDealer,
                            "previousRIA": obj.broker.previousRIA,
                            "gender": obj.broker.gender,
                            "teamId": obj.broker.teamId,
                            "personTagRole": obj.broker.personTagRole,
                            "personTagFamily": obj.broker.personTagFamily,
                            "personTagHobbies": obj.broker.personTagHobbies,
                            "personTagExpertise": obj.broker.personTagExpertise,
                            "personTagServices": obj.broker.personTagServices,
                            "personTagInvestments": obj.broker.personTagInvestments,
                            "personTagSportsTeams": obj.broker.personTagSportsTeams,
                            "personTagSchool": obj.broker.personTagSchool,
                            "personTagGreekLife": obj.broker.personTagGreekLife,
                            "personTagMilitaryStatus": obj.broker.personTagMilitaryStatus,
                            "personTagFaithBasedInvesting": obj.broker.personTagFaithBasedInvesting,
                            "firmTagPlatform": obj.broker.firmTagPlatform,
                            "firmTagTechnology": obj.broker.firmTagTechnology,
                            "firmTagServices": obj.broker.firmTagServices,
                            "firmTagInvestments": obj.broker.firmTagInvestments,
                            "firmTagCustodian": obj.broker.firmTagCustodian,
                            "firmTagClients": obj.broker.firmTagClients,
                            "firmTagCRM": obj.broker.firmTagCRM,
                            "notes": obj.broker.notes,
                            "profile": obj.broker.profile,
                            "secLink": obj.broker.secLink,
                            "finraLink": obj.broker.finraLink,
                            "firmCompanyName": obj.broker.firmCompanyName,
                            "firmType": obj.broker.firmType,
                            "firmAddress": obj.broker.firmAddress,
                            "firmCity": obj.broker.firmCity,
                            "firmState": obj.broker.firmState,
                            "firmZip": obj.broker.firmZip,
                            "firmPhone": obj.broker.firmPhone,
                            "firmAUM": obj.broker.firmAUM,
                            "firmTotalAccounts": obj.broker.firmTotalAccounts,
                            "firmCustodians": obj.broker.firmCustodians,
                            "firmTotalEmployees": obj.broker.firmTotalEmployees,
                            "firmRIAReps": obj.broker.firmRIAReps,
                            "firmBDReps": obj.broker.firmBDReps,
                            "firmForm13f": obj.broker.firmForm13f,
                            "lines": obj.broker.lines,
                            "carrier": obj.broker.carrier,
                            "company": obj.broker.company,
                            "initialAppointmentDate": str(
                                obj.broker.initialAppointmentDate
                            ),
                            "captive": obj.broker.captive,
                            "numOfCarriers": obj.broker.numOfCarriers,
                            "numOfLines": obj.broker.numOfLines,
                            "nonProducing": obj.broker.nonProducing,
                            "insuranceYearsOfExperience": obj.broker.insuranceYearsOfExperience,
                        },
                        "urn": obj.urn,
                        "username": obj.username,
                        "firstName": obj.firstName,
                        "lastName": obj.lastName,
                        "isOpenToWork": obj.isOpenToWork,
                        "isHiring": obj.isHiring,
                        "profilePicture": obj.profilePicture,
                        "summary": obj.summary,
                        "headline": obj.headline,
                        "geo": obj.geo,
                        "languages": obj.languages,
                        "educations": obj.educations,
                        "position": obj.position,
                        "fullPositions": obj.fullPositions,
                        "skills": obj.skills,
                        "givenRecommendation": obj.givenRecommendation,
                        "givenRecommendationCount": obj.givenRecommendationCount,
                        "receivedRecommendation": obj.receivedRecommendation,
                        "receivedRecommendationCount": obj.receivedRecommendationCount,
                        "courses": obj.courses,
                        "certifications": obj.certifications,
                        "honors": obj.honors,
                        "projects": obj.projects,
                        "volunteering": obj.volunteering,
                        "supportedLocales": obj.supportedLocales,
                        "multiLocaleFirstName": obj.multiLocaleFirstName,
                        "multiLocaleLastName": obj.multiLocaleLastName,
                        "multiLocaleHeadline": obj.multiLocaleHeadline,
                    }
                    data.append(obj_dict)

                # Define the file path for each JSON file
                file_path = f"linkedin_data_{idx + 1}.json"

                # Write JSON data to file
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

            self.stdout.write(self.style.SUCCESS("Successfully created 4 JSON files"))
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error: {e.__traceback__.tb_lineno}, {e}")
            )
