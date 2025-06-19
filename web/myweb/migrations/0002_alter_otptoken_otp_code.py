from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myweb", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otptoken",
            name="otp_code",
            field=models.CharField(default="2e116e", max_length=6),
        ),
    ]
