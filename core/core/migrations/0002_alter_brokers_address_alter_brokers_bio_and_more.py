# Generated by Django 5.0.6 on 2024-06-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brokers",
            name="address",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="bio",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="brokerDealer",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="brokerDealerCRD",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="captive",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="carrier",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="city",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="company",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="crd",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="designations",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="email1",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="email2",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="email3",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="estAge",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="finraLink",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmAUM",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmAddress",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmBDReps",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmCity",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmCompanyName",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmCustodians",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmForm13f",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmPhone",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmRIAReps",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmState",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagCRM",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagClients",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagCustodian",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagInvestments",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagPlatform",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagServices",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTagTechnology",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTotalAccounts",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmTotalEmployees",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmType",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firmZip",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="firstName",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="gender",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="initialAppointmentDate",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="insuranceYearsOfExperience",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="lastName",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="licensesAndExams",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="lines",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="linkedIn",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="metroArea",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="middleName",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="nonProducing",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="notes",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="npm",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="numOfCarriers",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="numOfLines",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="otherNames",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagExpertise",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagFaithBasedInvesting",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagFamily",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagGreekLife",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagHobbies",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagInvestments",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagMilitaryStatus",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagRole",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagSchool",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagServices",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personTagSportsTeams",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="personalEmail",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="phone",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="phone_type",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="previousBrokerDealer",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="previousRIA",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="profile",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="ria",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="riaCRD",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="secLink",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="state",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="team",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="teamId",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="title",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="yearsOfExperience",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="yearsWithCurrentBD",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="yearsWithCurrentRIA",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokers",
            name="zip",
            field=models.CharField(max_length=555),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="certifications",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="courses",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="firstName",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="givenRecommendation",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="givenRecommendationCount",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="headline",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="languages",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="lastName",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="receivedRecommendation",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="receivedRecommendationCount",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="summary",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="urn",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="username",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name="brokerslinkedinprofiledata",
            name="volunteering",
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
    ]