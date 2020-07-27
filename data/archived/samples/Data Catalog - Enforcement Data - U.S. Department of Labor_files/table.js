/* This notice must be untouched at all times.
Copyright (c) 2002-2008 Walter Zorn. All rights reserved.

wz_tooltip.js	 v. 5.31

The latest version is available at
http://www.walterzorn.com
or http://www.devira.com
or http://www.walterzorn.de

Created 1.12.2002 by Walter Zorn (Web: http://www.walterzorn.com )
Last modified: 7.11.2008

Easy-to-use cross-browser tooltips.
Just include the script at the beginning of the <body> section, and invoke
Tip('Tooltip text') to show and UnTip() to hide the tooltip, from the desired
HTML eventhandlers. Example:
<a onmouseover="Tip('Some text')" onmouseout="UnTip()" href="index.htm">My home page</a>
No container DIV required.
By default, width and height of tooltips are automatically adapted to content.
Is even capable of dynamically converting arbitrary HTML elements to tooltips
by calling TagToTip('ID_of_HTML_element_to_be_converted') instead of Tip(),
which means you can put important, search-engine-relevant stuff into tooltips.
Appearance & behaviour of tooltips can be individually configured
via commands passed to Tip() or TagToTip().

Tab Width: 4
LICENSE: LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License (LGPL) as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For more details on the GNU Lesser General Public License,
see http://www.gnu.org/copyleft/lesser.html
*/
    var arrayOfRolloverClasses = new Array();
	var arrayOfClickClasses = new Array();
	var activeRow = false;
	var activeRowClickArray = new Array();
	
	function highlightTableRow()
	{
		var tableObj = this.parentNode;
		if(tableObj.tagName!='TABLE')tableObj = tableObj.parentNode;

		if(this!=activeRow){
			this.setAttribute('origCl',this.className);
			this.origCl = this.className;
		}
		this.className = arrayOfRolloverClasses[tableObj.id];
		
		activeRow = this;
		
	}
	
	function clickOnTableRow()
	{
		var tableObj = this.parentNode;
		if(tableObj.tagName!='TABLE')tableObj = tableObj.parentNode;		
		
		if(activeRowClickArray[tableObj.id] && this!=activeRowClickArray[tableObj.id]){
			activeRowClickArray[tableObj.id].className='';
		}
		this.className = arrayOfClickClasses[tableObj.id];
		
		activeRowClickArray[tableObj.id] = this;
				
	}
	
	function resetRowStyle()
	{
		var tableObj = this.parentNode;
		if(tableObj.tagName!='TABLE')tableObj = tableObj.parentNode;

		if(activeRowClickArray[tableObj.id] && this==activeRowClickArray[tableObj.id]){
			this.className = arrayOfClickClasses[tableObj.id];
			return;	
		}
		
		var origCl = this.getAttribute('origCl');
		if(!origCl)origCl = this.origCl;
		this.className=origCl;
		
	}
		
	function addTableRolloverEffect(tableId,whichClass,whichClassOnClick)
	{
		arrayOfRolloverClasses[tableId] = whichClass;
		arrayOfClickClasses[tableId] = whichClassOnClick;
		
		var tableObj = document.getElementById(tableId);
		var tBody = tableObj.getElementsByTagName('TBODY');
		if(tBody){
			var rows = tBody[0].getElementsByTagName('TR');
		}else{
			var rows = tableObj.getElementsByTagName('TR');
		}
		for(var no=0;no<rows.length;no++){
			rows[no].onmouseover = highlightTableRow;
			rows[no].onmouseout = resetRowStyle;
			rows[no].onfocus = highlightTableRow;
			rows[no].onblur = resetRowStyle;
			
			if(whichClassOnClick){
				rows[no].onclick = clickOnTableRow;	
				rows[no].onkeypress = clickOnTableRow;	
			}
		}
		
	}