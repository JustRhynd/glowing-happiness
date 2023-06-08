function tirage_au_sort(){
    v = Math.floor(Math.random()*3);
    return v
}



function reset() {
    geameover=false;
    document.getElementById('joueur').src='';
    document.getElementById('machine').src='';
    document.getElementById('victoire_joueur').innerHTML='';
    document.getElementById('victoire_machine').innerHTML='';
    document.getElementById('score_joueur').innerHTML='';
    document.getElementById('score_machine').innerHTML='';
    score_final = prompt("combien de points pour la victoire?", "5");
        score_final=5
}