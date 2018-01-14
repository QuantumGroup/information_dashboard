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

| #  | Organization                                     | Feed          | URL                                                                           |                                                               
|--- | ---                                              | ---           | ---                                                                           |                                                       
| 1  | The New York Times (United States)               | world         | http://www.nytimes.com/services/xml/rss/nyt/World.xml                         |       
| 2  | The Washington Post (United States)              | world         | feed://feeds.washingtonpost.com/rss/world                                     |
| 3  | The Sydney Morning Herald (Australia)            | world         | http://www.smh.com.au/rssheadlines/world/article/rss.xml                      |
| 4  | The Daily Star (India)                           | world         | http://www.thedailystar.net/world/rss.xml                                     |    
| 5  | The Hindu (India)                                | world         | http://www.thehindu.com/news/international/?service=rss                       |
| 6  | The Times of India (India)                       | world         | http://timesofindia.indiatimes.com/rssfeeds/296589292.cms                     |
| 7  | Haaretz (Israel)                                 | world         | http://www.haaretz.com/cmlink/1.628765                                        |
| 8  | Haaretz (Israel)                                 | Middle East   | feed://www.haaretz.com/cmlink/1.798067                                        |
| 9  | Daily Nation (Kenya)                             | world         | feed://www.nation.co.ke/news/world/1068-1068-view-asFeed-hmfstbz/index.xml    |
| 10 | Daily Nation (Kenya)                             | Africa        | feed://www.nation.co.ke/news/africa/1066-1066-view-asFeed-15sj5pt/index.xml   |
| 11 | Yonhap (Korea, South)                            | all           | feed://english.yonhapnews.co.kr/RSS/headline.xml                              |
| 12 | Yonhap (Korea, South)                            | Korea, North  | feed://english.yonhapnews.co.kr/RSS/northkorea.xml                            |
| 13 | The Straits Times (Singapore)                    | Asia          | feed://www.straitstimes.com/news/asia/rss.xml                                 |
| 14 | Taipei Times (Taiwan)                            | world         | feed://www.taipeitimes.com/xml/world.rss                                      |
| 15 | BBC (United Kingdom)                             | Europe        | http://feeds.bbci.co.uk/news/world/europe/rss.xml                             |
| 16 | BBC (United Kingdom)                             | world         | http://feeds.bbci.co.uk/news/world/rss.xml                                    |
| 17 | The Christian Science Monitor (United States)    | world         | http://rss.csmonitor.com/feeds/world                                          |
| 18 | The Wall Street Journal (United States)          | world         | feed://www.wsj.com/xml/rss/3_7085.xml                                         |
| 19 | The Associated Press (United States)             | world         | feed://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5         |
| 20 | Reuters (United Kingdom)                         | world         | http://feeds.reuters.com/Reuters/worldNews                                    |
| 21 | The Los Angeles Times (United States)            | world         | feed://www.latimes.com/world/rss2.0.xml                                       |

### Financial markets

Market selection research is from Bloomberg Markets.

#### Stock Indexes

Information for list of indices by nation is from Bloomberg. Ticker data is from Yahoo Finance. Actual data for indices 
is from Alpha Vantage. 

|	Region	    |   	Country	    |	Market	                                |	Ticker	|In use?|
|	---	        |	---	            |	---	                                    |	---	    |	---	|
|	Americas	|		            |		                                    |		    |		|
|		        |	United States	|		                                    |		    |		|
|		        |		            |	NASDAQ TRANSPORTATION IX	            |	CTRN	|	x	|
|		        |	            	|	S&P 600 SMALLCAP INDEX	                |	SML	    |		|
|   	    	|	            	|	RUSSELL 2000 INDEX	                    |	RUT	    |	√	|
|	          	|	            	|	NASDAQ BIOTECH INDEX	                |	NBI	    |   	|
|		        |	            	|	DOW JONES INDUS. AVG	                |	DJI 	|	√	|
|   		    |	            	|	NASDAQ BANK INDEX	                    |	CBNK	|		|
|	    	    |	            	|	BBG NA REITS	                        |	BBREIT	|		|
|		        |	              	|	NYSE COMPOSITE INDEX	                |	NYA	    |		|
|   		    |	            	|	NASDAQ 100 STOCK INDX	                |	NDX	    |		|
|	    	    |		            |	NASDAQ OTHER FINANCIAL	                |	CFIN	|		|
|		        |	            	|	NASDAQ INSURANCE INDEX	                |	CINS	|		|
|   		    |           		|	DOW JONES TRANS. AVG	                |	TRAN	|		|
|	    	    |		            |	NASDAQ TELECOMM INDEX	                |	CUTL	|		|
|		        |	            	|	S&P 500 INDEX	                        |	SPX 	|	√	|
|		        |	            	|	NASDAQ COMPOSITE INDEX	                |	CCMP	|		|
|		        |	            	|	DOW JONES UTILITY AVG	                |	UTIL	|		|
|		        |	            	|	KBW BANK INDEX	                        |	BKX 	|		|
|		        |	            	|	RUSSELL 1000 INDEX	                    |	RIY	    |		|
|		        |	            	|	NASDAQ FINANCIAL INDEX	                |	NDF 	|		|
|		        |	            	|	RUSSELL 3000 INDEX	                    |	RAY	    |		|
|		        |	            	|	NASDAQ COMPUTER INDEX	                |	IXK	    |		|
|		        |		            |	NASDAQ INDUSTRIAL INDEX	                |	CIND	|		|
|		        |	Argentina	    |		                                    |		    |		|
|		        |		            |	ARGENTINA BURCAP INDEX	                |	BURCAP	|	√	|
|		        |		            |	M.AR MERVAL ARGENTINA IX	            |	MAR	    |		|
|		        |		            |	ARGENTINA MERVAL INDEX	                |	MERVAL	|		|
|		        |	Peru	        |		                                    |		    |		|
|		        |		            |	S&P/BVLLIMA25TRPEN	                    |	SPBL25PT|	x	|
|		        |		            |	S&P/BVLPeruGeneralTRPEN	                |	SPBLPGPT|	x	|
|		        |	Brazil	        |		                                    |		    |		|
|		        |		            |	BRAZIL IBrX INDEX	                    |	IBX	    |	x	|
|		        |		            |	BRAZIL IBOVESPA INDEX	                |	IBOV	|	x	|
|		        |	Mexico	        |		                                    |		    |		|
|		        |	            	|	S&P/BMV INMEX	                        |	INMEX	|	x	|
|		        |		            |	S&P/BMV IPC	                            |	MEXBOL	|	x	|
|		        |	Canada	        |		                                    |		    |		|
|		        |		            |	 S&P/TSX 60 INDEX	                    |	SPTSX60	|		|
|		        |		            |	S&P/TSX COMPOSITE INDEX	                |	SPTSX	|	x	|
|		        |	Chile	        |		                                    |		    |		|
|		        |		            |	CHILE STOCK MKT GENERAL	                |	IGPA	|	x	|
|		        |		            |	CHILE STOCK MKT SELECT	                |	IPSA	|		|
|		        |	Venezuela	    |		                                    |		    |		|
|		        |		            |	VENEZUELA STOCK MKT INDX	            |	IBVC	|	x	|
|		        |	Costa Rica	    |		                                    |		    |		|
|		        |		            |	BCT Corp Costa Rica Indx	            |	CRSMBCT	|	x	|
|		        |	Panama	        |		                                    |		    |		|
|		        |		            |	Bolsa de Panama General	                |	BVPSBVPS|	x	|
|		        |	Jamaica	        |		                                    |		    |		|
|		        |		            |	JSE MARKET INDEX	                    |	JMSMX	|		|
|		        |	Colombia	    |		                                    |		    |		|
|		        |		            |	COLOMBIA COLCAP INDEX	                |	COLCAP	|	x	|
|		        |	Bermuda	        |		                                    |		    |		|
|		        |		            |	BERMUDA STOCK EXCHANGE	                |	BSX	    |	x	|
|	EMEA	    |		            |		                                    |	    	|		|
|		        |	Europe	        |		                                    |		    |		|
|		        |		            |	S&P EURO INDEX	                        |	SPEU	|	x	|
|		        |		            |	Euro Stoxx 50 Pr	                    |	SX5E	|	√	|
|		        |		            |	BLOOMBERG EUROPEAN 500	                |	BE500	|	x	|
|		        |		            |	S&P EUROPE 350 INDEX	                |	SPEURO	|	x	|
|		        |		            |	FTSE ALL-SHARE INDEX	                |	ASX	    |		|
|		        |	United Kingdom	|		                                    |		    |		|
|		        |		            |	FTSE 100 INDEX	                        |	UKX	    |	√	|
|		        |		            |	FTSE AIM ALL SHARE INDEX	            |	AXX	    |		|
|		        |		            |	WIG30	                                |	WIG30	|		|
|		        |	Poland	        |		                                    |		    |		|
|		        |		            |	WSE WIG INDEX	                        |	WIG	    |	x	|
|		        |		            |	WIG 20	                                |	WIG20	|		|
|		        |	France	        |		                                    |		    |		|
|		        |		            |	CAC 40 INDEX	                        |	CAC	    |	x	|
|		        |		            |	CAC All-Tradable	                    |	SBF250	|		|
|		        |	Turkey      	|		                                    |		    |		|
|		        |		            |	BIST 30 Index	                        |	XU030	|	x	|
|		        |		            |	BIST 100 INDEX	                        |	XU100	|		|
|		        |	Bahrain	        |		                                    |		    |		|
|		        |		            |	BB ALL SHARE INDEX	                    |	BHSEASI	|	x	|
|		        |		            |	BB ESTERAD INDEX	                    |	BHSEEI	|		|
|		        |	Germany	        |		                                    |		    |		|
|		        |		            |	DAX INDEX	                            |	DAX	    |	x	|
|		        |		            |	HDAX INDEX	                            |	HDAX	|		|
|		        |	United Arab Emirates	    |		                        |		    |		|
|		        |		            |	ADX GENERAL INDEX	                    |	ADSMI	|		|
|		        |		            |	DFM GENERAL INDEX	                    |	DFMGI	|		|
|		        |	Greece	        |		                                    |		    |		|
|		        |		            |	FTSE/ASE Large Cap	                    |	FTASE	|		|
|		        |		            |	Athex Composite Share Pr	            |	ASE	    |		|
|		        |	Denmark	        |		                                    |		    |		|
|		        |		            |	OMX COPENHAGEN 20 INDEX	                |	KFX	    |		|
|		        |		            |	OMX COPENHAGEN INDEX	                |	KAX 	|		|
|		        |	South Africa	|		                                    |		    |		|
|		        |		            |	FTSE/JSE AFRICA ALL SHR	                |	JALSH	|		|
|		        |		            |	FTSE/JSE AFRICA TOP40 IX	            |	TOP40	|		|
|		        |	Finland	        |		                                    |		    |		|
|		        |		            |	OMX HELSINKI 25 INDEX	                |	HEX25	|		|
|		        |		            |	OMX HELSINKI INDEX	                    |	HEX	    |		|
|		        |	Kuwait	        |		                                    |		    |		|
|		        |		            |	KUWAIT SE PRICE INDEX	                |	KWSEIDX	|		|
|		        |		            |	KUWAIT SE WEIGHTED INDEX	            |	SECTMIND|		|
|		        |	Russia	        |		                                    |		    |		|
|		        |		            |	RUSSIAN RTS INDEX $	                    |	RTSI$	|		|
|		        |		            |	MOEX Russia Index	                    |	INDEXCF	|		|
|		        |	Ukraine	        |		                                    |		    |		|
|		        |		            |	Ukrainian Equities Index	            |	UX	    |		|
|		        |		            |	PFTS Index	                            |	PFTS	|		|
|		        |	Switzerland	    |		                                    |		    |		|
|		        |		            |	SWISS MARKET INDEX	                    |	SMI	    |		|
|		        |		            |	SPI SWISS PERFORMANCE IX	            |	SPI	    |		|
|		        |	Kenya	        |		                                    |		    |		|
|		        |		            |	Nairobi SE 20 Share	                    |	KNSMIDX	|		|
|		        |		            |	Nairobi All Share	                    |	NSEASI	|		|
|		        |	Serbia	        |		                                    |		    |		|
|		        |		            |	BELEXline Index 	                    |	BELEXLIN|		|
|		        |		            |	BELEX15 INDEX	                        |	BELEX15	|		|
|		        |	Norway	        |		                                    |		    |		|
|		        |		            |	OSE ALL SHARE INDEX	                    |	OSEAX	|		|
|		        |		            |	OSE BENCHMARK INDEX	                    |	OSEBX	|		|
|		        |	Hungary	        |		                                    |		    |		|
|		        |		            |	HUNGARIAN TRADED INDEX	                |	CHTX	|		|
|		        |		            |	BUDAPEST STOCK EXCH INDX	            |	BUX	    |		|
|		        |	Spain	        |		                                    |		    |		|
|		        |		            |	SPAIN MA  MADRID INDEX	                |	MADX    |		|
|		        |		            |	IBEX 35 INDEX	                        |	IBEX	|		|
|		        |	Netherlands	    |		                                    |		    |		|
|		        |		            |	AMSTERDAM MIDKAP INDEX	                |	AMX	    |		|
|		        |		            |	AEX-Index	                            |	AEX	    |		|
|		        |	Italy	        |		                                    |		    |		|
|		        |		            |	FTSE MIB INDEX	                        |	FTSEMIB	|		|
|		        |		            |	FTSE Italia All-Share	                |	ITLMS	|		|
|		        |	Bosnia & Herzegovina	|		                            |		    |		|
|		        |		            |	Bosnia BIRS Index	                    |	BIRS	|		|
|		        |		            |	SASE Free Market 10 Idx	                |	SASX10	|		|
|		        |	Belgium	        |		                                    |		    |		|
|		        |		            |	BELGIAN STK MRKT PRC IDX	            |	BELPRC	|		|
|		        |		            |	BEL 20 INDEX	                        |	BEL20	|		|
|		        |	Luxembourg	    |		                                    |		    |		|
|		        |		            |	LUXEMBOURG LuxX RETURN	                |	LUXXR	|		|
|		        |		            |	LUXEMBOURG LuxX INDEX	                |	LUXXX	|		|
|		        |	Portugal	    |		                                    |		    |		|
|		        |		            |	PSI All-Share Index GR	                |	BVLX	|		|
|		        |		            |	PSI 20 INDEX	                        |	PSI20	|		|
|		        |	Israel	        |		                                    |		    |		|
|		        |		            |	TA-125 Index	                        |	TA-125	|	x	|
|		        |		            |	TA-35 Index	                            |	TA-35	|		|
|		        |	Macedonia	    |		                                    |		    |		|
|		        |		            |	MBID Index	                            |	MBIDM	|		|
|		        |		            |	MBI 10 Index	                        |	MBI	    |		|
|		        |	Austria	        |		                                    |		    |		|
|		        |		            |	AUSTRIAN ATX PRIME INDEX	            |	ATXPRIME|		|
|		        |		            |	AUSTRIAN TRADED ATX INDX	            |	ATX	    |		|
|		        |	Sweden	        |		                                    |		    |		|
|		        |		            |	OMX STOCKHOLM BENCHMARK	                |	SBX	    |   	|
|		        |		            |	OMX STOCKHOLM 30 INDEX	                |	OMX	    |		|
|		        |	Tunisia	        |		                                    |		    |		|
|		        |		            |	Tunis SE TUNINDEX	                    |	TUSISE	|		|
|		        |	Montenegro	    |		                                    |		    |		|
|		        |		            |	MONEX INDEX	                            |	MONEX	|		|
|		        |	Saudi Arabia	|		                                    |		    |		|
|		        |		            |	TADAWUL ALL SHARE INDEX	                |	SASEIDX	|		|
|		        |	Botswana	    |		                                    |		    |		|
|		        |		            |	Botswana Gaborone Dom	                |	BGSMDC	|		|
|		        |	Qatar	        |		                                    |		    |		|
|		        |		            |	QE Index	                            |	DSM	    |		|
|		        |	Jordan	        |		                                    |		    |		|
|		        |		            |	AMMAN SE GENERAL INDEX	                |	JOSMGNFF|		|
|		        |	Slovenia	    |		                                    |	    	|		|
|		        |		            |	Slovenian Blue Chip Idx	                |	SBITOP	|		|
|		        |	Palestine	    |		                                    |		    |		|
|		        |		            |	PSE Al Quds	                            |	PASISI	|		|
|		        |	Nigeria 	    |		                                    |		    |		|
|		        |		            |	NIGERIA STCK EXC ALL SHR	            |	NGSEINDX|		|
|		        |	Iceland	        |		                                    |		    |		|
|		        |		            |	OMX Iceland All-Share PR	            |	ICEXI	|		|
|		        |	Namibia	        |		                                    |		    |		|
|		        |		            |	NAMIBIA OVERALL INDEX	                |	FTN098	|		|
|		        |	Cyprus	        |		                                    |		    |		|
|		        |		            |	GENERAL MARKET INDEX CSE	            |	CYSMMAPA|		|
|		        |	Lebanon	        |		                                    |		    |		|
|		        |		            |	BLOM STOCK INDEX	                    |	BLOM	|		|
|		        |	Oman	        |		                                    |		    |		|
|		        |		            |	MSM30 Index	                            |	MSM30	|		|
|		        |	Mauritius	    |		                                    |		    |		|
|		        |		            |	MAURITIUS STOCK EXCHANGE	            |	SEMDEX	|		|
|		        |	Ireland	        |		                                    |		    |		|
|		        |		            |	IRISH OVERALL INDEX	                    |	ISEQ	|		|
|		        |	Slovakia	    |		                                    |		    |		|
|		        |		            |	SLOVAK SHARE INDEX	                    |	SKSM	|		|
|		        |	Croatia	        |		                                    |		    |		|
|		        |		            |	CROATIA ZAGREB CROBEX	                |	CRO	    |		|
|		        |	Morocco	        |		                                    |		    |		|
|		        |		            |	MASI Free Float Index	                |	MOSENEW	|		|
|		        |	Tanzania	    |		                                    |	    	|		|
|		        |		            |	Tanzania All Share Index	            |	DARSDSEI|		|
|		        |	Bulgaria	    |		                                    |		    |		|
|		        |		            |	SOFIX INDEX	                            |	SOFIX	|		|
|		        |	Malta	        |		                                    |		    |		|
|		        |		            |	MALTA STOCK EXCHANGE IND	            |	MALTEX	|		|
|		        |	Latvia	        |		                                    |		    |		|
|		        |		            |	OMX RIGA OMXR	                        |	RIGSE	|		|
|		        |	Estonia	        |		                                    |		    |		|
|		        |		            |	OMX TALLINN OMXT	                    |	TALSE	|		|
|		        |	United States	|		                                    |		    |		|
|		        |		            |	BBG EMEA WORLD INDEX	                |	BWORLDEU|		|
|		        |	Kazakhstan	    |		                                    |		    |		|
|		        |		            |	Kazakhstan KASE Stock Ex	            |	KZKAK	|		|
|		        |	Romania	        |		                                    |		    |		|
|		        |		            |	BUCHAREST BET INDEX	                    |	BET	    |		|
|		        |	Lithuania	    |		                                    |		    |		|
|		        |		            |	OMX VILNIUS OMXV	                    |	VILSE	|		|
|		        |	Ghana	        |		                                    |		    |		|
|		        |       		    |	GSE Composite Index	                    |	GGSECI	|		|
|		        |	Czech Republic	|		                                    |		    |		|
|		        |		            |	PRAGUE STOCK EXCH INDEX	                |	PX	    |		|
|	APAC	    |		            |		                                    |		    |		|
|		        |	Japan	        |		                                    |		    |		|
|		        |		            |	TOPIX LARGE 70 IDX (TSE)	            |	TPXL70	|		|
|		        |		            |	TSE2 TOPIX 2ND SECT INDX	            |	TSE2	|		|
|		        |		            |	NIKKEI JASDAQ	                        |	NKYJQ	|		|
|       		|		            |	TOPIX MID 400 INDX (TSE)	            |	TPXM400	|		|
|       		|		            |	TOPIX SMALL INDEX (TSE)	                |	TPXSM	|		|
|       		|		            |	TSE MOTHERS INDEX	                    |	TSEMOTHR|		|
|       		|		            |	TOPIX CORE 30 IDX (TSE)	                |	TPXC30	|		|
|       		|		            |	JASDAQ: STOCK INDEX	                    |	JSDA	|		|
|       		|		            |	TSE REIT INDEX	                        |	TSEREIT	|		|
|	        	|		            |	NIKKEI 300 INDEX	                    |	NEY	    |		|
|	        	|		            |	TOPIX INDEX (TOKYO)	                    |	TPX	    |		|
|	        	|		            |	NIKKEI 500	                            |	NKY500  |		|
|	        	|		            |	NIKKEI 225	                            |	NKY	    |	x	|
|	        	|		            |	TOPIX 100 INDEX (TSE)	                |	TPX100	|		|
|	        	|		            |	TOPIX 500 INDEX (TSE)	                |	TPX500	|		|
|	        	|	China	        |		                                    |		    |		|
|	        	|		            |	SHENZHEN SE COMPOSITE IX	            |	SZCOMP	|		|
|	        	|	            	|	CSI 300 INDEX	                        |	SHSZ300	|		|
|	        	|	            	|	ChiNext Price Index	                    |	SZ399006|		|
|	        	|	            	|	SHANGHAI G-SHARES	                    |	SHNCOMP	|		|
|	        	|	            	|	SHANGHAI SE 180 A SHR IX	            |	SSE180	|		|
|	        	|	            	|	SSE 50 Index	                        |	SSE50	|		|
|	        	|	            	|	SHENZHEN SE B SHARE INDX	            |	SZBSHR	|		|
|	           	|	            	|	SHANGHAI SE B SHARE INDX	            |	SHBSHR	|		|
|		        |	            	|	SZSE COMPONENT INDEX	                |	SICOM	|		|
|		        |	            	|	SHENZHEN SE A SHARE INDX	            |	SZASHR	|		|
|	        	|	            	|	SHANGHAI SE A SHARE INDX	            |	SHASHR  |		|
|		        |	            	|	SHANGHAI SE COMPOSITE	                |	SHCOMP	|		|
|		        |	Hong Kong	    |		                                    |		    |		|
|		        |	            	|	HANG SENG COMPOSITE INDX	            |	HSCI	|		|
|		        |	            	|	HANG SENG CHINA AFF.CRP	                |	HSCCI	|		|
|		        |	            	|	HANG SENG HK 35 INDEX	                |	HSHK35	|		|
|	        	|	            	|	HANG SENG CHINA ENT INDX	            |	HSCEI	|		|
|	        	|	            	|	HANG SENG INDEX	                        |	HIS	    |		|
|	        	|	            	|	S&P/HKEx LargeCap Index	                |	HKSPLC25|		|
|	        	|		            |	HS China (HK-listed) 25	                |	HSFML25	|		|
|	        	|		            |	S&P ASIA 50 INDEX CME	                |	SAXCME	|		|
|	        	|		            |	S&P/HKEx GEM Index	                    | 	HKSPGEM	|		|
|	        	|		            |	HANG SENG H-FINANCIALS	                |	H-FIN	|		|
|	        	|		            |	 HS China (HK-listed) 100	            |	H-FIN	|		|
|	        	|	South Korea	    |		                                    |		    |		|
|	        	|		            |	KOREA KOSPI 100 INDEX	                |	KOSPI100|		|
|	        	|		            |	KOSDAQ STAR INDEX	                    |	KOSTAR	|		|
|	        	|		            |	KOREA KOSPI 50 INDEX	                |	KOSPI50	|		|
|	        	|		            |	KOSPI 200 INDEX	                        |	KOSPI2	|		|
|	          	|		            |	KOSPI INDEX	                            |	KOSPI	|		|
|	        	|		            |	KRX 100 INDEX	                        |	KRX100	|		|
|		        |		            |	KOSDAQ INDEX	                        |	KOSDAQ	|		|
|		        |	India	        |		                                    |		    |		|
|	        	|		            |	S&P BSE 200 IDX	                        |	BSE200	|		|
|	        	|		            |	S&P BSE 500 IDX	                        |	BSE500	|		|
|	        	|		            |	Nifty 50	                            |	NIFTY   |		|
|		        |		            |	S&P BSE SENSEX INDEX	                |	SENSEX	|	√	|
|		        |		            |	S&P BSE 100 IDX	                        |	BSE100	|		|
|		        |	New Zealand	    |		                                    |		    |		|
|	        	|		            |	S&P/NZX 10 Index	                    |	NZSE10	|		|
|	            |		            |	S&P/NZX 50 Index Gross	                |	NZSE50FG|		|
|	        	|		            |	S&P NZX All Index	                    |	NZSE	|		|
|	        	|		            |	S&P/NZX 20 Index	                    |	NZX20	|		|
|	        	|	Taiwan	        |		                                    |		    |		|
|		        |		            |	TAIWAN TPEx EXCHANGE	                |	TWOTCI	|		|
|	        	|		            |	FTSE TWSE Taiwan 50 Indx	            |	TW50	|		|
|		        |		            |	TAIWAN TAIEX INDEX	                    |	TWSE	|		|
|		        |	Australia	    |		                                    |		    |		|
|	        	|		            |	ALL ORDINARIES INDX	                    |	AS30	|		|
|		        |		            |	S&P/ASX 300 INDEX	                    |	AS52	|		|
|		        |		            |	S&P/ASX 200 INDEX	                    |	AS51	|		|
|		        |	Pakistan	    |		                                    |		    |		|
|	        	|		            |	KARACHI ALL SHARE INDEX	                |	KSE	    |		|
|		        |		            |	KARACHI 30 INDEX	                    |	KSE30	|		|
|	        	|	        	    |	KARACHI 100 INDEX	                    |	KSE100	|		|
|		        |	Malaysia	    |		                                    |		    |		|
|		        |		            |	FTSE BURSA MALAYSIA EMAS	            |	FBMEMAS	|		|
|		        |		            |	FTSE Bursa Malaysia KLCI	            |	FBMKLCI	|		|
|		        |	Indonesia	    |		                                    |		    |		|
|		        |		            |	JAKARTA LQ-45 INDEX	                    |	LQ45	|		|
|		        |		            |	JAKARTA COMPOSITE INDEX	                |	JCI	    |		|
|		        |	Singapore	    |		                                    |		    |		|
|		        |		            |	FTSE ST ALL SHARE INDEX	                |	FSTAS	|		|
|		        |		            |	Straits Times Index STI	                |	STI	    |		|
|		        |	Thailand	    |		                                    |		    |		|
|		        |		            |	STOCK EXCH OF THAI INDEX	            |	SET	    |		|
|		        |		            |	THAI SET 50 INDEX	                    |	SET50	|		|
|		        |	Vietnam	        |		                                    |		    |		|
|		        |		            |	HO CHI MINH STOCK INDEX	                |	VNINDEX	|		|
|		        |		            |	HNX INDEX	                            |	VHINDEX	|		|
|		        |	Bengladesh  	|		                                    |		    |		|
|		        |	              	|	DSE Broad Index	                        |	DSEX	|		|
|		        |	Mongolia	    |		                                    |		    |		|
|		        |	            	|	MSE Top 20 Index	                    |	MSETOP	|		|
|		        |	Asia	        |		                                    |		    |		|
|		        |	            	|	MSCI ASIA APEX 50	                    |	MXAPEXA |		|
|		        |	Laos        	|		                                    |		    |		|
|		        |		            |	Laos Composite Index	                |	LSXC	|		|
|		        |	Phillipines	    |		                                    |		    |		|
|		        |		            |	PSEi - PHILIPPINE SE IDX	            |	PCOMP	|		|
|		        |	Sri Lanka	    |		                                    |		    |		|
|		        |		            |	SRI LANKA COLOMBO ALL SH	            |	CSEALL  |		|
 
 
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