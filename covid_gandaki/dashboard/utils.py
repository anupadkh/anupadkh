class Table:

    def __init__(self, name, url, columns=[]):
        self.name = name
        self.url = url
        self.columns = columns


table_descriptions = []
table_descriptions.append(
    Table(
        name='विदेशबाट आएकाहरुको विवरण',
        url='/router/travel/',
        columns=[
            {
                'title': 'नगरपालिका',
                'type': 'dropdown',
                'name': 'mun',
                'url': '/router/muns/',
                'width': '300',
            },
            {
                'type': 'hidden',
                'title': 'सि.नं.',
                'name': 'id',
                'readOnly': 'true',
                'primaryKey': 'true'

            },
            {
                'type': 'hidden',
                'name': 'traveller'
            },
            {
                'type': 'hidden',
                'name': 'created_by'

            },
            {
                'type': 'text',
                'title': 'नाम',
                'width': '150',
                'name': 'name'
            },
            {
                'type': 'text',
                'title': 'उमेर',
                'width': '50',
                'name': 'age'
            },
            {
                'type': 'dropdown',
                'title': 'लिङ्ग',
                'width': '50',
                'name': 'gender',
                'autocomplete': 'true',
                'source': [{"id": 2, "name": 'महिला'}, {
                    "id": 1, "name": 'पुरुष'}, {"id": 3, "name": 'अन्य'}]

            },
            {
                'type': 'numeric',
                'title': 'वडा',
                'width': '50',
                'mask': '#,##',
                'decimal': '.',
                'name': 'ward'


            },
            {
                'type': 'text',
                'title': 'बाहिर रहेको देश',
                'width': '150',
                'name': 'Foreign Country'

            },
            {
                'type': 'text',
                'title': 'विदेशवाट नेपाल प्रवेश गर्दा प्रयोग गरेको यातायात साधन',
                'width': '150',
                'name': 'mode_of_transport_international'

            },
            {
                'type': 'text',
                'title': 'काठमाडौँ वा नाकावाट स्थानिय तहमा आउदा प्रयोग गरेको यातायात साधन',
                'width': '150',
                'name': 'mode_of_transport_national'

            },
            {
                'type': 'text',
                'title': 'नेपाल प्रवेश मिति',
                'width': '100',
                'name': 'Arrival Date',
                'mask': '0000-00-00'

            },

            {
                'type': 'text',
                'title': 'अन्य विवरण',
                'width': '300',
                'name': 'remarks'
            },
            
            {'type': 'hidden'},
            {'type': 'hidden'}
        ]
    )
)
