How To Compile the Dataset
1. Run download which will download all the bill data from govtrack.us in its own directory.
	- The resulting data directory looks like:
		[congress_number]
		---- bills
			---- [bill_folder]
				---- data.json
				---- data.xml
2. Run clean which will remove the date column and replace text values with proper discrete integers as defined by the data dictionary.
	- You may have to change the name of the file/data directory in this script.
	- Another file called subjects.csv will be produced. This will be used in a later step.
	- You may have to run -> sed -i 's/<< >>/<< >>/' data_file.csv again if there's still text values in the file (you can check by running grep [a-zA-Z] data_file.csv).
3. Run merge_congress_data.py (after making sure the file names point to the correct files).
4. Run merge_subjects.py (after making sure the file names point to the correct files) if you want the dataset to include subjects.

Help:  If you need help, contact Michael Noseworthy @ michael.noseworthy@mail.mcgill.ca.
