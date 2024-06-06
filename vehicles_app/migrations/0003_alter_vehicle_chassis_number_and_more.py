# Generated by Django 5.0.6 on 2024-06-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles_app", "0002_vehicle_insurance_payment_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="chassis_number",
            field=models.CharField(
                blank=True, max_length=50, null=True, unique=True, verbose_name="차대번호"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="depreciation_cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="감가상각(월)",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="depreciation_year",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="감가기준년도",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="driver",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="담당기사"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="engine_type",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="원동기형식"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="hot_water_heater",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="온수기 유무"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="inspection_date",
            field=models.DateField(blank=True, null=True, verbose_name="정기점검일"),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="installment_cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="할부",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="insurance_cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="보험비",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="insurance_payment_date",
            field=models.DateField(blank=True, null=True, verbose_name="보험납부일"),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="karaoke",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="노래방 유무"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="led_display",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="전광판 유무"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="license_number_0",
            field=models.CharField(
                blank=True, max_length=5, null=True, unique=True, verbose_name="차량 앞번호"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="license_number_1",
            field=models.CharField(
                blank=True, max_length=5, null=True, unique=True, verbose_name="차량 뒷번호"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="maintenance_cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="정비(월)",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="manufacturer",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="제조사"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="model_year",
            field=models.CharField(
                blank=True, max_length=4, null=True, verbose_name="모델연도"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="notes",
            field=models.TextField(blank=True, null=True, verbose_name="비고"),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="passenger_capacity",
            field=models.IntegerField(blank=True, null=True, verbose_name="승차인원"),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="plate_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="번호판가격",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="refrigerator",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="냉장고 유무"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="release_date",
            field=models.DateField(blank=True, null=True, verbose_name="출고일자(연도)"),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="tuning_cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="튜닝(일)",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="tv",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="TV"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="usage_status",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="사용 여부"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="usb",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="USB"
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="vehicle_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="차량가격",
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="vehicle_type",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="차량종류"
            ),
        ),
    ]
