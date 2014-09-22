comp-598-data-dictionary
========================

This dataset contains information about bills proposed in both the US House of Representatives and the Senate. It was assembled from GovTrack.us and may be freely used for any non-commercial application.

Size of the dataset:
220,484 bills from the 93rd Congressional session (1970s) to the present.
25,000 of these bills passed into law.

File Format:
CSV of integer values.
First line is a header with feature names.

Sample Line from the Dataset:
99,3,43,0,1,0,8,0,47,53,0,253,182,0,0

Features in the order they appear:
Congressional Session (99): The number of the United States Congress session. Can be correlated with a two-year period bracketed by elections.
Sponsor District (3): Integer representing the district from where the bill sponsor was elected. 
Committee (43): TODO
Sponsor Party (0): TODO
Sponsor Gender (1): Sex of the bill's sponsor with 1 representing female and 0 male.
Sponsor Role (0): TODO
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




