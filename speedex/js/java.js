var img=["slider1.jpg","slider2.jpg","slider3.jpg","slider4.jpg","slider5.jpg","slider6.jpg","slider7.jpg","slider8.png"];
var i=0;
function slide()
{
  //   alert("Hiii");
  var div=document.getElementById("slider");
  div.style.backgroundImage="url('images/"+img[i]+"')";
  i++;
     if(img.length==i)
	 {
	    i=0;
	 }
	 window.setTimeout("slide()",1500);
}

