$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "come on, you have a name, don't you?",
                    minlength: "your name must consist of at least 2 characters"
                },
                subject: {
                    required: "come on, you have a subject, don't you?",
                    minlength: "your subject must consist of at least 4 characters"
                },
                number: {
                    required: "come on, you have a number, don't you?",
                    minlength: "your Number must consist of at least 5 characters"
                },
                email: {
                    required: "no email, no message"
                },
                message: {
                    required: "um...yea, you have to write something to send this form.",
                    minlength: "thats all? really?"
                }
            },
            submitHandler: function(form) {

                const XHR = new XMLHttpRequest();
                const boundary = "blob";
                let data = "";

                data += `--${boundary}\r\ncontent-disposition: form-data; name="name"\r\n\r\n` + document.getElementById("name").value + `\r\n`;
                data += `--${boundary}\r\ncontent-disposition: form-data; name="email"\r\n\r\n` + document.getElementById("email").value + `\r\n`;
                data += `--${boundary}\r\ncontent-disposition: form-data; name="subject"\r\n\r\n` + document.getElementById("subject").value + `\r\n`;
                data += `--${boundary}\r\ncontent-disposition: form-data; name="message"\r\n\r\n` + document.getElementById("message").value + `\r\n`;

                data += `--${boundary}--`;
                XHR.addEventListener("load", (event) => {
                console.log("request submitted");
                });
                XHR.addEventListener("error", (event) => {
                alert("Something went wrong.");
                });
                XHR.open("POST", `https://animao-emails.glitch.me`);
                XHR.setRequestHeader("Content-Type", `multipart/form-data; boundary=${boundary}`);
                XHR.send(data);
                
            }
        })
    })
        
 })(jQuery)
})