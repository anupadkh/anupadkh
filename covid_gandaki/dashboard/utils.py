class Table:

    def __init__(self, name, url, columns=[]):
        self.name = name
        self.url = url
        self.columns = columns


table_descriptions = [
    Table(
        name='विदेशबाट आएकाहरुको विवरण',
        url='/router/travel/',
        columns=[
            {
                'title': 'पालिका',
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
    ),
    Table(
        name='राहत वितरणको विवरण',
        url='/router/reliefItem/',
        columns=[
            {
                'title': 'पालिका',
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
                'primaryKey': 'true',
                'mask': '#,##'

            },
            {
                'type': 'text',
                'title': 'राहत पाउनेको नाम',
                'width': '250',
                'name': 'full_name',
                # 'mask': '###'
            },
            {
                'type': 'numeric',
                'title': 'मोबाइल नं',
                'width': '150',
                'name': 'mobile',
                'mask': '###'
            },
            {
                'type': 'text',
                'title': 'ठेगाना',
                'width': '250',
                'name': 'permanent_address',

            },
            {
                'type': 'text',
                'title': 'बाबुको नाम',
                'width': '250',
                'name': 'father_name'
            },
            {
                'type': 'hidden',
                'title': 'हजुरबुबाको नाम',
                'width': '250',
                'name': 'grandfather_name'
            },
            {
                'type': 'text',
                'title': 'जम्मा परिवार संख्या',
                'width': '150',
                'name': 'remarks',
                'mask': '###'
            },
            {
                'type': 'number',
                'title': 'जम्मा प्याकेज संख्या',
                'width': '120',
                'name': 'package',
                'mask': '###'
            },
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},

        ]

    ),
    Table(
        name='COVID-19 विवरण',
        url='/router/covid/',
        columns=[
            {
                'title': 'पालिका',
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
                'type': 'text',
                'title': 'नाम',
                'width': '250',
                'name': 'name'
            },
            {
                'type': 'numeric',
                'title': 'उमेर',
                'width': '50',
                'name': 'age',
                'mask': '#,##', 

            },
            {
                'type': 'numeric',
                'title': 'वार्ड',
                'width': '50',
                'name': 'ward',
                'mask': '#,##', 

            },
            {
                'type': 'dropdown',
                'title': 'लिङ्ग',
                'width': '70',
                'name': 'gender',
                'autocomplete': 'true',
                'source': [{"id": 1, "name": "पुरुष"}, {"id": 2, "name": "महिला"}, {"id": 3, "name": "अन्य"}, ],
                'mask': '#,##', 

            },
            {
                'type': 'dropdown',
                'title': 'टेष्टको परिणाम',
                'width': '100',
                'name': 'is_positive',
                'source': [{"id": 'true', "name": 'Positive'},
                         {"id": 'false', "name": 'Negative'}]

            },
            {
                'type': 'dropdown',
                'title': 'क्वारेन्टाइन । आइसोलेसनको नाम',
                'width': '250',
                'name': 'quarantined_zone',
                'url': '/router/quarantines/user/?format=json'

            },
            {
                'type': 'text',
                'name': 'remarks',
                'width': '150',
                'title': 'अन्य विवरण'
            },
            {
                'type': 'hidden'
            },
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},
        ]    
    ),
    Table(
        name='Quarantine विवरण',
        url='/router/quarantines',
        columns=[
            {
                'title': 'पालिका',
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
                'primaryKey': "true",

            },
            {
                'type': 'text',
                'title': 'नाम',
                'width': '250',
                'name': 'name'
            },
            {
                'type': 'numeric',
                'title': 'बेड संख्या',
                'width': '150',
                'name': 'total_beds',
                'mask': '#,##', 

            },
            {
                'type': 'numeric',
                'title': 'वडा',
                'width': '50',
                'mask': '#,##', 
                'name': 'ward'

            },
            {
                'type': 'numeric',
                'title': 'हाल क्वारेन्टाइनमा बसेकाहरुको संख्या',
                'width': '250',
                'name': 'currently_quarantined',
                'mask': '#,##', 

            },
            {
                'type': 'dropdown',
                'title': 'क्वारेन्टाइन क्षेत्र या आइसोलेसन क्षेत्र',
                'width': '150',
                'name': 'is_quarantine',
                'autocomplete': 'true',
                'source': [{"id": "0", "name": 'क्वारेन्टाइन'}, {"id": "1", "name": 'आइसोलेसन'}],


            },
            {
                'type': 'hidden'
            },
            {'type': 'hidden'},
            {'type': 'hidden'},
            {'type': 'hidden'},


        ]
    ),
]
