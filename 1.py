from fhirclient import client
settings = {
    'app_id': 'my_web_app',
    'api_base': 'http://localhost:8088/fhir',
}
smart = client.FHIRClient(settings=settings)
print(f'{smart.ready=}')
smart.prepare()
print(f'after smart.prepare()')
print(f'{smart.ready=}')
print(f'{smart.authorize_url=}')

import fhirclient.models.patient as p
patient = p.Patient.read('206', smart.server)
print(f'{patient.birthDate.isostring=}')

print(f'{smart.human_name(patient.name[0])=}')

print('patient', patient)

import fhirclient.models.procedure as p
search = p.Procedure.where(struct={'subject': '206', 'status': 'completed'})
procedures = search.perform_resources(smart.server)
for procedure in procedures:
    procedure.as_json()
