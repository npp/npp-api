from django import db
from django.core.management.base import NoArgsCommand
from data.models import State, HealthInsuranceStateRaw, HealthInsuranceState
from npp_api.data.utils import clean_state_name
from decimal import Decimal

# National Priorities Project Data Repository
# load_health_insurance_state
# Created 1/18/2013

# Populates Health Insurance State table used by the API
# source model(s): HealthInsuranceStateRaw, State
# destination model:  HealthInsuranceState

# HOWTO:
# 1) Ensure that State is loaded and up to date
# 2) Run as Django management command from your project path "python manage.py load_health_insurance_state

# Safe to rerun: yes

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):

        state_name = ''
        total_inserts = 0
        total_updates = 0

        raw = HealthInsuranceStateRaw.objects.all().order_by('state')
        total_raw = raw.count()

        for r in raw:

            if r.state != state_name:
                clean_state = clean_state_name(r.state)
                try:
                    state_ref_current = State.objects.get(state_name=clean_state)
                except:
                    print 'Skipping record. Unable to find state: ' + clean_state
                    continue
                state_name = r.state

            try:
                record = HealthInsuranceState.objects.get(year=r.year,state=state_ref_current)
                total_updates = total_updates + 1
            except:
                record = HealthInsuranceState(year = r.year, state = state_ref_current)
                total_inserts = total_inserts + 1
            record.pop = r.pop
            record.pop_moe = r.pop_moe
            record.pop_no_ins = (r.pop_under_18_no_ins + r.pop_18_34_no_ins + 
                r.pop_35_64_no_ins + r.pop_over_64_no_ins)
            record.pop_no_ins_percent = format(
                record.pop_no_ins / Decimal(record.pop) * 100, '.1f')
            record.pop_ins = record.pop - record.pop_no_ins
            record.pop_ins_percent = format(
                record.pop_ins / Decimal(record.pop) * 100, '.1f')
            record.pop_under_18 = r.pop_under_18
            record.pop_under_18_moe = r.pop_under_18_moe
            record.pop_under_18_private = r.pop_under_18_private
            record.pop_under_18_private_moe = r.pop_under_18_private_moe
            record.pop_under_18_public = r.pop_under_18_public
            record.pop_under_18_public_moe = r.pop_under_18_public_moe
            record.pop_under_18_private_public = r.pop_under_18_private_public
            record.pop_under_18_private_public_moe = r.pop_under_18_private_public_moe
            record.pop_under_18_no_ins = r.pop_under_18_no_ins
            record.pop_under_18_no_ins_moe = r.pop_under_18_no_ins_moe
            record.pop_under_18_no_ins_percent = format(
                record.pop_under_18_no_ins / Decimal(record.pop_under_18) * 100, '.1f')
            record.pop_under_18_ins = record.pop_under_18 - record.pop_under_18_no_ins
            record.pop_under_18_ins_percent = format(
                record.pop_under_18_ins / Decimal(record.pop_under_18) * 100, '.1f')
            record.pop_18_34 = r.pop_18_34
            record.pop_18_34_moe = r.pop_18_34_moe
            record.pop_18_34_private = r.pop_18_34_private
            record.pop_18_34_private_moe = r.pop_18_34_private_moe
            record.pop_18_34_public = r.pop_18_34_public
            record.pop_18_34_public_moe = r.pop_18_34_public_moe
            record.pop_18_34_private_public = r.pop_18_34_private_public
            record.pop_18_34_private_public_moe = r.pop_18_34_private_public_moe
            record.pop_18_34_no_ins = r.pop_18_34_no_ins
            record.pop_18_34_no_ins_moe = r.pop_18_34_no_ins_moe
            record.pop_18_34_no_ins_percent = format(
                record.pop_18_34_no_ins / Decimal(record.pop_18_34) * 100, '.1f')
            record.pop_18_34_ins = record.pop_18_34 - record.pop_18_34_no_ins
            record.pop_18_34_ins_percent = format(
                record.pop_18_34_ins / Decimal(record.pop_18_34) * 100, '.1f')
            record.pop_35_64 = r.pop_35_64
            record.pop_35_64_moe = r.pop_35_64_moe
            record.pop_35_64_private = r.pop_35_64_private
            record.pop_35_64_private_moe = r.pop_35_64_private_moe
            record.pop_35_64_public = r.pop_35_64_public
            record.pop_35_64_public_moe = r.pop_35_64_public_moe
            record.pop_35_64_private_public = r.pop_35_64_private_public
            record.pop_35_64_private_public_moe = r.pop_35_64_private_public_moe
            record.pop_35_64_no_ins = r.pop_35_64_no_ins
            record.pop_35_64_no_ins_moe = r.pop_35_64_no_ins_moe
            record.pop_35_64_no_ins_percent = format(
                record.pop_35_64_no_ins / Decimal(record.pop_35_64) * 100, '.1f')
            record.pop_35_64_ins = record.pop_35_64 = record.pop_35_64_no_ins
            record.pop_35_64_ins_percent = format(
                record.pop_35_64_ins / Decimal(record.pop_35_64) * 100, '.1f')
            record.pop_18_64 = record.pop_18_34 + record.pop_35_64
            record.pop_18_64_private = (record.pop_18_34_private +
                record.pop_35_64_private)
            record.pop_18_64_public = (record.pop_18_34_public +
                record.pop_35_64_public)
            record.pop_18_64_private_public = (record.pop_18_34_private_public +
                record.pop_35_64_private_public)
            record.pop_18_64_no_ins = (record.pop_18_34_no_ins +
                record.pop_35_64_no_ins)
            record.pop_18_64_no_ins_percent = format(
                record.pop_18_64_no_ins / Decimal(record.pop_18_64) * 100, '.1f')
            record.pop_18_64_ins = record.pop_18_64 - record.pop_18_64_no_ins
            record.pop_18_64_ins_percent = format(
                record.pop_18_64_ins / Decimal(record.pop_18_64) * 100, '.1f')
            record.pop_over_64 = r.pop_over_64
            record.pop_over_64_moe = r.pop_over_64_moe
            record.pop_over_64_private = r.pop_over_64_private
            record.pop_over_64_private_moe = r.pop_over_64_private_moe
            record.pop_over_64_public = r.pop_over_64_public
            record.pop_over_64_public_moe = r.pop_over_64_public_moe
            record.pop_over_64_private_public = r.pop_over_64_private_public
            record.pop_over_64_private_public_moe = r.pop_over_64_private_public_moe
            record.pop_over_64_no_ins = r.pop_over_64_no_ins
            record.pop_over_64_no_ins_moe = r.pop_over_64_no_ins_moe
            record.pop_over_64_no_ins_percent = format(
                record.pop_over_64_no_ins / Decimal(record.pop_over_64) * 100, '.1f')
            record.pop_over_64_ins = record.pop_over_64 - record.pop_over_64_no_ins
            record.pop_over_64_ins_percent = format(
                record.pop_over_64_ins / Decimal(record.pop_over_64) * 100, '.1f')

            record.save()
            db.reset_queries()

        print 'Health Insurance (state): total records from raw data = %s' % total_raw
        print 'Health Insurance (state): total inserts = %s' % total_inserts
        print 'Health Insurance (state): total updates = %s' % total_updates