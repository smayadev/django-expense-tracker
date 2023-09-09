# Generated by Django 4.2.4 on 2023-09-09 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_expensesbase_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('amount', models.FloatField(default=0)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('slug', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='expensesbase',
            name='user',
        ),
        migrations.DeleteModel(
            name='EntertainmentExpenses',
        ),
        migrations.DeleteModel(
            name='ExpensesBase',
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.expensecategory'),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
