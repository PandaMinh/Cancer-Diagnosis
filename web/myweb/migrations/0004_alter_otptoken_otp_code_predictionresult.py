import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myweb", "0003_alter_otptoken_otp_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otptoken",
            name="otp_code",
            field=models.CharField(default="763120", max_length=6),
        ),
        migrations.CreateModel(
            name="PredictionResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prediction_method", models.CharField(max_length=10)),
                ("result", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
