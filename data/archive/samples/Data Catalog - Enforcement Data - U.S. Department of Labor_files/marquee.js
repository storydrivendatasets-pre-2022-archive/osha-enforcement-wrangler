//Paste this code into an external JavaScript file named: marquee.js

/* This script and many more are available free online at
The JavaScript Source :: http://javascript.internet.com
Created by: Mike Hudson :: http://www.afrozeus.com 


Altered by Bobby Anderson to enable the ability to add fade-in/fade-out to elements
*/

function setupFadeLinks() {
  arrFadeLinks[0] = "";
  arrFadeTitles[0] = "Note: Use the links on this page to navigate.";
  arrFadeLinks[1] = "";
  arrFadeTitles[1] = "Note: Use the links on this page to navigate.";
  arrFadeLinks[2] = "";
  arrFadeTitles[2] = "Note: Use the links on this page to navigate.";
  arrFadeLinks[3] = "";
  arrFadeTitles[3] = "Note: Use the links on this page to navigate.";
  arrFadeLinks[4] = "";
  arrFadeTitles[4] = "Note: Use the links on this page to navigate.";
}

function addFade(elementObject)
{
	if (elementObject == undefined) return;
	//alert('valid elementObject');
	//assume jQuery is available
	for (key in elementObject)
	{
	  alert("altering #"+elementObject[key]);
	  jQuery("#"+elementObject[key]).removeClass();
	  jQuery("#"+elementObject[key]).addClass('fade_link');
    }
}

function removeFade(elementObject)
{
	if (elementObject == undefined) return;
	for (key in elementObject)
	{
      jQuery("#"+elementObject[key]).removeClass('fade_link');
      jQuery("#"+elementObject[key]).addClass('label');
    }
	jQuery("label").css("color","#666");
}

// You can also play with these variables to control fade speed, fade color, and how fast the colors jump.

var m_FadeOut = 255;
var m_FadeIn=0;
var m_Fade = 0;
var m_FadeStep = 3;
var m_FadeWait = 1600;
var m_bFadeOut = true;

var m_iFadeInterval;

if (!(window.jQuery === undefined)){
	jQuery(document).ready(function() {
 	Fadewl();
	});
}else{
	window.onload = Fadewl;
}

var arrFadeLinks;
var arrFadeTitles;
var arrFadeCursor = 0;
var arrFadeMax;

function Fadewl() {
  m_iFadeInterval = setInterval(fade_ontimer, 10);
  arrFadeLinks = new Array();
  arrFadeTitles = new Array();
  setupFadeLinks();
  arrFadeMax = arrFadeLinks.length-1;
  setFadeLink();
}

function setFadeLink() {
  var ilink = document.getElementById("fade_link");
  if (ilink != undefined){
	  ilink.innerHTML = arrFadeTitles[arrFadeCursor];
	  ilink.href = arrFadeLinks[arrFadeCursor];
  }
}

function fade_ontimer() {
  if (m_bFadeOut) {
    m_Fade+=m_FadeStep;
    if (m_Fade>m_FadeOut) {
      arrFadeCursor++;
      if (arrFadeCursor>arrFadeMax)
        arrFadeCursor=0;
      setFadeLink();
      m_bFadeOut = false;
    }
  } else {
    m_Fade-=m_FadeStep;
    if (m_Fade<m_FadeIn) {
      clearInterval(m_iFadeInterval);
      setTimeout(Faderesume, m_FadeWait);
      m_bFadeOut=true;
    }
  }
  var ilink = document.getElementById("fade_link");
  if ((m_Fade<m_FadeOut)&&(m_Fade>m_FadeIn)){
    if (ilink != undefined){
    	ilink.style.color = "#" + ToHex(m_Fade);
	}
    //Assumes jQuery is available
	jQuery(".fade_link").css("color","#" + ToHex(m_Fade));
  }
}

function Faderesume() {
  m_iFadeInterval = setInterval(fade_ontimer, 10);
}

function ToHex(strValue) {
  try {
    var result= (parseInt(strValue).toString(16));

    while (result.length !=2)
            result= ("0" +result);
    result = result + result + result;
    return result.toUpperCase();
  }
  catch(e)
  {
  }
}


