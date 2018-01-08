# Batch Inputs

This directory contains the scripts that download non-real-time data: economic (non-financial), political, demographic, 
and other such data. 

## Source types

### News organizations

These include national papers of record and global news wires. 

### Financial markets

These include stock and stock futures markets, stock markets by industry sectors, commodities markets, currency markets, 
and fixed income markets.
 
### Health hazard indicators

These include infectious disease outbreaks and other related hazards such as famine.

### Country economic indicators

Economic indicators include national financial markets, GDP statistics, inflation, import and export figures, and other 
such information.

### Country political indicators

Political indicators include regime type, election information, human development indices and other such information.

### Country demographic indicators

Demographic indicators include total population and population breakdowns, birth and death rates, GDP per capita, and 
other such information.

## Sources

### News organizations

| #  | Organization                         | Feed      | URL                                                                           |                                                               
|--- | ---                                  | ---       | ---                                                                           |                                                       
| 1  | The New York Times (United States)   | world     | http://www.nytimes.com/services/xml/rss/nyt/World.xml                         |       
| 2  | The Washington Post (United States)  | world     | feed://feeds.washingtonpost.com/rss/world                                     |
| 3  | The Sydney Morning Herald (Australia)| world     | http://www.smh.com.au/rssheadlines/world/article/rss.xml                      |
| 4  | The Daily Star (India)               | world     | http://www.thedailystar.net/world/rss.xml                                     |    
| 5  | The Hindu (India)                    | world     | http://www.thehindu.com/news/international/?service=rss                       |
| 6  | The Times of India (India)           | world     | http://timesofindia.indiatimes.com/rssfeeds/296589292.cms                     |
| 7  | Haaretz (Israel)                     | world     | http://www.haaretz.com/cmlink/1.628765                                        |
| 8  | Haaretz (Israel)                     | Middle East  | feed://www.haaretz.com/cmlink/1.798067                                     |
| 9  | Daily Nation (Kenya)                 | world     | feed://www.nation.co.ke/news/world/1068-1068-view-asFeed-hmfstbz/index.xml    |
| 10 | Daily Nation (Kenya)                 | Africa    | feed://www.nation.co.ke/news/africa/1066-1066-view-asFeed-15sj5pt/index.xml   |
| 11 | Yonhap (Korea, South)                | all       | feed://english.yonhapnews.co.kr/RSS/headline.xml                              |
| 12 | Yonhap (Korea, South)                | Korea, North  | feed://english.yonhapnews.co.kr/RSS/northkorea.xml                        |
| 13 | The Straits Times (Singapore)        | Asia      | feed://www.straitstimes.com/news/asia/rss.xml                                 |
| 14 | Taipei Times (Taiwan)                | world     | feed://www.taipeitimes.com/xml/world.rss                                      |
| 15 | BBC (United Kingdom)                 | Europe    | http://feeds.bbci.co.uk/news/world/europe/rss.xml                             |
| 16 | BBC (United Kingdom)                 | world     | http://feeds.bbci.co.uk/news/world/rss.xml                                    |
| 17 | The Christian Science Monitor (United States)    | world | http://rss.csmonitor.com/feeds/world                                  |
| 18 | The Wall Street Journal (United States)          | world | feed://www.wsj.com/xml/rss/3_7085.xml                                 |
| 19 | The Associated Press (United States) | world | feed://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5             |
| 20 | Reuters (United Kingdom)             | world | http://feeds.reuters.com/Reuters/worldNews                                        |
| 21 | The Los Angeles Times (United States)| world | feed://www.latimes.com/world/rss2.0.xml                                           |

### Financial markets

Market selection research is from Bloomberg Markets.

#### Stocks

Region	    |	Country	        |	Market	                    |   In Use?
---	        |	---	            |	---	                        |   ---
Americas	|		            |		                        |
	        |	United States	|		                        |
	        |		            |	NASDAQ TRANSPORTATION IX	|
        	|		            |	S&P 600 SMALLCAP INDEX	    |
	        |		            |	RUSSELL 2000 INDEX"         |
	        |		            |	NASDAQ BIOTECH INDEX	    |
	        |		            |	DOW JONES INDUS. AVG	    |
	        |		            |	NASDAQ BANK INDEX           |
	        |		            |	BBG NA REITS	            |
	        |		            |	NYSE COMPOSITE INDEX	    |
	        |		            |	NASDAQ 100 STOCK INDX	    |
	        |		            |	NASDAQ OTHER FINANCIAL	    |
	        |		            |	NASDAQ INSURANCE INDEX	    |
	        |		            |	DOW JONES TRANS. AVG	    |
	        |		            |	NASDAQ TELECOMM INDEX	    |
	        |		            |	S&P 500 INDEX	            |
	        |		            |	NASDAQ COMPOSITE INDEX	    |
	        |		            |	DOW JONES UTILITY AVG	    |
	        |		            |	KBW BANK INDEX	            |
	        |		            |	RUSSELL 1000 INDEX	        |
	        |		            |	NASDAQ FINANCIAL INDEX	    |
	        |		            |	RUSSELL 3000 INDEX	        |
	        |		            |	NASDAQ COMPUTER INDEX	    |
	        |		            |	NASDAQ INDUSTRIAL INDEX	    |
	        |	Argentina	    |		                        |
	        |		            |	ARGENTINA BURCAP INDEX	    |
	        |		            |	M.AR MERVAL ARGENTINA IX	|
	        |		            |	ARGENTINA MERVAL INDEX	    |
	        |	Peru	        |		                        |
	        |		            |	S&P/BVLLIMA25TRPEN	        |
	        |		            |	S&P/BVLPeruGeneralTRPEN	    |
	        |	Brazil	        |		                        |
	        |		            |	BRAZIL IBrX INDEX	        |
	        |		            |	BRAZIL IBOVESPA INDEX	    |
	        |	Mexico	        |		                        |
	        |		            |	S&P/BMV INMEX	            |
	        |		            |	S&P/BMV IPC	                |
	        |	Canada	        |		                        |
	        |		            |	 S&P/TSX 60 INDEX	        |
	        |		            |	S&P/TSX COMPOSITE INDEX	    |
	        |	Chile	        |		                        |
	        |		            |	CHILE STOCK MKT GENERAL	    |
	        |		            |	CHILE STOCK MKT SELECT	    |
	        |	Venezulea	    |		                        |
	        |		            |	VENEZUELA STOCK MKT INDX	|
	        |	Costa Rica	    |		                        |
	        |		            |	BCT Corp Costa Rica Indx	|
	        |	Panama	        |		                        |
	        |		            |	Bolsa de Panama General	    |
	        |	Jamaica	        |		                        |
	        |		            |	JSE MARKET INDEX	        |
	        |	Colombia	    |		                        |
	        |		            |	COLOMBIA COLCAP INDEX	    |
	        |	Bermuda	        |		                        |
	        |		            |	BERMUDA STOCK EXCHANGE	    |
 
 Market data is from Alpha Vantage.
 
 #### Currencies
 
 currency code	|	currency name	|
---	|	---	|
AED	|	United Arab Emirates Dirham	|
AFN	|	Afghan Afghani	|
ALL	|	Albanian Lek	|
AMD	|	Armenian Dram	|
ANG	|	Netherlands Antillean Guilder	|
AOA	|	Angolan Kwanza	|
ARS	|	Argentine Peso	|
AUD	|	Australian Dollar	|
AWG	|	Aruban Florin	|
AZN	|	Azerbaijani Manat	|
BAM	|	Bosnia-Herzegovina Convertible Mark	|
BBD	|	Barbadian Dollar	|
BDT	|	Bangladeshi Taka	|
BGN	|	Bulgarian Lev	|
BHD	|	Bahraini Dinar	|
BIF	|	Burundian Franc	|
BITGOLD	|	BitGOLD	|
BMD	|	Bermudan Dollar	|
BND	|	Brunei Dollar	|
BOB	|	Bolivian Boliviano	|
BRL	|	Brazilian Real	|
BSD	|	Bahamian Dollar	|
BTN	|	Bhutanese Ngultrum	|
BWP	|	Botswanan Pula	|
BYR	|	Belarusian Ruble (pre-2016)	|
BZD	|	Belize Dollar	|
CAD	|	Canadian Dollar	|
CDF	|	Congolese Franc	|
CHF	|	Swiss Franc	|
CLF	|	Chilean Unit of Account (UF)	|
CLP	|	Chilean Peso	|
CNY	|	Chinese Yuan	|
COP	|	Colombian Peso	|
CRC	|	Costa Rican Colon	|
CUP	|	Cuban Peso	|
CVE	|	Cape Verdean Escudo	|
CZK	|	Czech Republic Koruna	|
DJF	|	Djiboutian Franc	|
DKK	|	Danish Krone	|
DOP	|	Dominican Peso	|
DZD	|	Algerian Dinar	|
EEK	|	Estonian Kroon	|
EGP	|	Egyptian Pound	|
ERN	|	Eritrean Nakfa	|
ETB	|	Ethiopian Birr	|
EUR	|	Euro	|
FJD	|	Fijian Dollar	|
FKP	|	Falkland Islands Pound	|
GBP	|	British Pound Sterling	|
GEL	|	Georgian Lari	|
GHS	|	Ghanaian Cedi	|
GIP	|	Gibraltar Pound	|
GMD	|	Gambian Dalasi	|
GNF	|	Guinean Franc	|
GTQ	|	Guatemalan Quetzal	|
GYD	|	Guyanaese Dollar	|
HKD	|	Hong Kong Dollar	|
HNL	|	Honduran Lempira	|
HRK	|	Croatian Kuna	|
HTG	|	Haitian Gourde	|
HUF	|	Hungarian Forint	|
IDR	|	Indonesian Rupiah	|
ILS	|	Israeli New Sheqel	|
INR	|	Indian Rupee	|
IQD	|	Iraqi Dinar	|
IRR	|	Iranian Rial	|
ISK	|	Icelandic Krona	|
JEP	|	Jersey Pound	|
JMD	|	Jamaican Dollar	|
JOD	|	Jordanian Dinar	|
JPY	|	Japanese Yen	|
KES	|	Kenyan Shilling	|
KGS	|	Kyrgystani Som	|
KHR	|	Cambodian Riel	|
KMF	|	Comorian Franc	|
KPW	|	North Korean Won	|
KRW	|	South Korean Won	|
KWD	|	Kuwaiti Dinar	|
KYD	|	Cayman Islands Dollar	|
KZT	|	Kazakhstani Tenge	|
LAK	|	Laotian Kip	|
LBP	|	Lebanese Pound	|
LKR	|	Sri Lankan Rupee	|
LRD	|	Liberian Dollar	|
LSL	|	Lesotho Loti	|
LTL	|	Lithuanian Litas	|
LVL	|	Latvian Lats	|
LYD	|	Libyan Dinar	|
MAD	|	Moroccan Dirham	|
MDL	|	Moldovan Leu	|
MGA	|	Malagasy Ariary	|
MKD	|	Macedonian Denar	|
MMK	|	Myanma Kyat	|
MNT	|	Mongolian Tugrik	|
MOP	|	Macanese Pataca	|
MRO	|	Mauritanian Ouguiya	|
MTL	|	Maltese Lira	|
MUR	|	Mauritian Rupee	|
MVR	|	Maldivian Rufiyaa	|
MWK	|	Malawian Kwacha	|
MXN	|	Mexican Peso	|
MZN	|	Mozambican Metical	|
NAD	|	Namibian Dollar	|
NGN	|	Nigerian Naira	|
NIO	|	Nicaraguan Cordoba	|
NOK	|	Norwegian Krone	|
NPR	|	Nepalese Rupee	|
NZD	|	New Zealand Dollar	|
OMR	|	Omani Rial	|
PAB	|	Panamanian Balboa	|
PEN	|	Peruvian Nuevo Sol	|
PGK	|	Papua New Guinean Kina	|
PHP	|	Philippine Peso	|
PKR	|	Pakistani Rupee	|
PLN	|	Polish Zloty	|
PYG	|	Paraguayan Guarani	|
QAR	|	Qatari Rial	|
RON	|	Romanian Leu	|
RSD	|	Serbian Dinar	|
RUB	|	Russian Ruble	|
RUR	|	Old Russian Ruble	|
RWF	|	Rwandan Franc	|
SAR	|	Saudi Riyal	|
SBDf	|	Solomon Islands Dollar	|
SCR	|	Seychellois Rupee	|
SDG	|	Sudanese Pound	|
SEK	|	Swedish Krona	|
SGD	|	Singapore Dollar	|
SHP	|	Saint Helena Pound	|
SLL	|	Sierra Leonean Leone	|
SOS	|	Somali Shilling	|
SRD	|	Surinamese Dollar	|
STD	|	Sao Tome and Principe Dobra	|
SVC	|	Salvadoran Colon	|
SYP	|	Syrian Pound	|
SZL	|	Swazi Lilangeni	|
THB	|	Thai Baht	|
TJS	|	Tajikistani Somoni	|
TMT	|	Turkmenistani Manat	|
TND	|	Tunisian Dinar	|
TOP	|	Tongan Pa'anga	|
TRY	|	Turkish Lira	|
TTD	|	Trinidad and Tobago Dollar	|
TWD	|	New Taiwan Dollar	|
TZS	|	Tanzanian Shilling	|
UAH	|	Ukrainian Hryvnia	|
UGX	|	Ugandan Shilling	|
USD	|	United States Dollar	|
USDE	|	USDe	|
UYU	|	Uruguayan Peso	|
UZS	|	Uzbekistan Som	|
VEF	|	Venezuelan Bolivar Fuerte	|
VND	|	Vietnamese Dong	|
VUV	|	Vanuatu Vatu	|
WST	|	Samoan Tala	|
XAF	|	CFA Franc BEAC	|
XAG	|	Silver Ounce	|
XAU	|	Gold Ounce	|
XCD	|	East Caribbean Dollar	|
XDR	|	Special Drawing Rights	|
XOF	|	CFA Franc BCEAO	|
XPF	|	CFP Franc	|
YER	|	Yemeni Rial	|
ZAR	|	South African Rand	|
ZMK	|	Zambian Kwacha (pre-2013)	|
ZMW	|	Zambian Kwacha	|
ZWL	|	Zimbabwean Dollar	|
 
### Health hazard indicators