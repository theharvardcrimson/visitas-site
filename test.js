  $(function(){
    // Get a handle to our canvas
    var canvas = $('#overlay');
    var ctx = canvas[0].getContext("2d");
    
    
    // Choose font
    ctx.font = "Bold 36px 'Helvetica'";

    // Draw the black rectangle
    ctx.fillStyle = "black";
    ctx.fillRect(0,0,240,70);
    
    // Punch out the text!
    ctx.globalCompositeOperation = 'destination-out'; 
    ctx.fillText("CENSORED", 20, 50);  
  });