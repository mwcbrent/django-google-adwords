# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ad.description_line1'
        db.delete_column(u'django_google_adwords_ad', 'description_line1')

        # Deleting field 'Ad.description_line2'
        db.delete_column(u'django_google_adwords_ad', 'description_line2')

        # Adding field 'Ad.description_line_1'
        db.add_column(u'django_google_adwords_ad', 'description_line_1',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ad.description_line_2'
        db.add_column(u'django_google_adwords_ad', 'description_line_2',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Ad.description_line1'
        db.add_column(u'django_google_adwords_ad', 'description_line1',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ad.description_line2'
        db.add_column(u'django_google_adwords_ad', 'description_line2',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Ad.description_line_1'
        db.delete_column(u'django_google_adwords_ad', 'description_line_1')

        # Deleting field 'Ad.description_line_2'
        db.delete_column(u'django_google_adwords_ad', 'description_line_2')


    models = {
        u'django_google_adwords.account': {
            'Meta': {'object_name': 'Account'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'account_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'account_last_synced': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ad_group_last_synced': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ad_last_synced': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'campaign_last_synced': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.ad': {
            'Meta': {'object_name': 'Ad'},
            'ad': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ad_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ads'", 'to': u"orm['django_google_adwords.AdGroup']"}),
            'ad_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'ad_state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ad_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_line_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_line_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.adgroup': {
            'Meta': {'object_name': 'AdGroup'},
            'ad_group': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ad_group_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'ad_group_state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ad_groups'", 'to': u"orm['django_google_adwords.Campaign']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.alert': {
            'Meta': {'object_name': 'Alert'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'alerts'", 'to': u"orm['django_google_adwords.Account']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurred': ('django.db.models.fields.DateTimeField', [], {}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campaigns'", 'to': u"orm['django_google_adwords.Account']"}),
            'budget': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'budget_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'campaign': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'campaign_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'campaign_state': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.dailyaccountmetrics': {
            'Meta': {'object_name': 'DailyAccountMetrics'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metrics'", 'to': u"orm['django_google_adwords.Account']"}),
            'avg_cpc': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpc_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_cpm': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpm_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_position': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'click_conversion_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_impr_share': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'content_lost_is_budget': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'content_lost_is_rank': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conversions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'converted_clicks': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_converted_click': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_converted_click_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_est_total_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_est_total_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            'device': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'est_cross_device_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_total_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_total_conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value_click': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'invalid_click_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'invalid_clicks': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'search_exact_match_is': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_impr_share': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_lost_is_budget': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_lost_is_rank': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.dailyadgroupmetrics': {
            'Meta': {'object_name': 'DailyAdGroupMetrics'},
            'ad_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metrics'", 'to': u"orm['django_google_adwords.AdGroup']"}),
            'avg_cpc': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpc_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_cpm': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpm_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_position': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'bid_strategy_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bid_strategy_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bid_strategy_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'click_conversion_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_impr_share': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'content_lost_is_rank': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conversions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'converted_clicks': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_converted_click': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_converted_click_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_est_total_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_est_total_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            'est_cross_device_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_total_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_total_conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value_click': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_cpa_converted_clicks': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'max_cpa_converted_clicks_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'search_exact_match_is': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_impr_share': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_lost_is_rank': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'value_conv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'value_converted_click': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'value_est_total_conv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'view_through_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.dailyadmetrics': {
            'Meta': {'object_name': 'DailyAdMetrics'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metrics'", 'to': u"orm['django_google_adwords.Ad']"}),
            'avg_cpc': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpc_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_cpm': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpm_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_position': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'click_conversion_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conversions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'converted_clicks': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_converted_click': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_converted_click_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'value_conv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'value_converted_click': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'view_through_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.dailycampaignmetrics': {
            'Meta': {'object_name': 'DailyCampaignMetrics'},
            'avg_cpc': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpc_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_cpm': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'avg_cpm_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'avg_position': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'bid_strategy_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bid_strategy_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bid_strategy_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metrics'", 'to': u"orm['django_google_adwords.Campaign']"}),
            'click_conversion_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_impr_share': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'content_lost_is_budget': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'content_lost_is_rank': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'conversions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'converted_clicks': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_converted_click': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_converted_click_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'cost_est_total_conv': ('money.contrib.django.models.fields.MoneyField', [], {'decimal_places': '2', 'default': '0', 'no_currency_field': 'True', 'max_digits': '12', 'blank': 'True', 'null': 'True'}),
            'cost_est_total_conv_currency': ('money.contrib.django.models.fields.CurrencyField', [], {'default': "'AUD'", 'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {}),
            'est_cross_device_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_total_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'est_total_conv_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value_click': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'est_total_conv_value_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'invalid_click_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'invalid_clicks': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'search_exact_match_is': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_impr_share': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_lost_is_budget': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'search_lost_is_rank': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'total_conv_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'value_conv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'value_converted_click': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'view_through_conv': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'django_google_adwords.reportfile': {
            'Meta': {'object_name': 'ReportFile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['django_google_adwords']