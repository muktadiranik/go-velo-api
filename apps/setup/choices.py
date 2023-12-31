'''
This file contains all the choices for the models in the 'common' app
'''


# Language Codes for the 'code' field in the 'Common/language' model

LANGUAGE_CODES = (
    ('EN', 'en'),
    ('ES', 'es'),
)


# Currency Symbols for the 'symbol' field in the 'Common/currency' model

CURRENCY_SYMBOLS = (
    ('USD', '$'),
    ('EUR', '€'),
    ('GBP', '£'),
    ('BDT', '৳'),
    ('INR', '₹')
    
    

)


# Currency Codes for the 'code' field in the 'Common/currency' model

CURRENCY_CODES = (
    ('$', 'USD'),
    ('€', 'EUR'),
    ('£', 'GBP'),
    ('৳', 'BDT'),
    ('₹', 'INR')
)


SHOP_VERIFICATION_STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)


ORDER_STATUS = (
    ('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
    ('Refunded', 'Refunded'),
    ('Past', 'Past'),
)

REFUND_STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
)


COUNTRIES_DICT = (
    ('Åland Islands', 'Åland Islands',),
    ('Afghanistan', 'Afghanistan',),
    ('Albania', 'Albania',),
    ('Algeria', 'Algeria',),
    ('American Samoa', 'American Samoa',),
    ('Andorra', 'Andorra',),
    ('Angola', 'Angola',),
    ('Anguilla', 'Anguilla',),
    ('Antarctica', 'Antarctica',),
    ('Argentina', 'Argentina',),
    ('Armenia', 'Armenia',),
    ('Aruba', 'Aruba',),
    ('Australia', 'Australia',),
    ('Austria', 'Austria',),
    ('Azerbaijan', 'Azerbaijan',),
    ('Bahamas', 'Bahamas',),
    ('Bahrain', 'Bahrain',),
    ('Bangladesh', 'Bangladesh',),
    ('Barbados', 'Barbados',),
    ('Belarus', 'Belarus',),
    ('Belgium', 'Belgium',),
    ('Belize', 'Belize',),
    ('Benin', 'Benin',),
    ('Bermuda', 'Bermuda',),
    ('Bhutan', 'Bhutan',),
    ('Bolivia', 'Bolivia',),
    ('Botswana', 'Botswana',),
    ('Bouvet Island', 'Bouvet Island',),
    ('Brazil', 'Brazil',),
    ('Bulgaria', 'Bulgaria',),
    ('Burundi', 'Burundi',),
    ('Cambodia', 'Cambodia',),
    ('Cameroon', 'Cameroon',),
    ('Canada', 'Canada',),
    ('Chad', 'Chad',),
    ('Chile', 'Chile',),
    ('China', 'China',),
    ('Colombia', 'Colombia',),
    ('Comoros', 'Comoros',),
    ('Congo', 'Congo',),
    ('Croatia', 'Croatia',),
    ('Cuba', 'Cuba',),
    ('Cyprus', 'Cyprus',),
    ('Denmark', 'Denmark',),
    ('Djibouti', 'Djibouti',),
    ('Dominica', 'Dominica',),
    ('Ecuador', 'Ecuador',),
    ('Egypt', 'Egypt',),
    ('Eritrea', 'Eritrea',),
    ('Estonia', 'Estonia',),
    ('Ethiopia', 'Ethiopia',),
    ('Fiji', 'Fiji',),
    ('Finland', 'Finland',),
    ('France', 'France',),
    ('Gabon', 'Gabon',),
    ('Gambia', 'Gambia',),
    ('Georgia', 'Georgia',),
    ('Germany', 'Germany',),
    ('Ghana', 'Ghana',),
    ('Gibraltar', 'Gibraltar',),
    ('Greece', 'Greece',),
    ('Greenland', 'Greenland',),
    ('Grenada', 'Grenada',),
    ('Guadeloupe', 'Guadeloupe',),
    ('Guam', 'Guam',),
    ('Guatemala', 'Guatemala',),
    ('Guernsey', 'Guernsey',),
    ('Guinea', 'Guinea',),
    ('Guyana', 'Guyana',),
    ('Honduras', 'Honduras',),
    ('Hong Kong', 'Hong Kong',),
    ('Hungary', 'Hungary',),
    ('Iceland', 'Iceland',),
    ('India', 'India',),
    ('Indonesia', 'Indonesia',),
    ('Iran', 'Iran',),
    ('Iraq', 'Iraq',),
    ('Ireland', 'Ireland',),
    ('Jersey', 'Jersey',),
    ('Jordan', 'Jordan',),
    ('Kazakhstan', 'Kazakhstan',),
    ('Kenya', 'Kenya',),
    ('Kiribati', 'Kiribati',),
    ('Kuwait', 'Kuwait',),
    ('Laos', 'Laos',),
    ('Latvia', 'Latvia',),
    ('Lebanon', 'Lebanon',),
    ('Liberia', 'Liberia',),
    ('Libya', 'Libya',),
    ('Macao', 'Macao',),
    ('Macedonia', 'Macedonia',),
    ('Madagascar', 'Madagascar',),
    ('Malawi', 'Malawi',),
    ('Malaysia', 'Malaysia',),
    ('Maldives', 'Maldives',),
    ('Mexico', 'Mexico',),
    ('Morocco', 'Morocco',),
    ('Myanmar', 'Myanmar',),
    ('Nepal', 'Nepal',),
    ('Netherlands', 'Netherlands',),
    ('New Caledonia', 'New Caledonia',),
    ('New Zealand', 'New Zealand',),
    ('Nicaragua', 'Nicaragua',),
    ('Niger', 'Niger',),
    ('Nigeria', 'Nigeria',),
    ('Niue', 'Niue',),
    ('Norfolk Island', 'Norfolk Island',),
    ('North Korea', 'North Korea',),
    ('Norway', 'Norway',),
    ('Oman', 'Oman',),
    ('Pakistan', 'Pakistan',),
    ('Palau', 'Palau',),
    ('Panama', 'Panama',),
    ('Papua New Guinea', 'Papua New Guinea',),
    ('Paraguay', 'Paraguay',),
    ('Peru', 'Peru',),
    ('Philippines', 'Philippines',),
    ('Poland', 'Poland',),
    ('Portugal', 'Portugal',),
    ('Puerto Rico', 'Puerto Rico',),
    ('Qatar', 'Qatar',),
    ('Romania', 'Romania',),
    ('Russia', 'Russia',),
    ('Rwanda', 'Rwanda',),
    ('Saint Helena', 'Saint Helena',),
    ('Saint Lucia', 'Saint Lucia',),
    ('Samoa', 'Samoa',),
    ('San Marino', 'San Marino',),
    ('Saudi Arabia', 'Saudi Arabia',),
    ('Senegal', 'Senegal',),
    ('Serbia', 'Serbia',),
    ('Seychelles', 'Seychelles',),
    ('Sierra Leone', 'Sierra Leone',),
    ('Singapore', 'Singapore',),
    ('Slovakia', 'Slovakia',),
    ('Slovenia', 'Slovenia',),
    ('Solomon Islands', 'Solomon Islands',),
    ('Somalia', 'Somalia',),
    ('South Africa', 'South Africa',),
    ('South Korea', 'South Korea',),
    ('Spain', 'Spain',),
    ('Sri Lanka', 'Sri Lanka',),
    ('Sudan', 'Sudan',),
    ('Suriname', 'Suriname',),
    ('Swaziland', 'Swaziland',),
    ('Sweden', 'Sweden',),
    ('Switzerland', 'Switzerland',),
    ('Syria', 'Syria',),
    ('Taiwan', 'Taiwan',),
    ('Tajikistan', 'Tajikistan',),
    ('Tanzania', 'Tanzania',),
    ('Thailand', 'Thailand',),
    ('Tunisia', 'Tunisia',),
    ('Turkey', 'Turkey',),
    ('Uganda', 'Uganda',),
    ('Ukraine', 'Ukraine',),
    ('United Arab Emirates', 'United Arab Emirates',),
    ('United Kingdom', 'United Kingdom',),
    ('United States', 'United States',),
    ('Uruguay', 'Uruguay',),

)
