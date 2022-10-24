document.getElementById("click").onclick = function() {myFunction();}
function myFunction(){
    document.getElementById("loader").innerHTML = `<div class="spinner-border m-5" role="status">
                                                    <span class="sr-only">Loading...</span>
                                                    </div>
                                                    <div class="spinner-border m-5" role="status">
                                                    <span class="sr-only">Loading...</span>
                                                    </div>
                                                    <div class="spinner-border m-5" role="status">
                                                    <span class="sr-only">Loading...</span>
                                                    </div>`
}   