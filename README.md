comp-598-data-dictionary
========================

This dataset contains information about bills proposed in both the US House of Representatives and the Senate. It was assembled from GovTrack.us and may be freely used for any non-commercial application.

##Size of the dataset:
220,484 bills from the 93rd Congressional session (1970s) to the present.
25,000 of these bills passed into law.

##File Format:
CSV of integer values.
First line is a header with feature names.

##Sample Line from the Dataset:
99,3,43,0,1,0,8,0,47,53,0,253,182,0,0

##Features in the order they appear:

Congressional Session (99): The number of the United States Congress session. Can be correlated with a two-year period bracketed by elections.

Sponsor District (3): Integer representing the district from where the bill sponsor was elected. 

Committee (43): Integer representing the first committee the bill was sent to. 
        - SPAG: 1       SSAF: 2         SSAP: 3         SSAS: 4         SSBK: 5 
          SSBU: 6       SSCM: 7         SSEG: 8         SSEV: 9         SLET: 11 
          SSFI: 12      SSFR: 13        SSFR: 14        SSGA: 15        SLIA: 16 
          SLIN: 17      SSJU: 18        SSRA: 19        SSSB: 20        SCNC: 21 
          SSVA: 22      HSAG: 23        HSAP: 24        HSAS: 25        HSBU: 26 
          HSED: 27      HSIF: 28        HSSO: 29        HLZI: 30        HSBA: 31 
          HSFA: 32      HSHM: 33        HSHA: 34        HLIG: 35        HSJU: 36
          HSII: 37      HSGO: 38        HSRU: 39        HSSY: 40        HSSM: 41 
          HSPW: 42      HSVR: 43        HSWM: 44	
	- For a detailed list of committee names, please visit: https://www.govtrack.us/congress/committees/

Sponsor Party (0): Integer representing which party the sponsor belongs to.
	- Democrat: 0
	- Republican: 1
	- Independent: 2
	- New Progressive: 3
	- Liberal: 4
	- Conservative: 5
	- Farmer Labor: 6

Sponsor Gender (1): Sex of the bill's sponsor with 1 representing female and 0 male.

Sponsor Role (0): Integer representing whether the sponsor is a senator (1) or representative (1).

Cosponsors (8): Number of cosponsors signed on to the bill.

Number of Democratic Cosponsors (0): Of the cosponsors, the number from the Democratic Party.

Number of Democrats in the Senate (47): Total number of Democrats in the Senate.

Number of Republicans in the Senate (53): Total number of Republicans in the Senate.

Number of Independents in the Senate (0): Total number of Independents in the Senate.

Number of Democrats in the House (253): Total number of voting Democrats in the House of Representatives.

Number of Republicans in the House (182): Total number of voting Republicans in the House of Representatives.

Number of Independents in the House (0): Total number of voting Independents in the House of Representatives.

Whether the bill became law (0): The final outcome of the bill where 1 indicates passage and 0 shows failure to be enacted.

NB. All Senate and House totals refer to the start of the Congressional session and do not include non-voting delegates, such as the one from the District of Columbia.




