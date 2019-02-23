// script by jurek.tk
// MIT License

var XMLHttpRequestObject = false;

if (window.XMLHttpRequest) {
    XMLHttpRequestObject = new XMLHttpRequest();
} else if (window.ActiveXObject) {
    XMLHttpRequestObject = new ActiveXObject("\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x2E\x58\x4D\x4C\x48\x54\x54\x50");
}

function getData() {
    var dataSource = "/" +
        document.getElementById("get_est_id").value;

    if(XMLHttpRequestObject) {
        XMLHttpRequestObject.open("GET", dataSource);
        
        XMLHttpRequestObject.onreadystatechange = function() {
            if (XMLHttpRequestObject.readyState == 4 && XMLHttpRequestObject.status == 200) {
                location.href = dataSource;
            } else if (XMLHttpRequestObject.readyState== 404 || XMLHttpRequestObject.status == 404) {
                document.getElementById("code").innerHTML = "<div class='alert alert-dismissible alert-warning' id='notfound'><button type='button' class='close' data-dismiss='alert'>&times;</button>Nieprawidłowy numer oferty</div>";
            }
        }
        
        XMLHttpRequestObject.send(null);
    }
}
