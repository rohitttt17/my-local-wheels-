# Generated by Django 5.1.6 on 2025-04-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Puducherry')], max_length=100),
        ),
    ]
