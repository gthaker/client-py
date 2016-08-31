#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 on 2016-08-31.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import measurereport
from .fhirdate import FHIRDate


class MeasureReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MeasureReport", js["resourceType"])
        return measurereport.MeasureReport(js)
    
    def testMeasureReport1(self):
        inst = self.instantiate_from("measurereport-cms146-cat1-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport1(inst2)
    
    def implMeasureReport1(self, inst):
        self.assertEqual(inst.contained[0].id, "reporter")
        self.assertEqual(inst.group[0].identifier.value, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].count, 1)
        self.assertEqual(inst.group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].population[1].count, 1)
        self.assertEqual(inst.group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].population[2].count, 1)
        self.assertEqual(inst.group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].population[3].count, 0)
        self.assertEqual(inst.group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[0].count, 1)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[1].count, 1)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[2].count, 1)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[0].value, "true")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[1].value, "false")
        self.assertEqual(inst.group[0].stratifier[0].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[1].group[0].value, "true")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[0].count, 1)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[1].count, 1)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[2].count, 1)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[1].group[1].value, "false")
        self.assertEqual(inst.group[0].stratifier[1].identifier.value, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[0].count, 1)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[1].count, 1)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[2].count, 1)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[0].value, "male")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[1].value, "female")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[2].value, "other")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[3].value, "unknown")
        self.assertEqual(inst.group[0].stratifier[2].identifier.value, "stratifier-gender")
        self.assertEqual(inst.group[0].supplementalData[0].group[0].count, 1)
        self.assertEqual(inst.group[0].supplementalData[0].group[0].value, "male")
        self.assertEqual(inst.group[0].supplementalData[0].group[1].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[1].value, "female")
        self.assertEqual(inst.group[0].supplementalData[0].group[2].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[2].value, "other")
        self.assertEqual(inst.group[0].supplementalData[0].group[3].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[3].value, "unknown")
        self.assertEqual(inst.group[0].supplementalData[0].identifier.value, "supplemental-data-gender")
        self.assertEqual(inst.group[0].supplementalData[1].group[0].count, 0)
        self.assertEqual(inst.group[0].supplementalData[1].group[0].value, "true")
        self.assertEqual(inst.group[0].supplementalData[1].group[1].count, 1)
        self.assertEqual(inst.group[0].supplementalData[1].group[1].value, "false")
        self.assertEqual(inst.group[0].supplementalData[1].identifier.value, "supplemental-data-deceased")
        self.assertEqual(inst.id, "measurereport-cms146-cat1-example")
        self.assertEqual(inst.period.end.date, FHIRDate("2014-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-01-01")
        self.assertEqual(inst.status, "complete")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "individual")
    
    def testMeasureReport2(self):
        inst = self.instantiate_from("measurereport-cms146-cat2-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport2(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport2(inst2)
    
    def implMeasureReport2(self, inst):
        self.assertEqual(inst.contained[0].id, "reporter")
        self.assertEqual(inst.group[0].identifier.value, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].count, 500)
        self.assertEqual(inst.group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].population[1].count, 200)
        self.assertEqual(inst.group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].population[2].count, 500)
        self.assertEqual(inst.group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].population[3].count, 100)
        self.assertEqual(inst.group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[0].value, "true")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[1].value, "false")
        self.assertEqual(inst.group[0].stratifier[0].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[1].group[0].value, "true")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[1].group[1].value, "false")
        self.assertEqual(inst.group[0].stratifier[1].identifier.value, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[0].value, "male")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[1].value, "female")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[2].value, "other")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[3].value, "unknown")
        self.assertEqual(inst.group[0].stratifier[2].identifier.value, "stratifier-gender")
        self.assertEqual(inst.group[0].supplementalData[0].group[0].count, 250)
        self.assertEqual(inst.group[0].supplementalData[0].group[0].value, "male")
        self.assertEqual(inst.group[0].supplementalData[0].group[1].count, 250)
        self.assertEqual(inst.group[0].supplementalData[0].group[1].value, "female")
        self.assertEqual(inst.group[0].supplementalData[0].group[2].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[2].value, "other")
        self.assertEqual(inst.group[0].supplementalData[0].group[3].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[3].value, "unknown")
        self.assertEqual(inst.group[0].supplementalData[0].identifier.value, "supplemental-data-gender")
        self.assertEqual(inst.group[0].supplementalData[1].group[0].count, 0)
        self.assertEqual(inst.group[0].supplementalData[1].group[0].value, "true")
        self.assertEqual(inst.group[0].supplementalData[1].group[1].count, 500)
        self.assertEqual(inst.group[0].supplementalData[1].group[1].value, "false")
        self.assertEqual(inst.group[0].supplementalData[1].identifier.value, "supplemental-data-deceased")
        self.assertEqual(inst.id, "measurereport-cms146-cat2-example")
        self.assertEqual(inst.period.end.date, FHIRDate("2014-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-01-01")
        self.assertEqual(inst.status, "complete")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "patient-list")
    
    def testMeasureReport3(self):
        inst = self.instantiate_from("measurereport-cms146-cat3-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport3(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport3(inst2)
    
    def implMeasureReport3(self, inst):
        self.assertEqual(inst.contained[0].id, "reporter")
        self.assertEqual(inst.group[0].identifier.value, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].count, 500)
        self.assertEqual(inst.group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].population[1].count, 200)
        self.assertEqual(inst.group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].population[2].count, 500)
        self.assertEqual(inst.group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].population[3].count, 100)
        self.assertEqual(inst.group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[0].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[0].value, "true")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[0].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].group[1].value, "false")
        self.assertEqual(inst.group[0].stratifier[0].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[1].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[1].group[0].value, "true")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[1].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[1].group[1].value, "false")
        self.assertEqual(inst.group[0].stratifier[1].identifier.value, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[2].group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[0].value, "male")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[0].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[1].count, 100)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[2].count, 250)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[3].count, 50)
        self.assertEqual(inst.group[0].stratifier[2].group[1].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[1].value, "female")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[2].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[2].value, "other")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[0].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[1].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[1].type, "numerator")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[2].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[2].type, "denominator")
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[3].count, 0)
        self.assertEqual(inst.group[0].stratifier[2].group[3].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[2].group[3].value, "unknown")
        self.assertEqual(inst.group[0].stratifier[2].identifier.value, "stratifier-gender")
        self.assertEqual(inst.group[0].supplementalData[0].group[0].count, 250)
        self.assertEqual(inst.group[0].supplementalData[0].group[0].value, "male")
        self.assertEqual(inst.group[0].supplementalData[0].group[1].count, 250)
        self.assertEqual(inst.group[0].supplementalData[0].group[1].value, "female")
        self.assertEqual(inst.group[0].supplementalData[0].group[2].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[2].value, "other")
        self.assertEqual(inst.group[0].supplementalData[0].group[3].count, 0)
        self.assertEqual(inst.group[0].supplementalData[0].group[3].value, "unknown")
        self.assertEqual(inst.group[0].supplementalData[0].identifier.value, "supplemental-data-gender")
        self.assertEqual(inst.group[0].supplementalData[1].group[0].count, 0)
        self.assertEqual(inst.group[0].supplementalData[1].group[0].value, "true")
        self.assertEqual(inst.group[0].supplementalData[1].group[1].count, 500)
        self.assertEqual(inst.group[0].supplementalData[1].group[1].value, "false")
        self.assertEqual(inst.group[0].supplementalData[1].identifier.value, "supplemental-data-deceased")
        self.assertEqual(inst.id, "measurereport-cms146-cat3-example")
        self.assertEqual(inst.period.end.date, FHIRDate("2014-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-01-01")
        self.assertEqual(inst.status, "complete")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "summary")

