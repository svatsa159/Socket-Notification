function send_ui_notif(){
    var user = document.getElementById("user").value;
    var mess = document.getElementById("data").value;
    data = JSON.stringify({"user":user,"message":mess});
    $.ajax({
        url: "http://localhost:8080/send_data",
        type: 'POST',
        data:data,
        success: function(res) {
            console.log(res);
            // alert(res);
        }
    });
}


