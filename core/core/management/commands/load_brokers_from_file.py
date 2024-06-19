import datetime
import pandas as pd
from core.models import Brokers
from django.utils import timezone
from django.core.management.base import BaseCommand


# Helper function to convert dates to timezone-aware
def make_aware(date):
    if pd.isna(date):
        return None
    return timezone.make_aware(date)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            df = pd.read_excel(
                "core/management/commands/AdvizorPro_Person_04.24.2024-1.xlsx"
            )
            Brokers.objects.all().delete()

            df.fillna(
                {
                    "NPN": "N/A",
                    "First Name": "N/A",
                    "Middle Name": "N/A",
                    "Last Name": "N/A",
                    "Other Names": "N/A",
                    "Team": "N/A",
                    "Broker-Dealer": "N/A",
                    "Broker-Dealer CRD": "N/A",
                    "Years with Current BD": "N/A",
                    "Current BD Start Date": datetime.datetime.now(),
                    "RIA": "N/A",
                    "RIA CRD": "N/A",
                    "Years with Current RIA": "N/A",
                    "Current RIA State Date": datetime.datetime.now(),
                    "Address": "N/A",
                    "City": "N/A",
                    "State": "N/A",
                    "Zip": "N/A",
                    "Metro Area": "N/A",
                    "Licenses & Exams": "N/A",
                    "Title": "N/A",
                    "Designations": "N/A",
                    "Phone": "N/A",
                    "Phone - Type": "N/A",
                    "LinkedIn": "N/A",
                    "Email 1": "N/A",
                    "Email 2": "N/A",
                    "Email 3": "N/A",
                    "Personal Email": "N/A",
                    "Bio": "N/A",
                    "Years of Experience": "N/A",
                    "Est. Age": "N/A",
                    "Previous Broker Dealer": "N/A",
                    "Previous RIA": "N/A",
                    "Gender": "N/A",
                    "Team ID": "N/A",
                    "Person Tag - Role": "N/A",
                    "Person Tag - Family": "N/A",
                    "Person Tag - Hobbies": "N/A",
                    "Person Tag - Expertise": "N/A",
                    "Person Tag - Services": "N/A",
                    "Person Tag - Investments": "N/A",
                    "Person Tag - Sports Teams": "N/A",
                    "Person Tag - School": "N/A",
                    "Person Tag - Greek Life": "N/A",
                    "Person Tag - Military Status": "N/A",
                    "Person Tag - Faith Based Investing": "N/A",
                    "Firm Tag - Platform": "N/A",
                    "Firm Tag - Technology": "N/A",
                    "Firm Tag - Services": "N/A",
                    "Firm Tag - Investments": "N/A",
                    "Firm Tag - Custodian": "N/A",
                    "Firm Tag - Clients": "N/A",
                    "Firm Tag - CRM": "N/A",
                    "Notes": "N/A",
                    "Profile": "N/A",
                    "SEC Link": "N/A",
                    "FINRA Link": "N/A",
                    "Firm Company Name": "N/A",
                    "Firm Type": "N/A",
                    "Firm Address": "N/A",
                    "Firm City": "N/A",
                    "Firm State": "N/A",
                    "Firm Zip": "N/A",
                    "Firm Phone": "N/A",
                    "Firm AUM": "N/A",
                    "Firm Total Accounts": "N/A",
                    "Firm Custodians": "N/A",
                    "Firm Total Employees": "N/A",
                    "Firm RIA Reps": "N/A",
                    "Firm BD Reps": "N/A",
                    "Firm Form 13F": "N/A",
                    "Lines": "N/A",
                    "Carrier": "N/A",
                    "Company": "N/A",
                    "Initial Appointment Date": "N/A",
                    "Captive": "N/A",
                    "Num of Carriers": "N/A",
                    "Num of Lines": "N/A",
                    "Non-Producing": "N/A",
                    "Insurance Years of Experience": "N/A",
                },
                inplace=True,
            )

            # Prepare a list of Brokers instances
            brokers = []

            for _, row in df.iterrows():
                broker = Brokers(
                    crd=row.get("CRD"),
                    npm=row.get("NPN"),
                    firstName=row.get("First Name"),
                    middleName=row.get("Middle Name"),
                    lastName=row.get("Last Name"),
                    otherNames=row.get("Other Names"),
                    team=row.get("Team"),
                    brokerDealer=row.get("Broker-Dealer"),
                    brokerDealerCRD=row.get("Broker-Dealer CRD"),
                    yearsWithCurrentBD=row.get("Years with Current BD"),
                    currentBDStartDate=make_aware(row.get("Current BD Start Date")),
                    ria=row.get("RIA"),
                    riaCRD=row.get("RIA CRD"),
                    yearsWithCurrentRIA=row.get("Years with Current RIA"),
                    currentRIAStateDate=make_aware(row.get("Current RIA State Date")),
                    address=row.get("Address"),
                    city=row.get("City"),
                    state=row.get("State"),
                    zip=row.get("Zip"),
                    metroArea=row.get("Metro Area"),
                    licensesAndExams=row.get("Licenses & Exams"),
                    title=row.get("Title"),
                    designations=row.get("Designations"),
                    phone=row.get("Phone"),
                    phone_type=row.get("Phone - Type"),
                    linkedIn=row.get("LinkedIn"),
                    email1=row.get("Email 1"),
                    email2=row.get("Email 2"),
                    email3=row.get("Email 3"),
                    personalEmail=row.get("Personal Email"),
                    bio=row.get("Bio"),
                    yearsOfExperience=row.get("Years of Experience"),
                    estAge=row.get("Est. Age"),
                    previousBrokerDealer=row.get("Previous Broker Dealer"),
                    previousRIA=row.get("Previous RIA"),
                    gender=row.get("Gender"),
                    teamId=row.get("Team ID"),
                    personTagRole=row.get("Person Tag - Role"),
                    personTagFamily=row.get("Person Tag - Family"),
                    personTagHobbies=row.get("Person Tag - Hobbies"),
                    personTagExpertise=row.get("Person Tag - Expertise"),
                    personTagServices=row.get("Person Tag - Services"),
                    personTagInvestments=row.get("Person Tag - Investments"),
                    personTagSportsTeams=row.get("Person Tag - Sports Teams"),
                    personTagSchool=row.get("Person Tag - School"),
                    personTagGreekLife=row.get("Person Tag - Greek Life"),
                    personTagMilitaryStatus=row.get("Person Tag - Military Status"),
                    personTagFaithBasedInvesting=row.get(
                        "Person Tag - Faith Based Investing"
                    ),
                    firmTagPlatform=row.get("Firm Tag - Platform"),
                    firmTagTechnology=row.get("Firm Tag - Technology"),
                    firmTagServices=row.get("Firm Tag - Services"),
                    firmTagInvestments=row.get("Firm Tag - Investments"),
                    firmTagCustodian=row.get("Firm Tag - Custodian"),
                    firmTagClients=row.get("Firm Tag - Clients"),
                    firmTagCRM=row.get("Firm Tag - CRM"),
                    notes=row.get("Notes"),
                    profile=row.get("Profile"),
                    secLink=row.get("SEC Link"),
                    finraLink=row.get("FINRA Link"),
                    firmCompanyName=row.get("Firm Company Name"),
                    firmType=row.get("Firm Type"),
                    firmAddress=row.get("Firm Address"),
                    firmCity=row.get("Firm City"),
                    firmState=row.get("Firm State"),
                    firmZip=row.get("Firm Zip"),
                    firmPhone=row.get("Firm Phone"),
                    firmAUM=row.get("Firm AUM"),
                    firmTotalAccounts=row.get("Firm Total Accounts"),
                    firmCustodians=row.get("Firm Custodians"),
                    firmTotalEmployees=row.get("Firm Total Employees"),
                    firmRIAReps=row.get("Firm RIA Reps"),
                    firmBDReps=row.get("Firm BD Reps"),
                    firmForm13f=row.get("Firm Form 13F"),
                    lines=row.get("Lines"),
                    carrier=row.get("Carrier"),
                    company=row.get("Company"),
                    initialAppointmentDate=row.get("Initial Appointment Date"),
                    captive=row.get("Captive"),
                    numOfCarriers=row.get("Num of Carriers"),
                    numOfLines=row.get("Num of Lines"),
                    nonProducing=row.get("Non-Producing"),
                    insuranceYearsOfExperience=row.get("Insurance Years of Experience"),
                )
                brokers.append(broker)

            # Bulk create Brokers instances
            Brokers.objects.bulk_create(brokers)

            self.stdout.write(self.style.SUCCESS("Successfully data populated"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
