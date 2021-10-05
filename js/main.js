//Read Youtube Data from csv src=https://stackoverflow.com/questions/7431268/how-to-read-data-from-csv-file-using-javascript


let dict = []

function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');

    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {
            var tarr = {};
            for (var j=0; j<headers.length; j++) {
                tarr[headers[j]] = data[j];
            }
            dict.push(tarr)
        }
    }
   
    //buildSite(dict,dict.length)
    
}

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "cleaned_links_with_data.csv",
        dataType: "text",
        success: function(data) {processData(data);}
     });
});


function display_title(element,i){
    var date = new Date(parseInt(element['date'])*1000);
    
    var stri = weekday[date.getDay()]+", "+date.getDate()+
        " "+(date.getMonth()+1)+
        " "+date.getFullYear()+
        ", "+date.getHours()+
        ":"+date.getMinutes()+
        ":"+date.getSeconds();

    //console.log("displaying title")
    //console.log(element['sentiment'])
    container = stri

    let sent = parseFloat(element['sentiment'])
    console.log(element['sentiment'],element['date'],element['title'])
    //Load corresponding audio buffer
    let filename = "audios/"+i.toString()+".aac";
    //console.log("playing audio", filename)
    let dist = new Tone.Distortion(0).toDestination();
    if(sent>0.15){
        dist = new Tone.Distortion(sent).toDestination();
        newBackgroundColor = color(255*sent,0,0)
    }
    else{
        dist = new Tone.FeedbackDelay("8n", Math.abs(sent)).toDestination();;
        newBackgroundColor = color(0,255*Math.abs(sent),0)
    }
    let player = new Tone.Player(filename).connect(dist);
    
    // play as soon as the buffer is loaded
    player.fadeOut = Math.random()*3;
    player.fadeIn = Math.random()*3;
    player.autostart = true;

}

let container = 'date'
let weekday = new Array(7);
weekday[0] = "Sunday";
weekday[1] = "Monday";
weekday[2] = "Tuesday";
weekday[3] = "Wednesday";
weekday[4] = "Thursday";
weekday[5] = "Friday";
weekday[6] = "Saturday";

/*
function buildSite(dict,len){
    console.log("building site")
    let i=0
    let delay = Math.floor(Math.random() * 4000);
    function loop(){
        let element=dict[i]
        console.log(element)
        var intervalId = setTimeout(function() {
            display_title(element,i)
            if(i<len){
                i+=1
            }
            else{
                i =0
            }
            loop()
          }, delay);
    }
    loop()
    
}*/

let backgroundColor = null
let newBackgroundColor = null


function setup(){
    createCanvas(innerWidth, innerHeight)
    console.log("setting up P5")
    backgroundColor = color(65)
    newBackgroundColor=color(65)
}

let i = 0
//ca 1/240 chance of i being triggered
let thresh = 0.988
console.log("dict",dict)

function draw(){
    //console.log("drawing")
    let trigger = Math.random()
    //console.log(trigger)
    if(trigger>thresh){
        let element=dict[i]
        display_title(element,i)
        if(i<dict.length){
                i+=1
        }
        else{
            i =0
        }
    }
    
    if(newBackgroundColor != backgroundColor){
        backgroundColor = lerpColor(backgroundColor, newBackgroundColor, 0.1);
    }
    textAlign(CENTER,CENTER)
    background(backgroundColor)
    textSize(50);
    fill(150, 150, 150);
    text(container, innerWidth/2, innerHeight/2);
    
}
