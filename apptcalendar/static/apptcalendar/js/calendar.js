/*
    Lauren Bricker
    Spring 2018
    Example code for showing and hiding elements
*/

"use strict";
(function() {
  let timer = null; 

  /**
   *  Helper function to get the element by
   *  @param The string ID of the DOM element to retrieve
   *  @return the DOM element denoted by the ID given
   */
  function $(id) {
    return document.getElementById(id);
  }

  /* Set up the onload so it wil call the initializeWindow function */
  window.onload = initializeWindow; 
  
  /**
   *  Helper function to initialize all of the window elements to respond to onclick 
   *  events. 
   */
  function initializeWindow() {
    // Handle if the manual button is clicked for showing and hiding the box. 
    var value = JSON.parse(document.getElementById('json-data').textContent);
    console.log(value);
    var data_from_django = "{{ appt_list }}";

/*    var myDjangoList = (("{{appt_list |safe}}").replace(/&(l|g|quo)t;/g, function(a,b){
            return {
                l   : '<',
                g   : '>',
                quo : '"'
            }[b];
        }));
    myDjangoList = myDjangoList.replace(/u'/g, '\'')
    myDjangoList = myDjangoList.replace(/'/g, '\"')

    myData = JSON.parse(myDjangoList);
    console.log(myData)
    console.log(data_from_django);
    $("test").innerHTML = "change of text"*/

/*    $("clicked-button").onclick = function() {
        let clickedbox = $("clickedbox"); 
        switchBox(clickedbox);
    };
    
    // handle if the Regular interval  button is clicked
    $("regular-button").onclick = regularButtonClicked; 
    
    // handled if the random
    $("random-button").onclick  = function () { 
      setTimeout(timeoutBox, 1000);
    }*/
    
  }
  
  /**
   *  This function is called whenever the regular button is clicked. If we are starting
   *  it will show the box, then set up a timer to change the color of the box on a 
   *  regular interval. If it is already displayed, it will stop the timer, and hide the box. . 
   */
/*  function regularButtonClicked() {
    $("regularbox").classList.toggle("hidden");
    let button = $("regular-button"); 
    if (timer === null) {
      button.innerHTML = "Stop";
      timer = setInterval(timerBox, 500);
    }
    else {
      button.innerHTML = "Start";
      clearInterval(timer);
      timer = null;
    }
  }*/

  /**
   *  This function is called on regular intervals to do the intented action (call switchbox
   *  to change the color of the box
   */
  function timerBox() {
    let regular = $("regularbox"); 
    switchBox(regular);
  }  
  
  /**
   *  This function is called when ever the button starting the random timeout is clicked. 
   *  It starts a timeout with a random interval and will just keep going - there's no stoping it
   *  because it starts a new timeout each time it's called. 
   */
/*  function timeoutBox() {
    let randombox = $("randombox");
    switchBox(randombox);
    // Generate a new random number between 0 - 4999ms
    let newTime = Math.floor(Math.random() * 5000);    
    setTimeout(timeoutBox, newTime);
  }*/
  
  /**
   *  This function is designed to change the classlist of a given DOM element from white 
   *  to red. 
   *  @param the box that it is changing the classes of. 
   */
/*  function switchBox(box)
  {
    if (box.classList.contains("white"))
    {
        box.classList.remove("white");
        box.classList.add("red");
    }
    else if (box.classList.contains("red"))
    {
        box.classList.remove("red");
        box.classList.add("white");
    }

  }
      */
      


})();
