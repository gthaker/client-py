#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 on 2016-08-31.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import structuredefinition
from .fhirdate import FHIRDate


class StructureDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("StructureDefinition", js["resourceType"])
        return structuredefinition.StructureDefinition(js)
    
    def testStructureDefinition1(self):
        inst = self.instantiate_from("extension-structuredefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureDefinition instance")
        self.implStructureDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureDefinition", js["resourceType"])
        inst2 = structuredefinition.StructureDefinition(js)
        self.implStructureDefinition1(inst2)
    
    def implStructureDefinition1(self, inst):
        self.assertFalse(inst.abstract)
        self.assertEqual(inst.baseDefinition, "http://hl7.org/fhir/StructureDefinition/Extension")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/special/committees/FHIR")
        self.assertEqual(inst.contextType, "datatype")
        self.assertEqual(inst.context[0], "ElementDefinition")
        self.assertEqual(inst.date.date, FHIRDate("2014-01-31").date)
        self.assertEqual(inst.date.as_json(), "2014-01-31")
        self.assertEqual(inst.derivation, "constraint")
        self.assertEqual(inst.description, "An additional example value.")
        self.assertEqual(inst.differential.element[0].definition, "An additional example value.")
        self.assertEqual(inst.differential.element[0].id, "Extension:anadditionalexamplevalue")
        self.assertEqual(inst.differential.element[0].max, "*")
        self.assertEqual(inst.differential.element[0].min, 0)
        self.assertEqual(inst.differential.element[0].path, "Extension")
        self.assertEqual(inst.differential.element[0].short, "An additional example value")
        self.assertEqual(inst.differential.element[1].definition, "Key for this example.")
        self.assertEqual(inst.differential.element[1].id, "Extension:anadditionalexamplevalue.extension:index")
        self.assertEqual(inst.differential.element[1].max, "1")
        self.assertEqual(inst.differential.element[1].min, 1)
        self.assertEqual(inst.differential.element[1].name, "index")
        self.assertEqual(inst.differential.element[1].path, "Extension.extension")
        self.assertEqual(inst.differential.element[1].short, "Key for this example")
        self.assertEqual(inst.differential.element[1].type[0].code, "Extension")
        self.assertEqual(inst.differential.element[2].id, "Extension:anadditionalexamplevalue.extension:index.extension:extension")
        self.assertEqual(inst.differential.element[2].max, "0")
        self.assertEqual(inst.differential.element[2].name, "extension")
        self.assertEqual(inst.differential.element[2].path, "Extension.extension.extension")
        self.assertEqual(inst.differential.element[3].fixedUri, "index")
        self.assertEqual(inst.differential.element[3].id, "Extension:anadditionalexamplevalue.extension:index.url")
        self.assertEqual(inst.differential.element[3].path, "Extension.extension.url")
        self.assertEqual(inst.differential.element[3].type[0].code, "uri")
        self.assertEqual(inst.differential.element[4].id, "Extension:anadditionalexamplevalue.extension:index.value[x]")
        self.assertEqual(inst.differential.element[4].min, 1)
        self.assertEqual(inst.differential.element[4].path, "Extension.extension.value[x]")
        self.assertEqual(inst.differential.element[4].type[0].code, "string")
        self.assertEqual(inst.differential.element[5].definition, "Value of the example.")
        self.assertEqual(inst.differential.element[5].id, "Extension:anadditionalexamplevalue.extension:exvalue")
        self.assertEqual(inst.differential.element[5].max, "1")
        self.assertEqual(inst.differential.element[5].min, 0)
        self.assertEqual(inst.differential.element[5].name, "exValue")
        self.assertEqual(inst.differential.element[5].path, "Extension.extension")
        self.assertEqual(inst.differential.element[5].short, "Value of the example")
        self.assertEqual(inst.differential.element[5].type[0].code, "Extension")
        self.assertEqual(inst.differential.element[6].id, "Extension:anadditionalexamplevalue.extension:exvalue.extension:extension")
        self.assertEqual(inst.differential.element[6].max, "0")
        self.assertEqual(inst.differential.element[6].name, "extension")
        self.assertEqual(inst.differential.element[6].path, "Extension.extension.extension")
        self.assertEqual(inst.differential.element[7].fixedUri, "exValue")
        self.assertEqual(inst.differential.element[7].id, "Extension:anadditionalexamplevalue.extension:exvalue.url")
        self.assertEqual(inst.differential.element[7].path, "Extension.extension.url")
        self.assertEqual(inst.differential.element[7].type[0].code, "uri")
        self.assertEqual(inst.differential.element[8].id, "Extension:anadditionalexamplevalue.extension:exvalue.value[x]")
        self.assertEqual(inst.differential.element[8].min, 1)
        self.assertEqual(inst.differential.element[8].path, "Extension.extension.value[x]")
        self.assertEqual(inst.differential.element[8].type[0].code, "base64Binary")
        self.assertEqual(inst.differential.element[8].type[1].code, "boolean")
        self.assertEqual(inst.differential.element[8].type[2].code, "code")
        self.assertEqual(inst.differential.element[8].type[3].code, "date")
        self.assertEqual(inst.differential.element[8].type[4].code, "dateTime")
        self.assertEqual(inst.differential.element[8].type[5].code, "decimal")
        self.assertEqual(inst.differential.element[8].type[6].code, "id")
        self.assertEqual(inst.differential.element[8].type[7].code, "instant")
        self.assertEqual(inst.differential.element[8].type[8].code, "integer")
        self.assertEqual(inst.differential.element[8].type[9].code, "markdown")
        self.assertEqual(inst.differential.element[9].fixedUri, "http://hl7.org/fhir/StructureDefinition/structuredefinition-example")
        self.assertEqual(inst.differential.element[9].id, "Extension:anadditionalexamplevalue.url")
        self.assertEqual(inst.differential.element[9].path, "Extension.url")
        self.assertEqual(inst.differential.element[9].type[0].code, "uri")
        self.assertEqual(inst.display, "example")
        self.assertEqual(inst.fhirVersion, "1.6.0")
        self.assertEqual(inst.id, "structuredefinition-example")
        self.assertEqual(inst.kind, "complex-type")
        self.assertEqual(inst.mapping[0].identity, "rim")
        self.assertEqual(inst.mapping[0].name, "RIM Mapping")
        self.assertEqual(inst.mapping[0].uri, "http://hl7.org/v3")
        self.assertEqual(inst.name, "An additional example value")
        self.assertEqual(inst.publisher, "Health Level Seven, Inc. - [WG Name] WG")
        self.assertEqual(inst.snapshot.element[0].base.max, "*")
        self.assertEqual(inst.snapshot.element[0].base.min, 0)
        self.assertEqual(inst.snapshot.element[0].base.path, "Extension")
        self.assertEqual(inst.snapshot.element[0].condition[0], "ele-1")
        self.assertEqual(inst.snapshot.element[0].constraint[0].expression, "children().count() > id.count()")
        self.assertEqual(inst.snapshot.element[0].constraint[0].human, "All FHIR elements must have a @value or children")
        self.assertEqual(inst.snapshot.element[0].constraint[0].key, "ele-1")
        self.assertEqual(inst.snapshot.element[0].constraint[0].severity, "error")
        self.assertEqual(inst.snapshot.element[0].constraint[0].xpath, "@value|f:*|h:div")
        self.assertEqual(inst.snapshot.element[0].constraint[1].expression, "extension.exists() != value.exists()")
        self.assertEqual(inst.snapshot.element[0].constraint[1].human, "Must have either extensions or value[x], not both")
        self.assertEqual(inst.snapshot.element[0].constraint[1].key, "ext-1")
        self.assertEqual(inst.snapshot.element[0].constraint[1].severity, "error")
        self.assertEqual(inst.snapshot.element[0].constraint[1].xpath, "exists(f:extension)!=exists(f:*[starts-with(local-name(.), 'value')])")
        self.assertEqual(inst.snapshot.element[0].definition, "An additional example value.")
        self.assertEqual(inst.snapshot.element[0].id, "Extension:anadditionalexamplevalue")
        self.assertEqual(inst.snapshot.element[0].max, "*")
        self.assertEqual(inst.snapshot.element[0].min, 0)
        self.assertEqual(inst.snapshot.element[0].path, "Extension")
        self.assertEqual(inst.snapshot.element[0].short, "An additional example value")
        self.assertEqual(inst.snapshot.element[1].base.max, "*")
        self.assertEqual(inst.snapshot.element[1].base.min, 0)
        self.assertEqual(inst.snapshot.element[1].base.path, "Element.id")
        self.assertEqual(inst.snapshot.element[1].definition, "unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.")
        self.assertEqual(inst.snapshot.element[1].id, "Extension:anadditionalexamplevalue.id")
        self.assertEqual(inst.snapshot.element[1].mapping[0].identity, "rim")
        self.assertEqual(inst.snapshot.element[1].mapping[0].map, "n/a")
        self.assertEqual(inst.snapshot.element[1].max, "1")
        self.assertEqual(inst.snapshot.element[1].min, 0)
        self.assertEqual(inst.snapshot.element[1].path, "Extension.id")
        self.assertEqual(inst.snapshot.element[1].representation[0], "xmlAttr")
        self.assertEqual(inst.snapshot.element[1].short, "xml:id (or equivalent in JSON)")
        self.assertEqual(inst.snapshot.element[1].type[0].code, "string")
        self.assertEqual(inst.snapshot.element[2].base.max, "*")
        self.assertEqual(inst.snapshot.element[2].base.min, 0)
        self.assertEqual(inst.snapshot.element[2].base.path, "Element.extension")
        self.assertEqual(inst.snapshot.element[2].definition, "An Extension")
        self.assertEqual(inst.snapshot.element[2].id, "Extension:anadditionalexamplevalue.extension")
        self.assertEqual(inst.snapshot.element[2].max, "*")
        self.assertEqual(inst.snapshot.element[2].min, 0)
        self.assertEqual(inst.snapshot.element[2].path, "Extension.extension")
        self.assertEqual(inst.snapshot.element[2].short, "Extension")
        self.assertEqual(inst.snapshot.element[2].slicing.discriminator[0], "url")
        self.assertEqual(inst.snapshot.element[2].slicing.id, "77")
        self.assertFalse(inst.snapshot.element[2].slicing.ordered)
        self.assertEqual(inst.snapshot.element[2].slicing.rules, "open")
        self.assertEqual(inst.snapshot.element[2].type[0].code, "Extension")
        self.assertEqual(inst.snapshot.element[3].base.max, "*")
        self.assertEqual(inst.snapshot.element[3].base.min, 0)
        self.assertEqual(inst.snapshot.element[3].base.path, "Element.extension")
        self.assertEqual(inst.snapshot.element[3].definition, "Key for this example.")
        self.assertEqual(inst.snapshot.element[3].id, "Extension:anadditionalexamplevalue.extension:index")
        self.assertEqual(inst.snapshot.element[3].max, "1")
        self.assertEqual(inst.snapshot.element[3].min, 1)
        self.assertEqual(inst.snapshot.element[3].name, "index")
        self.assertEqual(inst.snapshot.element[3].path, "Extension.extension")
        self.assertEqual(inst.snapshot.element[3].short, "Key for this example")
        self.assertEqual(inst.snapshot.element[3].type[0].code, "Extension")
        self.assertEqual(inst.snapshot.element[4].base.max, "*")
        self.assertEqual(inst.snapshot.element[4].base.min, 0)
        self.assertEqual(inst.snapshot.element[4].base.path, "Element.id")
        self.assertEqual(inst.snapshot.element[4].definition, "unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.")
        self.assertEqual(inst.snapshot.element[4].id, "Extension:anadditionalexamplevalue.extension:index.id")
        self.assertEqual(inst.snapshot.element[4].mapping[0].identity, "rim")
        self.assertEqual(inst.snapshot.element[4].mapping[0].map, "n/a")
        self.assertEqual(inst.snapshot.element[4].max, "1")
        self.assertEqual(inst.snapshot.element[4].min, 0)
        self.assertEqual(inst.snapshot.element[4].path, "Extension.extension.id")
        self.assertEqual(inst.snapshot.element[4].representation[0], "xmlAttr")
        self.assertEqual(inst.snapshot.element[4].short, "xml:id (or equivalent in JSON)")
        self.assertEqual(inst.snapshot.element[4].type[0].code, "string")
        self.assertEqual(inst.snapshot.element[5].base.max, "*")
        self.assertEqual(inst.snapshot.element[5].base.min, 0)
        self.assertEqual(inst.snapshot.element[5].base.path, "Element.extension")
        self.assertEqual(inst.snapshot.element[5].definition, "An Extension")
        self.assertEqual(inst.snapshot.element[5].id, "Extension:anadditionalexamplevalue.extension:index.extension:extension")
        self.assertEqual(inst.snapshot.element[5].max, "0")
        self.assertEqual(inst.snapshot.element[5].min, 0)
        self.assertEqual(inst.snapshot.element[5].name, "extension")
        self.assertEqual(inst.snapshot.element[5].path, "Extension.extension.extension")
        self.assertEqual(inst.snapshot.element[5].short, "Extension")
        self.assertEqual(inst.snapshot.element[5].type[0].code, "Extension")
        self.assertEqual(inst.snapshot.element[6].base.max, "1")
        self.assertEqual(inst.snapshot.element[6].base.min, 1)
        self.assertEqual(inst.snapshot.element[6].base.path, "Extension.url")
        self.assertEqual(inst.snapshot.element[6].definition, "Source of the definition for the extension code - a logical name or a URL.")
        self.assertEqual(inst.snapshot.element[6].fixedUri, "index")
        self.assertEqual(inst.snapshot.element[6].id, "Extension:anadditionalexamplevalue.extension:index.url")
        self.assertEqual(inst.snapshot.element[6].mapping[0].identity, "rim")
        self.assertEqual(inst.snapshot.element[6].mapping[0].map, "N/A")
        self.assertEqual(inst.snapshot.element[6].max, "1")
        self.assertEqual(inst.snapshot.element[6].min, 1)
        self.assertEqual(inst.snapshot.element[6].path, "Extension.extension.url")
        self.assertEqual(inst.snapshot.element[6].representation[0], "xmlAttr")
        self.assertEqual(inst.snapshot.element[6].short, "identifies the meaning of the extension")
        self.assertEqual(inst.snapshot.element[6].type[0].code, "uri")
        self.assertEqual(inst.snapshot.element[7].base.max, "1")
        self.assertEqual(inst.snapshot.element[7].base.min, 0)
        self.assertEqual(inst.snapshot.element[7].base.path, "Extension.value[x]")
        self.assertEqual(inst.snapshot.element[7].definition, "Value of extension - may be a resource or one of a constrained set of the data types (see Extensibility in the spec for list).")
        self.assertEqual(inst.snapshot.element[7].id, "Extension:anadditionalexamplevalue.extension:index.valueString")
        self.assertEqual(inst.snapshot.element[7].mapping[0].identity, "rim")
        self.assertEqual(inst.snapshot.element[7].mapping[0].map, "N/A")
        self.assertEqual(inst.snapshot.element[7].max, "1")
        self.assertEqual(inst.snapshot.element[7].min, 1)
        self.assertEqual(inst.snapshot.element[7].path, "Extension.extension.valueString")
        self.assertEqual(inst.snapshot.element[7].short, "Value of extension")
        self.assertEqual(inst.snapshot.element[7].type[0].code, "string")
        self.assertEqual(inst.snapshot.element[8].base.max, "*")
        self.assertEqual(inst.snapshot.element[8].base.min, 0)
        self.assertEqual(inst.snapshot.element[8].base.path, "Element.extension")
        self.assertEqual(inst.snapshot.element[8].definition, "Value of the example.")
        self.assertEqual(inst.snapshot.element[8].id, "Extension:anadditionalexamplevalue.extension:exvalue")
        self.assertEqual(inst.snapshot.element[8].max, "1")
        self.assertEqual(inst.snapshot.element[8].min, 0)
        self.assertEqual(inst.snapshot.element[8].name, "exValue")
        self.assertEqual(inst.snapshot.element[8].path, "Extension.extension")
        self.assertEqual(inst.snapshot.element[8].short, "Value of the example")
        self.assertEqual(inst.snapshot.element[8].type[0].code, "Extension")
        self.assertEqual(inst.snapshot.element[9].base.max, "*")
        self.assertEqual(inst.snapshot.element[9].base.min, 0)
        self.assertEqual(inst.snapshot.element[9].base.path, "Element.id")
        self.assertEqual(inst.snapshot.element[9].definition, "unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.")
        self.assertEqual(inst.snapshot.element[9].id, "Extension:anadditionalexamplevalue.extension:exvalue.id")
        self.assertEqual(inst.snapshot.element[9].mapping[0].identity, "rim")
        self.assertEqual(inst.snapshot.element[9].mapping[0].map, "n/a")
        self.assertEqual(inst.snapshot.element[9].max, "1")
        self.assertEqual(inst.snapshot.element[9].min, 0)
        self.assertEqual(inst.snapshot.element[9].path, "Extension.extension.id")
        self.assertEqual(inst.snapshot.element[9].representation[0], "xmlAttr")
        self.assertEqual(inst.snapshot.element[9].short, "xml:id (or equivalent in JSON)")
        self.assertEqual(inst.snapshot.element[9].type[0].code, "string")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.type, "Extension")
        self.assertEqual(inst.url, "http://hl7.org/fhir/StructureDefinition/structuredefinition-example")
    
    def testStructureDefinition2(self):
        inst = self.instantiate_from("structuredefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureDefinition instance")
        self.implStructureDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureDefinition", js["resourceType"])
        inst2 = structuredefinition.StructureDefinition(js)
        self.implStructureDefinition2(inst2)
    
    def implStructureDefinition2(self, inst):
        self.assertFalse(inst.abstract)
        self.assertEqual(inst.baseDefinition, "http://hl7.org/fhir/StructureDefinition/DiagnosticReport")
        self.assertEqual(inst.code[0].code, "314079002")
        self.assertEqual(inst.code[0].display, "314079002")
        self.assertEqual(inst.code[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contact[0].name, "Grahame Grieve")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "grahame@healthintersections.com.au")
        self.assertEqual(inst.copyright, "Createive Commons 0, per FHIR specification")
        self.assertEqual(inst.date.date, FHIRDate("2012-05-12").date)
        self.assertEqual(inst.date.as_json(), "2012-05-12")
        self.assertEqual(inst.derivation, "constraint")
        self.assertEqual(inst.description, "Describes how the lab report is used for a standard Lipid Profile - Cholesterol, Triglyceride and Cholesterol fractions. Uses LOINC codes")
        self.assertEqual(inst.display, "Example Lipid Profile")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.fhirVersion, "1.0.0")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "1.2.36.90146595217.4.2")
        self.assertEqual(inst.kind, "resource")
        self.assertEqual(inst.mapping[0].comments, "Actual mappings haven't yet been filled out")
        self.assertEqual(inst.mapping[0].identity, "m1")
        self.assertEqual(inst.mapping[0].name, "RCPA Lipid Report recommendations")
        self.assertEqual(inst.mapping[0].uri, "https://www.rcpa.edu.au/getattachment/0961c6d1-ec80-4500-8dc0-de516500e05b/Lipid-and-lipoprotein-testing.aspx")
        self.assertEqual(inst.name, "Example Lipid Profile")
        self.assertEqual(inst.publisher, "Health Intersections Pty Ltd")
        self.assertEqual(inst.requirements, "Provide an example to demonstrate how to use StructureDefinition")
        self.assertEqual(inst.snapshot.element[0].base.max, "1")
        self.assertEqual(inst.snapshot.element[0].base.min, 1)
        self.assertEqual(inst.snapshot.element[0].base.path, "DiagnosticReport")
        self.assertEqual(inst.snapshot.element[0].definition, "The findings and interpretation of a general lipd lab profile.")
        self.assertEqual(inst.snapshot.element[0].id, "DiagnosticReport")
        self.assertFalse(inst.snapshot.element[0].isModifier)
        self.assertEqual(inst.snapshot.element[0].max, "1")
        self.assertEqual(inst.snapshot.element[0].min, 1)
        self.assertEqual(inst.snapshot.element[0].name, "LipidProfile")
        self.assertEqual(inst.snapshot.element[0].path, "DiagnosticReport")
        self.assertEqual(inst.snapshot.element[0].short, "Lipid Lab Report")
        self.assertEqual(inst.snapshot.element[1].base.max, "*")
        self.assertEqual(inst.snapshot.element[1].base.min, 0)
        self.assertEqual(inst.snapshot.element[1].base.path, "DiagnosticReport.extension")
        self.assertEqual(inst.snapshot.element[1].id, "DiagnosticReport.extension")
        self.assertFalse(inst.snapshot.element[1].isModifier)
        self.assertEqual(inst.snapshot.element[1].max, "*")
        self.assertEqual(inst.snapshot.element[1].min, 0)
        self.assertEqual(inst.snapshot.element[1].path, "DiagnosticReport.extension")
        self.assertEqual(inst.snapshot.element[1].short, "Additional Content defined by implementations")
        self.assertEqual(inst.snapshot.element[1].slicing.discriminator[0], "url")
        self.assertFalse(inst.snapshot.element[1].slicing.ordered)
        self.assertEqual(inst.snapshot.element[1].slicing.rules, "open")
        self.assertEqual(inst.snapshot.element[1].type[0].code, "Extension")
        self.assertEqual(inst.snapshot.element[2].alias[0], "narrative")
        self.assertEqual(inst.snapshot.element[2].alias[1], "html")
        self.assertEqual(inst.snapshot.element[2].alias[2], "xhtml")
        self.assertEqual(inst.snapshot.element[2].alias[3], "display")
        self.assertEqual(inst.snapshot.element[2].base.max, "1")
        self.assertEqual(inst.snapshot.element[2].base.min, 0)
        self.assertEqual(inst.snapshot.element[2].base.path, "DiagnosticReport.text")
        self.assertEqual(inst.snapshot.element[2].comments, "Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative.")
        self.assertEqual(inst.snapshot.element[2].id, "DiagnosticReport.text")
        self.assertFalse(inst.snapshot.element[2].isModifier)
        self.assertEqual(inst.snapshot.element[2].max, "1")
        self.assertEqual(inst.snapshot.element[2].min, 0)
        self.assertEqual(inst.snapshot.element[2].path, "DiagnosticReport.text")
        self.assertEqual(inst.snapshot.element[2].short, "Text summary of the resource, for human interpretation")
        self.assertEqual(inst.snapshot.element[2].type[0].code, "Narrative")
        self.assertEqual(inst.snapshot.element[3].alias[0], "inline resources")
        self.assertEqual(inst.snapshot.element[3].alias[1], "anonymous resources")
        self.assertEqual(inst.snapshot.element[3].alias[2], "contained resources")
        self.assertEqual(inst.snapshot.element[3].base.max, "*")
        self.assertEqual(inst.snapshot.element[3].base.min, 0)
        self.assertEqual(inst.snapshot.element[3].base.path, "DiagnosticReport.contained")
        self.assertEqual(inst.snapshot.element[3].comments, "This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again.")
        self.assertEqual(inst.snapshot.element[3].id, "DiagnosticReport.contained")
        self.assertFalse(inst.snapshot.element[3].isModifier)
        self.assertEqual(inst.snapshot.element[3].max, "*")
        self.assertEqual(inst.snapshot.element[3].min, 0)
        self.assertEqual(inst.snapshot.element[3].path, "DiagnosticReport.contained")
        self.assertEqual(inst.snapshot.element[3].short, "Contained, inline Resources")
        self.assertEqual(inst.snapshot.element[3].type[0].code, "Resource")
        self.assertEqual(inst.snapshot.element[4].base.max, "1")
        self.assertEqual(inst.snapshot.element[4].base.min, 1)
        self.assertEqual(inst.snapshot.element[4].base.path, "DiagnosticReport.status")
        self.assertEqual(inst.snapshot.element[4].binding.strength, "required")
        self.assertEqual(inst.snapshot.element[4].comments, "This is labeled as \"Is Modifier\" because applications need to take appropriate action if a report is withdrawn.")
        self.assertEqual(inst.snapshot.element[4].definition, "The status of the diagnostic report as a whole.")
        self.assertEqual(inst.snapshot.element[4].id, "DiagnosticReport.status")
        self.assertFalse(inst.snapshot.element[4].isModifier)
        self.assertEqual(inst.snapshot.element[4].max, "1")
        self.assertEqual(inst.snapshot.element[4].min, 1)
        self.assertEqual(inst.snapshot.element[4].path, "DiagnosticReport.status")
        self.assertEqual(inst.snapshot.element[4].short, "registered|interim|final|amended|cancelled|withdrawn")
        self.assertEqual(inst.snapshot.element[4].type[0].code, "code")
        self.assertEqual(inst.snapshot.element[5].base.max, "1")
        self.assertEqual(inst.snapshot.element[5].base.min, 1)
        self.assertEqual(inst.snapshot.element[5].base.path, "DiagnosticReport.issued")
        self.assertEqual(inst.snapshot.element[5].comments, "May be different from the update time of the resource itself, because that is the status of the record (potentially a secondary copy), not the actual release time of the report.")
        self.assertEqual(inst.snapshot.element[5].definition, "The date and/or time that this version of the report was released from the source diagnostic service.")
        self.assertEqual(inst.snapshot.element[5].id, "DiagnosticReport.issued")
        self.assertFalse(inst.snapshot.element[5].isModifier)
        self.assertEqual(inst.snapshot.element[5].max, "1")
        self.assertEqual(inst.snapshot.element[5].min, 1)
        self.assertEqual(inst.snapshot.element[5].path, "DiagnosticReport.issued")
        self.assertEqual(inst.snapshot.element[5].short, "Date this version was released")
        self.assertEqual(inst.snapshot.element[5].type[0].code, "dateTime")
        self.assertEqual(inst.snapshot.element[6].base.max, "1")
        self.assertEqual(inst.snapshot.element[6].base.min, 1)
        self.assertEqual(inst.snapshot.element[6].base.path, "DiagnosticReport.subject")
        self.assertEqual(inst.snapshot.element[6].definition, "The subject of the report. Usually, but not always, this is a patient. However diagnostic services also perform analyses on specimens collected from a variety of other sources.")
        self.assertEqual(inst.snapshot.element[6].id, "DiagnosticReport.subject")
        self.assertFalse(inst.snapshot.element[6].isModifier)
        self.assertEqual(inst.snapshot.element[6].max, "1")
        self.assertEqual(inst.snapshot.element[6].min, 1)
        self.assertEqual(inst.snapshot.element[6].path, "DiagnosticReport.subject")
        self.assertEqual(inst.snapshot.element[6].short, "The subject of the report")
        self.assertEqual(inst.snapshot.element[6].type[0].code, "Reference")
        self.assertEqual(inst.snapshot.element[6].type[0].profile, "http://hl7.org/fhir/StructureDefinition/Patient")
        self.assertEqual(inst.snapshot.element[6].type[1].code, "Reference")
        self.assertEqual(inst.snapshot.element[6].type[1].profile, "http://hl7.org/fhir/StructureDefinition/Group")
        self.assertEqual(inst.snapshot.element[6].type[2].code, "Reference")
        self.assertEqual(inst.snapshot.element[6].type[2].profile, "http://hl7.org/fhir/StructureDefinition/Device")
        self.assertEqual(inst.snapshot.element[7].base.max, "1")
        self.assertEqual(inst.snapshot.element[7].base.min, 1)
        self.assertEqual(inst.snapshot.element[7].base.path, "DiagnosticReport.performer")
        self.assertEqual(inst.snapshot.element[7].comments, "This is not necessarily the source of the atomic data items - it's the entity that takes responsibility for the clinical report.")
        self.assertEqual(inst.snapshot.element[7].definition, "The diagnostic service that is responsible for issuing the report.")
        self.assertEqual(inst.snapshot.element[7].id, "DiagnosticReport.performer")
        self.assertFalse(inst.snapshot.element[7].isModifier)
        self.assertEqual(inst.snapshot.element[7].max, "1")
        self.assertEqual(inst.snapshot.element[7].min, 1)
        self.assertEqual(inst.snapshot.element[7].path, "DiagnosticReport.performer")
        self.assertEqual(inst.snapshot.element[7].short, "Responsible Diagnostic Service")
        self.assertEqual(inst.snapshot.element[7].type[0].code, "Reference")
        self.assertEqual(inst.snapshot.element[7].type[0].profile, "http://hl7.org/fhir/StructureDefinition/Observation")
        self.assertEqual(inst.snapshot.element[8].base.max, "*")
        self.assertEqual(inst.snapshot.element[8].base.min, 0)
        self.assertEqual(inst.snapshot.element[8].base.path, "DiagnosticReport.identifier")
        self.assertEqual(inst.snapshot.element[8].definition, "The local ID assigned to the report by the order filler, usually by the Information System of the diagnostic service provider.")
        self.assertEqual(inst.snapshot.element[8].id, "DiagnosticReport.identifier")
        self.assertFalse(inst.snapshot.element[8].isModifier)
        self.assertEqual(inst.snapshot.element[8].max, "1")
        self.assertEqual(inst.snapshot.element[8].min, 0)
        self.assertEqual(inst.snapshot.element[8].path, "DiagnosticReport.identifier")
        self.assertEqual(inst.snapshot.element[8].short, "Id for external references to this report")
        self.assertEqual(inst.snapshot.element[8].type[0].code, "Identifier")
        self.assertEqual(inst.snapshot.element[9].base.max, "*")
        self.assertEqual(inst.snapshot.element[9].base.min, 0)
        self.assertEqual(inst.snapshot.element[9].base.path, "DiagnosticReport.request")
        self.assertEqual(inst.snapshot.element[9].definition, "Details concerning a single pathology test requested.")
        self.assertEqual(inst.snapshot.element[9].id, "DiagnosticReport.request")
        self.assertFalse(inst.snapshot.element[9].isModifier)
        self.assertEqual(inst.snapshot.element[9].max, "*")
        self.assertEqual(inst.snapshot.element[9].min, 0)
        self.assertEqual(inst.snapshot.element[9].path, "DiagnosticReport.request")
        self.assertEqual(inst.snapshot.element[9].short, "What was requested")
        self.assertEqual(inst.snapshot.element[9].type[0].code, "Reference")
        self.assertEqual(inst.snapshot.element[9].type[0].profile, "http://hl7.org/fhir/StructureDefinition/DiagnosticRequest")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DiagnosticReport")
        self.assertEqual(inst.url, "http://hl7.org/fhir/StructureDefinition/example")
        self.assertEqual(inst.useContext[0].coding[0].code, "AU")
        self.assertEqual(inst.useContext[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.version, "2")

