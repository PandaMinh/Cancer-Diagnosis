from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myweb", "0002_alter_otptoken_otp_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otptoken",
            name="otp_code",
            field=models.CharField(default="68b242", max_length=6),
        ),
    ]
