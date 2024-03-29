# Generated by Django 4.2.10 on 2024-02-29 08:12

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discount', '0001_initial'),
        ('product', '0001_initial'),
        ('channel', '0001_initial'),
        ('order', '0001_initial'),
        ('app', '0001_initial'),
        ('checkout', '0002_initial'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AddField(
            model_name='voucher',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.category'),
        ),
        migrations.AddField(
            model_name='voucher',
            name='collections',
            field=models.ManyToManyField(blank=True, to='product.collection'),
        ),
        migrations.AddField(
            model_name='voucher',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.product'),
        ),
        migrations.AddField(
            model_name='voucher',
            name='variants',
            field=models.ManyToManyField(blank=True, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='promotiontranslation',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations',
                                    to='discount.promotion'),
        ),
        migrations.AddField(
            model_name='promotionruletranslation',
            name='promotion_rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations',
                                    to='discount.promotionrule'),
        ),
        migrations.AddField(
            model_name='promotionrule',
            name='channels',
            field=models.ManyToManyField(to='channel.channel'),
        ),
        migrations.AddField(
            model_name='promotionrule',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules',
                                    to='discount.promotion'),
        ),
        migrations.AddField(
            model_name='promotionrule',
            name='variants',
            field=models.ManyToManyField(blank=True, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='promotionevent',
            name='app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='promotion_events', to='app.app'),
        ),
        migrations.AddField(
            model_name='promotionevent',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events',
                                    to='discount.promotion'),
        ),
        migrations.AddField(
            model_name='promotionevent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='promotion_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='promotion',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['start_date'], name='start_date_idx'),
        ),
        migrations.AddIndex(
            model_name='promotion',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['end_date'], name='end_date_idx'),
        ),
        migrations.AddField(
            model_name='orderlinediscount',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='discounts', to='order.orderline'),
        ),
        migrations.AddField(
            model_name='orderlinediscount',
            name='promotion_rule',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', to='discount.promotionrule'),
        ),
        migrations.AddField(
            model_name='orderlinediscount',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', to='discount.voucher'),
        ),
        migrations.AddField(
            model_name='orderdiscount',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='discounts', to='order.order'),
        ),
        migrations.AddField(
            model_name='orderdiscount',
            name='promotion_rule',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', to='discount.promotionrule'),
        ),
        migrations.AddField(
            model_name='orderdiscount',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', to='discount.voucher'),
        ),
        migrations.AddField(
            model_name='checkoutlinediscount',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='discounts', to='checkout.checkoutline'),
        ),
        migrations.AddField(
            model_name='checkoutlinediscount',
            name='promotion_rule',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', to='discount.promotionrule'),
        ),
        migrations.AddField(
            model_name='checkoutlinediscount',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', to='discount.voucher'),
        ),
        migrations.AlterUniqueTogether(
            name='vouchertranslation',
            unique_together={('language_code', 'voucher')},
        ),
        migrations.AddIndex(
            model_name='vouchercustomer',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['voucher_code'],
                                                             name='vouchercustomer_voucher_code_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='vouchercustomer',
            unique_together={('voucher_code', 'customer_email')},
        ),
        migrations.AddIndex(
            model_name='vouchercode',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['voucher'], name='vouchercode_voucher_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='voucherchannellisting',
            unique_together={('voucher', 'channel')},
        ),
        migrations.AlterUniqueTogether(
            name='promotiontranslation',
            unique_together={('language_code', 'promotion')},
        ),
        migrations.AlterUniqueTogether(
            name='promotionruletranslation',
            unique_together={('language_code', 'promotion_rule')},
        ),
        migrations.AddIndex(
            model_name='orderlinediscount',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['promotion_rule'],
                                                             name='orderlinedisc_promotion_rule_idx'),
        ),
        migrations.AddIndex(
            model_name='orderlinediscount',
            index=django.contrib.postgres.indexes.GinIndex(fields=['voucher_code'],
                                                           name='orderlinedisc_voucher_code_idx'),
        ),
        migrations.AddIndex(
            model_name='orderdiscount',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['promotion_rule'],
                                                             name='orderdiscount_promotion_rule_idx'),
        ),
        migrations.AddIndex(
            model_name='orderdiscount',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name', 'translated_name'],
                                                           name='discount_or_name_d16858_gin'),
        ),
        migrations.AddIndex(
            model_name='orderdiscount',
            index=django.contrib.postgres.indexes.GinIndex(fields=['voucher_code'],
                                                           name='orderdiscount_voucher_code_idx'),
        ),
        migrations.AddIndex(
            model_name='checkoutlinediscount',
            index=django.contrib.postgres.indexes.BTreeIndex(fields=['promotion_rule'],
                                                             name='checklinedisc_promotion_rule_idx'),
        ),
        migrations.AddIndex(
            model_name='checkoutlinediscount',
            index=django.contrib.postgres.indexes.GinIndex(fields=['voucher_code'],
                                                           name='checklinedisc_voucher_code_idx'),
        ),
    ]
