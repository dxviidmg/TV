$(document).ready(function(){if($('.loadhorario').length==1){var channel=$('.loadhorario').attr("data-channel");var image=$('.loadhorario').attr("data-image");var load=$('.loadhorario').attr("data-load");$.post("embed/guia",{channel:channel,image:image,load:load},function(data){$('.loadhorario').hide().html(data).fadeIn("slow");});setInterval(function(){$.post("embed/guia",{channel:channel,image:image,load:load},function(data){$('.loadhorario').html(data);});},3600000);}
$("div a:contains('X')").each(function(){$(this).click(function(){$(".navbar-inverse").animate({paddingTop:"0"},100);});});$("#shadow").css("height",$(document).height()).hide();$(".lightSwitcher").click(function(){$("#shadow").animate({height:"toggle",opacity:"toggle"},"slow");if($("#shadow").is(":hidden"))
$(this).html("<i class=\"fa fa-moon-o\"></i> Apaga la luz");else
$(this).html("<i class=\"fa fa-sun-o\"></i> Enciende la luz");});$("#shadow").click(function(){$("#shadow").animate({height:"toggle",opacity:"toggle"},"slow");$(".lightSwitcher").html("<i class=\"fa fa-moon-o\"></i> Apaga la luz");});$('#enviarreporte').click(function(e){var postData=$('#report').serialize();$("#enviarreporte").attr("disabled","disabled");$("#enviarreporte").html("Enviando...");$.post("modules/embed/libs/reportchannel.php",postData,function(data){$(".reportfi").html(data);$("#enviarreporte").attr("disabled","disabled");$("#enviarreporte").html("Gracias!");});});setTimeout(function(){contador();},1000);function disableBtn(){document.getElementById("openreport").disabled=true;}
function undisableBtn(el){document.getElementById(el).disabled=false;}
function contador(){if($('.timereport').html()<=1){undisableBtn('openreport');$('#textir').html('Reportar canal');}
else{$('.timereport').html($('.timereport').text()-1);setTimeout("contador()",1000);}}
var qsRegex;var buttonFilter;var $container=$('.isotope').isotope({itemSelector:'.element-item',layoutMode:'fitRows',filter:function(){var $this=$(this);var searchResult=qsRegex?$this.text().match(qsRegex):true;var buttonResult=buttonFilter?$this.is(buttonFilter):true;return searchResult&&buttonResult;}});if($("#menulist").length==1){var curcar=$("#menulist").attr("data-current");$('#filters').ready(function(){buttonFilter='.'+ curcar;$container.isotope();});}
$('#filters').on('click','li',function(){$("#menu_iso").removeClass("in").addClass("collapse");buttonFilter=$(this).attr('data-filter');$container.isotope();});var $quicksearch=$('#quicksearch').keyup(debounce(function(){qsRegex=new RegExp($quicksearch.val(),'gi');buttonFilter=$(this).attr('data-filter');$container.isotope();}));$('.filter-group').each(function(i,buttonGroup){var $buttonGroup=$(buttonGroup);$buttonGroup.on('click','li',function(){$buttonGroup.find('.is-checked').removeClass('is-checked');$(this).addClass('is-checked');});});function debounce(fn,threshold){var timeout;return function debounced(){if(timeout){clearTimeout(timeout);}
function delayed(){fn();timeout=null;}
setTimeout(delayed,threshold||100);};}});