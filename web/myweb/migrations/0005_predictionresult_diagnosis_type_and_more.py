from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myweb", "0004_alter_otptoken_otp_code_predictionresult"),
    ]

    operations = [
        migrations.AddField(
            model_name="predictionresult",
            name="diagnosis_type",
            field=models.CharField(default="Unknown", max_length=255),
        ),
        migrations.AlterField(
            model_name="otptoken",
            name="otp_code",
            field=models.CharField(default="b9fe12", max_length=6),
        ),
    ]
