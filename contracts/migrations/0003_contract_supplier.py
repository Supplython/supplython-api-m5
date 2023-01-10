# Generated by Django 4.0.7 on 2023-01-10 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_alter_supplier_email_alter_supplier_name'),
        ('contracts', '0002_remove_contract_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='suppliers.supplier'),
            preserve_default=False,
        ),
    ]