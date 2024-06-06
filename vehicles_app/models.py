from django.db import models

class Vehicle(models.Model):
    license_number_0 = models.CharField(max_length=5, unique=True, verbose_name="차량 앞번호", blank=True, null=True)
    license_number_1 = models.CharField(max_length=5, unique=True, verbose_name="차량 뒷번호", blank=True, null=True)
    passenger_capacity = models.IntegerField(verbose_name="승차인원", blank=True, null=True)
    release_date = models.DateField(verbose_name="출고일자(연도)", blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, verbose_name="차량종류", blank=True, null=True)
    manufacturer = models.CharField(max_length=50, verbose_name="제조사", blank=True, null=True)
    model_year = models.CharField(max_length=4, verbose_name="모델연도", blank=True, null=True)
    chassis_number = models.CharField(max_length=50, unique=True, verbose_name="차대번호", blank=True, null=True)
    engine_type = models.CharField(max_length=50, verbose_name="원동기형식", blank=True, null=True)
    driver = models.CharField(max_length=50, verbose_name="담당기사", blank=True, null=True)
    inspection_date = models.DateField(verbose_name="정기점검일", blank=True, null=True)
    usage_status = models.BooleanField(default=False, verbose_name="사용 여부", blank=True, null=True)
    vehicle_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="차량가격", blank=True, null=True)
    plate_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="번호판가격", blank=True, null=True)
    insurance_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="보험비", blank=True, null=True)
    maintenance_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="정비(월)", blank=True, null=True)
    tuning_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="튜닝(일)", blank=True, null=True)
    depreciation_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="감가상각(월)", blank=True, null=True)
    depreciation_year = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="감가기준년도", blank=True, null=True)
    installment_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="할부", blank=True, null=True)
    led_display = models.BooleanField(default=False, verbose_name="전광판 유무", blank=True, null=True)
    karaoke = models.BooleanField(default=False, verbose_name="노래방 유무", blank=True, null=True)
    hot_water_heater = models.BooleanField(default=False, verbose_name="온수기 유무", blank=True, null=True)
    refrigerator = models.BooleanField(default=False, verbose_name="냉장고 유무", blank=True, null=True)
    usb = models.BooleanField(default=False, verbose_name="USB", blank=True, null=True)
    tv = models.BooleanField(default=False, verbose_name="TV", blank=True, null=True)
    notes = models.TextField(blank=True, verbose_name="비고", null=True)
    remaining_installment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="남은 할부액", blank=True, null=True)
    insurance_payment_date = models.DateField(verbose_name="보험납부일", blank=True, null=True)
    type = models.CharField(max_length=50, verbose_name="형식", blank=True, null=True)


    class Meta:
        unique_together = ['license_number_0', 'license_number_1']

    def __str__(self):
        return f"{self.license_number_0} {self.license_number_1} - {self.vehicle_type}"
    
    # detail information of craete vehicle form
    def detail_info(self):
        fields_filled = sum(1 for field in self._meta.fields if getattr(self, field.name))
        total_fields = len(self._meta.fields)
        return f"{fields_filled}/{total_fields}"

    # Document Count
    def get_total_documents(self):
        return self.documents.count()

# Vehicle Document Model
class VehicleDocument(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='documents', verbose_name="차량")
    document = models.FileField(upload_to='documents/', verbose_name="문서")
    upload_date = models.DateField(auto_now_add=True, verbose_name="업로드 날짜")

    def __str__(self):
        return f"Document for {self.vehicle}"