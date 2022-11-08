function funkcija(){
    document.write("Viss")
}
function radiChatu(dati){
    var jaunaRinda = "<br/>"
    var chats = "" ;
    var vieta = document.getElementById("chats")
    for (var rinda of dati["chats"]){
        chats += rinda + jaunaRinda
    }
    vieta.innerHTML = chats
}

async function lasi(){
    const atbilde = await fetch('/chats/lasi')
    const datuObj = await atbilde.json()
    radiChatu (datuObj);
    await new Promise (resolve => setTimeout(resolve, 5000));
    await lasi();
}

async function suti(){
    zinasElements = document.getElementById("zina")
    zina = zinasElements.value
    console.log(zina)
    zinasElements.value = ""
    const atbilde = await fetch('/chats/suti', {
        method: 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({"chats" : zina})
    })
    const datuObj = await atbilde.json()
    radiChatu (datuObj);
}
