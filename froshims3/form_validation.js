document.quesrySelector('form').onsubmit = function(){
    if (!document.quesrySelector('input').value){
        alert("You must provide name")
        return false;
    }
    if(!document.quesrySelector('input').value){
        alert("You must provide dorm")
        return false;
    }
    return true;
};