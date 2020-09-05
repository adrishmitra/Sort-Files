console.log("Hello There!");
dir_js = ""

async function onClick_path_btn(){
    dir_js = await eel.main()();
    document.getElementById("dir").innerHTML = "Path Selected:  ".bold() + dir_js;
}

function start(){
    var zip = [document.getElementById("zip_inp").value, document.getElementById('zip_chk').checked];
    var img = [document.getElementById('img_inp').value, document.getElementById('img_chk').checked];
    var app = [document.getElementById('app_inp').value, document.getElementById('app_chk').checked];
    var vdo = [document.getElementById('vdo_inp').value, document.getElementById('vdo_chk').checked];
    var mzc = [document.getElementById('mzc_inp').value, document.getElementById('mzc_chk').checked];
    var doc = [document.getElementById('doc_inp').value, document.getElementById('doc_chk').checked];
    obj = [zip, img, app, vdo, mzc, doc];

    if(dir_js == ''){
        alert("Path Not Selected! Plase select path and try again.")}

    else{
        eel.mkdir(obj, dir_js)(x);}
    
}

async function x(a){
    await eel.move(dir_js, a)
    alert("Sorting Done!")
}