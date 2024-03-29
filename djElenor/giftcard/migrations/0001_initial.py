# Generated by Django 4.2.10 on 2024-02-29 08:12

import djElenor.core.utils.json_serializer
import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_metadata', models.JSONField(blank=True, default=dict, encoder=djElenor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=djElenor.core.utils.json_serializer.CustomJsonEncoder, null=True)),
                ('code', models.CharField(db_index=True, max_length=16, unique=True, validators=[django.core.validators.MinLengthValidator(8)])),
                ('is_active', models.BooleanField(default=True)),
                ('created_by_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('used_by_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_used_on', models.DateTimeField(blank=True, null=True)),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('initial_balance_amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('current_balance_amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
                ('search_index_dirty', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('code',),
                'permissions': (('manage_gift_card', 'Manage gift cards.'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GiftCardTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'indexes': [django.contrib.postgres.indexes.GinIndex(fields=['name'], name='gift_card_tag_search_gin', opclasses=['gin_trgm_ops'])],
            },
        ),
        migrations.CreateModel(
            name='GiftCardEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('type', models.CharField(choices=[('issued', 'The gift card was created be staff user or app.'), ('bought', 'The gift card was bought by customer.'), ('updated', 'The gift card was updated.'), ('activated', 'The gift card was activated.'), ('deactivated', 'The gift card was deactivated.'), ('balance_reset', 'The gift card balance was reset.'), ('expiry_date_updated', 'The gift card expiry date was updated.'), ('tags_updated', 'The gift card tags were updated.'), ('sent_to_customer', 'The gift card was sent to the customer.'), ('resent', 'The gift card was resent to the customer.'), ('note_added', 'A note was added to the gift card.'), ('used_in_order', 'The gift card was used in order.')], max_length=255)),
                ('parameters', models.JSONField(blank=True, default=dict, encoder=djElenor.core.utils.json_serializer.CustomJsonEncoder)),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gift_card_events', to='app.app')),
                ('gift_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='giftcard.giftcard')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
