// AJAX Helper
//So I have to have the AJAX commands in a logical grouping
function AjaxHelper(){
}

AjaxHelper.prototype.createAjaxRequest = function(dname, doSynchronous, asyncHandler)
{
	
  if (window.XMLHttpRequest){ xhttp=new XMLHttpRequest(); }else{ xhttp=new ActiveXObject("Microsoft.XMLHTTP"); }
  if (asyncHandler != null){ xhttp.onreadystatechange = asyncHandler; }
  xhttp.open("GET",dname,!doSynchronous);
  return xhttp;
}
AjaxHelper.prototype.xml2string = function(xmlDom){ var strs = null; var doc = xmlDom.documentElement; if(doc.xml == undefined){ strs = (new XMLSerializer()).serializeToString(xmlDom); }else strs = doc.xml; return strs; }

AjaxHelper.prototype.requestIsReadyAndValid = function(xmlRequest, showProblem){
	if (typeof(xmlRequest) == 'undefined' || xmlRequest == null || typeof(xmlRequest.readyState) == 'undefined'){
		if (showProblem) alert("something is undefined, xmlRequest:"+xmlRequest);
		return false;
	}
	if (xmlRequest.readyState != 4){ if (showProblem) alert("isn't ready:"+xmlRequest.readyState); return false; }
	if (xmlRequest.status != 200){ if (showProblem) alert("isn't good status:"+xmlRequest.status); return false; }
	return true;
}

AjaxHelper.prototype.setContent = function(xml,xsl,baseElement, postProcessHtmlFunction){
	if (window.ActiveXObject){
		var ex = xml.transformNode(xsl);
                
		ex = this.fixAmpersands(ex);
		if (baseElement == null) return;
		this.removeAllChildren(baseElement);
		if (typeof(postProcessHtmlFunction) == 'function') ex = postProcessHtmlFunction(ex);
		baseElement.innerHTML=ex;
		//setting the innerHTML does NOT trigger scripts to run that are inside the html.  
		//So let's find them, extract and execute them
		var scriptElements = this.returnElementsOfType("script",baseElement);
		for (var i = 0; i < scriptElements.length; i++){
			eval(scriptElements[i].innerHTML);
		}
	}else if(navigator && navigator.userAgent && navigator.userAgent.indexOf && (-1 != navigator.userAgent.indexOf("Chrome"))){
		var xsltProcessor1 = new XSLTProcessor();
		xsltProcessor1.importStylesheet(xsl);
		resultDocument = xsltProcessor1.transformToFragment(xml,document);
		
		ex = this.fixAmpersands(resultDocument.firstChild.innerHTML);
		if (typeof(postProcessHtmlFunction) == 'function') ex = postProcessHtmlFunction(ex);
		resultDocument.firstChild.innerHTML=ex;
		this.removeAllChildren(baseElement);
		baseElement.appendChild(resultDocument);
	}else {
		//alert("AjaxHelper setting content NOActiveXObject, NOChrome");
		//Code for Safari  - doesn't support transformNode, and will not automatically run scripts when added to HTML
		// code for Mozilla, Firefox, Opera, etc.
		var xsltProcessor1=new XSLTProcessor();
		xsltProcessor1.importStylesheet(xsl);
                
		resultDocument = xsltProcessor1.transformToFragment(xml,document);
		ex = this.fixAmpersands(resultDocument.firstChild.innerHTML);
		if (typeof(postProcessHtmlFunction) == 'function') ex = postProcessHtmlFunction(ex);
		resultDocument.firstChild.innerHTML=ex;
		this.removeAllChildren(baseElement);
		baseElement.appendChild(resultDocument);
		var scriptElements = this.returnElementsOfType("script",baseElement);
		for (var i = 0; i < scriptElements.length; i++){
			eval(scriptElements[i].innerHTML);
		}
	}
}

/*
Convenience method to get all children from a DOM object that have the input type
*/
AjaxHelper.prototype.returnElementsOfType = function(typeName,element){
	if (element == null) return;
	var toReturn = [];
	if (element.nodeName==typeName.toUpperCase()){toReturn[0] = element;}
	if (element.childNodes){
		for (var i = 0; i < element.childNodes.length; i++){
			var toConcat = this.returnElementsOfType(typeName,element.childNodes[i]);
			toReturn = toReturn.concat(toConcat);
		}
	}
	return toReturn;
}

/*
Convenience method to remove all children from a DOM object
*/
AjaxHelper.prototype.removeAllChildren = function(fromElement)
{
	if (fromElement.hasChildNodes()){
		while(fromElement.childNodes.length >= 1){
			fromElement.removeChild(fromElement.firstChild);
		}
	}
}

/*
Due to a naked ampersand being invalid XML, an XSL transform cannot return "&"
So we get back &amp; wherever there should be an ampersand.  Since we are displaying this in
HTML, convert them to & before display occurs.  Other ways around this are currently buggy between browsers,
and this seems to work fine.
*/
AjaxHelper.prototype.fixAmpersands = function(toConvert){
	return toConvert.replace(/&amp;/g,"&");
}

AjaxHelper.prepareAmpersandsForXml = function(toConvert){
	return toConvert.replace(/&/g,"&amp;");
}

if(typeof String.prototype.trim !== 'function') {
  String.prototype.trim = function() {
    return this.replace(/^\s+|\s+$/g, ''); 
  }
}
