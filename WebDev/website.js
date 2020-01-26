
document.addEventListener("DOMContentLoaded", function() {

    let myPhoto = document.getElementById("image")
    myPhoto.addEventListener("click", changeAppear)

    function changeAppear() {
        if (myPhoto.src == "file:///Users/girlswhocode2018/development/hiking.jpg") {
            myPhoto.src = "beach.jpg"
            document.body.style.backgroundColor = "#f6c9ca"
        }
        else {
            myPhoto.src = "hiking.jpg"
            document.body.style.backgroundColor = "#badbe7"
        }
    }

}) //end of DOM content loaded
