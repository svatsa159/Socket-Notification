function socketRegister(){
    const socket = io("http://localhost:8080");
    socket.emit("user", document.getElementById("user").value);
    socket.on("message",function(data){
        // document.getElementById("logs").innerHTML+=data+"<br/>";
        //console.log(data);
        var notif=$('<div class="closas" id="closas"><div class="close" onclick="closa(this)">x</div><div class="messages">'+data+'</div></div>')
        $("#d").append(notif)
        var perst=$('<div class="closas" id="closas"><div class="close" onclick=""></div><div class="messages">'+data+'</div></div>')
        $("#di").append(perst)
     });
     RegisterDone();
}
var jq = document.createElement('script');
jq.src = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);
document.onload =RegisterTheGuy();
function RegisterTheGuy(){
    // document.getElementsByClassName("pop")[0].style.visibility="visible";
}
function RegisterDone(){
    $("#popup").fadeOut();
    $("#dark").fadeOut();
}

function closa(element){
    $(element).parent().fadeOut();
    setTimeout(function(){
        $(element).parent().remove();
    },500)
    console.log(element.innerHTML);
    
}