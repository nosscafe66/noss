float inc =0.05;
float scl = 5;//line interval
int cols,rows;

void setup(){
size(800,700);
cols = int(width/scl);
rows = int(height/scl);
//colorMode(HSB);
background(255);
}


void draw()
{ 
float yoff = 0;
for(int y = 0; y < rows; y++){
  
  int h = hour();
  int m = minute();
  int s = second();

if(s == 10){
background(255);
}

  else if(s > 40){
    //stroke(255);
    fill(10,60+s,255,1);
    rect(0,0,269.23,269.23);
    //fill(100,120,255,1);
    rect(269.25,0,161.55,161.55);
    //fill(100,120,255,1);
    rect(0,269.25,430.77,430.77);
    //fill(100,140,255,1);
    rect(323.08,161.55,107.7,107.7);
    translate(269.25,161.55);
    //fill(100,120,255,1);
    rect(0,0,53.85,53.85);
    //fill(0, 100, 0, 20);
    translate(0,53.85);
    translate(53.85,0);
    //fill(0,0,0,1);
    rect(0,0,53.85,53.85);
    fill(100,50,200+s,5);
    rect(0,0,53.85,53.85);
  }
    
    rotate(2*PI+ HALF_PI);
    //background(0,0,0,0);
    fill(240, 80, 50, 5);
    rect(0,0,269.23,269.23);
    //fill(100,120,255,1);
    rect(269.25,0,161.55,161.55);
    rect(0,269.25,430.77,430.77);
    //fill(100,140,255,1);
    //fill(0, 92, 0, 5);
    rect(323.08,161.55,107.7,107.7);
    translate(269.25,161.55);
    //fill(100,120,255,1);
    rect(0,0,53.85,53.85);
    //fill(0, 100, 0, 20);
    translate(0,53.85);
    translate(53.85,0);
    //fill(0,0,0,1);
    rect(0,0,53.85,53.85);
    //fill(random(255));
    rect(0,0,53.85,53.85);
    
    
    //scale(random(1));
    rotate(5*PI);
    rect(0,0,269.23,269.23);
    //fill(100,120,255,1);
    rect(269.25,0,161.55,161.55);
    //fill(100,120,255,1);
    rect(0,269.25,430.77,430.77);
    //fill(100,140,255,1);
    rect(323.08,161.55,107.7,107.7);
    translate(269.25,161.55);
    //fill(100,120,255,1);
    rect(0,0,53.85,53.85);
    //fill(0, 100, 0, 20);
    translate(0,53.85);
    translate(53.85,0);
    //fill(0,0,0,1);
    rect(0,0,53.85,53.85);
    //fill(random(255));
    rect(0,0,53.85,53.85);
    
    frameRate(5);
    scale(random(10));
    rotate(9*PI);
    rect(0,0,269.23,269.23);
    //fill(100,120,255,1);
    rect(269.25,0,161.55,161.55);
    //fill(100,120,255,1);
    rect(0,269.25,430.77,430.77);
    //fill(100,140,255,1);
    rect(323.08,161.55,107.7,107.7);
    translate(269.25,161.55);
    //fill(100,120,255,1);
    rect(0,0,53.85,53.85);
    //fill(0, 100, 0, 20);
    translate(0,53.85);
    translate(53.85,0);
    //fill(0,0,0,1);
    rect(0,0,53.85,53.85);
    
    rect(0,0,53.85,53.85);


    
      
    }
    yoff +=inc;
}


/*



    //fill(0,0,0,1);
    //frameRate(10);
    float xoff = 0;
    for(int x = 0; x< cols; x++){
    float angle = noise(xoff,yoff)*TWO_PI;
    PVector vector = new PVector(0,0).fromAngle(angle);//fromAngle lineangle
    xoff += inc;
    //stroke(0); //default
    //stroke(random(255),random(50),random(255),random(255));
    pushMatrix();
    translate(x*cols,y*cols);
    rotate(vector.heading());
    line(0,0,0,scl); //default
    ellipse(scl/scl,0,scl*1,scl*1000);
    rect(scl*100,0,scl*1,scl*1000);
    stroke(255,120,0,1);
    ellipse(0,0,scl*10,scl*10);
    popMatrix();
    //fill(random(255));
    //rect(x*scl,y*scl,scl,scl);
*/
