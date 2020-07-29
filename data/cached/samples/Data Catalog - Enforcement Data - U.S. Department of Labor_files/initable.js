
/*
Data table design initialization

Important: 	1) Added <script type="text/javascript" src="js/initTable.js"></script> at footer.php 
			2) Data table ID must be "ogdbTable". Otherwise, update variable "tableID"

What this does: 	1) Checks if table exist, then updates alternative rows with class name: "even" and "odd"

2/25/2011 by AT

Version 1.0	
*/

/* You can change these values */
var tableID = "ogdbTable";

alternateRows(tableID);

/* This is the working function */
function alternateRows(tableID) {
//	alert("Alternate Processing...");
	// Take object table and get all it's tbodies.
	var table = document.getElementById(tableID);
	if (table == null) return;
	var tableBodies = table.getElementsByTagName("tbody");
	// Loop through these tbodies
	for (var i = 0; i < tableBodies.length; i++) {
		// Take the tbody, and get all it's rows
		var tableRows = tableBodies[i].getElementsByTagName("tr");
		// Loop through these rows
		// Start at 1 because we want to leave the heading row untouched
		for (var j = 0; j < tableRows.length; j++) {
			// Check if j is even, and apply classes for both possible results
			if ( (j % 2) == 0  ) {
				if ( !(tableRows[j].className.indexOf('odd') == -1) ) {
					tableRows[j].className = tableRows[j].className.replace('odd', 'even');
				} else {
					if ( tableRows[j].className.indexOf('even') == -1 ) {
						//tableRows[j].className += " even";
						addClass(tableRows[j],"even");
					}
				}
			} else {
				if ( !(tableRows[j].className.indexOf('even') == -1) ) {
					tableRows[j].className = tableRows[j].className.replace('even', 'odd');
				} else {
					if ( tableRows[j].className.indexOf('odd') == -1 ) {
						//tableRows[j].className += " odd";
						addClass(tableRows[j],"odd");
					}
				}
			} 
		}
	}
}