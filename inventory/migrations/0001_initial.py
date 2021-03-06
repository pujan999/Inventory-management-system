# Generated by Django 3.1.5 on 2021-02-24 10:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='None', max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=255)),
                ('pan_number', models.CharField(max_length=255, null=True, unique=True)),
                ('title', models.CharField(default='Creditor', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_name', models.CharField(max_length=1000, null=True)),
                ('item_limit', models.PositiveIntegerField(null=True)),
                ('item_name', models.CharField(max_length=255)),
                ('item_code', models.CharField(default=uuid.uuid4, max_length=36)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_type', models.CharField(default='Purchase', max_length=1000)),
                ('bill_number', models.CharField(max_length=255)),
                ('bill_image', models.ImageField(null=True, upload_to='bill/')),
                ('date', models.DateField(auto_now_add=True)),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_type', models.CharField(default='Purchase Return', max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
                ('remarks', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_name', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(blank=True, max_length=100, null=True)),
                ('voucher_type', models.CharField(default='Sales', max_length=1000)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('remarks', models.CharField(max_length=1000, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SalesReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_type', models.CharField(default='Sales Return', max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
                ('remarks', models.CharField(max_length=1000, null=True)),
                ('bill_number', models.CharField(max_length=1000, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('quantity_after_transfer', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
            ],
        ),
        migrations.CreateModel(
            name='TestDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VendorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000)),
                ('address', models.CharField(default='Kathmandu', max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('company_contact', models.CharField(max_length=15)),
                ('contact', models.CharField(max_length=255)),
                ('pan_number', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(default='Debtor', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VoucherType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_type', models.CharField(choices=[('Sales', 'Sales'), ('SalesReturn', 'Sales Return'), ('PurchaseReturn', 'Purchase Return'), ('Purchase', 'Purchase'), ('LostDamage', 'Lost Damage')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.stock')),
            ],
        ),
        migrations.CreateModel(
            name='SalesReturnEntryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
                ('sales_return', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.salesreturn')),
            ],
        ),
        migrations.CreateModel(
            name='SalesEntryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.sales')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseReturnEntryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('purchase_return', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.purchasereturn')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
            ],
        ),
        migrations.AddField(
            model_name='purchasereturn',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.vendordetail'),
        ),
        migrations.CreateModel(
            name='PurchaseEntryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.purchase')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='vendor_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.vendordetail'),
        ),
        migrations.CreateModel(
            name='LostDamage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('remarks', models.CharField(max_length=1000, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('rack', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.rack')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('voucher_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.vouchertype')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.unit'),
        ),
    ]
